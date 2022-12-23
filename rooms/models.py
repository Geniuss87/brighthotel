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


class Booking(models.Model):
    room = models.ForeignKey(Room, on_delete=models.SET_NULL, null=True, related_name="booking")
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=50)
    checkin = models.DateField()
    checkout = models.DateField()

    def __str__(self):
        return f'{self.room}: {self.checkin} - {self.checkout}'
