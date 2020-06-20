from django.contrib.auth.models import User
from .models import Activity, MembersProfile
from datetime import datetime, timedelta, timezone
from faker import Faker
import random
fake = Faker()


def create_activity():
    user_list = User.objects.all().values_list('id', flat=True)
    for user in user_list:
        now = datetime.now()
        number= random.choice([i for i in range(20)])
        Activity.objects.create(user_id=user, start_time=now, end_time= now + timedelta(minutes = number))


def create_member():
    user_list = User.objects.all().values_list('id', flat=True)
    # print(user_list)
    member = MembersProfile.objects.all()
    member.delete()
    for user in user_list:
        activity_obj = Activity.objects.filter(user_id=user).values_list('id', flat=True)
        member = MembersProfile.objects.create(user_id=user, tz=fake.timezone())
        member.activity_periods.set(activity_obj)
        member.save()
#

def create_user(num):
    user = ['rajan', 'manish', 'john', 'allen', 'aalia', 'daren', 'Kiron', 'smith', 'Devid', 'michel', 'sarah']
    for i in range(num):
        user_lists = User.objects.create(first_name=fake.name(), username=user[i], password=user[i])


