from django.urls import path
from . import views

urlpatterns = [
    # Путь 'profile/' удален или закомментирован
    path('courses/', views.course_list, name='course_list'),
]