# Démarrage :

Pour lancer le projet, exécuter le `docker-compse.yaml` à la racine du projet:
```bash
docker-compose --build -d
```

# Utilisation :

## PhpMyAdmin :
PhpMyAdmin est disponible localement sur le port 8080 [http://localhost:8080/](http://localhost:8080/).

## MySQL :
MySQL est disponible localement au port 3306. Par défaut, l'identifiant et `root` et le mot de passe est `root`.

## Environnement Python :
Le projet embarque un environement de développement Python. Le volume se trouve dans ./app. Pour lancer le container :
```bash
docker exec -it cours_data_python bash
```