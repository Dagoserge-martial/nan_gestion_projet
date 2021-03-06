from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AdminPasswordChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'page/gitlogin/login.html')

@login_required
def settings(request):
    user = request.user
    print(user.username)

    try:
        github_login = user.social_auth.get(provider='github')
    except :
        return redirect('password')

    # try:
    #     twitter_login = user.social_auth.get(provider='twitter')
    # except UserSocialAuth.DoesNotExist:
    #     twitter_login = None

    # try:
    #     facebook_login = user.social_auth.get(provider='facebook')
    # except UserSocialAuth.DoesNotExist:
    #     facebook_login = None

    can_disconnect = (user.social_auth.count() > 1 or user.has_usable_password())
    data = {
        'github_login': github_login,
        # 'twitter_login': twitter_login,
        # 'facebook_login': facebook_login,
        'can_disconnect': can_disconnect,
    }

    return render(request, 'page/gitlogin/setting.html', data)
    
@login_required
def password(request):
    if request.user.has_usable_password():
        PasswordForm = PasswordChangeForm
    else:
        PasswordForm = AdminPasswordChangeForm

    if request.method == 'POST':
        form = PasswordForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Votre mot de passe a été mis à jour avec succès!')
            return redirect('password')
        else:
            messages.error(request, 'Veuillez corriger l\'erreur ci-dessous.')
    else:
        form = PasswordForm(request.user)
    return render(request, 'page/gitlogin/password.html', {'form': form})
