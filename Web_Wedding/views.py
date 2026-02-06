from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context = {
        'title':'heti & roby wedding',
        'heading':'undangan pernikahan ',
        'baground':'/static/images/baground.jpeg',
        'daun':'/static/images/daun.png',
        'bunga':'/static/images/tepi_kanan_atas.png',
        'bunga2':'/static/images/tepi_kiri_atas.png',
        'aktor':'/static/images/aktorbatik_prempuan.png',
        'aktor2':'/static/images/aktorbatik_laki.png',
        'text':"""Kami mengundang Bapak/Ibu/Saudara 
        untuk hadir dalam acara pernikahan kami:""",
        'text2':'dan',
        'nama_prempuan':'Wanda ',
        'nama_laki':'Rizky',


    }
    return render(request, 'index.html',context)
