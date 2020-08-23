# HarvardX-CS50W-final-project

This project consists of an online reading club. The users can search books, see information about them, add them to their reading list and keep track of the books they read.

To build this project I used all the languages I learned in the course (HTML, CSS, JavaScript and Python), together with Django. I also used a Google API to get information about the books.

## Global (layout.html)
For all the website, I designed, using Bootstrap, a header menu with a title and logo, some menu buttons and an integrated search bar. I also made sure it was mobile responsive. Also, I included a header image.

## Index page
In the index page, I used an integrated python method to display a random quote about books/reading.

## Top books
Displays a ranking of the books most read by the users of the webpage.

## Top readers
Displays a ranking of the top readers of the website.

## Register/Login/Logout
In the menu, we find a standard authentication system that uses the Django authentication functionalities.

## Search functionality
The user can type a book title in the search bar to search for that book in the Google Library. Then, the user can click on one of the results to open the book's information page, that displays the title, author, rating, categories, cover image..., as well as a button to open the book in the Google's store and another button to add the book to the user's reading list.

## User page
When the user clicks on its username in the menu, the user profile page is displayed. In this page, the user can see a summary of the books saved to read, currently reading and finished. The user can see which books are in the reading list and start reading it, by clicking on the "start" button, to keep track of the date she started. Then the book moves from "saved" to "reading". From the reading menu, the user can finish a book (it works just like the "start reading" button). Then the book saves the date and moves to "finished", where the user can see a summary of the books read, with the starting and finished dates.

## Project requirements
I think this project is interesting because it satisfies a need that I had, which was to keep track of the books I read.
Also, I think it is interesting because I used all the languages we used during the course, as well as the fact that this time, we weren't provided with a base project, but we had to do everything from scratch.
I used git for source control, html, css, databases, an api, bootstrap, django, python... I also think that even if it doesn't shows off much, I did a lot of research to try to implement details, that I didn't know how to do. For instance, when you visit the page of a book, you see the rating graphically with stars. Also the fact that the menu changes its format when you change from a large screen to a small one. By working in this kind of details, even if they are small things, I had to do some research and I learned things that weren't covered in the course. 
