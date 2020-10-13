from django.urls import path
from .views import CompanyListSearchView, FavouriteCreateView, FavouriteUpdateView, is_email_verified

urlpatterns = [
    path('search_page/', CompanyListSearchView.as_view(), name='search_page'),
    path('favourite/', FavouriteCreateView.as_view(), name='fav_create'),
    path('favourite/<int:pk>/', FavouriteUpdateView.as_view(), name='fav_update'),
    path('is_email_verified/<str:email>/', is_email_verified, name='is_email_verified'),
]