from django.urls import path
from app2.views import deal, tasks, calendar

urlpatterns = [
    path ('deal', deal),
    path ('tasks', tasks),
    path ('calendar', calendar),
]
