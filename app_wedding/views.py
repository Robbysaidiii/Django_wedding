from django.shortcuts import render

context = {
        'title':'heti & roby wedding',
        'heading':'undangan pernikahan ',
        'baground':'/static/images/baground.jpeg',
 }

def about(request):
    return render(request, 'app_wedding/about.html', context)