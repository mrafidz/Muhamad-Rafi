from django.shortcuts import render

# Create your views here.
def prodifkip(request):
    prodifkip = ["Pendidikan Matematika", "Pendidikan IPA", "Pendidikan Fisika", "Pendidikan Kimia", "Pendidikan Biologi",
    "Pendidikan Sejarah", "Pendidikan Sosiologi", "Pendidikan Bahasa Indonesia", "Pendidikan Bahasa Inggris",
    "Pendidikan Seni Pertunjukan", "Pendidikan Khusus", "Pendidikan Non Formal", "Pendidikan Vokasional Teknik Mesin",
    "Pendidikan Vokasional Teknik Elektro", "Pendidikan Guru Sekolah Dasar", "Pendidikan Guru Pendidikan Anak Usia Dini",
    "Pendidikan PKN"]
    

    konteks = {
        'prodifkip': prodifkip,

    }
    return render(request, 'indexfkip.html', konteks)
