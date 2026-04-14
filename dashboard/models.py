# models.py
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
import datetime

class Fault(models.Model):
    # ... your fields ...
    ref_number = models.CharField(max_length=20, unique=True, editable=False, null=True)
    status = models.CharField(max_length=20, default="Logged")
    created_at = models.DateTimeField(auto_now_add=True)

# THE SIGNAL (Outside the class)
@receiver(post_save, sender=Fault)
def create_ref_number(sender, instance, created, **kwargs):
    if created and not instance.ref_number:
        year = datetime.date.today().year
        instance.ref_number = f"SPF-{year}-{instance.id}"
        # We use .update to avoid triggering the signal again recursively
        sender.objects.filter(id=instance.id).update(ref_number=instance.ref_number)