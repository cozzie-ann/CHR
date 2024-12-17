from django.db import models

class PricingInquiry(models.Model):
    PLAN_CHOICES = [
        ('Option 1', 'Option 1'),
        ('Option 2', 'Option 2'),
        ('Small Business', 'Small Business'),
        ('Corporate', 'Corporate'),
        ('Custom', 'Custom'),
    ]
    
    company_name = models.CharField(max_length=255)
    contact_person = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    number_of_employees = models.PositiveIntegerField()
    enquiry_message = models.TextField()
    plan_name = models.CharField(choices=PLAN_CHOICES, max_length=50)
    plan_amount = models.DecimalField(max_digits=10, decimal_places=2)
    pricing_type = models.CharField(max_length=10, choices=[('monthly', 'Monthly'), ('yearly', 'Yearly')])

    def __str__(self):
        return f"Inquiry from {self.company_name} for {self.plan_name} plan"
