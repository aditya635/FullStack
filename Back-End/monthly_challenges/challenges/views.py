from django.http.response import HttpResponseNotFound
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse 


monthly_challenging={
    "january":"Start Working",
    "february":"Start Crying",
    "march":"Start Living",
    "april":"Start Rolling"
}
# Create your views here.


#def index(request):
  #  return HttpResponse("This Januray")

#def index1(request):
    #return HttpResponse("This February")


#def monthly_challenge(request,month):
#    if month=="january":
#        return HttpResponse("This is "+month+" Sleep!")
#    elif month=="february":
#        return HttpResponse("This is "+month+" love")
#    else:
#        return HttpResponseNotFound("Bad month")
def monthly_challenge(request,month):
    try:
        vro = monthly_challenging[month]
        return HttpResponse(vro)
    except:
        return HttpResponseNotFound("Shit ain't found!")
def monthly_challenges(request,month):
    forward=list(monthly_challenging.keys())
    forward_month=forward[month-1]
    newurl = reverse("dad", args = [forward_month] )  #we make /challenge/januray with this,basically we /challenge/ is preset we can't change it in response redirect like below
    #return HttpResponseRedirect("/challenges/+forward_month")
    return HttpResponseRedirect(newurl)