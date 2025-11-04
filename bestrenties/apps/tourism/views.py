"""from django.shortcuts import render
from .models import TouristSite
from django.http import HttpResponse

def index(request):
    return render(request, 'tourism/index.html')"""

# tourism/views.py

from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
import json

from .models import TouristSite
from .forms import TourRequestForm

def tourism_view(request):
    """
    Renders the tourism page with highlights for each country.
    """
    # Fetch some example sites or categorize them for display
    rwanda_sites = TouristSite.objects.filter(country='rwanda')[:3]
    burundi_sites = TouristSite.objects.filter(country='burundi')[:3]
    gabon_sites = TouristSite.objects.filter(country='gabon')[:3]
    senegal_sites = TouristSite.objects.filter(country='senegal')[:3]

    tour_form = TourRequestForm()

    context = {
        'rwanda_sites': rwanda_sites,
        'burundi_sites': burundi_sites,
        'gabon_sites': gabon_sites,
        'senegal_sites': senegal_sites,
        'tour_form': tour_form,
    }
    return render(request, 'tourism/tourism.html', context)


# I would like to add a function to handle the form submission for tourism inquiries
# no api requests, just a simple form submission    

@require_POST
def send_test_tour_email(request):  
    try:
        data = json.loads(request.body)
        form = TourRequestForm(data)

        if form.is_valid():
            tour_request = form.save()  # Save the request to DB

            # Send email notification
            subject = f"Nouvelle demande de voyage: {tour_request.name}"
            message = render_to_string('tourism/email/tour_request_email.html', {
                'request': tour_request,
            })
            from_email = settings.DEFAULT_FROM_EMAIL
            recipient_list = ['voyage@afripropconnect.com', 'admin@afripropconnect.com'] 

            send_mail(subject, message, from_email, recipient_list, fail_silently=False)

            return JsonResponse({'message': 'Votre demande de voyage a été envoyée avec succès !'})
        else:
            return JsonResponse({'message': 'Erreur de validation du formulaire.', 'errors': form.errors}, status=400)
    except json.JSONDecodeError:
        return JsonResponse({'message': 'Requête invalide.'}, status=400)
    except Exception as e:
        return JsonResponse({'message': f'Une erreur inattendue est survenue: {str(e)}'}, status=500)




