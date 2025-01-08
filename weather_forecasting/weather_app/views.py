from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from .forms import AddressForm

# Create your views here.



def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = AddressForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            template=loader.get_template('main.html')
            name=form.cleaned_data['address']
            
            #to again show the address bar where we can submit our address
            form=AddressForm()
            return render(request,"main.html",{'form':form,"name":name})            
    else:
        form=AddressForm()
        return render(request,"master.html",{'form':form})            

    # # if a GET (or any other method) we'll create a blank form
    # else:
    #     form=AddressForm()
    # return render(request, "name.html", {"name":name,"form": form})