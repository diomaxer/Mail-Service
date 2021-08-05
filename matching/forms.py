from django import forms
from .models import Investor, StartUP


class InvestorForm(forms.ModelForm):

    class Meta:
        model = Investor
        fields = [
            'name',
            'email',
            'low_price',
            'high_price',
            'stage',
            'industry_prefer',
            'industry',
        ]


class StartUpForm(forms.ModelForm):

    class Meta:
        model = StartUP
        fields = [
            'title',
            'price',
            'industry',
            'stage',
            'info',
        ]
