from django.shortcuts import render
from .models import Slider, Team
from youtubers.models import Youtubers
# Create your views here.

def home(request):
    Sliders = Slider.objects.all()
    Teams = Team.objects.all()
    featured_youtubers = Youtubers.objects.order_by('-created_date').filter(is_featured=True)
    all_tubers =Youtubers.objects.order_by('-created_date')
    data ={
        'sliders': Sliders,
        'teams':Teams,
        'featured_youtubers':featured_youtubers,
        'all_tubers':all_tubers
    }
    return render(request, 'webpages/home.html', data)

def about(request):
    Teams = Team.objects.order_by('-created_date')
    data = {
        'Teams': Teams
    }
    return render(request, 'webpages/about.html', data)
def services(request):
    return render(request, 'webpages/services.html')
def contact(request):
    return render(request, 'webpages/contact.html')