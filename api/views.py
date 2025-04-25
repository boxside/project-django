from django.shortcuts import render,get_object_or_404,redirect
from rest_framework import generics
from .models import Parameter
from django.http import HttpResponse
from django.template.loader import render_to_string
from .serializers import ParameterSerializer
from .forms import ParameterForm

class ParameterViewCreate(generics.ListCreateAPIView):
    queryset = Parameter.objects.all()
    serializer_class = ParameterSerializer

def parameter_list(request):
    parameters = Parameter.objects.all()
    return render(request, 'parameter_list.html', {'parameters': parameters})

def parameter_update(request, id_param):
    param = get_object_or_404(Parameter, id_param=id_param)
    
    if request.method == 'POST':
        form = ParameterForm(request.POST, instance=param)
        if form.is_valid():
            form.save()
            response = HttpResponse()
            response["HX-Redirect"] = "/api/parameters/"  # sesuaikan dengan URL parameter_list kamu
            return response
        else:
            # Kirim ulang form dengan error jika tidak valid
            return render(request, 'partials/parameter_edit.html', {'form': form, 'param': param})
    else:
        form = ParameterForm(instance=param)
        return render(request, 'partials/parameter_edit.html', {'form': form, 'param': param})
