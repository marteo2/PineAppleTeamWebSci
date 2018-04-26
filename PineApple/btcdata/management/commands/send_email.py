from django.utils import timezone

from django.core.management.base import BaseCommand
from btcdata.getbtcdata import save_btc
from btcdata.models import Email


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        all_address = Email.objects.all()
