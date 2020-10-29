import random
import time

from django.contrib.auth.models import User
from models import UserActivity, SubOrganization


def str_time_prop(start, end, format, prop):
    """Get a time at a proportion of a range of two formatted times.

    start and end should be strings specifying times formated in the
    given format (strftime-style), giving an interval [start, end].
    prop specifies how a proportion of the interval to be taken after
    start.  The returned time will be in the specified format.
    """

    stime = time.mktime(time.strptime(start, format))
    etime = time.mktime(time.strptime(end, format))

    ptime = stime + prop * (etime - stime)

    return time.strftime(format, time.localtime(ptime))


def random_date(start, end, prop):
    return str_time_prop(start, end, '%Y-%m-%d', prop)


def enter_each_user_activity():
    sub_org = SubOrganization.objects.get(id=1)
    for i in range(10):
        users = User.objects.all()
        for user in users:
            try:
                UserActivity.objects.create(user=user, sub_organization=sub_org)
            except:
                pass

        activities = UserActivity.objects.all()
        for activity in activities:
            try:
                activity.activity_date = random_date('2010-01-01', '2020-01-01', random.random())
                activity.save()
            except:
                pass
