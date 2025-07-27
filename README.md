<h1 align="center">🕵️‍♂️ Domain Recon Toolkit</h1>
<p align="center">
  <strong>Analyse complète de domaines — en un seul script Python.</strong><br>
  WHOIS • DNS • Sous-domaines • Scan de ports • Fingerprinting HTTP • Rapport PDF
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10%2B-blue?logo=python">
  <img src="https://img.shields.io/badge/License-Free-green">
  <img src="https://img.shields.io/badge/Scan-Nmap-critical?logo=nmap">
  <img src="https://img.shields.io/badge/Output-PDF-lightgrey?logo=adobeacrobatreader">
</p>

---

## 🧠 Aperçu

Ce script réalise automatiquement une phase complète de reconnaissance sur un domaine donné :

- 🔎 **Analyse WHOIS**
- 🌐 **Résolution DNS (A, MX, NS)**
- 🧭 **Bruteforce de sous-domaines via `subdomains.txt`**
- 🚪 **Scan de ports avec Nmap (1–1024)**
- 🧠 **Fingerprinting du serveur HTTP (headers, bannière)**
- 📝 **Génération d’un rapport PDF clair et lisible**

---

## 📦 Installation

### 🔧 Dépendances Python

```bash
pip install fpdf python-nmap dnspython whois requests
