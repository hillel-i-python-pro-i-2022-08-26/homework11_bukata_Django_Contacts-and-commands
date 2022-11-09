import logging

from django.core.management import BaseCommand, CommandParser

from apps.contact_book.models import Contact_book
from apps.contact_book.moduls.services import fake_data


class Command(BaseCommand):
    # help its discription of class
    help = "Generate required amount of animals"

    # here we add django logger
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.logger = logging.getLogger("django")

    # function of arguments parsing
    # #parser to make console output
    def add_arguments(self, parser: CommandParser):

        parser.add_argument(
            "--amount",
            type=int,
            default=10,
            help="Amount of generated contacts",
        )

    # function for processing
    def handle(self, *args, **options):
        amount: int = options["amount"]
        # upgrated with logger usage
        # here we do notification what we are doing
        self.logger.info(f"Generate {amount} contacts")

        # to count current amount of contacts and use them in logger below
        current_amount = Contact_book.objects.all().count()
        self.logger.info(f"Current amount of contacts: {current_amount}")

        for number, contact in enumerate(fake_data(amount=amount), start=1):

            message = f"Generating contact. {number}/{amount}."
            self.logger.info(f"{message} Start")

            contact.is_auto_generated = True
            contact.save()

            self.logger.info(f"{message} End")

        # to count generated amount of contacts and use them in logger below
        amount_after_generating = Contact_book.objects.all().count()
        self.logger.info(
            f"Amount of contacts after generating: {amount_after_generating}"
        )
