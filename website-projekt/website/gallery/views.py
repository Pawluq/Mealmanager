from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from gallery import models

class ImageForm(forms.ModelForm):
    """Klasse zur Formularerstellung."""
    class Meta:
        model = models.Image
        exclude = []

class MealForm(forms.ModelForm):
    class Meta:
        model = models.Meal
        exclude = []

def upload(request):
    # werden Formulardaten geschickt?
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():  # Formular überprüfen
            new_image = form.save()
            return HttpResponseRedirect('/')  # Umleitung
    else:
        form = ImageForm()  # leeres Formular
    return render(request, 'upload.html', dict(upload_form=form))


def index(request):
    all_images = models.Image.objects.all().order_by('name')
    return render(request, 'index.html', dict(images=all_images))

def create_meal(request):
    if request.method == "POST":
        form = MealForm(request.POST)
        if form.is_valid():  # Formular überprüfen
            new_meal = form.save()
            return HttpResponseRedirect('/')  # Umleitung
    else:
        form = MealForm()  # leeres Formular
        return render(request, 'create_meal.html', dict(meal_form=form))

def weekplan(request):
    all_meals = models.Meal.objects.all().order_by('name')
    return render(request, 'weekplan.html', dict(meals=all_meals))
        