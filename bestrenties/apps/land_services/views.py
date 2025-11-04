"""from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from .models import LandService

def index(request):
    return render(request, 'land_services/index.html')"""

# land_services/views.py

from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
import json

from .forms import LandServiceForm

def land_services_view(request):
    """
    Renders the land services page.
    """
    form = LandServiceForm()
    context = {'form': form}
    return render(request, 'land_services/land_services.html', context)

@require_POST
def submit_land_service_request(request):
    """
    Handles AJAX submission for the land service request form.
    """
    try:
        data = json.loads(request.body)
        form = LandServiceForm(data)

        if form.is_valid():
            service_request = form.save() # Save the request to DB

            # Send email notification
            subject = f"Nouvelle demande de service foncier: {service_request.get_service_type_display()}"
            message = render_to_string('land_services/email/land_service_request_email.html', {
                'request': service_request,
            })
            from_email = settings.DEFAULT_FROM_EMAIL
            recipient_list = ['servicesfonciers@afripropconnect.com', 'admin@afripropconnect.com'] 

            send_mail(subject, message, from_email, recipient_list, fail_silently=False)

            return JsonResponse({'message': 'Votre demande de service a été envoyée avec succès !'})
        else:
            return JsonResponse({'message': 'Erreur de validation du formulaire.', 'errors': form.errors}, status=400)
    except json.JSONDecodeError:
        return JsonResponse({'message': 'Requête invalide.'}, status=400)
    except Exception as e:
        return JsonResponse({'message': f'Une erreur inattendue est survenue: {str(e)}'}, status=500)