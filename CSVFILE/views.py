from django.shortcuts import render
import csv,io
from django.contrib import messages
from .models import Employee
def EmployeeDetails(request):
    if request.method=="GET":
        return render(request,"CSVFILE/Employee.html",{"Order":"First_Name,Last_Name,Email,Position,Company,City"})
    csv_file=request.FILES['file']
    if not csv_file.name.endswith(".csv"):
        messages.error(request,"Only CSV Format Files Are Accepted")
    data_set=csv_file.read().decode("UTF-8")
    io_string=io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string,delimiter="," , quotechar="|"):
        _,created=Employee.objects.update_or_create(
            first_name=column[0],
            last_name=column[1],
            email=column[2],
            position=column[3],
            company=column[4],
            city=column[5]
        )

    return render(request,'CSVFILE/Employee.html',messages.success(request,"File Uploaded SuccessFully"))


