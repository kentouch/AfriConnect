"""from django.shortcuts import render
from django.http import HttpResponse
from .models import Property

def index(request):
    return render(request, 'real_estate/index.html')

# contact view to handle form submission
def contact(request):
    if request.method == 'POST':
        # Handle form submission logic here
        return HttpResponse("Form submitted successfully!")
    else:
        return render(request, 'real_estate/contact.html')
    
# properties view to list all properties
def properties(request):
    all_properties = Property.objects.all()
    return render(request, 'real_estate/properties.html', {'properties': all_properties})
    # Add more views for real estate as needed

# property_detail view to show details of a specific property
def property_detail(request, property_id):
    try:
        property = Property.objects.get(id=property_id)
        return render(request, 'real_estate/property_detail.html', {'property': property})
    except Property.DoesNotExist:
        return HttpResponse("Property not found", status=404)"""

# real_estate/views.py

from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
import json

from django.db import models

from .models import Property, AgentContact
from .forms import PropertySearchForm, AgentContactForm

def home_view(request):
    """
    Renders the home page with a summary of services and featured properties.
    """
    featured_properties = Property.objects.filter(is_featured=True)[:8] # Get up to 8 featured properties
    search_form = PropertySearchForm() # Initialize search form for the hero section
    context = {
        'featured_properties': featured_properties,
        'search_form': search_form,
    }
    return render(request, 'real_estate/index.html', context)


def property_list_view(request):
    """
    Handles property search and displays listings.
    """
    properties = Property.objects.all()
    form = PropertySearchForm(request.GET)

    if form.is_valid():
        location_search = form.cleaned_data.get('location_search')
        transaction_type = form.cleaned_data.get('transaction_type')
        property_type = form.cleaned_data.get('property_type')
        min_budget = form.cleaned_data.get('min_budget')
        max_budget = form.cleaned_data.get('max_budget')

        if location_search:
            properties = properties.filter(
                models.Q(location_city__icontains=location_search) |
                models.Q(location_country__icontains=location_search) |
                models.Q(location_address__icontains=location_search) |
                models.Q(description__icontains=location_search) # Search in description too
            )
        if transaction_type:
            properties = properties.filter(transaction_type=transaction_type)
        if property_type:
            properties = properties.filter(property_type=property_type)
        if min_budget:
            properties = properties.filter(price__gte=min_budget)
        if max_budget:
            properties = properties.filter(price__lte=max_budget)
    
    context = {
        'properties': properties,
        'form': form,
    }
    return render(request, 'real_estate/property_list.html', context)

def property_detail_view(request, pk):
    """
    Displays a single property's detailed information.
    """
    property_obj = get_object_or_404(Property, pk=pk)
    agent_contact_form = AgentContactForm(initial={'property': property_obj.pk}) # Pre-fill property for the form
    context = {
        'property': property_obj,
        'agent_contact_form': agent_contact_form,
    }
    return render(request, 'real_estate/property_detail.html', context)

@require_POST
def contact_agent_view(request):
    """
    Handles AJAX submission for the agent contact form.
    """
    try:
        data = json.loads(request.body)
        form = AgentContactForm(data)

        if form.is_valid():
            agent_contact = form.save() # Save the contact request to DB
            property_obj = agent_contact.property

            # Send email to agent (or admin)
            subject = f"Nouvelle demande pour la propriété: {property_obj.title}"
            message = render_to_string('real_estate/email/agent_contact_email.html', {
                'contact': agent_contact,
                'property': property_obj,
            })
            from_email = settings.DEFAULT_FROM_EMAIL
            # Replace with actual agent email or admin email
            recipient_list = ['agent@afripropconnect.com', 'admin@afripropconnect.com'] 

            send_mail(subject, message, from_email, recipient_list, fail_silently=False)

            return JsonResponse({'message': 'Votre message a été envoyé avec succès à l\'agent !'})
        else:
            return JsonResponse({'message': 'Erreur de validation du formulaire.', 'errors': form.errors}, status=400)
    except json.JSONDecodeError:
        return JsonResponse({'message': 'Requête invalide.'}, status=400)
    except Exception as e:
        return JsonResponse({'message': f'Une erreur inattendue est survenue: {str(e)}'}, status=500)