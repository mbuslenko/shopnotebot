from django.urls import path
from .views import ProfileList, ItemList


urlpatterns = [
    path('profile/', ProfileList.as_view(), name='profile_list'),
    path('item/', ItemList.as_view(), name="item_list"),
]
