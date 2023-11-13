from django import forms
from .models import Mail
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.utils import timezone

class JobForm(forms.ModelForm):
    class Meta:
        model = Mail
        fields = ('company', 'email', 'jobtitle', 'package','location','mobile_number','description')

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if not email:
            raise ValidationError('Email field should not be empty')  
        try:
            validate_email(email)
        except ValidationError:
            raise ValidationError('Please enter a valid email')
        
        if Mail.objects.filter(email=email).exists():
            objc = Mail.objects.filter(email=email).first()
            now = timezone.now()
            delta = now - objc.timestamp
            if delta.days < 15:
                raise ValidationError('Already sent a mail within last 15 days')
        
        return email