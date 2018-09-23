from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

from sk.forms import ContactForm
from sk.models import *


class index(TemplateView):

    template_name = 'index.html'
    contact_form = ContactForm

    def get(self, request, *args, **kwargs):

       folders = GalleryFolders.objects.all()
       images = GalleryImages.objects.all()
       args = {'folder_names': folders, 'images': images, 'form': self.contact_form}
       return render(request,self.template_name,args)

    def post(self, request, **kwargs):
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Email From skassociates.pk"
            from_email = form.cleaned_data['Email']
            message = form.cleaned_data['Message']
            message = "From : " + from_email+ "\n" + "Message: " + message + "\n"
            try:
                send_mail(subject, message, 'directorsohaib.burraqmarketing@gmail.com', ['skassociates1600@gmail.com'],
                          fail_silently=False)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
        return render(request,self.template_name)