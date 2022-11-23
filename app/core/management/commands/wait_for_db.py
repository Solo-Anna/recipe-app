"""
Django command to wait for database to be available
"""

from django.core.management.base import BaseCommand
"""DJango command to wait for database."""


class Command(BaseCommand):
    """Django command to wait for database"""
    
    def handle(self, *args, **options):
        pass