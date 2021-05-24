from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse


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
    "december": "Learn django 200 minutes per day"
}

# Create your views here.

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid input")
    
    redirect_month = months[month - 1]
    redirect_path = reverse("month_challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("This month is not supported!")
    