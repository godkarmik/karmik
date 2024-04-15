import requests
import time

def request(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    try:
        n_url = "http://" + url
        response = requests.get(n_url, headers=headers, timeout=10)
        if response.status_code == 200:
            return response
        else:
            return None
    except requests.exceptions.RequestException:
        return None
    except KeyboardInterrupt:
        print("[!]ERROR KEYBOARD INTERRUPTION ")
        exit()

def main():
    target_url = input("[+]ENTER DOMAIN TO CRAWL: ")
    with open("/home/bhavya/Desktop/sub_domain_list.txt", "r") as wordlist:
        for line in wordlist:
            word = line.strip()
            final_url = word + "." + target_url
            response = request(final_url)
            if response:
                print(f"[+]DISCOVERED SUBDOMAIN AT: {final_url}")

if __name__ == "__main__":
    main()
