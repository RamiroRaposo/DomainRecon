import requests
import re
import json

def inf_subdmn(domain, report):

    url = f"https://crt.sh/?q=%25.{domain}&output=json"

    try:
        response = requests.get(url, timeout=10)
        
        if response.status_code != 200 or not response.text.strip().startswith('['):
            print("[!] Error querying subdomains or empty response")

        data = response.json()
        subdomains = set()

        pattern = re.compile(r"^[a-zA-Z0-9.-]+\." + re.escape(domain) + r"$")

        for entry in data:
            name = entry.get("name_value", "")
            for sub in name.split("\n"):
                if pattern.match(sub):
                    subdomains.add(sub.strip())
        
        subdmn_list = sorted(subdomains)
    
        print("[+] Subdomains found:\n")
        for s in subdmn_list:
            print(f"> {s}")

    except Exception as e:
        print(f"[!] Error obtaining subdomains: {e}")
        return []

    save = input("\nDo you want to add this information to the final report?(y/n) ")

    if domain not in report:
        report[domain] = []
    
    report[domain].append(f"SUBDOMAINS FOUNDED FOR {domain.upper()}\n\n{json.dumps(sorted(subdmn_list), indent=2, default=str)}")