from django.shortcuts import render
from django.views.generic import TemplateView

from sk.models import *


class index(TemplateView):

    template_name = 'index.html'

    def get(self, request, *args, **kwargs):

       folders = GalleryFolders.objects.all()
       images = GalleryImages.objects.all()
       args = {'folder_names': folders, 'images': images}
       return render(request,self.template_name,args)
