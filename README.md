# Application Flask pour la Gestion des Étudiants

Ce projet est une application Flask simple qui permet aux utilisateurs d'inscrire des étudiants et de consulter une liste des étudiants inscrits. Il utilise une base de données SQLite pour stocker les informations des étudiants.

## Structure du Projet

```
flask-student-app
├── static
│   ├── css
│   │   └── styles.css
│   └── js
│       └── scripts.js
├── templates
│   ├── add_student.html
│   └── students_list.html
├── app.py
├── database
│   └── students.db
└── README.md
```

## Instructions d'Installation

1. **Cloner le dépôt :**
   ```
   git clone <repository-url>
   cd flask-student-app
   ```

2. **Installer les dépendances nécessaires :**
   Il est recommandé d'utiliser un environnement virtuel. Vous pouvez en créer un avec :
   ```
   python -m venv venv
   source venv/bin/activate  # Sur Windows utilisez `venv\Scripts\activate`
   ```
   Ensuite, installez toutes les dependances :
   ```
   pip install -r requirements.txt
   ```

3. **Initialiser la base de données :**
   La base de données sera créée automatiquement lors du premier lancement de l'application.

4. **Lancer l'application :**
   ```
   python app.py
   ```
   L'application sera disponible sur `http://127.0.0.1:5000/`.

## Utilisation

- Pour ajouter un nouvel étudiant, accédez à `http://127.0.0.1:5000/students` et remplissez le formulaire avec le nom, l'email et la faculté de l'étudiant.
- Pour consulter la liste des étudiants inscrits, accédez à `http://127.0.0.1:5000/students` (requête GET).

## Fonctionnalités

- Interface conviviale pour ajouter des étudiants.
- Validation des champs obligatoires et des adresses email uniques.
- Affichage dynamique de la liste des étudiants inscrits.

## Licence


Ce projet est sous licence MIT.