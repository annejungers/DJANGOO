from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string



monthly_challenges = {
    "january": "Eat no chocolate for the entire month!!!",
    "february": "Do the TA beginner workout each day!",
    "march":"Code at least in Python for 1hour everyday!",
    "april": "Do the TA intermediate workout each day!",
    "may": "Eat vegan for 1 month",
    "june": "Replace coffee by green tea",
    "july": "Take at least to weeks holidays",
    "august": "Go to the sea and see your childhood friends!",
    "september": "Revise Machine Learning more in depth!",
    "october": "Revise Machine Learning and Deploy Webb Apps with AI (chat bots, computer vision,algorithms, sentiment analysis)! ",
    "november": "Apply for jobs in ML",
    "december": "Start your new job, be happyyyy and involved in tech in Belgium and Luxemburg "
}


#Create your views here


def index(request):
    list_items = ""
    months =list(monthly_challenges.keys())
    return render(request, "challenges/index", {
        "months":months
    })
    
    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month-challenge", args = [month])
        list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"
        #"<li><a href="...">January</a></li><li><a href="...">February</a></li>..."

    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid month!")

    redirect_month = months[month-1]
    redirect_path = reverse("month-challenge", args= [redirect_month]) #/challenge/january
    return HttpResponseRedirect(redirect_path)

#dynamic way
def monthly_challenge(request, month):
    """
    challenge_text = None
    if month == "january":
        challenge_text = "Eat no chocolate for the entire month!!! "
    elif month == "february":
        challenge_text = "Do the TA beginner workout each day!"
    elif month == "march":
        challenge_text = "Code at least in Python for 1hour everyday!"
    else:
        return HttpResponseNotFound("This month is not in your workout planning"
    """
    try:
        challenge_text = monthly_challenges[month]
        return render (request,"challenges/challenge.html",{
            "text":challenge_text,
            "month_name": month #capitalize() is to transform the first letter of the word in capital letter

            })
        #response_data = render_to_string("challenges/challenge.html")   same thing as line above
        #return HttpResponse(response_data)
    except:
        raise Http404()
        
    

"""
the normal way

def january(request):
    return HttpResponse("This works well!! :D")

def february(request):
    return HttpResponse("Walk for at least 20 minutes everyday")

def march(request):
    return HttpResponse("Walk for at least 20 minutes everyday")


"""