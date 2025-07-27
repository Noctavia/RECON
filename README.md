# 🔎 Reconnaissance Automatisée de Domaine

<div align="center">

**Script Python complet pour l'audit de sécurité et la reconnaissance de domaines**

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Security](https://img.shields.io/badge/Purpose-Security%20Testing-red.svg)](/)

*WHOIS • DNS • Sous-domaines • Scan de ports • Fingerprinting serveur*

</div>

---

## 🎯 Vue d'ensemble

Ce script Python automatise les phases de reconnaissance passive et active lors d'audits de sécurité. Il collecte des informations sur un domaine cible et génère un rapport PDF professionnel avec tous les résultats obtenus.

> ⚠️ **Important** : Cet outil est destiné uniquement aux tests de pénétration autorisés et à l'audit de vos propres systèmes. L'utilisation sur des domaines tiers sans autorisation est illégale.

## ⚙️ Fonctionnalités

### 🔍 Reconnaissance passive
- **Analyse WHOIS** - Informations sur le propriétaire et l'enregistrement
- **Résolution DNS** - Enregistrements A, MX, NS, CNAME, TXT
- **Détection de technologies** - Stack technique utilisée

### 🎯 Reconnaissance active  
- **Découverte de sous-domaines** - Bruteforce via wordlist personnalisable
- **Scan de ports** - Détection des services ouverts (ports 1-1024)
- **Fingerprinting HTTP** - Bannières serveur, headers de sécurité
- **Détection de CMS** - WordPress, Drupal, Joomla, etc.

### 📊 Génération de rapport
- **Rapport PDF automatique** - Mise en page professionnelle
- **Graphiques et statistiques** - Visualisation des données collectées
- **Recommandations de sécurité** - Suggestions d'amélioration

---

## 📦 Installation

### Prérequis système

- **Python 3.8+** 
- **Nmap** installé sur le système
- **Connexion Internet** pour les requêtes DNS/WHOIS

### 1. Cloner le repository

```bash
git clone https://github.com/Noctavia/RECON.git
cd RECON
```

### 2. Installer les dépendances Python

```bash
pip install -r requirements.txt
```

**Ou manuellement :**
```bash
pip install fpdf python-nmap dnspython whois requests beautifulsoup4 python-whois
```

### 3. Installation de Nmap

**Ubuntu/Debian :**
```bash
sudo apt-get install nmap
```

**CentOS/RHEL :**
```bash
sudo yum install nmap
```

**Windows :**
Télécharger depuis [nmap.org](https://nmap.org/download.html)

**macOS :**
```bash
brew install nmap
```

---

## 🚀 Utilisation

### Utilisation basique

```bash
python reconnaissance.py -d example.com
```

### Options avancées

```bash
python reconnaissance.py -d example.com -o rapport_custom.pdf -w wordlist_custom.txt -p 1-65535
```

### Paramètres disponibles

| Option | Description | Exemple |
|--------|-------------|---------|
| `-d, --domain` | Domaine cible (obligatoire) | `example.com` |
| `-o, --output` | Nom du fichier PDF de sortie | `rapport.pdf` |
| `-w, --wordlist` | Wordlist pour sous-domaines | `subdomains.txt` |
| `-p, --ports` | Plage de ports à scanner | `1-1000` |
| `-t, --threads` | Nombre de threads | `50` |
| `--timeout` | Timeout des requêtes (secondes) | `5` |
| `-v, --verbose` | Affichage détaillé | - |

### Exemple de session

```bash
$ python reconnaissance.py -d example.com -v

[+] Démarrage de la reconnaissance pour : example.com
[+] Analyse WHOIS...
[+] Résolution DNS...
[+] Découverte de sous-domaines...
    ├── www.example.com (192.168.1.1)
    ├── mail.example.com (192.168.1.2)
    └── api.example.com (192.168.1.3)
[+] Scan de ports...
[+] Fingerprinting des services...
[+] Génération du rapport PDF...
[✓] Rapport généré : example.com_reconnaissance.pdf
```

---

## 📁 Structure du projet

```
domain-reconnaissance/
├── reconnaissance.py       # Script principal
├── requirements.txt        # Dépendances Python
├── wordlists/             # Listes de mots pour sous-domaines
│   ├── common.txt         # Sous-domaines courants
│   └── extended.txt       # Liste étendue
├── templates/             # Templates pour le rapport PDF
├── output/               # Rapports générés
└── README.md             # Ce fichier
```

---

## 📄 Contenu du rapport PDF

Le rapport généré contient les sections suivantes :

1. **Résumé exécutif** - Vue d'ensemble des résultats
2. **Informations WHOIS** - Détails de l'enregistrement
3. **Analyse DNS** - Tous les enregistrements trouvés
4. **Sous-domaines découverts** - Liste complète avec IPs
5. **Services et ports ouverts** - Détail par service
6. **Fingerprinting HTTP** - Headers et technologies
7. **Recommandations** - Suggestions de sécurisation

---

## ⚡ Performance et optimisation

- **Multithreading** : Scan parallèle des sous-domaines et ports
- **Cache DNS** : Évite les requêtes redondantes
- **Rate limiting** : Respecte les limites des serveurs cibles
- **Timeout configurables** : Adaptation selon la connectivité

---

## 🛡️ Considérations légales

- ✅ Utilisez uniquement sur vos propres domaines
- ✅ Obtenez une autorisation écrite pour les tests tiers
- ✅ Respectez les conditions d'utilisation des services
- ❌ Ne pas utiliser à des fins malveillantes
- ❌ Ne pas surcharger les serveurs cibles

---

## 🤝 Contribution

Les contributions sont les bienvenues ! Pour contribuer :

1. **Fork** le projet
2. **Créer** une branche pour votre fonctionnalité
3. **Commit** vos changements
4. **Push** vers la branche
5. **Ouvrir** une Pull Request

---

## 📝 Changelog

### Version 2.1.0
- ✨ Ajout de la détection CMS
- 🔧 Amélioration des performances de scan
- 📊 Nouveaux graphiques dans le rapport

### Version 2.0.0
- 🎨 Refonte complète de l'interface
- 📄 Nouveau format de rapport PDF
- 🔍 Support des sous-domaines avec wildcards

---

## 📞 Support

- **Issues** : [GitHub Issues](https://github.com/username/domain-reconnaissance/issues)
- **Documentation** : [Wiki du projet](https://github.com/username/domain-reconnaissance/wiki)
- **Email** : security@example.com

---

## 📜 Licence

Ce projet est sous licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus de détails.

---

<div align="center">

**⭐ N'oubliez pas de mettre une étoile si ce projet vous aide ! ⭐**

*Développé avec ❤️ pour la communauté cybersécurité*

</div>
