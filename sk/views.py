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
            name = form.cleaned_data['Name']
            subject = form.cleaned_data['Subject']
            from_email = form.cleaned_data['Email']
            message = form.cleaned_data['Message']
            if subject == "1":
                subject = 'General Customer Service'
            elif subject == "2":
                subject = 'Suggestion'
            elif subject == "3":
                subject = 'Product Support'
            message = "Name : " + name + "\n" + message + "\n" + "From :" + from_email
            try:
                send_mail(subject, message, 'azeem.esketchers@gmail.com', ['mazeemarif0@gmail.com'],
                          fail_silently=False)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
        return render(request,self.template_name)