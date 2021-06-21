# QuizApp
Application de quiz d'événement de codage et de programmation Fbla

## À propos
Le projet est une application de quiz FBLA. Vous avez la possibilité de vous connecter, de créer des tests, de passer des tests et de les noter automatiquement.

## Installation
Vous n'avez besoin que d'un seul outil installé : Docker
1. `git clone` ou téléchargez le zip de ce fichier et extrayez. `cd` dans ce répertoire nouvellement créé.
2. `docker-compose up --build`.
3. Et c'est fait ! Visitez `localhost:8000` pour afficher le site Web. Pour arrêter le serveur, entrez `Ctrl-c`.

## Utilisation du site Web
Lorsque vous accédez à `localhost:8000`, vous serez redirigé vers une page de connexion. Vous pouvez vous inscrire en cliquant sur le bouton d'inscription sur la barre de navigation. Une fois que vous avez fait cela, vous pouvez cliquer sur créer un quiz pour créer un nouveau quiz. Ajoutez un nom et une description (facultatif), puis cliquez sur créer.

 - *Modifier un quiz*
 Dans la liste principale, cliquez sur un titre. Ensuite, puisque vous êtes le propriétaire, cliquez sur le bouton Modifier. Maintenant, vous devriez voir toutes les questions. Ajoutez une question en utilisant le formulaire. Vous pouvez également supprimer des questions en cliquant sur le bouton Supprimer. Pour de nombreuses questions, importez à partir d'un fichier `*.json*`.
 
 - *Supprimer un quiz*
 Pour supprimer, retournez à la vue détaillée du quiz. Cliquez sur le gros bouton de suppression à côté de modifier. Vous serez invité avec un modal, et vous pouvez simplement l'accepter.
 
 - *Répondre à un quiz*
 Dans la vue détaillée, cliquez sur le bouton Démarrer. Répondez au quiz en remplissant la case appropriée. Cliquez sur soumettre.
 
 - *Affichage des résultats*
 Une fois soumis, les résultats apparaissent automatiquement. Cliquez sur Afficher le PDF pour trouver une version imprimable.
 
## Extension du site Web avec des fonctionnalités avancées
La logique derrière le site est stockée dans le fichier `quiz/views.py`. Manipuler cela vous permettra de changer : le caractère aléatoire des questions, les requêtes de base de données, les exigences de connexion, les champs PDF, les soumissions de formulaires de connexion, et bien plus encore. Vous pouvez ajouter des champs de base de données personnalisés en manipulant l'ORM Django dans le fichier `models.py`. Après toute modification, exécutez : `docker-compose run web python manage.py makemigrations` et `docker-compose run web python manage.py migrate`.

## Faire
- [X] Ajouter WASM à l'application Web
- [X] Correction de la présentation
- [X] Ajouter des modules Rust
- [X] Ajouter une API avec Django Rest Framework
- [X] Ajout de Rust CLI qui utilise Reqwest

## Contributeurs
Ce projet a été créé uniquement par Abhinav Chavali, licence GNU/GPLv3
