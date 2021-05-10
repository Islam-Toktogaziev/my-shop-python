from celery import task
from django.core.mail import send_mail
from .models import Order


@task
def order_created(order_id):
    """
    Задача для отправки уведомления по электронной почте при успешном создании заказа.
    """
    order = Order.objects.get(id=order_id)
    subject = 'Заказ {}'.format(order_id)
    message = 'Уважаемый {},\n\nУ вас успешно оформлен заказ.\
                Номер вашего заказа {}.'.format(order.first_name,
                                                order.id)
    send_mail(subject,
              message,
              'neocustomersystem@gmail.com',
              [order.email])
