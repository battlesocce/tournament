from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CustomUserForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth import get_user_model
from django.contrib import messages
User = get_user_model()

def register(request):
    if request.method == 'POST': #if the form has been submitted
        form = CustomUserForm(request.POST) #form bound with post data
        if form.is_valid():
            user = form.save(commit=False)
            user.is_team = True
            user.is_active = False
            user.is_activated = False
            user.save()
            current_site = request.get_host()
            mail_subject = 'Activate your blog account.'
            message = render_to_string('acc_active_email.html', {
                'user': user,
                'domain': current_site,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode(),
                'token': account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                mail_subject, message, to=[to_email]
            )
            email.send()
            return render(request, 'register.html', {'form': form, 
            'message':"  Registration successful...We have sent a confirmaion link to your mail,please confirm your mail-id to continue login!!"
            })

    else:
        form = CustomUserForm()
    return render(request, 'register.html', {'form': form})


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user , backend='django.contrib.auth.backends.ModelBackend')
        messages.success(request, "Now you can login to your account")
        return redirect('/accounts/login/')
    else:
        return HttpResponse('Activation link is invalid!')
