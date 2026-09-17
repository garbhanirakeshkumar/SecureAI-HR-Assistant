
import re


def validate_response(response):
    warnings = []

    # Check for email addresses
    if re.search(
        r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b',
        response
    ):
        warnings.append("Email address detected")

    # Check for 10-digit phone numbers
    if re.search(r'\b\d{10}\b', response):
        warnings.append("Phone number detected")

    # Check for password-related information
    sensitive_words = ["password", "secret key", "api key"]

    for word in sensitive_words:
        if word in response.lower():
            warnings.append("Sensitive information detected")
            break

    if warnings:
        return {
            "is_safe": False,
            "warnings": warnings,
            "message": "Response requires security review."
        }

    return {
        "is_safe": True,
        "warnings": [],
        "message": "Response passed security validation."
    }