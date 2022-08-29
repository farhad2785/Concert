from django.urls import path
from accounts import views
urlpatterns = [
    path('login/', views.login_view),
    path('logout/', views.logout_view),
    path('profile/', views.profile_view),
    path('register/', views.registerView),
    path('profile_edit/', views.profileEditView),
]