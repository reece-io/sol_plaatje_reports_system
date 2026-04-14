from django.db import models
from django.core.validators import RegexValidator

class Fault(models.Model):
    # Regex for SA phone numbers (e.g., 071... or +27...)
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$', 
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
    )

    NATURE_CHOICES = [
        ('Water', 'Water'),
        ('Power', 'Power'),
        ('Roads', 'Roads'),
        ('Sewerage', 'Sewerage'),
    ]

    nature = models.CharField(max_length=20, choices=NATURE_CHOICES)
    location = models.CharField(max_length=255)
    reporter_name = models.CharField(max_length=100)
    contact_number = models.CharField(validators=[phone_regex], max_length=17)
    ref_number = models.CharField(max_length=20, unique=True, editable=False, null=True)
    status = models.CharField(max_length=20, default="Logged")
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.nature} at {self.location}"

status = models.CharField(
        max_length=20, 
        default="Logged"  # <--- Add this line
    )

