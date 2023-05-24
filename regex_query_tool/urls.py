from django.urls import path
from . import views

app_name = "regex_query_tool"

urlpatterns = [
    path("", views.home, name="query"),
]
