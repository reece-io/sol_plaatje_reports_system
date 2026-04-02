from django.db import models

class Fault(models.Model):
    NATURE_CHOICES = [
        ('Power', 'Power Outage'),
        ('Water', 'Water Leak'),
        ('Pothole', 'Pothole'),
    ]
    STATUS_CHOICES = [
        ('Logged', 'Logged'),
        ('In Progress', 'Technician Dispatched'),
        ('Resolved', 'Resolved'),
    ]
    
    nature = models.CharField(max_length=50, choices=NATURE_CHOICES)
    location = models.CharField(max_length=255)
    reporter_name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=15)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Logged')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nature} at {self.location}"