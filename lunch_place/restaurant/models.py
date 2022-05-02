from django.db import models


class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    rating = models.FloatField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ['-rating']


class Menu(models.Model):
    restaurant_id = models.ForeignKey(
        Restaurant,
        on_delete=models.CASCADE
    )
    description = models.TextField()
    votes = models.IntegerField(default=0)
    menu_date = models.DateField(auto_now_add=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.description

    class Meta:
        ordering = ['-created']
