from django.shortcuts import render
from django.http import HttpResponseNotFound, HttpResponseRedirect, Http404
from django.urls import reverse
from django.template.loader import render_to_string


monthly_challenges = {
    "january": "Eat no meat this month",
    "february": "Walk 20 minutes every day",
    "march": "Learn django 200 minutes per day",
    "april": "Eat no meat this month",
    "may": "Walk 20 minutes every day",
    "june": "Learn django 200 minutes per day",
    "july": "Eat no meat this month",
    "august": "Walk 20 minutes every day",
    "september": "Learn django 200 minutes per day",
    "october": "Eat no meat this month",
    "november": "Walk 20 minutes every day",
    "december": None
}

# Create your views here.

def index(request):
    months = list(monthly_challenges.keys())
    return render(request, "challenges/index.html", {
        "months": months
    })

    

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("<h1>Invalid input</h1>")
    
    redirect_month = months[month - 1]
    redirect_path = reverse("month_challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
            "month": month,
            "text": challenge_text
        })
    except:
        """"The First solution"""
        # raise Http404()

        """The second solution"""
        error_page = render_to_string("404.html")
        return HttpResponseNotFound(error_page)
    