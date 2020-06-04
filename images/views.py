from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import generic

from .forms import ImageCreateForm
from .models import Image


class ImageListView(generic.ListView):
    model = Image
    template_name = 'images/list.html'


class ImageCreateView(generic.CreateView):
    model = Image
    form_class = ImageCreateForm
    template_name = 'images/image/create.html'
    success_url = '/'


class ImageCreate(generic.View):
    def get(self, request):
        form = ImageCreateForm(data=request.GET)
        return render(request, 'images/image/create.html',
                      {'section': 'images', 'form': form})

    def post(self, request):
        form = ImageCreateForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Image added successfully!')
            return redirect('/')
