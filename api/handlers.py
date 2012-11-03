from piston.handler import BaseHandler
from apps.calendar.models import *
from django.contrib.auth.models import User

class CalendarHandler(BaseHandler):
    allowed_methods = ('GET', 'POST', 'PUT', 'DELETE',)
    model = Calendar

    def read(self, request, calendar_id=None):
        """
        Returns a single calendar if 'calendar_id' is given, otherwise a subset
        """
        base = Calendar.objects

        if calendar_id:
            return base.get(pk= User.username)

        else:
            return base.all()  # or base.filter(...) can be used here


class TaskHandler(BaseHandler):
    allowed_methods = ('GET', 'POST', 'PUT', 'DELETE',)
    model = Task

    def read(self, request, task_id=None):
        """
        Returns a single calendar if 'task_id' is given, otherwise a subset
        """
        base = Task.objects

        if task_id:
            return base.get(pk= task_id)

        else:
            return base.all()  # or base.filter(...) can be used here

