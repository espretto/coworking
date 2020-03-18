from django.core.management import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):
    """
    The `hash_passwords` command allows to encrypt plaintext passwords
    already present in the database. This is useful after insertion of
    dummy users with non-encrypted passwords.
    """
    help = "DEV COMMAND: hash user passwords"

    def handle(self, *args, **options):
        # hash passwords of fixtures
        for user in User.objects.all():
            if not user.password.startswith('pbkdf2_sha256'):
                user.set_password(user.password)
                user.save()
