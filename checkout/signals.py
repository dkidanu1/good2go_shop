from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import OrderLineItem

@receiver(post_save, sender=OderLineItem)
def update_on_save(sender, instance, created, **kwargs):
    """ Update order total on the line item """
    instance.order.update_total()

@receiver(post_delete, sender=OderLineItem)
def update_on_save(sender, instance, created, **kwargs):
    """ Update order total on the line item delete """
    instance.order.update_total()