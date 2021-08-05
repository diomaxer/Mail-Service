from django.shortcuts import render, get_object_or_404
from .models import Investor, StartUP, Mail
from .forms import InvestorForm, StartUpForm
from .find_startup import find_startup


def start_page_view(request, *args, **kwargs):
    """Стартвоая страница"""
    return render(request, 'start_page.html', {})


def investor_create_view(request):
    """Добавить инвестора"""
    form = InvestorForm(request.POST or None)
    if form.is_valid():
        form.save()
        find_startup(form.cleaned_data['email'])
        form = InvestorForm()

    context = {
        'form': form,
    }
    return render(request, 'investor/investor_create.html', context)


def all_investors_list(request):
    """Вск инвесторы"""
    obj = Investor.objects.all()
    context = {
        'obj': obj,
    }
    return render(request, 'investor/all_investors.html', context)


def all_investors_detail_view(request, id):
    """Одиин определенные инвестор"""
    obj = get_object_or_404(Investor, id=id)
    mail = Mail.objects.filter(destination=obj.id)
    context = {
        'obj': obj,
        'mail': mail,
    }
    return render(request, 'investor/investor_detail.html', context)


def startup_create_view(request):
    """Добавить стартап"""
    form = StartUpForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = StartUpForm()

    context = {
        'form': form,
    }
    return render(request, 'startup/startup_create.html', context)


def all_startups_list(request):
    """Все стартапы"""
    obj = StartUP.objects.all()
    context = {
        'obj': obj,
    }
    return render(request, 'startup/all_startup.html', context)


def all_startups_detail_view(request, id):
    """Один определенные стартап"""
    obj = get_object_or_404(StartUP, id=id)
    context = {
        'obj': obj,
    }
    return render(request, 'startup/startup_detail.html', context)
