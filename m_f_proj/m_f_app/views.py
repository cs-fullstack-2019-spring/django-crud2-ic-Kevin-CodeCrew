from django.shortcuts import render, redirect

# This view handles the landing page
from .forms import NewUserForm


def index(request):
    return render(request, 'm_f_app/index.html')


# This page will provide a form to add users
def users(request):
    new_form = NewUserForm(request.POST or None)
    if new_form.is_valid():
        new_form.save()
        return redirect('index')

    return render(request, 'm_f_app/users.html', {'userform': new_form})
