// Creating key.pem & cert.pem: -->
openssl req -newkey rsa:2048 -new -nodes -x509 -days 3650 -keyout key.pem -out cert.pem

Etape 1 - Créer un dyndns (gratuit): Pour commencer les ip des boxes peuvent changer donc il faut un programme (client) qui va chercher l'adresse publique de la boxe et le lier au nom de domaine dyndns
(www.dynu.com a la possibilité qu'on lui associe directement notre ip publique au nom de domaine créé)

Etape 2: Rendre l'Ip de ton serveur fixe en utilisant l'adresse mac via la boxe

Etape 3 - port forwarding: Lier le numéro de port a une ip d'ordinateur (le serveur)

Etape 3 bis - Trouver un moyenne de créer le ssl

___
Partie changer Http en Https

sudo apt-get instal certbot

sudo certbot certonly --manual
    - In the process it will ask you for the domain name: 'glencho.casacam.net'
    
    http://glencho.casacam.net/.well-known/acme-challenge/uTmrvNCXQXbkHwMUr0hiC00F7arKgiGBNALszqs47Bo


???BaseHTTPRequestHandler /cgi-bin/luci/;stok=/locale
