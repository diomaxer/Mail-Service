from .models import Investor, StartUP
from .add_mail import add_mail


def find_startup(email):
    """Найти стартап для Инвестора"""
    stage_list = []
    industry_prefer_list = []
    industry_list = []
    investor = Investor.objects.filter(email=email)[0]
    startups = StartUP.objects.all()
    for item in startups:
        for stage in investor.stage.all():
            if stage == item.stage:
                stage_list.append(item)
    for item in startups:
        for industry_prefer in investor.industry_prefer.all():
            if industry_prefer == item.industry:
                industry_prefer_list.append(item)
    for item in startups:
        for industry in investor.industry.all():
            if industry == item.industry:
                industry_list.append(item)
    result_prefer = list(set(stage_list) & set(industry_prefer_list))
    result = list(set(stage_list) & set(industry_list))
    for item in result:
        if item in result_prefer:
            result.remove(item)
    add_mail(investor, result_prefer, result)

"""
Стадия
Предпочитаемые индучтрии
Все индустри
"""