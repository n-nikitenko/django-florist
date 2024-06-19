from smtplib import SMTPSenderRefused

from django.core.mail import send_mail

from config.settings import EMAIL_HOST_USER


def send_congratulations(article_title, recipient_list=None):
    if not recipient_list:
        recipient_list = [EMAIL_HOST_USER]
        try:
            send_mail(
                'Поздравляем',
                f'Ваша статья "{article_title}" набрала 100 просмотров',
                EMAIL_HOST_USER,
                recipient_list,
                fail_silently=False, )
        except SMTPSenderRefused as e:
            pass  # TODO: logging error
