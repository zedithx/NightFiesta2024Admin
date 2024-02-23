import traceback

from django.core.management.base import BaseCommand
# import function file to run here
from booths.functions.process_winners import process_winners


class Command(BaseCommand):
    def handle(self, *args, **options):
        try:
            print(f"Converting winners...")
            winners = process_winners()
            print(f"The winners generated are {winners}")
        except Exception as e:
            traceback.print_exc()
            print(f"Generate Winners: {e}")
            raise Exception("Generation of winners failed")