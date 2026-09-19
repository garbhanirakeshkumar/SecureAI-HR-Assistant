import re


def scan_prompt(message):
    suspicious_patterns = {
        "Ignore previous instructions": r"ignore previous instructions",

        "Reveal system prompt": r"(reveal|show|tell me).*(system prompt)",

        "Bypass security": r"(bypass|disable).*(security|restriction)",

        "Reveal password": r"(reveal|show|give).*(password|secret)",

        "Role manipulation": r"you are now"
    }

    matched_rules = []

    for rule_name, pattern in suspicious_patterns.items():
        if re.search(pattern, message, re.IGNORECASE):
            matched_rules.append(rule_name)

    if matched_rules:
        return {
            "is_suspicious": True,
            "risk_level": "High",
            "matched_rules": matched_rules,
            "message": "Suspicious instruction detected."
        }

    return {
        "is_suspicious": False,
        "risk_level": "Low",
        "matched_rules": [],
        "message": "No suspicious instruction detected."
    }


def mask_sensitive_data(message):

    # Mask email addresses
    message = re.sub(
        r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b',
        '[EMAIL PROTECTED]',
        message
    )

    # Mask 10-digit phone numbers
    message = re.sub(
        r'\b\d{10}\b',
        '[PHONE NUMBER PROTECTED]',
        message
    )

    # Mask 12-digit Aadhaar-like numbers
    message = re.sub(
        r'\b\d{4}\s?\d{4}\s?\d{4}\b',
        '[ID NUMBER PROTECTED]',
        message
    )

    return message