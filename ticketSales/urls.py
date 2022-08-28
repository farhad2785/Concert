from django.urls import path
from ticketSales import views
urlpatterns = [
    path('concert/list/', views.concertListView),
    path('location/list/', views.locationListView),
    path('concert/<int:concert_id>/', views.concertdDtailsView),
    path('time/list/', views.timeView),
    path('concert_edit/<int:concert_id>/', views.concertEditView),

]