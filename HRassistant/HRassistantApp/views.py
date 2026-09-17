from django.shortcuts import render
from .security_scanner import scan_prompt


def home(request):
    return render(request, "home.html")


def security_scanner(request):
    result = None

    if request.method == "POST":
        message = request.POST.get("message", "")
        result = scan_prompt(message)

    return render(
        request,
        "security_scanner.html",
        {"result": result}
    )