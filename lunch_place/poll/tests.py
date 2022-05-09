from django.test import TestCase
from poll.models import Poll
from app_logging import logger
from datetime import datetime, date


class PollTestCase(TestCase):

    def test_poll_create(self):
        logger.info(
            "Poll Create Test Running"
        )
        Poll.objects.create(
            start_datetime=datetime.now(),
            end_datetime=datetime.now(),
            poll_date=date.today(),
        )
        res = Poll.objects.all()
        self.assertGreater(len(res), 0)

