import random
import string

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand


from faker import Faker


def randompassword():
    chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
    size = random.randint(8, 12)
    return ''.join(random.choice(chars) for x in range(size))


fake = Faker()


class Command(BaseCommand):
    help = 'create user'

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='how many users create', choices=range(1, 11))

    def handle(self, *args, **kwargs):
        total = kwargs['total']
        for i in range(total):
            User.objects.create_user(username=fake.name(), email=fake.email(), password=randompassword())
