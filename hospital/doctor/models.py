from django.db import models

class Department(models.Model):
    name=models.CharField(max_length=100)
    desc=models.TextField(max_length=200)
    def __str__(self):
        return self.name
class Doctor(models.Model):
    name=models.CharField(max_length=100)
    spec=models.CharField(max_length=200)
    dep=models.ForeignKey(Department,on_delete=models.CASCADE)
    image=models.CharField(max_length=500)
    def __str__(self):
        return self.name
class Booking(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    phone=models.CharField(max_length=100)
    doc_name=models.ForeignKey(Doctor,on_delete=models.CASCADE)
    booking_date=models.DateField()
    booked_on=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
