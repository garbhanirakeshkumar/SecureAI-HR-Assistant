from django.shortcuts import render
from .security_scanner import scan_prompt, mask_sensitive_data
from .hr_chatbot import get_hr_response
from .response_validator import validate_response

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

def hr_chatbot(request):
    response = None

    if request.method == "POST":
        message = request.POST.get("message", "")
        response = get_hr_response(message)

    return render(
        request,
        "hr_chatbot.html",
        {"response": response}
    )


def hr_chatbot(request):
    response = None
    validation = None

    if request.method == "POST":
        message = request.POST.get("message", "")

        response = get_hr_response(message)
        validation = validate_response(response)

    return render(
        request,
        "hr_chatbot.html",
        {
            "response": response,
            "validation": validation,
        }
    )