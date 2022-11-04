import email
from django.shortcuts import render

from django.shortcuts import HttpResponse, render,redirect,get_object_or_404
from .forms import EmployeeForm,DeleteForm,UpdateForm
from .models import Employee


# Create your views here.

# rendering first form
def home(request):
    form=EmployeeForm()
    return render(request,'employee_db/index2.html',{'form':form})
# function for first form button
def add_record(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return HttpResponse('<h2>Data Added Successfully</h2>')


# reading the data
def read_record(request):
    employee=Employee.objects.all()
    # return render(request,'employee_db/employee.html',{'employee':employee})
    return render(request,'employee_db/employee2.html',{'employee':employee})


# rendering updation form
def update_record(request):
    uform = UpdateForm()
    return render(request,'employee_db/update_page.html',{'uform':uform})

def update_info(request):
    if request.method=="POST":
        # form = EmployeeForm(request.POST, request.FILES)
        email_ID = request.POST.get('uemail')
        fname = request.POST.get('first_name')
        lname = request.POST.get("last_name")
        new_email = request.POST.get("email")
        new_phone = request.POST.get("phone")
        # new_img = request.POST.get("img")
        # print(email_ID)
        # print(new_img)

        for x in Employee.objects.all():
            # print(x.email)
            if x.email == email_ID:
                obj = Employee.objects.get(email=email_ID)
                obj.first_name = fname
                obj.last_name = lname
                obj.phone = new_phone
                # obj.img = new_img

                print(fname)
                for y in Employee.objects.all():
                    # print("in 2nd if loop")
                    if (y.email == new_email):
                        # print("in if loop condition")
                        return HttpResponse("<h2>This email already exists! Try another..</h2>")

                    else:
                        obj.email = new_email
                obj.save()
            return HttpResponse("<h2>Data updated</h2>")



# when the user is entering a query, if it matches then it will display it
# if it does not matches, return an httpresponse
# no query but entered, redirect to read_record page

def search(request):
    query=request.GET['query']
    if len(query) > 0:
        if Employee.objects.filter(first_name__istartswith = query):
            employee=Employee.objects.filter(first_name__istartswith = query)
            return render(request,'employee_db/employee2.html',{'employee':employee})

        else:
            # messages.warning(request, 'Your searched query does not match with any of the data.')
            return HttpResponse("<h2>Search not found! Try with other keywords</h2>")
    else:
        return redirect("read_record")

def delete(request):
    dform = DeleteForm()
    return render(request,'employee_db/delete.html',{'dform':dform})

def delete_info(request):
    if request.method == "POST":
        demail = request.POST.get('email')

        obj = get_object_or_404(Employee, email = demail)
        obj.delete()
        return HttpResponse("<h2>Deleted</h2>")


