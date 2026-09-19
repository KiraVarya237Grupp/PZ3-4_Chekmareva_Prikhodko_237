from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    # Маршруты для авторизации
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # Страницы приложения
    path('profile/', views.profile, name='profile'),
    path('courses/', views.course_list, name='course_list'),
]