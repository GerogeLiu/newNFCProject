from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from . import views

urlpatterns = [
    url("^$", views.index, name='index'),
    url("^customerLogin$", views.customerLogin, name="customer_login"),
    url("^userLogin$", views.userLogin, name="user_login"),
    url("^userRegister$", views.userRegister, name="user_register"),
    url("^logout$", views.userLogout, name="logout"),
    url("^password-change$", auth_views.PasswordChangeView.as_view(
        success_url=reverse_lazy("account:password_change_done")), name='password_change'),
    url("^password-change-done$", auth_views.PasswordChangeDoneView.as_view(
        template_name="account/password_change_done.html"), name="password_change_done"),
    url("^password-reset$", auth_views.PasswordResetView.as_view(
        template_name="account/password_reset_form.html",
        success_url=reverse_lazy("account:password_reset_done")), name="password_reset"),
    url("^password-reset-done$", auth_views.PasswordResetDoneView.as_view(
        template_name="account/password_reset_done.html"), name="password_reset_done"),
    url("password-reset-confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$", auth_views.PasswordResetConfirmView.as_view(
        template_name="account/password_reset_confirm.html",
        success_url=reverse_lazy("account:password_reset_complete")), name="password_reset_confirm"),
    url("^password-reset-complete$", auth_views.PasswordResetCompleteView.as_view(
        template_name="account/password_reset_complete.html"), name="password_reset_complete"),

    url("^user-information/$", views.endUser, name="user_information"),
    url("^edit-user-information$", views.endUserEdit, name="edit_user_information"),
    url("^user-image$", views.userImage, name="user_image"),
]