from django.urls import path
from accounts import views as account_views 

urlpatterns = [
    # Other URL patterns
    path('logout/', account_views.logout_view, name='logout'),
]
