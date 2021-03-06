from django.core.management.base import BaseCommand
from django.db.utils import IntegrityError
from sensoroad.apps.user.models import User


class Command(BaseCommand):
    help = 'Create new user'

    def add_arguments(self, parser):
        parser.add_argument('-u', '--username', type=str, help="Username")

    def handle(self, *args, **kwargs):
        if kwargs['username'] is None:
            self.stdout.write(self.style.WARNING("Username must be specified."))
            return
        username = kwargs['username']

        try:
            user = User.objects.get(username=username)
            user.delete()
        except IntegrityError as e:
            self.stdout.write(self.style.ERROR('User deletion failed: {}'.format(e)))
            return
        except User.DoesNotExist:
            self.stdout.write(self.style.ERROR('User not found: {}'.format(username)))
            return

        self.stdout.write(self.style.SUCCESS("User deleted successfully."))
