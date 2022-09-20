from django.shortcuts import render

# Create your views here.
def prodifh(request):
    prodifh = ["Ilmu Hukum"]
    

    konteks = {
        'prodifh': prodifh,

    }
    return render(request, 'indexfh.html', konteks)