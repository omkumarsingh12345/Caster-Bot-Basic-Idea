import pytesseract

def detect_event(frame):
    text = pytesseract.image_to_string(frame)

    if "Victory" in text:
        return "win"
    elif "Killed" in text:
        return "kill"
    elif "Low Health" in text:
        return "low_health"
    else:
        return None
