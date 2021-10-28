#!/usr/bin/env python
"""Export data from deskpro and upload to Google Cloud

Usage:
  deskpro_export.py [--config=<file>] [--dry-run]
  deskpro_export.py [--config=<file>] [--start-date=<date>] [--dry-run]
  deskpro_export.py [--config=<file>] [--start-date=<date>] [--end-date=<date>] [--dry-run]
  deskpro_export.py -h | --help
  deskpro_export.py --version

Options
  -h --help                 Show this screen
  --version                 Show version
  --config=<file>           Specify configuration file [Default: /usr/local/etc/deskpro_export.conf]
  --start-date=<date>       Begin date in format 'YYYY-MM-dd'
  --end-date=<date>         End date in format 'YYYY-MM-dd'
  --dry-run                 Only query the database, don't upload
"""
from docopt import docopt
import datetime
import calendar

if __name__ == '__main__':
    arguments = docopt(__doc__)
    print(arguments)

    start_date = arguments['--start-date']
    end_date = arguments['--end-date']

    today = datetime.date.today()
    first_of_month = today.replace(day=1)
    last_day_last_month = first_of_month - datetime.timedelta(days=1)
    mdays = calendar.monthrange(last_day_last_month.year, last_day_last_month.month)[1]

    startDate = datetime.date(last_day_last_month.year, 1, 1)
    endDate = last_day_last_month

    if start_date is not None:
        startDate = datetime.date(datetime.datetime.strptime(start_date, '%Y-%m-%d').year, 1, 1)

    if end_date is not None:
        first_of_month = datetime.datetime.strptime(end_date, '%Y-%m-%d').replace(day=1)
        last_day_last_month = first_of_month - datetime.timedelta(days=1)
        mdays = calendar.monthrange(last_day_last_month.year, last_day_last_month.month)[1]
        endDate = last_day_last_month

    sStartDate = startDate.strftime('%Y-%m-%d')
    sEndDate = endDate.strftime('%Y-%m-%d')

    print(sStartDate)
    print(sEndDate)
