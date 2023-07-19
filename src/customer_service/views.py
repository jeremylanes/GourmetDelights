from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from customer_service.models import Message


def message(request):
    if request.method == 'POST':

        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        if request.user.is_authenticated:
            Message.objects.create(name=name, email=email, subject=subject, content=message, author=request.user)
        else:
            Message.objects.create(name=name, email=email, subject=subject, content=message)

        return HttpResponse("<p>Je vous confirme la <a> réception </a> de votre message. Je vous remercie pour l'intérêt que vous portez à mes réalisations et je reviendrai vers vous dès que possible.</p>")

    return render(request, 'customer_service/message.html')

