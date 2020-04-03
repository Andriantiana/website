Présentation:
Ceci est une application flask qui fait apparaitre un site internet plus exactement un blog
Lire attentivement ce document avant de lancer l'application


Pour lancer l'application, changer le répertoire par défaut jusqu'à l'application
Créer un environnement virtuel si premier lancement avec venv

python -m venv path\vers\Nom_du_projet

Activation
Windows>Scripts\activate.bat
Linux>source venv/bin/activate

Si non présentes, télécharger les bibliothèques nécessaires dans le fichier requierement.txt:

pip install -r path\vers\requierement.txt

Dans la ligne de commande lancer:
Windows> set FLASK_APP=microblog.py
Linux> export FLASK_APP=microblog.py


Debug
Dans un environnement de développement, mettre debug=1 pour faire apparaitre les bugs dans le navigateur (ne pas faire cela dans le deployement)
(venv) $ set FLASK_DEBUG=1 (Windows)
(venv) $ export FLASK_DEBUG=1 (Linux)

Voir database pour la configuration de la base de données


Email d'erreurs
set MAIL_SERVER=mail.yahoo.fr
set MAIL_PORT=465
set MAIL_USE_TLS=1
set MAIL_USERNAME=tianakevin.andrianina@gmail.com
set MAIL_PASSWORD=<motdepasse>
