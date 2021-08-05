from django.http.response import HttpResponse
from django.shortcuts import redirect, render

# Create your views here.
def home(request):
    return render(request, 'mycrypto/index.html', {'active': 'active'})

def cryptoone(request):
    if request.method == 'POST':
        req = request.POST['desc']
        select = request.POST['algo']
        select1 = int(select)
        if select1 == 1:
            output = req[::-1]
        elif select1 == 2:
            a = ''
            for i in req:
                a = a + i + 'Xx'
            output = a
        return render(request, 'mycrypto/result.html', {'output': output, 'select':select, 'active': 'active'})
    else:
        return redirect('home')


def decryptpage(request):
    return render(request, 'mycrypto/decryptpage.html', {'active1': 'active'})


def decrypt(request):
    if request.method == 'POST':
        reqdc = request.POST['desc']
        selectdc = request.POST['decalgo']
        select2 = int(selectdc)
        # print("Decrypt data:",reqdc)
        if select2 == 1:
            output = reqdc[::-1]
        elif select2 == 2: # This algo has some logical error
            output = ''
            for i in reqdc:
                if i == 'X' or i == 'x':
                    pass
                else:
                    output += i
        return render(request, 'mycrypto/result.html', {'output': output, 'select2':select2})


