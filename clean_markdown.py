import re

def clean_text(text):
    # 1. Entferne alle HTML-Tags
    text = re.sub(r'<[^>]+>', '', text)

    # 2. Ersetze doppelte oder mehrfache Leerzeichen durch ein einzelnes Leerzeichen
    text = re.sub(r'\s+', ' ', text)

    return text.strip()

def extract_emails(text):
    # 3. Finde alle E-Mail-Adressen
    return re.findall(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+', text)

if __name__ == "__main__":
    # 4. Lies deine Eingabedatei ein
    with open("example.md", "r", encoding="utf-8") as f:
        raw_text = f.read()

    # 5. Wende die Funktionen an
    cleaned_text = clean_text(raw_text)
    emails = extract_emails(raw_text)

    # 6. Speichere die bereinigte Version
    with open("example_cleaned.md", "w", encoding="utf-8") as f:
        f.write(cleaned_text)

    # 7. Zeige gefundene E-Mails
    print("Gefundene E-Mail-Adressen:")
    for email in emails:
        print(f" - {email}")
