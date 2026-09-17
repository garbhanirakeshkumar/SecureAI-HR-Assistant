from django.shortcuts import render
from .security_scanner import scan_prompt, mask_sensitive_data


def home(request):
    return render(request, "home.html")


def security_scanner(request):
    result = None
    masked_message = None

    if request.method == "POST":
        message = request.POST.get("message", "")

        result = scan_prompt(message)
        masked_message = mask_sensitive_data(message)

    return render(
        request,
        "security_scanner.html",
        {
            "result": result,
            "masked_message": masked_message,
        }
    )