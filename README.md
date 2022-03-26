# TER
Projet de recherche concernant la détection d'anomalies dans le domaine de la e-Santé. 
Notre algorithme se base sur les données statistiques pour détecter les anomalies vraisemblables et non dûes à des problèmes de capteurs provoquant des valeurs incohérentes. 
Ce dépôt a donc pour but de comparer notre algorithme à des algorithmes déjà existants. 
## Description des fichiers 
* Classifiers.ipynb : Utilise Xboost et provient du dépôt suivant : https://github.com/ynaveena/COVID-19-vs-Influenza ***Attention Shap peut provoquer des problèmes avec des versions trop récentes de numpy --> Veuillez passer par Google Colab***
* Covid-CT-Lung.ipyng : Utilise un CNN et provient du dépôt suivant : https://github.com/rabia174/COVID-19-Deep-Learning-CNN-Model
* pyDeepInsight : Bibliothèque Python transformant des données en images pour le CNN ci-dessus et qui provient de : https://github.com/alok-ai-lab/pyDeepInsight
* TER.yaml : Fichier de configuration de l'environnement Anaconda pour faire tourner les différents notebook
