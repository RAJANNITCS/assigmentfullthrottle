from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import MembersProfile, Activity
from .serializers import MembersProfileSerializer, ActivitySerializer
from .fake_data_generator import create_activity,create_member, create_user
from django.views.generic import View,TemplateView
from django.http import HttpResponse

class MemberProfileApi(APIView):

    def get(self, request):
        user_ids = MembersProfile.objects.all().values_list('user_id', flat=True)
        print(user_ids)
        members = []
        for user in user_ids:
            new_member = dict()
            member_object = MembersProfile.objects.get(user_id=user)
            new_member['id'] = member_object.id
            new_member['real_name'] = member_object.user.first_name
            new_member['tz'] = member_object.tz
            activity_object = Activity.objects.filter(user_id=user)
            new_member['activity_periods'] = ActivitySerializer(activity_object, many=True).data
            members.append(new_member)
        response = {'ok':True, 'member':members}
        return Response(response, status=status.HTTP_200_OK)
            

class FakeData(APIView):
    def get(self, request):
        # create_user(10)
        create_member()
        # create_activity()
        # create_activity()
        # create_activity()
        return Response("success")


class Index(TemplateView):
    template_name='testapp/index.html'