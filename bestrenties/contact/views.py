#from django.shortcuts import render

# Create your views here.
# contact/views.py

from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
import json

from .forms import ContactForm

def contact_view(request):
    """
    Renders the contact page with the contact form.
    """
    form = ContactForm()
    context = {'form': form}
    return render(request, 'contact/contact.html', context)

@require_POST
def submit_contact_form(request):
    """
    Handles AJAX submission for the general contact form.
    """
    try:
        data = json.loads(request.body)
        form = ContactForm(data)

        if form.is_valid():
            contact_message = form.save() # Save the message to DB

            # Send email notification
            subject = f"Nouveau message de contact: {contact_message.subject}"
            message = render_to_string('contact/email/contact_message_email.html', {
                'message_obj': contact_message,
            })
            from_email = settings.DEFAULT_FROM_EMAIL
            recipient_list = ['contact@afripropconnect.com', 'admin@afripropconnect.com'] 

            send_mail(subject, message, from_email, recipient_list, fail_silently=False)

            return JsonResponse({'message': 'Votre message a été envoyé avec succès !'})
        else:
            return JsonResponse({'message': 'Erreur de validation du formulaire.', 'errors': form.errors}, status=400)
    except json.JSONDecodeError:
        return JsonResponse({'message': 'Requête invalide.'}, status=400)
    except Exception as e:
        return JsonResponse({'message': f'Une erreur inattendue est survenue: {str(e)}'}, status=500)