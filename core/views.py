from django.shortcuts import render
from .models import Event, Activity, Photo, Sponsor, RecommendedRace
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from .forms import ContactForm

def home(request):
    event = Event.objects.first()
    activities = Activity.objects.filter(event=event)
    photos = Photo.objects.filter(event=event)[:6]
    sponsors = Sponsor.objects.all()
    recommended_races = RecommendedRace.objects.all()[:3]
    return render(request, 'core/home.html', {
        'event': event,
        'activities': activities,
        'photos': photos,
        'sponsors': sponsors,
        'recommended_races': recommended_races,
    })

def gallery(request):
    photos = Photo.objects.all()
    return render(request, 'components/gallery.html', {'photos': photos})

from django.shortcuts import render, redirect

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            message = form.cleaned_data["message"]

            send_mail(
                subject=f"Contact from {name}",
                message=message,
                from_email=email,
                recipient_list=[settings.DEFAULT_FROM_EMAIL],
                fail_silently=False,
            )

            messages.success(request, "Message sent successfully!")
            return redirect('contact')  # 👈 redirigimos después del POST
    else:
        form = ContactForm()

    return render(request, "core/contact.html", {"form": form})
