from django.db import models

# Create your models here.


# resume
class Resume(models.Model):
    resume=models.FileField(upload_to='resume/', blank=True, null= False)
    uploaded_at=models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f'This resume was uploaded at {self.uploaded_at}'
    
    
#porfolio
class Portfolio(models.Model):
    name = models.CharField(max_length=50, null=False, blank=True)
    tools = models.CharField(max_length=50, null=False, blank=True)
    github_link = models.CharField(max_length=500, null=False, blank=True)
    live_link = models.CharField(max_length=100, null=False, blank=True)

    def __str__(self):
        return self.name

    def cover_image(self):
        img = self.images.filter(is_main=True).first()
        return img.screenshot if img else None


class PortfolioImage(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE, related_name='images')
    screenshot = models.ImageField(upload_to='screenshots/')
    is_main = models.BooleanField(default=False)  # acts as cover image
    

#contact form
class ContactModel(models.Model):
    name=models.CharField(max_length=50, null=False, blank=True)
    email=models.EmailField(max_length=100, null=False, blank=True)
    message=models.TextField(max_length=250, null=False, blank=True)
    
    def __str__(self):
        return f"{self.email} send {self.message}"

