from django.core.management.base import BaseCommand
from django_seed import Seed
from accounts.models import User

class Command(BaseCommand):
    help = "테스트 유저 생성"

    def add_arguments(self, parser):
        parser.add_argument(
            "--total",
            default=2
        )