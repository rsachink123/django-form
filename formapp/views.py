from django.shortcuts import render
from .forms import AddressForm
from .models import Address
from django.http.response import HttpResponse
def addressview(request):
    if request.method =='POST':
        form = AddressForm(request.POST)
        if form.is_valid():
            name = request.POST.get('name','')
            father_name = request.POST.get('father_name','')
            mother_name = request.POST.get('mother_name','')
            mobile_number = request.POST.get('mobile_number','')
            email_id = request.POST.get('email_id','')
            salary = request.POST.get('salary','')
            comm = request.POST.get('comm','')
            location = request.POST.get('location','')
            a = Address(name=name,father_name=father_name,mother_name=mother_name,mobile_number=mobile_number,email_id=email_id,
                        salary=salary,comm=comm,location=location)
            a.save()
            return render(request, 'tanku.html')
        else:
            return HttpResponse('Data is not inserted')

    else:
        form = AddressForm()
        return render(request,'address.html',{'form':form})


