import whois
import json

def inf_whois(domain, report):
    
    data = whois.whois(domain)

    print(f"WHOIS INFORMATION FOR {domain.upper()}\n")

    print(json.dumps(data, indent=2, default=str))

    save = input("\nDo you want to add this information to the final report?(y/n) ")

    report.append(f"WHOIS INFORMATION FOR {domain.upper()}\n{json.dumps(data, indent=2, default=str)}")

