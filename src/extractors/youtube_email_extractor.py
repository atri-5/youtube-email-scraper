thonimport requests
from bs4 import BeautifulSoup

def extract_email(profile_url, email_type="both"):
    page = requests.get(profile_url)
    soup = BeautifulSoup(page.content, "html.parser")
    
    emails = []
    if email_type == "both" or email_type == "personal":
        emails += find_emails_in_text(soup)
    
    if email_type == "both" or email_type == "business":
        emails += find_business_emails(soup)
    
    return emails[0] if emails else None

def find_emails_in_text(soup):
    # A simple regex to find emails in the text content of the page
    import re
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    return re.findall(email_pattern, soup.get_text())

def find_business_emails(soup):
    # Look for email-like text on the page
    return find_emails_in_text(soup)