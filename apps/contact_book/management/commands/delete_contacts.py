import logging

from django.core.management import BaseCommand, CommandParser

from apps.contact_book import models


class Command(BaseCommand):
    help = "Delete contacts"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.logger = logging.getLogger("django")

    def add_arguments(self, parser: CommandParser):
        parser.add_argument(
            "--amount",
            default=0,
            help="Delete ALL users",
            #    action="store_true",
        )

    def handle(self, *args, **options):
        current_amount = models.Contact_book.objects.all().count()
        self.logger.info(f"Current amount of contacts: {current_amount}")

        amount: int = options["amount"]

        amount_message = str(amount) if amount else "ALL"
        self.logger.info(f"Delete contacts: {amount_message}")

        current_amount_1 = models.Contact_book.objects.all().count()
        self.logger.info(f"Current amount of contacts: {current_amount_1}")

        count, details = models.Contact_book.objects.all().delete()

        self.logger.info(f"Amount of deleted contacts : {count}")

        amount_after_deleting = models.Contact_book.objects.all().count()
        self.logger.info(f"Amount of contacts after action: {amount_after_deleting}")
