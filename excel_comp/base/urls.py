from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name="home_page"),
    path('about/', views.about_page, name="about_page"),
    path('view_csv/', views.view_csv_page, name="view_csv_page"),
    path('profile/', views.profile_page, name="profile_page"),
    path('register/', views.register_page, name="register_page"),
    path('login/', views.login_page, name="login_page"),
    path('logout/', views.logout_page, name="logout_page"),
    path('upload_csv/', views.upload_csv_page, name="upload_csv_page"),
    path('download_csv/', views.download_csv_page)
]
