from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import Course
def index(request):
	qs = Course.objects.all()
	context = {'courses' : qs}
	return render(request, "courses/index.html", context)

def add(request):
	errors = Course.objects.basic_validator(request.POST)
	# check if there are any errors
	if len(errors):
		# if there are errors loop through key value pairs
		for key, value in errors.items():
			messages.error(request,value)
			# redirect to new user form
		return redirect(index)
	else:
		# if th errors object is empty, there are no errors
		# retrieve the blog and make changes
		newcourse = Course(name = request.POST['courseName'], desc= request.POST['courseDescription'])
		print(newcourse)
		newcourse.save()
		messages.success(request,"Added new course")
		return redirect(index)
def destroy(request):
	qs = Course.objects.get(id = request.POST['item'])
	qs.delete()
	return redirect(index)
def confirm(request, id):
	qs = Course.objects.get(id = id)
	context = {'courses': qs}
	return render(request, "courses/confirm.html", context)
