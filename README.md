# QuizApp
Fbla Coding and Programming event quiz app

## About
The project is an FBLA Quiz App. You have the ability to log in, create tests, take tests, and have them automatically graded.

## Installation
You only need one tool installed: Docker
1. `git clone` or download the zip of this file and extract. `cd` into that newly created directory.
2. `docker-compose up --build`.
3.  And it's done! Visit `localhost:8000` to view the website. To stop the server, enter `Ctrl-c`.

## Using the website
When you go to `localhost:8000`, you will be redirected to a login page. You can sign up by clicking the sign up button on the nav-bar. Once you do that, you can click create a quiz to make a new quiz. Add a name and an (optional) description, and click create.

 - *Editing a quiz*
 In the main list view, click on a title. Then, since you are the owner, click the edit button. Now, you should see all the questions. Add a question using the form. You can also delete questions by clicking the delete button. For many questions, import from a `*.json*` file.
 
 - *Deleting a quiz*
 To delete, go back to the detail view of the quiz. Click the large delete button next to edit. You will be prompted with a modal, and you can just accept that.
 
 - *Taking a quiz*
 In the detail view, click the start button. Take the quiz by filling in the box appropriately. Click submit.
 
 - *Viewing results*
 Once submitted, the results appear automatically. Click view PDF to find a printable version.
 
## Extending the website with advanced functionality
The logic behind the site is stored in the `quiz/views.py` file. Manipulating that will allow you to change: Question randomness, Database querying, login requirements, PDF fields, Login form submissions, and much more. You can add custom database fields by manipulating the Django ORM in the `models.py` file. After any changes, run: `docker-compose run web python manage.py makemigrations` and `docker-compose run web python manage.py migrate`.

## Todo
- [X] Add WASM to Web App
- [X] Fix presentation
- [X] Add Rust modules
- [X] Add API with Django Rest Framework
- [X] Add Rust CLI that uses Reqwest

## Contributors
This project was created solely by Abhinav Chavali, GNU/GPLv3 license
