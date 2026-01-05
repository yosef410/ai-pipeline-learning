def route_text(text):
    text = text.lower()
    if "refund" in text or "charged" in text:
        return "billing"
    if "error" in text or "crash" in text:
        return "technical"
    return "unknown"

print(route_text("I was charged twice"))
#first pipeline logic
