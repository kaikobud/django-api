from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls import url

from dj_rest_auth.registration.views import VerifyEmailView
from dj_rest_auth.views import *

# drf_yasg code starts here
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="Django React Project API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="kaikobudsarker@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    # this url is used to generate email content
    path('api/rest_auth/password/reset/', PasswordResetView.as_view(), name='rest_password_reset'),
    path('api/rest_auth/password/reset/confirm/', PasswordResetConfirmView.as_view(), name='rest_password_reset_confirm'),
    path('api/rest_auth/login/', LoginView.as_view(), name='rest_login'),
    # URLs that require a user to be logged in with a valid session / token.
    path('api/rest_auth/logout/', LogoutView.as_view(), name='rest_logout'),
    path('api/rest_auth/user/', UserDetailsView.as_view(), name='rest_user_details'),
    path('api/rest_auth/password/change/', PasswordChangeView.as_view(), name='rest_password_change'),

    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('api/rest_auth/', include('dj_rest_auth.urls')),
    path('api/rest_auth/registration/', include('dj_rest_auth.registration.urls')),
    path('api/rest_auth/account-confirm-email/', VerifyEmailView.as_view(), name='account_email_verification_sent'),

    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

if getattr(settings, 'REST_USE_JWT', False):
    from rest_framework_simplejwt.views import (
        TokenRefreshView, TokenVerifyView,
    )
    urlpatterns += [
        path('api/rest_auth/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
        path('api/rest_auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    ]