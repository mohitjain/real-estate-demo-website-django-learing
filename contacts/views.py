from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Contact

# Create your views here.
def contact(request):
    if request.method == "POST":
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        email = request.POST['email']
        user_id = request.POST['user_id']
        phone = request.POST['phone']
        name = request.POST['name']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']

        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)
            if has_contacted:
                messages.error(request, "You have already made an inquiry. Please wait.")
                return redirect('/listings/' + listing_id)

        contact = Contact(
            listing=listing,
            listing_id=listing_id,
            name=name, email=email,
            phone=phone,
            message=message,
            user_id=user_id
        )

        contact.save()

        messages.success(request, "Thank you for contacting us. We will get back to real soon.")

        return redirect('/listings/' + listing_id)

