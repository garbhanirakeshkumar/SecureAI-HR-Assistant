
import re


def scan_prompt(message):

    message = message.lower().strip()

    high_risk_patterns = {
        "Ignore previous instructions": r"ignore previous instructions",

        "Reveal system prompt": r"(reveal|show|tell me).*(system prompt)",

        "Bypass security": r"(bypass|disable).*(security|restriction)",

        "Reveal password": r"(reveal|show|give).*(password|secret)",

        "Role manipulation": r"you are now"
    }

    medium_risk_patterns = {
        "Employee personal information": (
            r"(show|give|tell me).*(employee data|personal information)"
        ),

        "Confidential information": (
            r"(show|give|reveal).*(confidential|private information)"
        ),

        "Employee salary information": (
            r"(show|give|tell me).*(employee salary|salary details)"
        )
    }

    matched_rules = []

    # Check High Risk patterns
    for rule_name, pattern in high_risk_patterns.items():

        if re.search(pattern, message, re.IGNORECASE):
            matched_rules.append(rule_name)

    if matched_rules:

        return {
            "is_suspicious": True,
            "risk_level": "High",
            "matched_rules": matched_rules,
            "message": "High-risk instruction detected."
        }

    # Check Medium Risk patterns
    for rule_name, pattern in medium_risk_patterns.items():

        if re.search(pattern, message, re.IGNORECASE):
            matched_rules.append(rule_name)

    if matched_rules:

        return {
            "is_suspicious": True,
            "risk_level": "Medium",
            "matched_rules": matched_rules,
            "message": "Medium-risk instruction detected."
        }

    # Normal prompt
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