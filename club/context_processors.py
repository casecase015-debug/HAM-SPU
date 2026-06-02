from django.conf import settings


def site(request):
    active = ""
    if request.resolver_match:
        active = request.resolver_match.url_name or ""
    return {
        "SITE_NAME": settings.SITE_NAME,
        "SITE_SHORT": settings.SITE_SHORT,
        "SITE_TAGLINE": settings.SITE_TAGLINE,
        "CONTACT_EMAIL": settings.CONTACT_EMAIL,
        "CONTACT_PHONE": settings.CONTACT_PHONE,
        "active": active,
    }
