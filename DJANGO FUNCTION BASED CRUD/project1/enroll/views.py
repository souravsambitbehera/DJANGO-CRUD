from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import StudentRegistration
from .models import User
# Create your views here.


def create(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            name = fm.cleaned_data['name']
            email = fm.cleaned_data['email']
            password = fm.cleaned_data['password']

            register = User(name=name, email=email, password=password)
            register.save()
            return HttpResponseRedirect('/')
            fm = StudentRegistration()

    else:
        fm = StudentRegistration()
    stud = User.objects.all()

    return render(request, 'enroll/create.html', {'form': fm, 'students': stud})

def update(request, id):
    if request.method == 'POST':
        update_info = User.objects.get(pk=id)
        fm = StudentRegistration(request.POST, instance=update_info)
        if fm.is_valid:
            fm.save()
    else:
        update_info = User.objects.get(pk=id)
        fm = StudentRegistration(instance=update_info)
    return render (request, 'enroll/update.html', {'form':fm})
        





def delete(request, id):
    if request.method == 'POST':
        delete_info = User.objects.get(pk=id)
        delete_info.delete()
        return HttpResponseRedirect('/')
