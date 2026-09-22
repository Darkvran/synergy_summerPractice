from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .forms import NameForm
from .models import UserProfile

def index_view(request):
    greeting = None
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            user_profile = form.save()
            greeting = f"Привет, {user_profile.name}!"
    else:
        form = NameForm()

    # Получаем список всех ранее сохраненных имен для отображения
    users = UserProfile.objects.all().order_by('-id')

    return render(request, 'index.html', {
        'form': form, 
        'greeting': greeting,
        'users': users
    })