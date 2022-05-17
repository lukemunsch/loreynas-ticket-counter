![Loreyna's Ticket Counter Responsive Image](media/readme-images/am-i-resp-img.png)

# Loreyna's Ticket Counter

## # Table of contents:

1. [Link To Live Site](#link-to-live-site)
2. [LucidChart ERD Diagram](#lucidchart-erd-diagram)
3. [Wireframes](#wireframes)
4. [Overview](#overview)
5. [User Stories](#user-stories)
6. [Features](#features)
    1. [Index Page](#index-page)
    2. [Destination Page](#index-page)
    3. [Areas Page](#index-page)
    4. [District Page](#index-page)
    5. [Add/Edit Pages](#index-page)
    6. [Delete Page](#index-page)
    7. [Destination Detail Page](#index-page)
    8. [Wallet Page](#index-page)
    9. [Checkout Page](#index-page)
    10. [Confirmation Page](#index-page)
    11. [Profile Page](#index-page)
7. [Features to Implement](#features-to-implement)
8. [Testing](#testing)
    1. [Lighthouse Reports](#lighthouse-reports)
    2. [HTML Testing](#html-testing)  
    3. [CSS Testing](#css-testing)
    4. [PEP8 Testing](#pep8-testing)
    5. [Automated Testing](#automated-testing)
    6. [Manual Testing](#manual-testing)
9. [Unfixed Bugs](#unfixed-bugs)
10. [Deployment](#deployment)
    1. [Forking and Cloning](#forking-and-cloning)
    2. [Local Deployment](#local-deployment)
    3. [Remote Deployment](#remote-deployment)
11. [Credits](#credits)

## Link to Live Site

https://loreynas-ticket-counter.herokuapp.com

## LudicChart ERD Diagram

[Loreyna's Ticket Counter ERD](media/readme-images/loreynas-counter-erd.png)

## Wireframes

In order to help me realise how i want to build the site, i have created a series of wireframes using Balsamiq:

[Index page](media/readme-images/index.png)

[Destinations](media/readme-images/destinations.png)

[Destination Details](media/readme-images/destination-details.png)

[Area List](media/readme-images/areas.png)

[District List](media/readme-images/districts.png)

[Add/Edit Entry](media/readme-images/addandedit.png)

[Delete](media/readme-images/delete.png)

[Wallet](media/readme-images/wallet.png)

[Checkout](media/readme-images/checkout.png)

[Confirmation](media/readme-images/confirmation.png)

[Profile](media/readme-images/profile.png)

## Overview

As a fan of the Final Fantasy franchise, I have enjoyed all aspects of the game and thought how interesting it would be the make a location site that people can browse and see the complete list of destinations for the 14th game in the series. As a fan of the game, I am forever trying to find the correct locations for travelling and this allows user to search for their destinations and admins to update Loreyna's Ticket Counter whenever new desitnations or locations are released.
The app for Loreyna's Ticket Counter is foremost an online ticket sales site that allows adventurers to book their travel destinations to anywhere on Eorzea. The tickets are a digital product and therefore have no delivery requirements, the products are redeemable from the aetheryte plaza to anywhere that also houses an aetheryte crystal.
The site offers a simple as well as helpful solution to navigate the wide world of Eorzea; locating where you would like to travel to and searching from a list of locations, with the feature to filter based on the main locations in the world and even the more specific districts within the locations. Each specific destination has a recogniseable image, a supporting description, there is even a badge that can be added to specific hotspots for people to see where is most popular.
The list of destinations will continue to increase while destinations are discovered and new Aetheryte crystals are installed, which means that the site owners will be able to update and keep materials fresh for the adventurers that want to travel to these destinations as and when they want.

## User Stories

kanban board with user stories broken up into sprints

## Features

I am a huge fan of the Final Fantasy gaming franchise and decided to adopt a similar style to Loreyna's Ticket Counter.

The color scheme I have chosen is the dark blue for a night feel and then a gold colour for the text; where the background has changed to gold I have inverted the colours so the text would be the dark blue. I have included some borders and section dividers for my site which are a darker gold colur; still standing out from the dark background but not drawing the attention away from the text and objects. When differentiation is needed from the normal dark blue or gold colours, I have included a lightblue contrasting colour that is similar to the design of the Aetheryte crystal in the image from the home page. The inspiration for the gold is taken from the gold band around the Aetheryte crystal and what all adventurers are really after besides glory - Gold.

### Index Page

### Destination Page

### Areas Page

### Districts Page

### Add/Edit Page

### Delete Page

### Destination Detail Page

### Wallet Page

### Checkout Page

### Confirmation Page

### Profile Page



## Features to Implement

Hotspot Filtering

## Testing

Lighthouse Reports

HTML Validation

CSS Validation

PEP8 Validation

Manual Testing

Automated Testing

## Bugs

secret key as exposed so a new secret key was generated

## Deployment

To deploy Loreyna's Ticket Counter, allow other people to run the app and see it working, there are 3 methods to allow you to complete these actions:

### Forking and Cloning

Accessing GitHub and navigating to my repositories will allow users to copy my code directly from the source, either by forking or cloning: Accessing the Loreyna's Ticket Counter repository and clicking on the code button next to Gitpod link will bring up a menu to create a repository of your own in your own GitHub repo. There is also the Download zip file option which will allow you to save a copy of my code as well.

### Local Deployment

For local deployment of Loreyna's Ticket Counter, I will be using Gitpod to edit and run my workspace;
- From GitHub, once the repository has been created (either as a new project or by forking/cloning) I will then click on the Gitpod button to implement the creation of a workspace to edit the promotional sales review system.

***The workspace should not be closed due to the env.py file; as it is never added to GitHub, if you create a new workspace you will need to re-add the env.py file and reinstall all libraries used each time. Pinning a workspace and accessing it from Gitpod workspaces will save time and repetition***


### Remote Deployment

For deployment of Loreyna's Ticket Counter, there are a number of steps required to complete this action;

- We are using the Site Heroku for our deployment;
    - In Heroku, create a new app and give it a name befitting your project.
    - In settings, we first need to make sure the config vars contain DEVELOPMENT with the value of False.
- We need to make sure a couple of our variable in our settings app are updated so that they are no longer developer enabled.
    - For our DEBUG setting;
            DEBUG = 'DEVELOPMENT' in os.environ
    - For our DATABASES variable;
            if 'DATABASE_URL' in os.environ:
                DATABASES = {
                    'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
                }
            else:
                DATABASES = {
                    'default': {
                        'ENGINE': 'django.db.backends.sqlite3',
                        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
                    }
                }
    This is to ensure that the debug and database are using the correct variables so that when Loreyna's Ticket Counter is deployed, the users will be unable to see any of the secrets from the debug window and the correct database is being used.
- We need to set up our Stripe variables in settings and our Heroku dashboard in order to allow our deployed site to continue working.
    - Once you have logged in and set up our stripe endpoint using the code institute's walkthrough and cheat sheet, we can add the following variables to settings.py;

            STRIPE_CURRENCY = 'gbp'
            STRIPE_PUBLIC_KEY = os.getenv('STRIPE_PUBLIC_KEY', '')
            STRIPE_SECRET_KEY = os.getenv('STRIPE_SECRET_KEY', '')
            STRIPE_WH_SECRET = os.getenv('STRIPE_WH_SECRET', '')

    - In our dashboard settings for Gitpod, we need to add these in order for our environmental variables to work while in deployment.
        - Add the above variables to the env settings
        - For each variable, go to stripe and copy the secret codes
        - Add them to the relevant variables.
    
    - In Heroku, we need to include the last three as config vars in the settings page on the heroku dashboard.
- We will need to set up our resources so that the deployed project can work correctly;

        pip3 install gunicorn
        pip3 install dj_database_url
        pip3 install psycopg2-binary

        pip3 freeze > requirements.txt

- For our deployment, we will be using Heroku and we need to set up our database for the deployed version;
    - We need to add the Heroku Postgres resource from the Resources tab in the Heroku dashboard. This will assign us a variable which we will then need to add to our env.py file so that no one except ourselves can see it.
- For all of our deployed apps, we need to set up a Procfile to instruct Heroku how to handle the application;
    - In our Procfile, we need to add;

            web: gunicorn loreynas_counter.wsgi:application

- We need to add our AWS for media storage to the heroku variables as well;
    - First log in to AWS dashboard and set up your bucket using the code institute's walkthrough and cheat sheet.
    - You will end up producing an excel document that contains secret values that we need to use in Heroku in order to see our media.
    - Add the following KEY : Value variables to the Heroku Config Vars;

            AWS_ACCESS_KEY_ID : 'value'
            AWS_SECRET_ACCESS_KEY : 'value'
            USE_AWS : True

- For the emails and ability to send confirmations, we need to set up a few variables for the settings.py file and a couple in the heroku config variables.
    - In settings.py, add;

            if 'DEVELOPEMENT' in os.environ:
                EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
                DEFAULT_FROM_EMAIL = 'loreynascounter@aetheryte.com'
            else:
                EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
                EMAIL_USE_TLS = True
                EMAIL_PORT = 587
                EMAIL_HOST = 'smtp.gmail.com'
                EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
                EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASS')
                DEFAULT_FROM_EMAIL = os.environ.get('EMAIL_HOST_USER')
    
    - In Heroku config vars, add;

            EMAIL_HOST_PASS : 'leave blank for now'
            EMAIL_HOST_USER : 'your email address'

    ***It is best to use a gmail for this as our walkthrough from code institute gives clear instructions on how to set this up.***
    
    - In mail.google.com, go to the cog/settings for the account
    - Click Accounts and Imports tab
    - Click Other Google Account Settings
    - Head to security
    - Make sure 2-Step-Auth is turned on
    - Under this, click on App Passwords
    - Select Mail on first drop down
    - Select Other on second drop down and add text 'Django'
    - Once completed, you have generated a 16 digit code - Copy this
    - In Heroku dashboard config vars, add in;

            EMAIL_HOST_PASS : 'paste 16-digit code here'
    
    This will now allow our emails to correctly send from deployed site.

- Now we need to connect our Gitpod to Heroku

***Due to a serious Security breach, we are unable to link our gitpod to heroku using conventional means - this means we need to take an alternative approach; HEROKU CLI THROUGH GITPOD***

- To start the process, we need to sign in to Heroku CLI in the terminal;
        
        heroku login -i
    
- Sign in with your regular email account for heroku

- If you have an up-to-date account with Heroku, you will have switched on 2 step auth for your account, so you cannot sign in using you password; To get around this;
    - You can head to your account icon in Heroku dashboard
    - Select Account Settings
    - Scroll to bottom and reveal your API key
    - Copy this code and paste into your password field in terminal.
- You should now be connected to Heroku CLI which means we can now complete the Deployment procedure;
    - In terminal, type;

            heroku git:remote -a heroku-app-name

***This must contain the app name we have set up in heorku otherwise the app will not connect***

- As we have now linked up our new database to postgres, we need to migrate all our files to the new database;

        python3 manage.py migrate 

***You do not need to makemigrations first as we have already created them, we just need to move them to the correct place***
        
        git add .
        git commit -m "Complete deployment process to Heroku"
        git push
        git push heroku main

***By pushing to Heroku main, we are sending a copy for all of our code to Heroku to be deployed which means we can avoid the issue regarding the Security breach and not being able to connect for auto or manual deployments***


## Credits

- https://levelup.gitconnected.com/django-customize-404-error-page-72c6b6277317 - This page helped me to build a custom 404 html page in order to make the user experience much improved.
- All of the amazing team members working at the tutor team for the Code Institute, whom, without which, I would be a blubbering mess!
- My mentor Chris Quinn who has provided me with sound guidance and direction from the inception of Loreyna's Ticket Counter.
- All of the learning materials I have been studying provided by the Code Institute.
