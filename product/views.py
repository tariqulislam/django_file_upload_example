from datetime import time
from django.views.generic import ListView
from django.views.generic.dates import timezone_today
from .forms import UploadForm
from django.views.generic.edit import FormView
from django.shortcuts import render
from .forms import UploadForm
from .models import FileUpload
from django.utils import timezone

class FileListView(ListView):
    template_name="product/list.html"
    model = FileUpload
    paginate_by=100

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class FileUploadView(FormView):
    form_class = UploadForm
    template_name = 'product/index.html'
    success_url='....'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

   
    def post(self, request, *args, **kwargs):
        form = self.form_class(
            data=request.POST,
            files=request.FILES
        )

        if form.is_valid():
            form.save()
    
        return render(request, self.template_name, {'form': form})
        
        