from django.shortcuts import render,redirect
from news.models import newsinfo

def INDEX(request):
    news = newsinfo.objects.all()

    context = {
        'news':news,
    }

    return render(request,'index.html',context)

def ADD(request):
    if request.method == "POST":
        title = request.POST.get('title')
        news_details = request.POST.get('news_details')
        cover_image = request.POST.get('cover_image')

        news = newsinfo(
            title = title,
            news_details = news_details,
            cover_image = cover_image,
        )
        news.save()
        return redirect('home')         
    return render(request,'index.html')

def EDIT(request):
    news=newsinfo.objects.all()

    context = {
        'news':news,
    }

    return redirect(request,'index.html',context)

def UPDATE(request,id):
    if request.method == "POST":
        title=request.POST.get('title')
        news_details=request.POST.get('news_details')
        cover_image = request.POST.get('cover_image')


        news = newsinfo(
            id = id,
            title = title,
            news_details = news_details,
            cover_image = cover_image,

    )
        news.save()
        return redirect('home')
    return redirect(request,'index.html')

def DELETE(request,id):
    news = newsinfo.objects.filter(id = id)
    news.delete()

    context = {
        'news': news,
    }

    return redirect('home')


