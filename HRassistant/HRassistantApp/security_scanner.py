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