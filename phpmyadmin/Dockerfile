# Utiliser l'image officielle de phpMyAdmin
FROM phpmyadmin/phpmyadmin:5.0

# Définir les variables d'environnement pour la connexion à MySQL
ENV PMA_HOST=mysql
ENV PMA_PORT=3306
ENV PMA_USER=root
ENV PMA_PASSWORD=root
ENV MYSQL_DATABASE=cours_data

# Exposer le port 80 pour accéder à phpMyAdmin depuis l'extérieur du conteneur
EXPOSE 80