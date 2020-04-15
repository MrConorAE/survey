from django.shortcuts import render

# Create your views here.
'''
def customers(request):
    try:
        if request.GET['load']:
            load = request.GET['load']
            if load =='true':
                return load_customers(request)
    except:
        return render(request, 'customers_loading_page.html')

def add_customer(request):
    if request.method == "POST":
        form = customer_form(request.POST)
        add = address_form(request.POST)
        addresses = request.POST.getlist('address')
        x=0
        if form.is_valid() and add.is_valid():
            created_customer = form.save()
            for i in addresses:
                created = address(address=i,customer=created_customer)
                created.save()
                x=x+1
            return redirect('/customers/'+str(created_customer.id))
    else:
        form = customer_form()

    content = {
        'form':form,
        'address_form':address_form,
    }

    return render(request, 'add_customer.html', content)'''

def main(request):
    if request.method == "POST":
        print('received form')
    else:
        return render(request, 'Instagram.html')
