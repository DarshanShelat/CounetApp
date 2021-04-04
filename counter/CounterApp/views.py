from django.shortcuts import render, redirect
from .models import CounterModel


def helloworld(request):
    name = 'Darshan'
    obj = CounterModel.objects.filter(id=1)[0]
    ournumber = obj.number
    context = {'name': name, 'number': ournumber}
    return render(request, 'helloworld/helloworld.html', context)

def Increment(request):
    # Code to increse the counter value by pressing Increment button.
    obj = CounterModel.objects.filter(id=1)[0]
    obj.number = int(obj.number) + 1
    obj.save()
    return redirect(request.META['HTTP_REFERER'])

def Decrement(request):
# Code to decrese the counter value by pressing Decrement button.
    obj = CounterModel.objects.filter(id=1)[0]
    obj.number = int(obj.number) - 1
    obj.save()
    return redirect(request.META['HTTP_REFERER'])

def Reset(request):
# Code to reset the counter value by pressing Reset button.
    obj = CounterModel.objects.filter(id=1)[0]
    obj.number = 0
    obj.save()
    return redirect(request.META['HTTP_REFERER'])