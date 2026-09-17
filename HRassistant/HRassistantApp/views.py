
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from .security_scanner import scan_prompt, mask_sensitive_data
from .hr_chatbot import get_hr_response
from .response_validator import validate_response
from .models import SecurityAuditLog
from django.db.models import Count
from django.contrib.auth.decorators import login_required

@login_required(login_url="user_login")
def home(request):
    return render(request, "home.html")

def user_login(request):
    error = None

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect("security_dashboard")
        else:
            error = "Invalid username or password."

    return render(
        request,
        "login.html",
        {"error": error}
    )

def user_logout(request):
    logout(request)
    return redirect("user_login")

@login_required(login_url="user_login")
def security_scanner(request):
    result = None
    masked_message = None

    if request.method == "POST":
        message = request.POST.get("message", "")

        result = scan_prompt(message)
        masked_message = mask_sensitive_data(message)

        if result["is_suspicious"]:
            SecurityAuditLog.objects.create(
                event_type="Prompt Injection",
                message=message,
                risk_level=result["risk_level"]
            )

    return render(
        request,
        "security_scanner.html",
        {
            "result": result,
            "masked_message": masked_message,
        }
    )


@login_required(login_url="user_login")
def hr_chatbot(request):
    response = None
    validation = None

    if request.method == "POST":
        message = request.POST.get("message", "")

        response = get_hr_response(message)
        validation = validate_response(response)

        if not validation["is_safe"]:
            SecurityAuditLog.objects.create(
                event_type="Unsafe AI Response",
                message=response,
                risk_level="Medium"
            )

    return render(
        request,
        "hr_chatbot.html",
        {
            "response": response,
            "validation": validation,
        }
    )

@login_required(login_url="user_login")
def security_dashboard(request):
    total_events = SecurityAuditLog.objects.count()

    high_risk_events = SecurityAuditLog.objects.filter(
        risk_level="High"
    ).count()

    medium_risk_events = SecurityAuditLog.objects.filter(
        risk_level="Medium"
    ).count()

    recent_logs = SecurityAuditLog.objects.order_by(
        "-created_at"
    )[:10]

    return render(
        request,
        "security_dashboard.html",
        {
            "total_events": total_events,
            "high_risk_events": high_risk_events,
            "medium_risk_events": medium_risk_events,
            "recent_logs": recent_logs,
        }
    )