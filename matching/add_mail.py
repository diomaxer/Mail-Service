from .models import Mail
import datetime


def add_mail(investor, prefer_startups, other_startups):
    for item in prefer_startups:
        Mail.objects.create(
            destination=investor,
            start_up=item,
            sent_date=datetime.date.today() + datetime.timedelta(days=1),
            industry_prefer=True,
        )
    for item in other_startups:
        Mail.objects.create(
            destination=investor,
            start_up=item,
            sent_date=datetime.date.today() + datetime.timedelta(days=1),
        )
