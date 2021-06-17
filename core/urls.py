from django.urls import path

from .views import HomeView, LoginFormView

app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),

    # path('login/', LoginFormView.as_view(), name='login'),
]
