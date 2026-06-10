import re


def extract_experience(text):

    text = text.lower()

    pattern = r"(\d+)\+?\s*year"

    matches = re.findall(pattern, text)

    if matches:

        years = max(
            int(year)
            for year in matches
        )

        return years

    return 0