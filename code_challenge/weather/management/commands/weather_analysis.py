from django.core.management.base import BaseCommand
from weather.models import WeatherData
import pandas as pd
import os
import datetime


class Command(BaseCommand):
    help = 'import crop data'

    def add_argument(self, parser):
        pass

    def format_date(self, date):
        return date[:4] + '-' + date[4:6]+'-' + date[6:]

    def handle(self, *args, **options):
        num_of_records_before_insert = WeatherData.objects.all().count()
        start_time = datetime.datetime.now()

        #to do
