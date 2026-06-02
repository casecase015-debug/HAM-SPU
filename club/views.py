import json
from pathlib import Path

from django.conf import settings
from django.shortcuts import render

from . import data


def _load_callsigns():
    path = Path(settings.BASE_DIR) / "club" / "static" / "club" / "js" / "callsigns.json"
    with path.open(encoding="utf-8") as f:
        return json.load(f)


def home(request):
    return render(request, "club/home.html")


def about(request):
    return render(
        request,
        "club/about.html",
        {"objectives": data.OBJECTIVES, "advisors": data.ADVISORS},
    )


def policy(request):
    return render(request, "club/policy.html")


def callsign(request):
    return render(request, "club/callsign.html", {"callsigns": _load_callsigns()})


def frequencies(request):
    return render(
        request,
        "club/frequencies.html",
        {
            "freq_internal": data.FREQ_INTERNAL,
            "freq_vra": data.FREQ_VRA,
        },
    )


def project(request):
    return render(
        request,
        "club/project.html",
        {"focus_areas": data.PROJECT_FOCUS},
    )


def team(request):
    return render(
        request,
        "club/team.html",
        {"team": data.TEAM, "advisors": data.ADVISORS},
    )


def members(request):
    return render(request, "club/members.html", {"members": data.MEMBERS})
