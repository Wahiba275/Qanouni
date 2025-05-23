
# ⚖️ Chatbot Dyal L9anoun b Darija 🇲🇦

Un chatbot intelligent conçu pour répondre aux questions juridiques en dialecte marocain (Darija) à l’aide du modèle GPT-4.

---

## 🧭 Table des Matières

- [Introduction](#introduction)
- [Architecture technique du projet](#architecture-technique-du-projet)
- [Prérequis](#prérequis)
- [Fonctionnalités principales](#fonctionnalités-principales)
- [Installation et Lancement](#installation-et-lancement)
- [Personnalisation](#personnalisation)
- [Perspectives futures](#perspectives-futures)
- [Aperçu du Chatbot](#aperçu-du-chatbot)
- [Crédits](#crédits)

---

## 📌 introduction

Ce projet vise à démocratiser l’accès à l’information juridique pour les citoyens marocains en proposant un chatbot capable de comprendre et répondre en **darija**, sur des sujets tels que le droit du travail, le droit de la famille, les contrats, l’héritage, etc.

---

## 🧱 Architecture technique du projet

Voici une vue d'ensemble de l'architecture du chatbot :

![Architecture du projet](images/architecture.png)

---

## 🛠️ Prérequis

![Python](https://img.shields.io/badge/-Python-blue?logo=python)
![Streamlit](https://img.shields.io/badge/-Streamlit-ff4b4b?logo=streamlit)
![Langchain](https://img.shields.io/badge/-LangChain-yellow)
![OpenAI](https://img.shields.io/badge/-OpenAI-black?logo=openai)
![dotenv](https://img.shields.io/badge/-dotenv-green)
![Git](https://img.shields.io/badge/-Git-black?logo=git)

---

## 🚀 Fonctionnalités principales

- 💬 Dialogue en **darija marocaine**
- 🧑‍⚖️ Réponses ciblées sur le droit marocain
- 🧠 Mémoire contextuelle pour un échange naturel
- 🔒 Masquage automatique des réponses non juridiques
- 🌍 Facile à héberger localement ou en ligne

---

## ⚙️ Installation et Lancement

```bash
# 1. Cloner le projet
git clone https://github.com/Wahiba275/Qanouni.git
cd Qanouni

# 2. Installer les dépendances
pip install -r requirements.txt

# 3. Ajouter votre clé API dans .env
echo "OPENAI_API_KEY=your_openai_key_here" > .env

# 4. Lancer l'application
streamlit run chatbot_darija.py
```

---

## 🧩 Personnalisation

- Modifier le **prompt** dans `chatbot_darija.py` pour adapter le style ou ajouter des consignes spécifiques.
- Ajouter des outils avec Langchain (`Tool.from_function`) pour intégrer des recherches externes, des bases de données ou des documents juridiques personnalisés.

---

## 💡 Perspectives futures

| Idée | Description |
|------|-------------|
| 🔍 RAG (Retrieval-Augmented Generation) | Connecter le chatbot à une base de données juridique marocaine |
| 📑 Résumés PDF | Uploader un contrat et recevoir un résumé en darija |
| 🧾 Génération automatique | Générer un modèle de plainte ou de contrat |
| 📱 Application mobile | Version Android/iOS du chatbot |
| 🔐 Authentification | Ajouter un espace utilisateur sécurisé pour historiser les échanges |

---

## 🖼️ Aperçu du Chatbot

| Question en darija | Réponse générée |
|--------------------|------------------|
| `Chno l9anoun dyal lwiratha ?` | `F lmaghrib, lwiratha katsir 3la 7asab l9orba...` |
| `Chno houwa l9anoun lmaghribi ?` | `L9anoun lmaghribi howa majmou3a dyal lwa9anin...` |

---


