from django.shortcuts import render
from .models import Image
from .forms import ImageForm
from django.http import JsonResponse

def main_view(request):
  form = ImageForm(request.POST or None, request.FILES or None)
  if form.is_valid():
    form.save()
    return JsonResponse({'message':'works'})

  context={'form':form}
  return render(request, 'images/T_main.html', context)
