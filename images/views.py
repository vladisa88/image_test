from django.shortcuts import render
from django.views import generic

from .forms import ImageCreateForm
from .models import Image


class ImageListView(generic.ListView):
    model = Image
    template_name = 'images/image/list.html'


class ImageCreateView(generic.CreateView):
    model = Image
    form_class = ImageCreateForm
    template_name = 'images/image/create.html'
    success_url = '/'


class ImageDetailView(generic.View):
    def get(self, request, pk):
        image = Image.objects.get(id=pk)
        width = request.GET.get('width')
        height = request.GET.get('height')
        return render(request, 'images/image/detail.html',
                      {'image': image, 'width': width, 'height': height})
