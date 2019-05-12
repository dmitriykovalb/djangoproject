from django.contrib import admin
from django.urls import path, include
from users import views as userViews
from django.contrib.auth import views as authViews
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('registration/', userViews.register, name="reg"),
    path('profile/', userViews.profile, name="profile"),
    path('user/', authViews.LoginView.as_view(template_name='users/user.html'), name="auth"),
    path('pass-reset/', authViews.PasswordResetView.as_view(
        template_name='users/pass_reset.html'), name="pass-reset"),
    path('pass-reset_confirm/<uidb64>/<token>/', authViews.PasswordResetConfirmView.as_view(
        template_name='users/password_reset_confirm.html'), name="password_reset_confirm"),
    path('pass-reset_complete/',
         authViews.PasswordResetCompleteView.as_view(
             template_name='users/password_reset_complete.html'), name="password_reset_complete"),
    path('password-reset/done/', authViews.PasswordResetDoneView.as_view(
        template_name='users/password_reset_done.html'), name="password_reset_done"),
    path('exit/', authViews.LogoutView.as_view(template_name='users/exit.html'), name="exit"),
    path('', include('blog.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)