from django.db import models


class Room(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.CharField(max_length=50)
    description = models.TextField()
    size = models.PositiveSmallIntegerField()
    number = models.PositiveSmallIntegerField()
    bed_type = models.CharField(max_length=50)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}'


class Image(models.Model):
    image = models.ImageField(upload_to="rooms")
    room = models.ForeignKey(Room,
                             on_delete=models.CASCADE,
                             related_name="images")


class Message(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=50)
    msg = models.TextField()

    def __str__(self):
        return f'{self.subject}'
