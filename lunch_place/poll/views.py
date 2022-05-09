from rest_framework.response import Response
from datetime import datetime, date
from poll.models import Poll, Vote, POLL_TYPE
from .serializers import (
    PollSerializer,
    ResultSerializer,
    VoteSerializer
)
from restaurant.models import Menu
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from restaurant.serializers import (
    MenuSerializer,
    RestaurantSerializer
)
from restaurant.models import Restaurant
from drf_yasg.utils import swagger_auto_schema
from drf_yasg.openapi import (
    Schema,
    TYPE_OBJECT,
    TYPE_NUMBER,
)
from app_logging import logger


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_vote_choices(request):
    menus = Menu.objects.select_related('restaurant_id').filter(
        menu_date=date.today()
    )
    serializer = MenuSerializer(
        menus,
        many=True
    )

    for i in range(len(serializer.data)):
        each = serializer.data[i]
        each['restaurant'] = RestaurantSerializer(
            Restaurant.objects.filter(
                id=each['restaurant_id']
            ).first()
        ).data
        serializer.data[i] = each

    logger.info('Returning all the menus today for vote.')
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.IsAdminUser])
def start_poll(request):
    serializer = PollSerializer(data={
        'start_datetime': datetime.now(),
        'poll_date': datetime.today()
    })

    if serializer.is_valid():
        serializer.save()
        logger.info('A new poll is being started.')
        return Response(serializer.data)
    else:
        logger.error('Error in starting poll.')
        return Response(serializer.errors, 400)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_result(request):

    poll = Poll.objects.filter(
        poll_date=date.today()
    ).first()

    if not poll:
        logger.warning('There is no poll for today\
            either running or finished.')
        return Response({
            'error': 'No poll found for today.'
        }, 400)

    if poll.status == "running":
        logger.warning('There is a poll for today\
            but it is on running mode\
                to get the result it has to be finished first.')
        return Response({
            'error': 'Poll is still running.'
        }, 400)

    serializer = ResultSerializer(
        poll
    )
    logger.info('Returning result of the poll for today.')
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.IsAdminUser])
def end_poll(request):
    poll = Poll.objects.filter(
        poll_date=date.today(),
        status=POLL_TYPE.running
    ).first()

    if not poll:
        logger.warning('There is no poll for today\
            in running to end.')
        return Response({
            'error': 'No poll found (Running) for today.'
        }, 400)

    menus = Menu.objects.filter(
        menu_date=poll.poll_date,
        votes__gt=0
    ).all().order_by('-votes')

    probable_winners = menus[:2] if len(menus) > 1 else menus
    winner = None

    if len(probable_winners) == 0:
        logger.warning('No vote given \
            thus winner calculation is not possible.')
        return Response({
            'error': 'No vote given to find the winner.'
        }, 400)

    last_winners = Poll.objects.filter(
        poll_date__lt=poll.poll_date,
        winner_menu_id__isnull=False
    ).all().order_by('-poll_date')

    if len(last_winners) < 2:
        winner = probable_winners[0]
    elif last_winners[0].restaurant_id != last_winners[1].restaurant_id \
            or last_winners[0].restaurant_id != \
            probable_winners[0].restaurant_id:
        winner = probable_winners[0]
    elif len(probable_winners) > 1:
        logger.warning(f'{probable_winners[0]} is not winning \
            despite of getting most votes, as it will it\'s third\
            win on strike.')
        winner = probable_winners[1]

    poll.end_datetime = datetime.now()
    poll.status = POLL_TYPE.finished

    if not winner:
        poll_serializer = PollSerializer(poll)
        poll_serializer.data['message'] = 'No poll winner can be determined'
    else:
        poll.winner_menu_id = winner
        poll_serializer = PollSerializer(poll)
        poll_serializer.data['message'] = f'Menu : {winner.id} \
            is determined as the winner for today.'
    logger.info(f'Menu : {winner.id} \
            is determined as the winner for today.')
    poll.save()

    return Response(poll_serializer.data)


@swagger_auto_schema(method='post', request_body=Schema(
    type=TYPE_OBJECT,
    properties={
        'menu_id': Schema(
            type=TYPE_NUMBER,
            description='Menu ID (we are voting)'
        ),
    }
))
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def vote(request):
    menu_id = request.data.get('menu_id', None)
    user_id = request.user.id

    poll = Poll.objects.filter(
        poll_date=date.today(),
        status=POLL_TYPE.running
    ).first()

    if not poll:
        return Response({
            'error': 'No poll found (Running) for today.'
        }, 400)

    is_exist = Vote.objects.filter(
        user_id=user_id,
        poll_id=poll.id
    ).exists()

    if is_exist:
        logger.warning('Already a vote is registered from this account.')
        return Response({
            'error': 'You have already submitted your vote for today.'
        }, 400)

    serializer = VoteSerializer(
        data=request.data
    )

    menu = Menu.objects.filter(
        id=menu_id,
        menu_date=poll.poll_date
    ).first()

    serializer.initial_data['poll_id'] = poll.id

    serializer.initial_data['user_id'] = user_id

    if not menu:
        return Response({
            'error': f'No menu found with menu id {menu_id}.'
        }, 400)

    if serializer.is_valid():
        menu.votes = menu.votes + 1
        menu.save()

        logger.info('Registering a vote for today.')
        serializer.save()

        return Response(serializer.data)
    else:
        return Response(serializer.errors, 400)
