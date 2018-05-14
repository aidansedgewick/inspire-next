import datetime 
from inspire_crawler.tasks import schedule_crawl
from flask import Flask, current_app()

today = datetime.datetime.today()

delta_days = 1  #Number of days to harvest at once.
Ndays = 100

dates = [ str( today-datetime.timedelta(days=x) ).split()[0] for x in xrange(0,Ndays,delta_days) ]

list_of_sets = "physics,math,cs,econ,eess,q-bio,q-fin,stat"

app = Flask(__name__)
with app.app_context():
    for start, stop in zip(dates[:-1], dates[1:]):

        from_date = "from_date='%s'" % start
        until_date = "until_date='%s'" % stop
       
        schedule_crawl("arXiv", "article", sets="physics,math,cs,econ,eess,q-bio,q-fin,stat",from_date="%s" %start, until_date="%s" %stop )

        print from_date, until_date
