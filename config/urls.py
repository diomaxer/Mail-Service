"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from matching.views import (start_page_view,
                            investor_create_view,
                            all_investors_list,
                            all_investors_detail_view,
                            startup_create_view,
                            all_startups_list,
                            all_startups_detail_view,)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', start_page_view, name='start_page'),
    path('add_investor/', investor_create_view, name='add_investor'),
    path('all_investors/', all_investors_list, name='all_investors'),
    path('all_investors/<int:id>/', all_investors_detail_view, name='all_investors_detail'),
    path('add_startup/', startup_create_view, name='add_startup'),
    path('all_startups/', all_startups_list, name='all_startups'),
    path('all_startups/<int:id>/', all_startups_detail_view, name='all_startups_detail'),
]
