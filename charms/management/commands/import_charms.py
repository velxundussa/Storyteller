from os.path import join

from django.core.management.base import BaseCommand

from charms.models import Charm, Exalt
from charms.reader.load import read_2e_charms_from_string


class Command(BaseCommand):
    help = 'Import txt charms'

    def handle(self, *args, **kwarfs):
        Charm.objects.all().delete()
        Exalt.objects.all().delete()

        files = {
            'Dragon Blooded': 'dragon_blooded.txt',
            'Lunar Knacks': 'knack.txt',
            'Lunar': 'lunar.txt',
            'Solar': 'solar.txt',
            'Abyssal': 'abyssals.txt',
            'Alchemical': 'alchemicals.txt',
            'Infernal': 'infernal.txt',
            'Sidereal': 'sidereal.txt',
        }

        for exalt_name, cfile in files.items():
            try:
                charm_file = open(join('charms', 'reader', 'data', cfile), 'r')
                charms = read_2e_charms_from_string(charm_file)
                charm_file.close()

                try:
                    exalt = Exalt.objects.get(name=exalt_name)
                except:
                    exalt = Exalt(name=exalt_name)
                    exalt.save()

                for ccharm in charms:
                    if ccharm['whole_string'] != '':
                        charm = Charm(**ccharm)
                        charm.exalt_type = exalt
                        charm.save()
            except:
                # File does not exist or is empty, maybe the user didn't create it yet.
                pass
