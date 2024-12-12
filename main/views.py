from django.shortcuts import render, redirect
from .forms import PricingInquiryForm
from django.contrib import messages

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def pricing(request):
    return render(request, 'pricing.html')

def contact(request):
    return render(request, 'contact.html')

def faq(request):
    return render(request, 'faq.html')

def pricing_inquiry(request, plan_name, plan_amount):
    if request.method == 'POST':
        form = PricingInquiryForm(request.POST)
        if form.is_valid():
            # Set plan name and plan amount from URL parameters
            form.instance.plan_name = plan_name
            form.instance.plan_amount = plan_amount
            form.save()

            # Optionally, show a success message and redirect
            messages.success(request, 'Thank you for your inquiry! We will get back to you soon.')
            return redirect('thank_you')  # Redirect to a thank you page or another view
    else:
        form = PricingInquiryForm()

    return render(request, 'pricing_inquiry_form.html', {
        'form': form,
        'plan_name': plan_name,
        'plan_amount': plan_amount,
    })

def base(request):
    return render(request, 'base.html')
    