from django.views.generic import ListView
from .models import *
from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

class HotelListView(ListView):
    model = Hotel
    template_name = "listhotel.html"
    queryset = Hotel.objects.all()

    def get_queryset(self):
        qs = Hotel.objects.all()
        if "name" in self.request.GET and self.request.GET["name"]:
            qs = qs.filter(name__icontains=self.request.GET["name"])
        return qs

def main(request):
    return render(request, "main.html")

def zakaz(request):
    if "save" in request.GET:
        name = request.GET['name']
        surname = request.GET['surname']
        passport = request.GET['passport']
        hotel = request.GET['hotel']
        telephone = request.GET['telephone']
        Zakaz.objects.create(name = name, surname = surname, passport=passport, hotel = hotel, telephone = telephone)
    main = Zakaz.objects.all()
    return render(request, "zakaz.html", context={})


class IndexView(TemplateView):
    template_name = "main.html"

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)

class RegistrationView(TemplateView):
    template_name = "registration.html"

    def post(self, request, *args, **kwargs):
        User.objects.create_user(username=request.POST['username'],
                                 password=request.POST['password'])
        return redirect(reverse('hotel_list'))


class LoginView(TemplateView):
    template_name = "login.html"

    def post(self, request, *args, **kwargs):
        user = authenticate(username=request.POST['username'],
                            password=request.POST['password'])
        if user:
            login(request, user)
            return redirect(reverse('hotel_list'))
        else:
            return HttpResponse("Invalid login or password")
