from django.http.response import HttpResponseNotFound
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse 
from django.template.loader import render_to_string

monthly_challenging={
    "january":"Start Working",
    "february":"Start Crying",
    "march":"Start Living",
    "april":"Start Rolling"
    ,"december": None
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
        #responsedata=f"<h1>{vro}</h1>"
        #responsedata = render_to_string("challenges/challenge.html")
        #return HttpResponse(responsedata)
        #return render(request, "challenges/challenge.html" ) can't send dynamic data without 3rd arguement
        return render(request, "challenges/challenge.html", {"text" : vro, "dad": month} )
    except:
        return HttpResponseNotFound("<h1>Shit ain't found!</h1>")


def monthly_challenges(request,month):
    forward=list(monthly_challenging.keys())
    forward_month=forward[month-1]
    newurl = reverse("dad", args = [forward_month] )  #we make /challenge/januray with this,basically we /challenge/ is preset we can't change it in response redirect like below
    #return HttpResponseRedirect("/challenges/+forward_month")
    return HttpResponseRedirect(newurl)

def index(request):
    #listitems=""
    forward=list(monthly_challenging.keys())
    #for month in forward:
    #    cmonth=month.capitalize()
    #    monthpath = reverse("dad", args = [month] )
    #    listitems += f"<li><a href=\"{monthpath}\">{cmonth}</a></li>" #we used \with other double quotes as to not confuse interpretor with which quotes is for html and which for the string part
    #responsedata=f"<ul>{listitems}</ul>"
    return render(request, "challenges/index.html", {"forward": forward})