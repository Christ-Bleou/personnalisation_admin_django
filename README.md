# Personnalisation Admin Django
Package pour moderniser Django Admin.

---

# 🚀 Django Custom Admin Pro

**Django Custom Admin Pro** est un package léger et moderne conçu pour transformer l'interface d'administration par défaut de Django en un véritable tableau de bord analytique. Fini le design de 2010 : place à **Bootstrap 5**, **FontAwesome** et des graphiques interactifs avec **Chart.js**.

---

## ✨ Points Forts

* **Design Moderne :** Intégration complète de **Bootstrap 5** pour une interface responsive et élégante.
* **Dashboards Dynamiques :** Configurez vos graphiques (Bar, Line, Pie) directement depuis l'interface admin.
* **Performance :** Chargement asynchrone des données via Chart.js pour ne pas ralentir l'expérience utilisateur.
* **Simple & Léger :** Zéro configuration complexe. Installez, ajoutez à vos apps, et profitez.

---

## 🛠️ Installation

Installez le package via pip (une fois publié ou en local) :

```bash
pip install django-custom-admin-pro

```

### Configuration

Dans votre fichier `settings.py`, ajoutez l'application **au-dessus** de l'admin de Django :

```python
INSTALLED_APPS = [
    'custom_admin', # Doit être AVANT django.contrib.admin
    'django.contrib.admin',
    'django.contrib.auth',
    # ... autres apps
]

```

Lancez ensuite les migrations pour créer les tables de configuration des graphiques :

```bash
python manage.py migrate

```

---

## 📊 Utilisation : Ajouter un Graphique

1. Rendez-vous dans la section **Custom Admin** de votre interface d'administration.
2. Créez un nouvel objet **Admin Graph**.
3. Remplissez les informations :
* **App Label :** ex: `auth`
* **Model Name :** ex: `User`
* **Type :** Choisissez entre Bar, Pie, ou Line.


4. Enregistrez. Votre graphique apparaît instantanément sur votre Dashboard !

---

## 🎨 Personnalisation

Vous pouvez surcharger les couleurs principales directement dans votre `settings.py` :

| Variable | Description | Valeur par défaut |
| --- | --- | --- |
| `CUSTOM_ADMIN_THEME` | Couleur de la barre de navigation | `#343a40` (Dark) |
| `CUSTOM_ADMIN_SIDEBAR` | Couleur de la sidebar | `#ffffff` (White) |

---

## 🏗️ Stack Technique

* **Backend :** Python & Django
* **Frontend :** Bootstrap 5, FontAwesome 6, Chart.js
* **Packaging :** Hatch
* **Test Environment :** Virtualenv

---

## 🤝 Contribution

Les contributions sont les bienvenues ! Pour toute suggestion ou bug, n'hésitez pas à ouvrir une *Issue* ou une *Pull Request* sur le dépôt GitHub.

> **Note :** Ce projet a été développé avec passion dans le cadre d'un projet académique à l'IIT, visant à améliorer l'expérience utilisateur des administrateurs Django.

---

## 📄 Licence

Distribué sous la licence MIT. Voir `LICENSE` pour plus d'informations.