from modulos.info_whois import inf_whois
import os

report = {}

def gen_report():

    rep_dir = "reports"

    if not os.path.exists(rep_dir):
        os.makedirs(rep_dir)

    for domain, seccions in report.items():
        filename = f"report_{domain}.txt"
        filepath = os.path.join(rep_dir,filename)

        with open(filepath, "w") as f:
            f.write("\n\n".join(seccions))

print("-------------------------------")
print("Automatic information gathering")
print("-------------------------------")

domain = input("Domain: ")

while True:

    os.system('cls' if os.name == 'nt' else 'clear')

    print("-------------------------------")
    print("Automatic information gathering")
    print("-------------------------------")

    print(f"DOMAIN > {domain}")

    opcion = input("""
[MENU]
1) View WHOIS
2) Search for subdomains
3) Search for public emails
4) View exposed documents
5) Search on Shodan
6) Generate the report and exit
7) Change domain
8) Exit
              
Opcion: """)
    
    print("")

    if opcion == "1":
        inf_whois(domain, report)

        new_opcion = input("\nDo you want to search for more information?(y/n) ")

        if new_opcion.lower() == "n":
            
            gen_rep_opcion = input("\nDo you want to generate the report?(y/n) ")
            
            if gen_rep_opcion.lower() == "y":
                gen_report()

                print("\n[+] Report generated > report.txt")

                break
            elif gen_rep_opcion.lower() == "n":
                break
        elif new_opcion.lower() == "y":
            pass
            
    elif opcion == "2":
        pass

    elif opcion == "3":
        pass

    elif opcion == "4":
        pass

    elif opcion == "5":
        pass

    elif opcion == "6":
        gen_report()

        print("\n[+] Report generated > report.txt")
        
        break

    elif opcion == "7":
        domain = input("New domain: ")

    elif opcion == "8":
        break