from django.shortcuts import render,redirect
from .models import AccessCount

def count_view(request):
    # Increment the access count
    access_count, created = AccessCount.objects.get_or_create(id=1)
    access_count.count += 1
    access_count.save()

    # Render the count in the template
    return render(request, 'counter/count.html', {'count': access_count.count})

def reset_count_view(request):
    access_count, created = AccessCount.objects.get_or_create(id=1)
    access_count.count = -1
    access_count.save()

    return redirect('count_view')

def double_counter(request):
    access_count, created = AccessCount.objects.get_or_create(id=1)
    access_count.count = access_count.count*2-1
    access_count.save()

    return redirect('count_view')