from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.decorators import login_required
from .forms import UserUpdateForm, UserProfileUpdateForm
from django.utils.translation import gettext_lazy as _


@csrf_protect
def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        password2 = request.POST.get("password2")
        error = False
        if not password or password != password2:
            messages.error(
                request, _("Passwords do not match or have not been entered.")
            )
            error = True
        if not username or User.objects.filter(username=username).exists():
            messages.error(
                request, _(f"User {username} already exists or not entered.")
            )
            error = True
        if not email or User.objects.filter(email=email).exists():
            messages.error(
                request, _(f"User with email {email} already exists or not entered.")
            )
            error = True
        if error:
            return redirect("register")
        else:
            User.objects.create_user(username=username, email=email, password=password)
            messages.success(
                request, _(f"User {username} registered successfully. You can log in")
            )
            return redirect("index")
    return render(request, "user_profile/register.html")


@login_required
def view_my_profile(request):
    return render(request, "user_profile/view_profile.html", {"user_": request.user})


@login_required
def edit_profile(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = UserProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile
        )
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(
                request, _("User {} profile was updated").format(request.user)
            )
            return redirect("view_profile")
    else:

        u_form = UserUpdateForm(instance=request.user)
        p_form = UserProfileUpdateForm(instance=request.user.profile)

    context = {
        "u_form": u_form,
        "p_form": p_form,
    }
    return render(request, "user_profile/edit_profile.html", context)
