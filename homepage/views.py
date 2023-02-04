from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import re
from django.utils.timezone import datetime
from django.shortcuts import render
from django.shortcuts import redirect
from homepage.forms import LogMessageForm
from homepage.models import LogMessage




#def home(request):
 #   return HttpResponse("EugeneAnipa")
 
 
def home(request):
    return render(request, "homepage/home.html")

def projects(request):
    return render(request, "homepage/projects.html")

def gblog(request):
    return render(request, "homepage/blog.html") 

def about(request):
    return render(request, "homepage/about.html")

def contact(request):
    return render(request, "homepage/contact.html")


def homepage_there(request, name):
    return render(
        request,
        'homepage/homepage_there.html',
        {
            'name': name,
            'date': datetime.now()
        }
    )
    #now = datetime.now()
    #formatted_now = now.strftime("%A, %d %B, %Y at %X") 
    #Filter the name to letters only using regular expressions. URL arguments
    # can contain arbitrary text, so we restrict to safe characters only.
    
    #match_object = re.match("[a-zA-Z]+", name)
    #if match_object:
    #    clean_name = match_object.group(0)
        
    #else:
    #    clean_name = "Friend"
        
        
    #content = "Hello there, " + clean_name + "! It,s " + formatted_now
    #return HttpResponse(content)
# Add this code elsewhere in the file:
def log_message(request):
    form = LogMessageForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            message = form.save(commit=False)
            message.log_date = datetime.now()
            message.save()
            return redirect("home")
    else:
        return render(request, "homepage/log_message.html", {"form": form})
    
    
              


