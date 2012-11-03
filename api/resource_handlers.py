from django.conf import settings
from api.handlers import *
from api.authentication import DjangoAuthentication
from piston.resource import Resource

auth = {'authentication': DjangoAuthentication(realm="Veracal")}

if getattr(settings, "API_DEBUG", None):
    from piston.authentication import HttpBasicAuthentication
    auth = {'authentication': HttpBasicAuthentication(realm="Veracal")}


calendar_handler = Resource(CalendarHandler)
task_handler= Resource(TaskHandler)
