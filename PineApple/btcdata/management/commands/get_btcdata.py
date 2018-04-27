from django.core.management.base import BaseCommand
from django.utils import timezone

from btcdata.getbtcdata import save_btc
from btcdata.models import PriceData


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        btc_data = save_btc()
        p = PriceData()
        temp = timezone.datetime.fromtimestamp(btc_data["time"]).strftime(
            '%Y-%m-%d %H:%M:%S.%f')
        p.time = temp
        p.price = btc_data
        p.save()
        self.stdout.write(self.style.SUCCESS('Successfully write to database with id "%d"' % p.id))
