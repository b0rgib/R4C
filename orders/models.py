from django.db import models
from customers.models import Customer
from django.dispatch import receiver
from robots.models import Robot
from django.core.mail import send_mail


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    robot_serial = models.CharField(max_length=5, blank=False, null=False)


@receiver(models.signals.post_save, sender=Robot)
def send_email(sender, instance, **kwargs):
    model, version, email_list = get_orders(instance)
    send_mail(
        'Робот появился в продаже',
        f'Добрый день!\
        Недавно вы интересовались нашим роботом модели {model}, версии {version}.\
        Этот робот теперь в наличии. Если вам подходит этот вариант - пожалуйста, свяжитесь с нами',
        '***',
        email_list,
        fail_silently=False,
    )


def get_orders(instance):
    orders = Order.objects.filter(robot_serial=instance.serial)
    email_list = []
    for order in orders:
        email_list.append(order.customer.email)
    model, version = instance.serial.split('-')
    return model, version, email_list
