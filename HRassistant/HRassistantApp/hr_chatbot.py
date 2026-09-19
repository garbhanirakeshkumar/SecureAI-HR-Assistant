def get_hr_response(message):
    message = message.lower().strip()

    if not message:
        return "Please enter a question."

    if "leave" in message:
        return "Please check your company's leave policy or contact HR for leave-related questions."

    elif "working hours" in message or "office hours" in message:
        return "Working hours depend on your company policy. Please contact HR for confirmation."

    elif "contact hr" in message or "hr contact" in message:
        return "You can contact your HR department through the official company communication channel."

    elif "ticket" in message or "complaint" in message:
        return "You can raise an HR ticket through the company's official helpdesk."

    elif "salary" in message or "payroll" in message:
        return "For salary and payroll questions, please contact your HR or payroll department."

    elif "hello" in message or "hi" in message:
        return "Hello! I am your SecureAI HR Assistant. How can I help you?"

    else:
        return "Sorry, I don't have an answer for that question. Please contact HR for further assistance."