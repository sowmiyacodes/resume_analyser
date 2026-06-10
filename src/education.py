def extract_education(text):

    text = text.lower()

    if "b.tech" in text:
        return "B.Tech"

    elif "b.e" in text:
        return "B.E"

    elif "m.tech" in text:
        return "M.Tech"

    elif "mca" in text:
        return "MCA"

    return "Unknown"