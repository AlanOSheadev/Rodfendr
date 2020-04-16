# Rodfendr
 
## Fourth Milestone Project -Full Stack Frameworks with Django Milestone Project - Code Institute April 2020
 
### What is the purpose of this App?
 
This app allows the visitor to look at the different products which are available to purchase at Rodfendr.  On the visitors first visit to the site there is a modal which pops up and requires the visitor accepts that there are cookies on the site, this will only pop up once unless the visitor clears their browser and loads the site again in which case the modal will reopen. There is a search funtion which allow the visitor to search for products. There is also a back to top button which is particularly useful if someone is looking through our legal pages. 

Click on the image to go to the live app.
 
[![Responsive Design](https://alans-ecommerce.s3-eu-west-1.amazonaws.com/static/images/responsive.png?versionId=null "Responsive Design")](https://rodfendr.herokuapp.com/)
 
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
* [Technologies](#technologies)
* [Testing](#testing)
* [Deployment](#deployment)
* [Media](#media)
* [Credits](#credits)
 
### UX
 
User expectations:
 
A visitor to the app will expect to see a well themed app with relevant information. This app is giving the user the opportunity to purchase unique fishing tackle.  These products are ideal as gifts for those who have loved ones who partake in fishing. 
 
### Strategy
I wanted to produce a simple ecommerce site with very little distracting the visitor from the products which are available to purchase.  The colours were chosen to compliment eachother and to provide a pleasing contrast to eachother. The hero image immediately portrays me relaxing and fishing while using my patented rod rest Rodfendr, but it is also used to invoke the benefits of going to relax on a fishing trip, hopefully inspiring the visitor to make a purchase as they will realise how much an angler would enjoy our unique tackle solutions. 

 
### Scope
 
The app is designed to get the visitor to think about what fishing tackle they would like have, or which of our products would make a great gift for an angler they might know.
 
### Structure
 
The page is designed to make the visitor feel welcome and to think about what fishing tackle they might need it is likely that they have not seen all of our products before anywhere.  The hero image give a great sense of how a relaxing day fishing can be good for you.  The message within the image is welcoming and lets you know that the price includes shipping.  As you scroll down you immediately see our unique list of products each has a picture and a brief description as well as a short video.  I felt that this was the best way to communicate the benefits of our products without overwhelming the visitor with information and allowing them to a decision on what to purchase.
 
[Back to Top](#summary)
 
### Skeleton
 
1. [Landing page wireframe](https://alans-ecommerce.s3-eu-west-1.amazonaws.com/static/images/landingpage.png)
2. [Contact page wireframe](https://alans-ecommerce.s3-eu-west-1.amazonaws.com/static/images/contact.png)
3. [Legal page wireframe](https://alans-ecommerce.s3-eu-west-1.amazonaws.com/static/images/legal.png)
 
### Surface
The colours were chosen to contrast easily and make it easier for the visitor to see the content.  The site is supposed to look clean and clear without clutter so that the visitor can concentrate on the products which sre the main focus of the site.  
 
## Features
 
### Existing Features:

On entering the site a modal opens and explains that this site contains cookies and has a link which goes to our legal page.  The visitor must click withtin the modal therefore accepting the cookies.  The modal will only open once unless the visitor clears their browser in which case the modal will fire again.
 
The top navigation bar contains a link to the landing page which is marked as Home and has a house icon you can return home from any page by using this button,  there is also a contact page which is an active email request and is marked as contact us with a speech bubble icon. The bottom navigation bar also has home and contact us buttons as well as links to all of Rodfendr's social media sites. These buttons will change when you hover over them to let you know that they are buttons to be clicked.
 
The top navigation bar has two orientations one for a new visitor who has not registered with the site and the other is when visitors decide to login.  Login is required when making purchases which is what was intended, this allows a vititor time to familiarize themselves with the site before being required to register.

Before you have registeres the top navigation bar shows the following options 'Register', 'Login', 'Contact us' and 'Privacy'.  After the visitor has logged in the top navigation bar changes to 'Home', 'Contact Us', 'Profile', 'Log Out', 'Legal' and  'Cart'.  The bottom navigation bar does not change.

There is a large but not overwhelming hero image which shows me fishing with Rodfendr the message contained within is welcoming and lets you know that shipping is included in our pricing.

There is a simple search bar which will bring you to a product within our range of products. 

There is also a button which will take the visitor to our product reviews which are reviews from customers and industry experts.  The visitor can also add their own reviews which can include pictures if they wish.

Next you are shown all our current products which have a picture of the product as well as a biref description and a short video of each product and an option to select the number of each product you wish to purchase.  This sections is very clean and clear as I want the main focus to be on the products.

If you choose a product or number of products they are added to the cart automatically and a badge will appear on the top navigation bar letting you know how many items are in your cart.

To purchase your items first you must select the cart and you are given a chance to amend your items, change quantities etc.  Once you are happy with the items in your cart you will click on the checkout button where your payment details will be taken using Stripe.  At the checkout you will also enter the delivery address for the order.  An image and the price of each item your are paying for is desplayed above the forms as well as the total amount which will be taken from your card.

Google analytics records your visit and your behaviour while on the site.

Based on feedback from friends and Matt Rudge of The Code Institute I made it clear what the site is about by adding a hero image, I added complimentary fonts to the headings and body and I added an if statement to the cart so that if there is an empty cart you cannot go to the checkout.

[Back to Top](#summary)
 
### Future Features
 
I would like to add facebook pixels so that I can retarget those visiting the site with products that may interest them.

I tried to add discount codes to the app but it proved a little difficult so I made the decision to add them later when I have more experience.

I tried to add trustpilot to the app but it would not function as expected to I had to remove it for the project but I will try again later.

 
[Back to Top](#summary)
 
### Technologies
 
1. HTML5        To set up the basic structure of the pages.
2. CSS3         To add styling to the app.
3. Bootstrap    Makes it easy to implement structures within the pages of the app and allows them to be responsive eg for mobile phones
4. JQuery       Required in conjunction with Javascript to enable the email to function properly which also utilized email.js       
5. Heroku       Heroku is a cloud platform as a service supporting several programming languages. I am using Heroku to deploy the app.
6. Django       Django is a Python-based free and open-source web framework, which follows the model-template-view architectural pattern. It is maintained by the Django Software Foundation, an independent organization established as a 501 non-profit. Django's primary goal is to ease the creation of complex, database-driven websites.
7. Database     Heroku Postgres is a SQL database as a service with operational expertise built in, easy setup, security by default, database forking, credentials, and more
8. AWS          Amazon Web Services is a subsidiary of Amazon that provides on-demand cloud computing platforms and APIs to individuals, companies, and governments, on a metered pay-as-you-go basis.
9. Bootstrap    Bootstrap is a free and open-source CSS framework directed at responsive, mobile-first front-end web development. It contains CSS- and JavaScript-based design templates for typography, forms, buttons, navigation, and other interface components.
10. EnailJS     EmailJS helps sending emails using client side technologies only. No server is required – just connect EmailJS to one of the supported email services, create an email template, and use our Javascript library to trigger an email.
11. Stripe    Stripe is an American technology company based in San Francisco, California. Its software allows individuals and businesses to make and receive payments over the Internet.
12. Travis CI   Travis CI is a hosted continuous integration service used to build and test software projects hosted at GitHub and Bitbucket. Travis CI provides various paid plan for private projects, and a free plan for open source. TravisPro provides custom deployments of a proprietary version on the customer's own hardware.

 
[Back to Top](#summary)
 
### Testing
 
Extensive manual testing was carried out on this app.  It was tested in Chrome, Firefox and Edge the app did not load properly in Edge and therefore did not function as expected but in Chrome and Firefox all areas functioned as expected.  The nav bar buttons top and bottom bring the user to the correct page whether that is inside the app or to a new page in the case of the social media and buy buttons.  The contact us page sends an email and the privacy page displays as expected.  

The checkout page was tested using Stripe in test mode but now it's a live version.
![Checkout](https://alans-ecommerce.s3-eu-west-1.amazonaws.com/static/images/checkoutpage.png "Checkout")
![Checkout result](https://alans-ecommerce.s3-eu-west-1.amazonaws.com/static/images/checkoutresulttest.png "Checkout result") 

The contact us page was extensively tested and at the start I had issues as can be seen from the following photos.  First I had to link with my gmail account which I had created for this app.
![Gmail error](https://alans-ecommerce.s3-eu-west-1.amazonaws.com/static/images/mailtest1.png "Gmail error")

Secondly I had to wire up the js file correctly.
![js error](https://alans-ecommerce.s3-eu-west-1.amazonaws.com/static/images/jsmailtesterror.png "js error")
Once these errors were identified and rectified the email works just as expected.


Travis CI was used to continuously test the building of the app.

[![Build Status](https://travis-ci.com/AlanOSheadev/Rodfendr.svg?branch=master)](https://travis-ci.com/AlanOSheadev/Rodfendr) 
 
Responsiveness:  The site was tested on multiple devices (iPhone 4, 5/SE,6,7,8 iPhone 6,7,8 plus, iPhone X : Chrome and Safari, iPad, iPad Pro,Samsung Galaxy Slll,5S)  and was shown to load and respond as expected with all the buttons being visible and functioning in accordance with expectations 
 
To validate my code I used the dev tools to examine each page and then run them through appropriate validators as follows I also beautified the code using online beautifiers.
 
HTML code is validated through [W3C Markup validator](https://validator.w3.org/)
 
CSS code is validated through [W3C CSS validator](https://jigsaw.w3.org/css-validator/)

Javascript code is validated through [JSHint](https://jshint.com/)
 
Python code is validated through [PEP8](http://pep8online.com/).
 
[Back to Top](#summary)
 
### Deployment
The app was written and developed on Gitpod and was regularly committed and pushed to Github and Heroku.

The following pip commands are necessary for the app to function properly.
pip3 install django==1.11.29

pip3 freeze > requirements.txt

django-admin startproject file_name .

django-admin startapp app_name

python3 manage.py migrate

python3 manage.py runserver

python3 manage.py createsuperuser

pip3 install django_forms_bootstrap

pip3 install Pillow

pip3 install dj_database_url

pip3 install psycopg2

pip3 install django-storages

pip3 install boto3

pip3 install stripe

pip3 install gunicorn


Add all secret keys to heroku config vars and add 
DISABLE_COLLECTSTATIC and make it’s value 1

python3 manage.py collectstatic 

Need to run this after any changes to static files in the IDE
 
Heroku required that some variables are set up in order to deploy the app.  All secret keys and passwords used in the env.py file which is ignored by Github in the .gitignore file are stored in the config vars section of Heroku.  In order to send the app to Heroku I first had to login into Heroku through the Gitpod IDE and then push all the commits to Heroku so any changes could be added to the app, on the last few pushes the Debug was set to False

To set up and install AWS I followed the instruction video on the Code Institutes training and the following steps were taken. If you don't have an amazon account you need to open one and select amazon web services (AWS) and then S3.

In AWS S3

Create Bucket

Unique name ie - niels-ecommerce
Ireland
Allow public access

Create

Open bucket
Properties - staic website hosting
Index.html

Error.html

Permissions 
Cors configuraton
Add our arn keeping /*

IAM
Create a group
Name it close to buket name  - neils ecommerce-group
Next and create group

Greate policy
Import managed polcy 
Choose S3 full policy
Import
Change string to a list [ ]
The first item in the list is going to be our own ARN which we used earlier, but it has been closed in quotes
The second item in the list again in quotes is going to be the same ARNThis time we append a forward slash and an asterisk
Review and name it in association with the bucket - niels-eccomerce-policy

Add policy to group
Got to groups and select my group, goto permissions tap in group search for the policy  we created and check the box and attach

Create user
New user
Name - niels-eccomerce-user
Allow programatic access
No keys or tags
Download CSV file


Cahnge our files
Pip3 install django-storages
Pip3 install boto3
Add this to settings.py above static_url

AWS_S3_OBJECT_PARAMETERS = {




   'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',


   'CacheControl': 'max-age=94608000'


}


AWS_STORAGE_BUCKET_NAME = 'ecommerce'

AWS_S3_REGION_NAME = 'eu-west-1'

AWS_ACCESS_KEY_ID = os.environ.get("AWS_SECRET_KEY_ID")

AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")

AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

Add AWS keys to env.py file using CSV information
next
Python3 manage.py collectstatic
Yes to change warning

Custom_storages.py file

from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage
class StaticStorage(S3Boto3Storage):


   location = settings.STATICFILES_LOCATION
class MediaStorage(S3Boto3Storage):
   location = settings.MEDIAFILES_LOCATION
ADD these changes to staticfiles in settings.py

STATICFILES_LOCATION = 'static'
STATICFILES_STORAGE = 'custom_storages.StaticStorage'
And 
Python3 manage.py collectstatic

Do similar action for media
To fix console errors
In permissions - Cors configuration
Copy the GET line and change it to HEAD to read font awesome CSS properly

 
[Back to Top](#summary)
 
### Media 
The photos and videos on the app are mine. I also appear in many of them myself. The photos in the reviews section are the property of the person who submitted them and have done so willingly.

 
### Credits
 
All the content has been written by myself. The code I have used has come from videos that I have watched from the Code Institute and from previous projects I have made comments on code that I have used throughout the project.  I would like to thank Cormac, Stephen and my classmates who were a great resource during this project. 
 
[Back to Top](#summary)
