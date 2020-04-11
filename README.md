# Rodfendr
 
## Fourth Milestone Project -Full Stack Frameworks with Django Milestone Project - Code Institute April 2020
 
### What is the purpose of this App?
 
This app allows the visitor to look at the different products which are available to purchase at Rodfendr.  On the visitors first visit to the site there is a modal which pops up and requires the visitor accepts that there are cookies on the site, this will only pop up once unless the visitor clears their browser and loads the site again in which case the modal will reopen. There is a search funtion which allow the visitor to search for products. There is also a back to top button which is particularly useful if someone is looking through our legal pages. 

Click on the image to go to the live app.
 
[![Responsive Design](https://alans-ecommerce.s3-eu-west-1.amazonaws.com/static/images/responsive.png "Responsive Design")](https://rodfendr.herokuapp.com/)
 
### Summary
 
* [UX](#ux)
* [Strategy](#strategy)
* [Scope](#scope)
* [Structure](#structure)
* [Skeleton](#skeleton)
* [Surface](#surface)
* [Features](#features)
    * [Existing Features](#existing-features)
    * [Future Features](#future-features)
* [Database](#database)
* [Technologies](#technologies)
* [Testing](#testing)
* [Deployment](#deployment)
* [Media](#media)
* [Credits](#credits)
 
### UX
 
User expectations:
 
A visitor to the app will expect to see a well themed app with relevant information.  This app has the potential to hold a lot of information for that reason I decided to add pagination.  I have limited my pages to 8 flies so that the visitor is not overwhelmed by too much information.  The hero image is also selected to remind the visitor of that precious moment when a fish takes your fly.  In this way I hope that they will feel encouraged to interact more with the app and to even click on the link to the sponsors page and make a purchase.  I sent the app link to several fly fishermen and fly tiers and the feedback was that it was a nice app and would be very useful.
 
### Strategy
 
I want the visitor to immediately think of fly fishing and the excitement of connecting with a fish.  I want them to learn how to tie the flies that they might need for their next fishing trip and I want them to start to think about Rodfendr Pro and to get curious enough to visit the page through the link in the top and bottom nav bars and consider making a purchase.
 
### Scope
 
The app is designed to get the visitor to think about what flies they have, and which flies they can make themselves while adding their own creations and allowing others to see what can be done.  There is also the subtle reminder that this app is sponsored by Rodfendr Pro and they might consider visiting the sponsors page to get more information or make a purchase.
 
### Structure
 
The page is made to make the visitor want to tie a fly and go fishing with a large 'Hero' image and the relevant information pertaining to each fly and how to make it below.  The site is paginated to ensure that the visitor is not overwhelmed.  I added a search by fly name and a search by submitted by.  Some people will want to search by those who have submitted the fly as fly tying could be considered an artform with different artists having a better reputation.
 
[Back to Top](#summary)
 
### Skeleton
 
1. [Landing page wireframe](https://alans-ecommerce.s3-eu-west-1.amazonaws.com/static/images/landingpage.png)
2. [Contact page wireframe](https://alans-ecommerce.s3-eu-west-1.amazonaws.com/static/images/contact.png)
3. [Legal page wireframe](https://alans-ecommerce.s3-eu-west-1.amazonaws.com/static/images/legal.png)
 
### Surface
The colours were chosen to contrast easily and make it easier for the visitor to see the content.  The site is supposed to look clean and clear without clutter so that the visitor can concentrate on the products which sre the main focus of the site.  
 
## Features
 
### Existing Features:
 
The top navigation bar contains a link to the landing page which is marked as Home and has a house icon you can return home from any page by using this button,  there is also a contact page which is an active email request and is marked as contact us with a speech bubble icon.
 

 
The search bar has two options for the visitor:
1. The search by fly name allows the visitor to search for the information regarding a specific fly by it's name, it is not case sensitive and will search for single letters also giving a full list of fly names which match the input.  This search is paginated again to 8 flies so as not to overload the visitor.
2. The search by submitted by allows the visitor to search for flies that have been submitted by a specific contributor to the database. This is not case sensitive and will search with only a letter also returning all the contributors who have submitted to the database matching the input. This search is also paginated as above.
 
The Add Fly button is highlighted in green and is in the middle of the page this allows a contributor to add all the components of a fly it's name etc and a link to further instructions if they wish and they can also add their own name or company name as the one who submitted the information.(Create)
 
All the flies in the database are then listed they are paginate into pages of 8 flies so as not to overload the page,  they have a dropdown menu which contains all the components of each fly, the name of the fly, and options to edit or delete flies.(Read, Update and Delete) I have purposefully prevented some flies from being edited or deleted, I don't want anyone to accidentally or purposefully delete or edit all the entries.
 
The bottom navigation bar has the same home button as the top and will return the visitor home from any page,  it also has a privacy page, it is marked with a legal scales icon, which is a step towards making the app a legal page. There are several links to social media sites which are marked by their brand icons and all of these will take the visitor to a social media page owned by the sponsor Rodfendr.  Finally there is a buy button as in the top bar for Rodfendr Pro again marked with an orange credit card logo to draw the visitors attention and encourage them to visit the sponsors website.
 
I did include a back to top button but when I added pagination this was no longer needed.  Pagination has helped not to clutter the page with too much information and for now I have chosen to limit the number to 8 flies per page.
 
[Back to Top](#summary)
 
### Future Features
 
I would like to add a login to the page so that contributors can only edit and delete their own contributions to the database.  
 
A cookie bar would make the app fully legal but since no data except for what the visitor inserts into the database is being taken right now it is not necessary.
 
I would like to add facebook pixels so that I can retarget those visiting the site with products that may interest them.
 
I may decide to change the colours of the app to match those of the sponsors site I will await user feedback and decide then.
 
[Back to Top](#summary)
 
### Technologies
 
1. HTML5        To set up the basic structure of the pages.
2. CSS3         To add styling to the app.
3. Bootstrap    Makes it easy to implement structures within the pages of the app and allows them to be responsive eg for mobile phones
4. JQuery       Required in conjunction with Javascript to enable the email to function properly which also utilized email.js       
5. Heroku       Heroku is a cloud platform as a service supporting several programming languages. I am using Heroku to deploy the app.
6. Django
7. AWS

 
[Back to Top](#summary)
 
### Testing
 
Extensive manual testing was carried out on this app.  It was tested in Chrome, Firefox and Edge the app did not load properly in Edge and therefore did not function as expected but in Chrome and Firefox all areas functioned as expected.  The nav bar buttons top and bottom bring the user to the correct page whether that is inside the app or to a new page in the case of the social media and buy buttons.  The drop down for the contents and the edit and delete buttons functioned as expected as did the add new fly button.  The contact us page sends an email and the privacy page displays as expected.
 
[Link to some screenshots of testing](https://drive.google.com/drive/folders/1cWNedjMQ3PXY46fiiigJ-YNp7qzmITsn?usp=sharing)
 
Responsiveness:  The site was tested on multiple devices (iPhone 4, 5/SE,6,7,8 iPhone 6,7,8 plus, iPhone X : Chrome and Safari, iPad, iPad Pro,Samsung Galaxy Slll,5S)  and was shown to load an respond as expected with all the buttons being visible and functioning in accordance with expectations 
 
Create:  The add fly button effectively creates a new entry into the database.  Some fields such as Name, Hook Size and Thread were made required so that only after they have been filled in the fly will be added to the database.  The fields are not case sensitive and at present will allow duplication, this is inline with expectations.
 
Read:  The fly name and submitted by are immediately visible on the page the rest of the components required including links if any are included in the drop down menu, this is so as not to over crowd the page with information. This is as expected.
 
Update:  Most of the flies have the option to be updated through the edit button on clicking edit the user is brought to a new page where all the entries except for 'Submitted by' and 'Delete' can be changed.  Only I can change the submitted by and delete information and this is as expected.
 
Delete:  If a fly has the option to be deleted by the presence of the red delete button it will disappear from the page and the database when this button is clicked, this is what is expected.
 
The search buttons are not case sensitive and will search even with a partial or even just a letter as an input.  If you enter 'a' in the Search fly by name button any fly with the letter 'a' in its name will load in a separate page, the same is true for the Search by Submitted by search box.  This is what is expected. 
 
The home page and search pages are paginated.  When there are more than 8 flies in the database the landing page displays them in pages of 8 with a number counter telling the visitor how many flies are being displayed and how many there are in total.  The search pages are also paginated and will display the flies in groups of 8 per page.  The search pages do not have a counter in them.  This is as expected.
 
I sent the Heroku link to fly fishermen and fly tiers and the feedback was that the app looks well and was seen as being very useful. They suggested that for mobile phones I should increase the size of the Link on the drop down menu on the home page as it could be hard to see otherwise.  This was adjusted and is now in line with expectations.  
 
To validate my code I used the dev tools to examine each page and then run them through appropriate validators as follows I also beautified the code using online beautifiers.
 
HTML code is validated through [W3C Markup validator](https://validator.w3.org/)
 
CSS code is validated through [W3C CSS validator](https://jigsaw.w3.org/css-validator/)

Javascript code is validated through [JSHint](https://jshint.com/)
 
Python code is validated through [PEP8](http://pep8online.com/).
 
[Back to Top](#summary)
 
### Deployment
The app was written and developed on Gitpod and was regularly committed and pushed to Github and Heroku.
 
To deploy properly the following are required to be installed using the pip3 install command as follows.
 
pip3 install flask
 
pip3 install flask-pymongo
 
pip3 install dnspython
 
pip3 install bson
 
pip3 freeze --local > requirements.tx
 
echo web: python app. py > Procfile
 
The app uses MongoDB and there is a URI needed to run MongoDB,  this is a secret password and as such has been placed into a file which was then added to a gitignore file.  This was done to protect the password as it should not appear on Github, if it did then anyone could copy and use my URI  
 
Heroku required that some variables are set up in order to deploy the app.  In this case the IP was set to 0.0.0.0 the PORT was set to 5000 and the MongoDB URI was also added.  In order to send the app to Heroku I first had to login into Heroku through the Gitpod IDE and then push all the commits to Heroku so any changes could be added to the app, on the last few pushes the Debug was set to False
 
[Back to Top](#summary)
 
### Media 
The  backend photos on the app are mine. People are free to add their own links to the app.
 
### Credits
 
All the content has been written by myself or contributors. The code I have used has come from videos that I have watched from the Code Institute and from previous projects I have made comments on code that I have used throughout the project.  I would like to thank Cormac, Stephen and my classmates who were a great resource during this project. 
 
[Back to Top](#summary)



[![Build Status](https://travis-ci.com/AlanOSheadev/Rodfendr.svg?branch=master)](https://travis-ci.com/AlanOSheadev/Rodfendr)
