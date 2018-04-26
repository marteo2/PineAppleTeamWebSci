import os

from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.template.loader import get_template, render_to_string
from django.utils import timezone

from django.core.management.base import BaseCommand
from email.mime.image import MIMEImage

from btcdata.getbtcdata import save_btc
from btcdata.models import Email


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        content = render_to_string("email/index.html")
        msg = EmailMultiAlternatives("User Email", "wow",
                                     'cmappcmkmarketing@gmail.com', ['chinqrw@gmail.com'])
        msg.attach_alternative(content, "text/html")
        msg.mixed_subtype = 'related'
        for f in ['img-01.png']:
            fp = open(os.path.join(os.path.dirname(__file__), f), 'rb')
            msg_img = MIMEImage(fp.read())
            fp.close()
            msg_img.add_header('Content-ID', '<{}>'.format(f))
            msg.attach(msg_img)
        msg.send()
