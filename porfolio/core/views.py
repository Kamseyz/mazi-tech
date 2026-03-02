from django.shortcuts import redirect
from django.views.generic import TemplateView,View
from .models import Resume,Portfolio
from django.conf import settings
from django.http import HttpResponse 
from django.contrib import messages
from django.core.mail import send_mail
from .forms import ContactForm

# Create your views here.
class IndexPage(TemplateView):
    template_name='index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # resume
        context["resume"] = Resume.objects.last()
        
        #porfolio
        context['portfolio'] = Portfolio.objects.all()
        return context
    
    

#contact me 
class ContactView(View):
    def post(self,request):
        form=ContactForm(request.POST)
        
        if form.is_valid():
            
            contact_instance=form.save()
            
            subject=f"New Portfolio Inquiry from {contact_instance.name}"
            email_body=f"Name: {contact_instance.name}\nEmail: {contact_instance.email}\n\nMessage:\n{contact_instance.message}"
            
            try:
                send_mail(
                    subject=subject,
                    message=email_body,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[settings.EMAIL_HOST_USER],
                    fail_silently=False
                )
                
            except Exception as e:
                print(f"Email failed to save {e}")
                
            messages.success(request, "Your message was sent successfully! I will get back to you soon.")
            return redirect('/#contact')
        
        messages.success(request, "There was an error sending your message. Please try again.")
        return redirect('/#contact')
        
        
        