from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.views import View
from .models import Carousel,OurService,Achievement,Blog,Team,MisconductReport
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponseRedirect
from .form import ContactForm
from django.template.loader import render_to_string
from django.contrib import messages
from django.core.mail import EmailMessage
from django.contrib import messages
# Create your views here.
class Home(View):
    def get(self,request):
        carousel=Carousel.objects.all().order_by('-created_at')[:10]
        service=OurService.objects.all().order_by('-created_at')[:10]
        achievements = Achievement.objects.all()
        blogs = Blog.objects.all().order_by('-date')[:5]
        featured_blog = blogs[0] if blogs else None
        other_blogs = blogs[1:] if blogs else []
        context={
            'services':service,
            'achievements':achievements,
            'carousel':carousel,
            'featured_blog': featured_blog,
            'other_blogs': other_blogs, 
        }
        return render(request, './home.html',context)
def filter_projects(request):
    category = request.GET.get('category')  # Get the category from the request
    projects = Achievement.objects.filter(category=category)
    project_list = [
        {
            'id': project.id,
            'title': project.title,
            'description': project.description,
            'image': request.build_absolute_uri(project.image.url) if project.image else None
        }
        for project in projects
    ]
    return JsonResponse(project_list, safe=False)
def About_us(request):
    team_members =Team.objects.filter(board_member=False)
    board_members = Team.objects.filter(board_member=True)
    return render(request, './About_us.html',{'team_members':team_members,'board_members':board_members})
def Services(request):
    service=OurService.objects.all().order_by('-created_at')
    return render(request, './services.html',{'services':service})
def Esg(request):
    return render(request, './esg.html')
def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save to database (optional)
            # Contact.objects.create(**form.cleaned_data)

            # Send email
            subject = f"New Inquiry from {form.cleaned_data['first_name']} {form.cleaned_data['last_name']}"
            recipient_email = settings.DEFAULT_CONTACT_EMAIL
            message = render_to_string("emails/contact_email.html", {"form_data": form.cleaned_data})

            # Send email as HTML
            email = EmailMessage(
                subject=subject,
                body=message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=[recipient_email],
            )
            email.content_subtype = "html"  # Set content type to HTML
            email.send()
            messages.success(request, "Your message has been sent successfully! We will get back to you soon.")
            form = ContactForm() 
    else:
        form = ContactForm()

    return render(request, "contact.html", {"form": form})
def blog_list_view(request):
    blogs = Blog.objects.all().order_by('-date')  # Fetch blogs, latest first
    return render(request, 'blogs.html', {'blogs': blogs})
def blog_detail_view(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    return render(request, 'blog_detail.html', {'blog': blog})
def OurMarkets(request):
    return render(request, 'our_markets.html')
def Solutions(request):
    return render(request, 'solutions.html')
def JoinTeam(request):
    return render(request, 'join_team.html')
class WhistleBlowing(View):
    def get(self, request):
        return render(request, 'whistleBlowing.html')
    def post(self, request):
        anonymous = request.POST.get("anonymous") 
        name = request.POST.get("names") if anonymous == "no" else None
        email = request.POST.get("email") if anonymous == "no" else None
        phone_number = request.POST.get("phone") if anonymous == "no" else None
        country = request.POST.get("country")
        city = request.POST.get("city")
        case_details = request.POST.get("case_details")
        # captcha = request.POST.get("captcha")
        evidence = request.FILES.get("evidence")  # File upload

        # Save to database
        misconduct = MisconductReport.objects.create(
            anonymous=True if anonymous =='yes' else False,
            names=name,
            email=email,
            phone_number=phone_number,
            country=country,
            city=city,
            case_details=case_details,
            # captcha=captcha,
            evidence=evidence,
        )
        if misconduct.id:
            messages.success(request,'Thank you for Information')
            return redirect('whistle_blowing')
        else:
            messages.error(request,'Failed to Inform please try again')
            return redirect('whistle_blowing')