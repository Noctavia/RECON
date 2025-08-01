import whois
import dns.resolver
import socket
import requests
import nmap
import shutil
from fpdf import FPDF
import os

def clean_domain(domain):
    for prefix in ["http://", "https://", "www."]:
        domain = domain.replace(prefix, "")
    return domain.strip("/")

def get_whois(domain):
    try:
        w = whois.whois(domain)
        return str(w)
    except Exception as e:
        return f"[WHOIS] Erreur: {e}"

def get_dns(domain):
    dns_info = ""
    try:
        for record in ['A', 'MX', 'NS']:
            answers = dns.resolver.resolve(domain, record)
            dns_info += f"{record} Records:\n"
            for rdata in answers:
                dns_info += f"  {rdata.to_text()}\n"
    except Exception as e:
        dns_info += f"[DNS] Erreur: {e}\n"
    return dns_info

def brute_subdomains(domain, wordlist='subdomains.txt'):
    found = []
    try:
        with open(wordlist, 'r') as f:
            for line in f:
                sub = line.strip()
                subdomain = f"{sub}.{domain}"
                try:
                    socket.gethostbyname(subdomain)
                    found.append(subdomain)
                except:
                    pass
    except Exception as e:
        return [f"[SOUS-DOMAINE] Erreur: {e}"]
    return found

def is_nmap_available():
    return shutil.which("nmap") is not None

def scan_ports(domain):
    if not is_nmap_available():
        return "[PORT SCAN] Nmap n'est pas installé sur ce système. Scan ignoré."
    
    nm = nmap.PortScanner()
    try:
        ip = socket.gethostbyname(domain)
        nm.scan(ip, '1-1024')
        ports_info = f"Adresse IP : {ip}\n"
        for proto in nm[ip].all_protocols():
            lport = nm[ip][proto].keys()
            for port in sorted(lport):
                state = nm[ip][proto][port]['state']
                ports_info += f"Port {port}/{proto}: {state}\n"
        return ports_info
    except Exception as e:
        return f"[PORT SCAN] Erreur lors du scan Nmap: {e}"

def fingerprint(domain):
    info = ""
    try:
        r = requests.get(f"http://{domain}", timeout=5)
        server = r.headers.get("Server", "Inconnu")
        info += f"Header Server: {server}\n"
        info += f"Code HTTP: {r.status_code}\n"
        info += f"Headers HTTP:\n"
        for header, val in r.headers.items():
            info += f"  {header}: {val}\n"
    except Exception as e:
        info += f"[FINGERPRINTING] Erreur: {e}"
    return info

class PDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 16)
        self.cell(0, 10, "Rapport de Reconnaissance", ln=True, align="C")
        self.ln(5)

    def section_title(self, title):
        self.set_font("Arial", "B", 14)
        self.set_text_color(0, 0, 128)
        self.cell(0, 10, f"[{title}]", ln=True)

    def section_body(self, body):
        self.set_font("Courier", "", 9)
        self.set_text_color(0)
        self.multi_cell(0, 5, body)
        self.ln()

def generate_pdf(report, domain, filename="rapport_recon.pdf"):
    pdf = PDF()
    pdf.add_page()
    pdf.set_font("Arial", "I", 12)
    pdf.cell(0, 10, f"Domaine analysé : {domain}", ln=True)
    pdf.ln(5)
    for section, content in report.items():
        pdf.section_title(section)
        pdf.section_body(content)
    pdf.output(filename)
    print(f"\n[+] Rapport généré : {filename}")

def reconnaissance(domaine):
    domain = clean_domain(domaine)
    print("[*] Début reconnaissance...\n")

    report = {
        "WHOIS": get_whois(domain),
        "Résolution DNS": get_dns(domain),
        "Sous-domaines trouvés": "\n".join(brute_subdomains(domain)),
        "Scan de ports": scan_ports(domain),
        "Fingerprinting du serveur web": fingerprint(domain)
    }

    generate_pdf(report, domain)

if __name__ == "__main__":
    cible = input("Entrez le domaine cible : ")
    reconnaissance(cible)