# 🍽️ Restaurants Dakar API

API permettant de récupérer les restaurants de Dakar stockés dans PostgreSQL et accessible en ligne.

---

## 🌐 Accès à l’API

Après déploiement sur Render :

* Accueil → `/`
* Restaurants → `/restaurants`

Exemple :
https://ton-service.onrender.com/restaurants

---

## ⚙️ Technologies

* Python
* Flask
* PostgreSQL
* Gunicorn
* Render

---

## 🚀 Déploiement

Le projet est prêt pour un déploiement automatique.

### Fichiers importants

* `app.py` → API Flask
* `requirements.txt` → dépendances
* `Procfile` → commande de démarrage

### Commande de démarrage

gunicorn app:app

### Variables d’environnement (Render → Environment)

DATABASE_URL=postgresql://...
GOOGLE_API_KEY=...

---

## 📊 Endpoints

### GET /

Retour :
Service Restaurants Dakar actif ✅

### GET /restaurants

Retourne la liste des restaurants en JSON

---

## 💻 Lancer en local (optionnel)

Installer dépendances :
pip install -r requirements.txt

Créer `.env` :
DATABASE_URL=postgresql://...
GOOGLE_API_KEY=...

Lancer :
python app.py
