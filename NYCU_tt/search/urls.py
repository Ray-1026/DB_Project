from django.urls import path
from search import views

urlpatterns = [
    path('', views.home, name = "home"),
    path('<int:pk>', views.detail, name = "course_detail")
]
