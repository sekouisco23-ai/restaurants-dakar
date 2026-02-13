# Restaurants Dakar

Projet pour récupérer, filtrer et insérer les restaurants de Dakar dans PostgreSQL.

## Installation

1. Cloner le dépôt :
   git clone https://github.com/<username>/restaurants-dakar.git

2. Installer les dépendances :
   pip install -r requirements.txt

3. Créer un fichier .env avec :
   DATABASE_URL=postgresql://...
   GOOGLE_API_KEY=...

## Scripts

- insert_restaurants.py : insère les restaurants dans PostgreSQL
- filter_restaurants.py : filtre et affiche les restaurants

## Usage

python insert_restaurants.py
python filter_restaurants.py
