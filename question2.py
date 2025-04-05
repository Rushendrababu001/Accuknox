''' Question 2: Do django signals run in the same thread as the caller?
Answer:  Yes, Django signals run in the same thread as the caller by default.
In the example code, we print the thread ID from both the caller and the signal handler. 
Since both IDs match, it confirms that the signal executes in the same thread as the one triggering it.'''

from django.db import models
from django.db.models.signals import post_save
import threading

# Simple model with one field
class SecondModel(models.Model):
    title = models.CharField(max_length=100)

# Signal handler for post_save
def post_save_handler(sender, instance, **kwargs):
    print(f"Signal thread ID: {threading.get_ident()}")  # Called after save()

# Connect the signal to the model
post_save.connect(post_save_handler, sender=SecondModel)

# Function to test thread identity between caller and signal
def save_second_model():
    print(f"Caller thread ID: {threading.get_ident()}")
    SecondModel(title="Thread Test").save()
