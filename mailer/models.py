from django.db import models
from django.core.validators import RegexValidator
# Create your models here.

class Mail(models.Model):
    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Interview Attended', 'Interview Attended'),
        ('Rejected', 'Rejected'),
        ('Completed', 'Completed'),
    )
    mobile_number_regex = RegexValidator(
        regex=r'^\+?91?\d{10}$',
        message="Phone number must be entered in the format: '+919999999999'. 10 digits allowed."
    )
    company = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    jobtitle = models.CharField(max_length=100, null=True, blank=True)
    package = models.CharField(max_length=100, null=True, blank=True)
    location = models.TextField(null=True, blank=True)
    mobile_number = models.CharField(max_length=13,null=True, blank=True, validators=[mobile_number_regex])
    description = models.TextField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=30, default='Pending', choices=STATUS_CHOICES)

    def __str__(self):
        return self.email or "No Email"
    