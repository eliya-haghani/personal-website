from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ContactForm
from django.contrib import messages
def ilia_view(request):
    return HttpResponse("Hello from ilia App")

# Create your views here.
from django.shortcuts import render

def home(request):
    return render(request, 'ilia/index.html')

def about(request):
    return render(request, 'ilia/about.html')

def contact(request):
    return render(request, 'ilia/contact.html')

def test(request):
    posts = Post.objects.all() # مطمئن شو حرف اول Post بزرگ است
    context = {
        'posts': posts, 
        'name': 'ilia', 
        'last_name': 'haghani'
    }
    return render(request, 'ilia/test.html', context)


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()

            messages.success(
                request,
                'پیام شما با موفقیت ارسال شد. به زودی با شما تماس خواهیم گرفت.'
            )

            return redirect('website:contact')

    else:
        form = ContactForm()

    return render(request, 'ilia/contact.html', {'form': form})