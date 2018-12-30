from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('alarms/create/', views.AlarmCreateView.as_view(), name='alarm-create'),
    path('alarms/<int:pk>', views.AlarmDetailView.as_view(), name='alarm-detail'),
    path('alarms/update/<int:pk>/', views.AlarmUpdateView.as_view(), name='alarm-update'),
    path('alarms/delete/<int:pk>/', views.AlarmDeleteView.as_view(), name='alarm-delete'),

    # API functions
    path('show_color', views.ColorView.as_view(), name='color'),
    path('transition_color', views.TransitionColorView.as_view(), name='transition_color'),
    path('show_clock', views.ClockView.as_view(), name='clock'),
]