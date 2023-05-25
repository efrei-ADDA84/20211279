# Projet de Prédiction Météo

Ce projet contient une application Flask qui interagit avec l'API OpenWeatherMap pour obtenir les données météorologiques actuelles pour un emplacement spécifique.

# Fonctionnalités
API qui accepte des coordonnées de latitude et de longitude en entrée
Interagit avec l'API OpenWeatherMap pour récupérer les données météorologiques
Retourne une réponse JSON avec une description de la météo, la température actuelle, la sensation thermique et l'humidité.
# Comment utiliser
Effectuez une requête GET à l'URL suivante :
http://devops-20211279.francecentral.azurecontainer.io:8081/?lat=5&lon=105

Remplacez <your-deployed-api-url>, <latitude> et <longitude> par les valeurs correspondantes.

## Installation en local
Clonez ce repository :
git clone https://github.com/efrei-ADDA84/20211279.git

## Construisez l'image Docker :
docker build -t <your-image-name> .

## Exécutez le conteneur Docker :
docker run -e API_KEY=<your-openweathermap-api-key> -p 8081:8081 <your-image-name>

L'application sera accessible à http://localhost:8081

Remarque : remplacez <your-github-username>, <your-repo>, <your-image-name> et <your-openweathermap-api-key> par les valeurs correspondantes.

# Technologies utilisées
Flask : Framework web pour le développement de l'API.
Docker : Conteneurisation de l'application pour une portabilité accrue.
OpenWeatherMap API : API tierce pour obtenir des données météorologiques.
Déploiement

# Azure Container

Ce projet est déployé sur Azure Container Instance avec l'utilisation de GitHub Actions pour le CI/CD.

Déployer mon projet sur Azure Container Instance (ACI) m'offre plusieurs avantages :

Facilité d'utilisation : ACI est conçu pour être simple et facile à utiliser. Je peux déployer un conteneur sans avoir à gérer l'infrastructure sous-jacente.

Rapidité : ACI est rapide. Je peux déployer un conteneur en quelques secondes, ce qui est beaucoup plus rapide que la plupart des autres services de conteneur.

Scalabilité : Avec ACI, je peux facilement augmenter ou diminuer le nombre de conteneurs en fonction de mes besoins. Cela rend ACI idéal pour les applications avec des charges de travail variables.

Tarification à l'utilisation : Avec ACI, je ne paye que pour ce que j'utilise. Cela signifie que je n'ai pas à payer pour des ressources inutilisées, ce qui peut me faire économiser de l'argent.

Intégration avec d'autres services Azure : ACI s'intègre facilement avec d'autres services Azure, tels que Azure Logic Apps, Azure Functions et Azure Kubernetes Service. Cela me donne une plus grande flexibilité pour créer des solutions personnalisées.

Sécurité : Azure offre de nombreuses fonctionnalités de sécurité, y compris le chiffrement au repos et en transit, les réseaux virtuels pour isoler mes conteneurs, et Azure Policy pour assurer la conformité.

Gestion des secrets : ACI s'intègre avec Azure Key Vault, ce qui me permet de gérer de manière sécurisée les secrets utilisés par mes conteneurs.

Compatibilité : Comme ACI peut exécuter n'importe quel conteneur compatible avec Docker, j'ai une grande liberté pour choisir les technologies à utiliser dans mon application.

En somme, Azure Container Instance est une excellente option si je souhaite déployer des conteneurs rapidement et facilement, sans avoir à me soucier de la gestion de l'infrastructure sous-jacente.