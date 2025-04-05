# Question 1: By default are django signals executed synchronously or asynchronously?
# Answer: By default, Django signals are executed synchronously because they are part of the same execution as the sender, also the signal handler block the flow of the caller until the execution is complete.

from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver

# Simple model with one field
class MyModel(models.Model):
    name = models.CharField(max_length=100)

# Signal handler for pre_save (called before instance.save())
@receiver(pre_save, sender=MyModel)
def my_signal_handler(sender, instance, **kwargs):
    print("Step 2 - Signal triggered (before save)")

# Function to test the flow
def create_instance():
    print("Step 1 - Creating instance")
    MyModel(name="Test").save()
    print("Step 3 - Save complete")
