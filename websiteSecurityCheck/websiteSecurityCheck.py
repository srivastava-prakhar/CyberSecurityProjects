import requests
from bs4 import BeautifulSoup
import time

max_attempts = 3
lockout_time = 30 

def log_results(results):
    with open("scan_report.txt", "a") as f:
        f.write(results + "\n")

def scan_url(url):
    print(f"Scanning {url}...")
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print("Successfully accessed the URL.")
            return response.text
        else:
            print(f"Failed to access {url}. Status code: {response.status_code}")
            log_results(f"Failed to access {url}. Status code: {response.status_code}")
            return None
    except Exception as e:
        print(f"Error accessing {url}: {str(e)}")
        log_results(f"Error accessing {url}: {str(e)}")
        return None

def check_sql_injection(url):
    print("Checking for SQL Injection...")
    injection_url = f"{url}' OR '1'='1"
    try:
        response = requests.get(injection_url)
        if "error" in response.text.lower() or "syntax" in response.text.lower():
            result = "Potential SQL injection vulnerability detected!"
            print(result)
            log_results(result)
        else:
            result = "No SQL injection vulnerability detected."
            print(result)
            log_results(result)
    except Exception as e:
        print(f"Error in SQL injection check: {str(e)}")
        log_results(f"Error in SQL injection check: {str(e)}")

def check_xss(url):
    print("Checking for XSS...")
    xss_payload = "<script>alert('XSS')</script>"
    try:
        response = requests.get(f"{url}?param={xss_payload}")
        if xss_payload in response.text:
            result = "Potential XSS vulnerability detected!"
            print(result)
            log_results(result)
        else:
            result = "No XSS vulnerability detected."
            print(result)
            log_results(result)
    except Exception as e:
        print(f"Error in XSS check: {str(e)}")
        log_results(f"Error in XSS check: {str(e)}")

def main():
    target_url = input("Enter the URL to scan: ")
    page_content = scan_url(target_url)
    if page_content:
        check_sql_injection(target_url)
        check_xss(target_url)
        print("Scan complete.")
        log_results("Scan complete for " + target_url)

if __name__ == "__main__":
    main()
