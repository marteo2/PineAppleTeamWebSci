from django.core.mail import EmailMessage
from django.template.loader import get_template
from django.utils import timezone

from django.core.management.base import BaseCommand
from btcdata.getbtcdata import save_btc
from btcdata.models import Email


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        t = get_template("email/index.html")
        content = t.render()
        msg = EmailMessage('User Email', content, 'cmappcmkmarketing@gmail.com', ['chinqrw@gmail.com'])
        msg.content_subtype = "html"
        msg.send()
