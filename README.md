# API Wars

## Story

Because you are so awesome, a golden humanoid droid wants to meet you in the nearest Kantina....

[Watch this intro!](https://starwarsintrocreator.kassellabs.io/?ref=redirect#!/BM1kT5Ezi0Q0b-Ell8TE)

Your task is to create a web application which shows data about the Star
Wars universe, store visitor preferences with cookies and handle user login with
sessions.

## What are you going to learn?

- create a Flask backend project
- use routes with Flask
- use Bootstrap
- simple queries in SQL
- use AJAX for API requests
- session handling
- store passwords

## Tasks

1. Create a web server rendering a page that shows a table with all the planets in the Star Wars universe.
    - The opening page of the website (`/`) shows data of 10 planets
    - The page has an HTML `<table>` element containing the data
    - The columns of the table are `name`, `diameter` (shown in km), `climate`, `terrain`, `surface water` (shown as percentage), `population` (formatted as `1,000,000 people`)
    - The column titles are proper table headers
    - The page follows this basic design: ![API Wars Screenshot 01](https://learn.code.cool/media/web/apiwars-screenshot-01.png)
    - There's a next button above the table, clicking that shows the next 10 planets, if any
    - There's a previous button above the table, clicking that shows the previous 10 planets, if any
    - Double clicking on the next or previous buttons shows the next/previous 10 planets only once
    - Unknown values for surface water percentage and population are stated clearly and without any suffix (e.g for planet Coruscant and Hoth)

2. Display a button in each row if the planet has residents. These buttons should open a modal, populate its data containing the list of residents with more detailed information.
    - In the planet table there is a button in each row in a new column showing the planet's number of residents if the planet has any, otherwise the `No known residents` text is shown
    - Clicking the `<n> residents` button in the planet table, a modal shows up showing all the residents of that planet (every time)
    - The modal has an HTML `<table>` element containing the data
    - The columns of the table are `name`, `height` (shown in meters), `mass` (shown in kg), `skin color`, `hair color`, `eye color`, `birth year`, `gender` (an icon representation)
    - Data is loaded into the table without page refresh (with AJAX)
    - There is an X icon in the top right corner and a `Close` button in the bottom right corner; clicking these closes the modal
    - The modal follows this basic design: ![API Wars Screenshot 02](https://learn.code.cool/media/web/apiwars-screenshot-02.png)

3. Create a simple user login system with registration page, login page and logout link in the header.
    - There is a link in the header that leads to the registration page
    - On the registration page (`/register` route) the visitor can create a username/password pair that gets stored in the database
    - Password storage and retrieval uses salted password hashing for maximum security
    - If either field is empty while clicking on the `Submit` button on the registration page the `Please, fill in both fields.` error message appears
    - If the username field contains a username that already exists in the database while clicking on the `Submit` button on the registration page the `Username already exists, please choose another one!` error message appears
    - On successful registration the `Successful registration. Log in to continue.` text is shown and the user is redirected to the login page
    - There is a link in the header that leads to the login page
    - On the login page (`/login` route) the visitor can log in using the username/password previously created during registration
    - If the username/password pair doesn't match while clicking on the `Submit` button on the login page the `Wrong username or password.` error message appears
    - After logging in, the username is displayed in the top right corner with the text `Signed in as <username>` and a logout link is shown in the header
    - Clicking the logout link (`/logout` route) logs the user out

4. [OPTIONAL] If the user is logged in, display a button in each row with which the logged in user can vote on a planet. Save this vote in a database and inform a user that the vote has been saved.
    - If the user is logged in, a `Vote` button is displayed in the planet table in a new column
    - Clicking the vote button saves the vote in the database without refreshing the page (with AJAX)
    - If the save is successful after clicking the vote button, the `Voted on planet <planetname> successfully.` message appears
    - If the save is failed after clicking the vote button, the `There was an error during voting on planet <planetname>.` error message appears
    - Users can vote on unlimited number of planets and with unlimited number of votes on a planet

5. [OPTIONAL] Create a new modal window accessible from the main page where you display the statistics about voted planets.
    - There is a link in the header that opens a modal showing voting statistics based on the user votes saved in the database
    - The modal has an HTML `<table>` element containing the data
    - The columns of the table are `Planet name`, `Received votes`
    - Data is loaded into the table without page refresh (with AJAX)
    - There is an X icon in the top right corner and a `Close` button in the bottom right corner; clicking these closes the modal
    - The modal follows this basic design: ![API Wars Screenshot 03](https://learn.code.cool/media/web/apiwars-screenshot-03.png)

6. [OPTIONAL] Do some improvements in order to make the web application easier to use.
    - Planet list is showing a loading indicator while the content is loading
    - Planet list navigation gets disabled while the requested data is loading
    - Residents modal is showing a loading indicator while the content is loading
    - Residents modal is not showing the table's header until the content is loaded
    - A nice background image is used, that fits nicely to the site and does not draw your attention out from actual content
    - If a UI framework is used (Bootstrap, Material-UI, etc), the default theme is personalized for the project and not just used without changes.

## General requirements

- For the whole assignment, get the data using [The Star Wars API](https://swapi.dev/)
- The page doesn't show a server error anytime during the review

## Hints

- The starting repository is empty on purpose.

- Use Bootstrap, if you don't want to spend too much time with design.
- For displaying various (error) messages, you can use the flash function of Flask.
- Use Javascript `modules` for cleaner codebase.

- Use a `<h1>` tag for the page heading.
- Add buttons for navigating between chunks of data (loading all planets would
  take too much resources, so SWAPI implements a pagination. Just look into it's
  response, it has a `next` and a `previous` attribute).
- Use a bordered table to display the needed information.
- You are not required to use AJAX for the base page data. If you like, you can
  use the back-end for parts of the data processing (like the planet list), BUT
  the modal windows **must** load by calling an API with AJAX. This API can be
  SWAPI directly, or you can write a proxy in your web-server. When using Bootstrap, the
  "[Varying modal content based on trigger
  button](https://getbootstrap.com/docs/4.1/components/modal/#via-javascript)"
  section of the Bootstrap documentation might help a lot.
- For the login system use sessions.
- For sending data from server side to client side with AJAX, it is advised to
  use JSON.
- You are advised to use a data schema based on this for the login system and voting tasks:
  - `users` table
    - `id` : serial, primary key
    - `username` : unique name for users - varchar
    - `password` : hashed password - varchar
  - `planet-votes` table
    - `id` : serial, primary key
    - `planet_id` : integer (id from SWAPI data)
    - `planet_name` : varchar
    - `user_id` : integer, foreign_key
    - `submission_time` : datetime

## Starting your project



## Background materials

- <i class="far fa-exclamation"></i> [The last missing piece: API](project/curriculum/materials/pages/web/the-last-missing-piece-api.md)
- <i class="far fa-book-open"></i> [RESTful](project/curriculum/materials/pages/web/restful.md)
- <i class="far fa-book-open"></i> [Front-End Frameworks and Libraries (including Bootstrap)](project/curriculum/materials/pages/javascript/frontend-libraries-and-frameworks.md)
- <i class="far fa-exclamation"></i> [A web-framework for Python: Flask](project/curriculum/materials/pages/python/python-flask.md)
- <i class="far fa-book-open"></i> [Flask documentation](http://flask.palletsprojects.com/) (the Quickstart gives a good overview)
- <i class="far fa-exclamation"></i> [Creating DOM elements](project/curriculum/materials/pages/javascript/javascript-extending-the-dom.md)
- <i class="far fa-exclamation"></i> [JavaScript modules](project/curriculum/materials/pages/javascript/javascript-modules.md)
- <i class="far fa-exclamation"></i> [Sessions](project/curriculum/materials/pages/web/authentication-sessions.md)
- <i class="far fa-exclamation"></i> [Salted password hashing functions in Werkzeug](https://werkzeug.palletsprojects.com/en/1.0.x/utils/#module-werkzeug.security)
- <i class="far fa-book-open"></i> [Web storage mechanisms](project/curriculum/materials/pages/javascript/web-storage-mechanisms.md)
- <i class="far fa-book-open"></i> [Database glossary](project/curriculum/materials/pages/sql/database-glossary.md)
- <i class="far fa-candy-cane"></i> [Flask's jsonify function](https://flask.palletsprojects.com/en/1.1.x/api/#flask.json.jsonify)

