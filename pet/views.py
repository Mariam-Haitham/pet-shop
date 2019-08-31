from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Q

from .models import Pet
from .forms import PetForm, UpdateForm

# Create your views here.
def list (request):
	pets = Pet.objects.all()

	query = request.GET.get('q')
	if query:
		pets = pets.filter(

            Q(name__icontains = query)|
            Q(age__icontains = query)|
            Q(price__icontains = query)
        ).distinct()

	context = {
		"pets": pets,
	}
	return render(request, "list.html", context)

def detail (request, pet_id):
	pet = Pet.objects.get(id = pet_id)
	context = {
		"pet": pet,
	}
	return render(request, "detail.html", context)

def create(request):

	form = PetForm()
	if request.method == "POST":
		form = PetForm(request.POST, request.FILES or None)
		if form.is_valid():
			pet = form.save(commit = False)
			name = pet.name
			pet.save()
			messages.success(request, "%s is Successfully Added" %name)
			return redirect('pet-list')
		print (form.errors)
	context = {
		"form": form,
	}
	return render(request, 'create.html', context)

def update(request, pet_id):
	pet = Pet.objects.get(id = pet_id)
	form = UpdateForm(instance = pet)
	if request.method == "POST":
		form = UpdateForm(request.POST, request.FILES or None, instance = pet)
		if form.is_valid():
			pet = form.save(commit = False)
			messages.success(request, "Successfully Updated!")
			pet.save()
			if pet.available:
				return redirect('pet-detail', pet_id)
			else:
				return redirect('pet-list')
		print (form.errors)
	context = {
		"form": form,
		"pet": pet,
	}
	return render(request, 'update.html', context)

def delete(request, pet_id):
	pet = Pet.objects.get(id = pet_id)
	pet.delete()
	messages.success(request, "Successfully Deleted!")
	return redirect('pet-list')
