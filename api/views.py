from django.shortcuts import render, get_object_or_404
from api.models import OlxCarData
from django import forms


class ContactForm(forms.Form):
    price = forms.IntegerField(required=False)


# Create your views here.
def viewCars(request):
    if request.method == "POST":
        if request.method == 'POST':
            form = ContactForm(request.POST)
            if form.is_valid():
                form = ContactForm(request.POST)
                if form.is_valid():
                    query = form.cleaned_data
                    obj = OlxCarData.objects.filter(
                        price__lte=(query['price'] + 400000),
                        price__gte=(query['price'] - 400000)
                    )[1:100]  # Get Cars between given price with 4 LAC Difference. Sliced resultant rows to 100 only
                    context = {
                        'object': obj
                    }
                    return render(request, "index.html", context)

    else:
        obj = OlxCarData.objects.all().order_by('-id')[
              1:100]  # Get all rows and sliced from 1 to 100 to show only 100 rows
        context = {
            'object': obj
        }
        return render(request, "index.html", context)
