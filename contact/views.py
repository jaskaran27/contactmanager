from django.http import HttpResponse, HttpResponseRedirect
from contact.models import Contact
from django.shortcuts import render_to_response, render
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse

def landing(request):
	return render(request, 'contact/landing.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
			new_user = form.save()
			new_user = authenticate(username=request.POST['username'], password=request.POST['password1'])
			login(request, new_user)
			return HttpResponseRedirect("/contacts/")
    else:
        form = UserCreationForm()
    return render(request, "registration/register.html", {
        'form': form,
    })

def logout_page(request):
	logout(request)
	return HttpResponseRedirect('/')

@login_required
def contacts(request):
	contact_list = Contact.objects.filter(user=request.user).order_by('first_name')
	pages = [{"letter": i, "contacts": contact_list.filter(first_name__istartswith=i) } for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"]
	return render(request, 'contact/contact.html', {'contact_list': contact_list, 'pages': pages})

@login_required
def add_contact(request):
	if request.method == 'POST':
		first_name = request.POST.get('firstname', '')
		last_name = request.POST.get('lastname', '')
		email = request.POST.get('email', '')
		mobile = request.POST.get('mobile', '')
		alternate_number = request.POST.get('alternate_number', '')
		contact_obj = Contact(user=request.user, first_name=first_name, last_name=last_name, email=email, mobile=mobile, alternate_number=alternate_number)
		contact_obj.save()
		return HttpResponseRedirect(reverse('contacts'))
	return render(request, 'contact/add_contact.html')

@login_required
def update_contact(request, contact_id):
	contact = Contact.objects.get(id=contact_id)
	if request.user != contact.user:
		return HttpResponse("You don't have permission to update this contact.")
	if request.method == 'POST':
		contact.first_name = request.POST.get('firstname', '')
		contact.last_name = request.POST.get('lastname', '')
		contact.email = request.POST.get('email', '')
		contact.mobile = request.POST.get('mobile', '')
		contact.alternate_number = request.POST.get('alternate_number', '')
		contact.save()
		return HttpResponseRedirect(reverse('contacts'))
	return render(request, 'contact/update_contact.html', {'contact': contact})

@login_required	
def contact_details(request, contact_id):
	contact = Contact.objects.get(id=contact_id)
	if request.user != contact.user:
		return HttpResponse("You don't have permission to view this contact.")
	if request.method == 'POST':
		contact.delete()
		return HttpResponseRedirect(reverse('contacts'))
	return render(request, 'contact/contact_details.html', {'contact': contact})