from django.urls import path
from .views import ChildrenView

app_name = "children"

urlpatterns = [
    path('', ChildrenView.as_view()),
]