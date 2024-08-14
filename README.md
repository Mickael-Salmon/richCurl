# 🔥 cURL Command Line Interface (CLI) with Rich
<p align="center">
  <img src="./banner.webp" alt="cURL CLI" width="200"/>
</p>
Bienvenue dans le projet <strong>richCurl</strong>  ! 🚀

Ce script Python te permet d'exécuter des commandes `curl` courantes à travers une interface en ligne de commande interactive et colorée, propulsée par la bibliothèque <strong>Rich</strong> .

## 📋 Sommaire
- [🚀 Fonctionnalités](#-fonctionnalités)
- [💾 Installation](#-installation)
- [🛠️ Utilisation](#%EF%B8%8F-utilisation)
- [📚 Exemples](#-exemples)
- [📜 Licence](#-licence)

## 🚀 Fonctionnalités
- 🌐 Fetch data from a URL
- 💾 Download files
- 🔄 Send POST and PUT requests
- 📬 Fetch HTTP headers
- 🔧 Utilize proxies, custom headers, and more!
- 🍪 Manage cookies during requests
- 🕵️ Set custom User-Agent strings
- 🔍 Verbose output for detailed debugging
- 📊 Progress bars and silent modes for seamless experiences

## 💾 Installation

### Prérequis
- Python 3.x
- `pip` pour installer les dépendances

### Étapes d'installation

1. **Clone le repository :**
    ```bash
    gh repo clone Mickael-Salmon/richCurl
    cd richCurl
    ```

2. **Installer les dépendances :**
    ```bash
    pip install rich
    ```

3. **Exécute le script :**
    ```bash
    python richCurl.py
    ```

## 🛠️ Utilisation

Après avoir installé les dépendances et lancé le script, tu verras apparaître un menu interactif dans le terminal. Suis les instructions pour exécuter différentes commandes `curl`.

### Commandes disponibles

- **1. 🌐 Fetch data from a URL** : Récupère le contenu d'une page web.
- **2. 💾 Download a file** : Télécharge un fichier depuis une URL.
- **3. 🔄 Send a POST request** : Envoie une requête POST avec des données personnalisées.
- **4. 📬 Fetch HTTP headers** : Récupère les en-têtes HTTP d'une URL.
- **...** : Et bien plus encore ! Consulte le menu pour voir toutes les options.

### Quitter
- **q. Quit** : Quitte le programme.

## 📚 Exemples

### 🌐 Récupérer le contenu d'une page web
1. Sélectionne `1. Fetch data from a URL`.
2. Entre l'URL que tu veux récupérer, par exemple `https://www.example.com`.
3. Le contenu de la page s'affiche dans le terminal.

### 💾 Télécharger un fichier
1. Sélectionne `2. Download a file`.
2. Entre l'URL du fichier, par exemple `https://www.example.com/file.txt`.
3. Le fichier est téléchargé dans le répertoire courant.

## 📜 Licence

Free, quick and Fun script.

## 📚 Bibliothèque utilisée

Ce projet utilise la bibliothèque [Rich](https://github.com/Textualize/rich) pour afficher une interface en ligne de commande élégante et colorée.

### À propos de Rich
**Rich** est une bibliothèque Python qui rend l'affichage dans le terminal plus attractif et interactif. Elle permet de facilement créer des tables, des barres de progression, des logs colorés, et bien plus encore. Grâce à Rich, ce projet bénéficie d'une interface utilisateur moderne et agréable à utiliser.

---

Un grand merci aux créateurs de Rich pour cette formidable bibliothèque qui a grandement facilité la création de ce projet. 🙏


---

✨ **Améliorez vos interactions avec cURL grâce à cette interface CLI moderne et colorée !** ✨

