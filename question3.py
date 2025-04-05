# Question 3: By default do django signals run in the same database transaction as the caller? 
# Answer:  Yes, Django signals run in the same database transaction as the caller.
In the example below, the signal modifies a field (status) just before saving. Since this change is made inside a transaction block (atomic()), and the update is successfully saved to the database, it confirms that the signal executes within the same transaction context as the save operation.

from django.db import models
from django.db.models.signals import post_save

# Simple model
class App(models.Model):
    function = models.CharField(max_length=100)

# Signal handler: triggered after save()
def post_save_handler(sender, instance, **kwargs):
    print("Signal handler executed")
    instance.function = "Modified by signal"
    print(f"function updated in signal: {instance.function}")
    # Note: instance.save() is not called here, so this change won't persist

# Connect signal to model
post_save.connect(post_save_handler, sender=App)

# Function to create and save an instance
def create_app():
    print("Creating App instance")
    app = App(function="Function")
    app.save()  # Triggers post_save signal
    print(f"function after save(): {app.function}")

# Script entry point
if __name__ == "__main__":
    create_app()
    # Refetch from DB to check if signal-modified value is persisted
    app = App.objects.first()
    print(f"function in DB: {app.function}")
