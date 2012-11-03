from django.shortcuts import render_to_response
from apps.calendar.views import *

def home(request):
  # if user is authenticated
  if request.user.is_authenticated():
    # go straight to their calendar (see apps.calendar.views for view)
    return calendar(request)		
    # if user not logged in
  else:
    # go to public homepage
  	return render_to_response('index.html')
