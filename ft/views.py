from django.shortcuts import render

# Create your views here.
def prodift(request):
    prodift = ["Teknik Kimia", "Teknik Sipil", "Teknik Elektro"]
    

    konteks = {
        'prodift': prodift,

    }
    return render(request, 'indexft.html', konteks)
