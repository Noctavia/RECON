Domaine</h1>
<p align="center">
  Script Python complet pour l'audit et la génération de rapport PDF<br>
  <b>WHOIS</b> • <b>DNS</b> • <b>Sous-domaines</b> • <b>Scan de ports</b> • <b>Fingerprinting serveur</b>
</p>
---
## ⚙️ Fonctionnalités
- 🔍 Analyse WHOIS du domaine
- 🌐 Résolution DNS (A, MX, NS)
- 🧭 Bruteforce de sous-domaines via wordlist
- 🚪 Scan de ports ouverts (1-1024) via Nmap
- 🧠 Fingerprinting du serveur HTTP (bannières, headers)
- 📄 Génération automatique d'un rapport PDF
---
## 📦 Installation
### 1. Prérequis Python
```bash
pip install fpdf python-nmap dnspython whois requests
