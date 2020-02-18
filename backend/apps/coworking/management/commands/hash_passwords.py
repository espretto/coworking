from django.core.management import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = "DEV COMMAND: hash user passwords"

    def handle(self, *args, **options):
        
        # Fix the passwords of fixtures
        for user in User.objects.all():
            if not user.password.startswith('pbkdf2_sha256'):
                user.set_password(user.password)
                user.save()
