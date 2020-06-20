from django.urls import path
from .views import MemberProfileApi, FakeData

urlpatterns = [
    path('members/', MemberProfileApi.as_view()),
    path('fake_data/', FakeData.as_view())
]