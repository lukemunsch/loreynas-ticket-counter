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
11. [E-Commerce Business Model](#e-commerce-business-model)
    1. [SEO Research](#seo-research)
12. [Marketing Research](#marketing-research)
    1. [Facebook Business Page](#facebook-business-page)
    2. [Content Research](#content-research)
    3. [E-Mail Marketing](#email-marketing)
13. [Credits](#credits)

## Link to Live Site

https://loreynas-ticket-counter.herokuapp.com

## LudicChart ERD Diagram

[Loreyna's Ticket Counter ERD](media/readme-images/loreynas-counter-erd.png)

## Wireframes

To help me realize how I want to build the site, I have created a series of wireframes using Balsamiq:

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

As a fan of the Final Fantasy franchise, I have enjoyed all aspects of the game and thought how interesting it would be the make a location site that people can browse and see the complete list of destinations for the 14th game in the series. As a fan of the game, I am forever trying to find the correct locations for traveling and this allows users to search for their destinations and admins to update Loreyna's Ticket Counter whenever new destinations or locations are released.

The app for Loreyna's Ticket Counter is foremost an online ticket sales site that allows adventurers to book their travel destinations to anywhere on Eorzea. The tickets are a digital product and therefore have no delivery requirements, the products are redeemable from the aetheryte plaza to anywhere that also houses an aetheryte crystal.

The site offers a simple as well as a helpful solution to navigate the wide world of Eorzea; locating where you would like to travel to and searching from a list of locations, with the feature to filter based on the main locations in the world and even the more specific districts within the locations. Each specific destination has a recognizable image, and a supporting description, there is even a badge that can be added to specific hotspots for people to see where is most popular.

The list of destinations will continue to increase while destinations are discovered and new Aetheryte crystals are installed, which means that the site owners will be able to update and keep materials fresh for the adventurers that want to travel to these destinations as and when they want.

## User Stories

The main purpose for my site is for people to browse through a list of destinations - searchable and filterable to their needs - that they want to go to, add the destinations to a ticket wallet to then checkout. The confirmation emails will contain an order number that will be redeemable at any of the Aetheryte plaza around Eorzea. Advancing from the basic visit, customer can then also create a profile and store their personal information securely to speed up their checkout process the next time they choose to purchase tickets.

Upon a secondary visit, customers can then review their previous orders and view them in a recreation of the original confirmation page. The users can return to browse the list of destinations or return to their profile to make any adjustments to the personal data saved.

Email confirmations are primarily used as the customer MUST have an email address and VERIFY the email is correct to be able to log in to the site therefore an email means there is less risk to incorrect email addresses to the registered users.

Upon all further visits, adventurers can browse through the list of destinations which may be updated periodically to either reflect new hotspots that the site owners feel are more popular or even add new destinations as they are discovered aroud the world of Eorzea.

I have created a kanban board for this project to help me manage and complete tasks.

To keep the project moving at a correct and efficient pace, I have broken down all the tasks into sprints; this will allow me to see what it is that I need to focus on in specific sections of my project and know what I am looking for next.

[Loreynas Ticket Counter Project Board](https://github.com/lukemunsch/loreynas-ticket-counter/projects/1)

## Features

I am a huge fan of the Final Fantasy gaming franchise and decided to adopt a similar style to Loreyna's Ticket Counter.

The color scheme I have chosen is dark blue for a night feel and then a gold color for the text; where the background has changed to gold I have inverted the colors so the text would be dark blue. I have included some borders and section dividers for my site which are a darker gold color; still standing out from the dark background but not drawing the attention away from the text and objects. When differentiation is needed from the normally dark blue or gold colors, I have included a light blue contrasting color that is similar to the design of the Aetheryte crystal in the image from the home page. The inspiration for the gold is taken from the gold band around the Aetheryte crystal and what all adventurers are really after besides glory - Gold.

### Main Nav Bar

I wanted to have simple navigation that is clear to the users as to what each button means. The title of the site will be a simple gold Title linking back to the home page, a search bar that allows users to search for a destination term at any time, as well as a link to the profile page or login in/out/sign up page and a link to the wallet, so that users can see what they are currently going to be spending at any time. All text is written in gold and the title has a different font to make sure it stands out slightly more than the regularly used text font.

### Index Page

The background image is an iconic Aetheryte Crystal which most users who visit the site would recognize almost immediately. The image also sets up the color scheme for the rest of the site with the dark blue main color, light blue, and golds that stand out from the image.

[Index and nav bar](media/readme-images/ss-index.png)

### Destination Page

The destination page is a collection of card-styled items that will allow the user to glean some simple information such as name and location details as well as price. The list at the top of the page below the header is all the currently available list of areas that the admins have assigned, allowing the users to filter the list of destinations. We also have a list of districts on the left-hand side which will also filter and reduce depending on the area chosen.

[Destination page](media/readme-images/ss-destinations.png)

### Areas Page

The area page is a simple page for listing the areas and a description for them so that users can decide if they want to go to these specific areas. The text is in gold to stand out from the background and there are simple links (if logged in as an admin) to allow admins to edit or delete the entry.

[Areas page](media/readme-images/ss-areas.png)

### Districts Page

The districts are also a simply displayed list of available districts for the areas that we have set up. These will be arranged as cards as they have very little information; we only need to know the name of the district and the area that it is associated with. This will also have admin-only edit | delete links. The main text is written in gold and the area text is written in light blue.

[Districts page](media/readme-images/ss-districts.png)

### Add/Edit Page

The add and edit page will be identical in appearance as they both fulfill the same criteria; to post the details, whether new details or updating details. The forms themselves will have white backgrounds to help them stand out against the dark blue and muted grey text that disappears when there is text inputted. the buttons will align with the same style that the rest of the site has with gold background and dark blue text. a simple icon on each button to identify the action pairing with the text.

[Add/Edit page](media/readme-images/ss-add-edit.png)

### Delete Page

The delete page is a safeguard against accidental deletions; the page itself is a basic text-driven page with a request that the admin definitely wants to delete the specific entry. The main text is again written in gold and the warning text is written in red to make sure the user is fully aware of the action. The name of the entry is written on the page as well so that the user knows what they are deleting with buttons to either cancel and go back or complete the deleting process in the same style of gold with dark blue text and icon.

[Delete page](media/readme-images/ss-delete.png)

### Destination Detail Page

The destination detail page is a much more in-depth look at a specific destination; the larger image displayed on the page will give the user a view of the destination, with the details such as description and location in a more eloquent and visible style. There are also the links for admins to edit and delete this entry if need be, with a simple quantity adjuster and gold buttons to keep the style in line with the rest of the site.

[Destination Details](media/readme-images/ss-destination-detail.png)

### Wallet Page

The wallet page has a list of destinations one on top of the other; images, names price, quantity, and subtotal for how much each specific destination is going to cost. A the bottom of the page we can see a total for the ticket wallet and if there are 5 or more tickets in the wallet then a discount of 20% is applied to the wallet and the savings are listed in light blue to draw attention away from the gold text. Two buttons for returning to the destinations page or heading to the checkout page in the same style as the other pages.

[Wallet page](media/readme-images/ss-wallet.png)

### Checkout Page

The checkout page is going to have a form on the left-hand side of the page for inputting our name/email and location information as well as our stripe card details input. Gold buttons for completing a purchase or adjusting the wallet before checking out again. On the right-hand side, there is a list of all the destination images, details, and subtotals for that location. We can also see the total, discount, and grand total for the wallet so the user has a clear idea of what they are paying for and how much it will be.

[Checkout page](media/readme-images/ss-checkout.png)

### Confirmation Page

The confirmation page is basic text, most text is written in gold but the specific details, such as the information we inputted into the form are displayed in light blue. the display is broken down into three sections for order details, personal details, and order tickets; all in the same gold and light blue pairing styles.

[Confirmation page](media/readme-images/ss-confirmation.png)

### Profile Page

Out profile page will consist of a form on the left-hand side where a user can store information, either directly from the checkout page or manually add them so that they will display on new orders they place automatically if the user is signed in. on the right-hand side we also have a list of previous orders so that the user can see what they have ordered in the past in case they want to go back to the same places again. the order history is written in a simple table that will scroll vertically through the list.

[Profile page](media/readme-images/ss-profile.png)

## Testing

### HTML Validation

HTML pages have been run through https://validator.w3.org/ and the pages have all come back without errors.



### CSS Validation

I have passed through my CSS files into the https://jigsaw.w3.org/ checker and reported no issues with my code.

[CSS Validator](media/readme-images/validation/css-val.png)

### PEP8 Validation

Loreyna's Ticket Counter code has been run through a PEP8 validator and reported no issues other than migration files which are unable to be adjusted once created.

### Manual Testing

For manual testing, I ran through testing the full functionality of my site to make sure it was successful and the procedures all worked properly. I also provided my site's deployed address to three different users who ran tests from their devices to see how they work;

For responsivity I have tested the device on three different devices; mobile phone, ipad and desktop. The desktop screenshots are displayed above in the features section, but for the mobile and ipad I have provided screenshots for how they look in a smaple of different pages.

For the mobile phone tests, the menus correctly fold away into collapsable menu where appropriate, forms and fields fill the screen instead of shrinking beyond easily managable inputs. The text was adjusted so that the larger fonts for the larger screen display smaller and less bulky on the smaller screens, but still retain the nice feel of the site.

[add/Edit](media/readme-images/responsive/mobile/add-edit-resp-mob.png)
[Area List](media/readme-images/responsive/mobile/area-list-resp-mob.png)
[Checkout](media/readme-images/responsive/mobile/checkout-resp-mob.png)
[Collapsed Menu](media/readme-images/responsive/mobile/colapsed-menu-resp-mob.png)
[Destination Details](media/readme-images/responsive/mobile/dest-details-resp-mob.png)
[Destinations List](media/readme-images/responsive/mobile/destinations-resp-mob.png)
[Districts List](media/readme-images/responsive/mobile/district-list-resp-mob.png)
[Wallet](media/readme-images/responsive/mobile/wallet-resp-mob.png)

For the ipad view, the pages are larger and the amount of items in a line are increased but dont appear bundled all together. The forms still have a nice size to them and forms have a decent width to them, with the buttons still having a nice manage size without blocking too much of the screen around them. Drop down menues are still there as below the smaller media queries, but they still feel aesthetically correct to the size of the screen.

[Add/Edit](media/readme-images/responsive/ipad/add-edit-resp-ipad.png)
[Areas List](media/readme-images/responsive/ipad/areas-list-resp-ipad.png)
[Checkout](media/readme-images/responsive/ipad/checkout-resp-ipad.png)
[Destinations list](media/readme-images/responsive/ipad/destinations-resp-ipad.png)
[Districts List](media/readme-images/responsive/ipad/district-list-resp-ipad.png)
[Menu](media/readme-images/responsive/ipad/menu-resp-ipad.png)
[Profile](media/readme-images/responsive/ipad/profile-resp-ipad.png)
[Wallet](media/readme-images/responsive/ipad/wallet-resp-ipad.png)

User 1 tested the account registration;
User 1 was able to run through the complete registration process and receive the correct email and validate their address through the website. They reported no issues and the email contained only the relevant information as expected.

User 2 tested functionality for the wallet;
Their test was to make sure the addition of destinations into the wallet was carried out by adding destinations of any amount to the wallet, testing the limits of minimum 1 and max 99. They further developed their test by making sure the quantity can be updated using the function button in the wallet view as well as the remove button that completely removes the destination from the wallet. The total, discount, and grand total are updated and reflected correctly in the view for the wallet as well as the notification popups for successful additions/updates/removals. No reported issues for user's tests for any part.

User 3 tested the checkout function and profile view, split into the two different sections;
For the checkout, the user was able to sign in and add destinations to a wallet and view them in the checkout window with all the correct information displayed on the page; totals, discounts, destinations, and subtotals for each location line item for the second set of test, they chose to save their information to their profile. Upon completing a purchase using the correct test card number, the user was correctly delivered to the confirmation page with the correct information for the purchase that was made. In one instance the confirmation page failed to load, but the webhook completed the purchase and a confirmation email was still delivered correctly.
For the second section, the user was then able to view the profile page and view the correct input information from the checkout view. The information can then be adjusted and updated correctly to then be used once again in the checkout view. The correct information was correctly displayed after checkout and the updated information showed on the profile page. The updated information is then displayed correctly on the checkout page again. On the profile page, there is also a list displayed on the right-hand side of the successful orders placed by the user. the list displayed only the order that the user created, with the correct information they were expecting. No reported issues with either section of the tests.

### Automated Testing

coverage report after testing

## Bugs

Currently, there is a small issue that my icons for the smaller mobile-top-nav are not responsive and only sit on the right-hand side instead of nicely displaying evenly spaced. I have adjusted it manually but have been unable to affect the outcome positively.

I have a small issue with overflow on the x-axis on screens with any content there is a small section that pushes the content to the right and this is causing the screen to be slightly to large. i HAVE ead through stackoverflow and slack to find out what might be a good fix for this, but was unable to located the cause of the issue.

## Deployment

To deploy Loreyna's Ticket Counter, allow other people to run the app and see it working, there are 3 methods to allow you to complete these actions:

### Forking and Cloning

Accessing GitHub and navigating to my repositories will allow users to copy my code directly from the source, either by forking or cloning: Accessing the Loreyna's Ticket Counter repository and clicking on the code button next to Gitpod link will bring up a menu to create a repository of your own in your own GitHub repo. There is also the Download zip file option which will allow you to save a copy of my code as well.

### Local Deployment

For local deployment of Loreyna's Ticket Counter, I will be using Gitpod to edit and run my workspace;
- From GitHub, once the repository has been created (either as a new project or by forking/cloning) I will then click on the Gitpod button to implement the creation of a workspace to edit the promotional sales review system.
- You will also need to complete the installation of packages that I have created in the current version of the site

        pip3 install -r requirements.txt

***The workspace should not be closed due to the env.py file; as it is never added to GitHub, if you create a new workspace you will need to re-add the env.py file and reinstall all libraries used each time. Pinning a workspace and accessing it from Gitpod workspaces will save time and repetition***


### Remote Deployment

For deployment of Loreyna's Ticket Counter, there are several steps required to complete this action;

- We are using the Site Heroku for our deployment;
    - In Heroku, create a new app and give it a name befitting your project.
- We need to make sure a couple of our variables in our settings app are updated so that they are no longer developer enabled.
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
- We need to set up some of the environmental variables that are used on our site, but due to the nature of secret codes that external users should NOT know about, we keep them in an env.py file and declare it in the .gitignore file to avoid the secrets being made less secret. an example of an env.py file is as such;

        import os

        os.environ.setdefault('DATABASE_URL', 'postgres database from heroku setting config vars')
        os.environ.setdefault('SECRET_KEY', 'any randomly generated secret code')

- We need to set up our Stripe variables in settings and our Heroku dashboard to allow our deployed site to continue working.
    - Once you have logged in and set up our stripe endpoint using the code institute's walkthrough and cheat sheet, we can add the following variables to settings.py;

            STRIPE_CURRENCY = 'gbp'
            STRIPE_PUBLIC_KEY = os.getenv('STRIPE_PUBLIC_KEY', '')
            STRIPE_SECRET_KEY = os.getenv('STRIPE_SECRET_KEY', '')
            STRIPE_WH_SECRET = os.getenv('STRIPE_WH_SECRET', '')

    - In our dashboard settings for Gitpod, we need to add these for our environmental variables to work while in deployment.
        - Add the above variables to the env settings
        - For each variable, go to stripe and copy the secret codes
        - Add them to the relevant variables.
    
    - In Heroku, we need to include the last three as config vars in the settings page on the Heroku dashboard.
- We will need to set up our resources so that the deployed project can work correctly;

        pip3 install gunicorn
        pip3 install dj_database_url
        pip3 install psycopg2-binary

        pip3 freeze > requirements.txt

- For our deployment, we will be using Heroku and we need to set up our database for the deployed version;
    - We need to add the Heroku Postgres resource from the Resources tab in the Heroku dashboard. This will assign us a variable which we will then need to add to our env.py file so that no one except ourselves can see it.
- For all of our deployed apps, we need to set up a Procfile to instruct Heroku on how to handle the application;
    - In our Procfile, we need to add;

            web: gunicorn loreynas_counter.wsgi:application

- We need to add our AWS for media storage to the Heroku variables as well;
    - First, log in to the AWS dashboard and set up your bucket using the code institute's walkthrough and cheat sheet.
    - You will end up producing an excel document that contains secret values that we need to use in Heroku to see our media.
    - Add the following KEY: Value variables to the Heroku Config Vars;

            AWS_ACCESS_KEY_ID : 'value'
            AWS_SECRET_ACCESS_KEY : 'value'
            USE_AWS : True

- For the emails and ability to send confirmations, we need to set up a few variables for the settings.py file and a couple in the Heroku config variables.
    - In settings.py, add;

            if 'DEVELOPMENT' in os.environ:
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

            EMAIL_HOST_PASS: 'leave blank for now'
            EMAIL_HOST_USER: 'your email address'

    ***It is best to use a Gmail for this as our walkthrough from code institute gives clear instructions on how to set this up.***
    
    - In mail.google.com, go to the cog/settings for the account
    - Click Accounts and Imports tab
    - Click Other Google Account Settings
    - Head to security
    - Make sure 2-Step-Auth is turned on
    - Under this, click on App Passwords
    - Select Mail on the first dropdown
    - Select Other on the second drop-down and add the text 'Django'
    - Once completed, you have generated a 16 digit code - Copy this
    - In Heroku dashboard config vars, add-in;

            EMAIL_HOST_PASS : 'paste 16-digit code here'
    
    This will now allow our emails to be correctly sent from the deployed site.

- Now we need to connect our Gitpod to Heroku

***Due to a serious security breach, we are unable to link our gitpod to Heroku using conventional means - this means we need to take an alternative approach; HEROKU CLI THROUGH GITPOD***

- To start the process, we need to sign in to Heroku CLI in the terminal;
        
        Heroku login -i
    
- Sign in with your regular email account for Heroku

- If you have an up-to-date account with Heroku, you will have switched on 2 step auth for your account, so you cannot sign in using your password; To get around this;
    - You can head to your account icon in the Heroku dashboard
    - Select Account Settings
    - Scroll to the bottom and reveal your API key
    - Copy this code and paste it into your password field in the terminal.
- You should now be connected to Heroku CLI which means we can now complete the Deployment procedure;
    - In terminal, type;

            heroku git:remote -a heroku-app-name

***This must contain the app name we have set up in Heroku otherwise the app will not connect***

- As we have now linked up to our new database to Postgres, we need to migrate all our files to the new database;

        python3 manage.py migrate 

***You do not need to makemigrations first as we have already created them, we just need to move them to the correct place***
        
        git add .
        git commit -m "Complete deployment process to Heroku"
        git push
        git push heroku main

***By pushing to Heroku main, we are sending a copy for all of our code to Heroku to be deployed which means we can avoid the issue regarding the Security breach and not being able to connect for auto or manual deployments***

## E-Commerce Business Model

For Loreyna's Ticket Counter, I have documented the steps to creating my business model.

I have looked at what my site actually is; A site to search for and purchase tickets to redeem at teleportation Aetheryte plaza to any of the popular destinations around the world of Eorzea. My site contains multiple pages with sorting and filtering methods to make the search for a specific destination as efficient as possible.

I have focussed on how I wanted to build this with my users and visitors in mind; I wanted to build an easily navigated site that allows users to add to a storage wallet as much as they want (with incentives to purchasing multiple tickets) And receive all the communications directly to the user without the need for a physical product. The Product is a digital resource which means that there is no requirement for delivery other than the email confirmations with the order number which is then provided to the ticket counter when visiting the plaza. I have also looked into the best methods of marketing and improvements to how my site would be searched for by adding extra keword research as well. These practices and techniques I have documented below;

### SEO Research

I have looked into Search engine optimization for Loreyna's Ticket Counter to improve how my site appears in google searches. By adding metadata with the keywords I have discovered from the research and by adding certain keywords into my site where necessary without abusing the words, this should make my site appear better when searching on google.

My research on what my users need showed me that the users who use traveling sites need to be able to navigate the site with relative ease and often need to purchase tickets quickly if they are in a rush. With that in mind, the stages to finding the locations they may need are as minimal as possible with only one click to get to the list of destinations as well as filterable and searchable fields and options to assist them.

Descriptions of areas and destinations are all containing accurate information and other notes that may help users find locations that may benefit their travels. The content can be updated to add key locations as and when they are discovered to provide the users with the most up-to-date list.

[Seo Research](media/readme-images/seo-research.png)

## Marketing Research

As mentioned in my overview, Loreyna's Ticket Counter is a site for booking tickets for traveling to the far reaches of Eorzea. I have a digital product that enables the customers to my site to purchase the tickets they need and redeem them at any of the aetheryte plazas around Eorzea. With this in mind, I have looked into how it is best to market my site;

### Facebook Business Page

I have created a business page using a popular social media platform to gain the largest possible audience for the launch of the new business - Facebook. 
The main benefit of our site is that use of social media is free to use and is becoming increasingly popular and branching across many platforms; Facebook, Instagram, Snapchat, and Twitter - By participating in Social Media marketing then the business is highly likely to receive a large number of views for people with many different desires and purposes for visiting.
The use of social media platforms for advertising and gaining followers will allow my business to grow as more people can use it. As a travel site, it can be updated at any time with new pictures of locations and offers that users may find interesting. This can be shared by other users of social media as well as added to other platforms should the business prove effective and require expansion.
On the new page, I have created the main identity (the first impression) with recognizable images from the site as well as a logo containing the face of the site, Loreyna Evi'stasia herself. The categories listed are for travel and transport, as well as video game as this is related to our Final Fantasy 14 content on the site itself (for educational purposes only).

I have also added the crucial information that allows visitors to my business page so that they have a way of contacting me through; Email address or visiting my site directly with the linked 'Shop On Website' button. I have no limited trading hours, my shop has no physical address as the products are digital codes redeemable at any location and (even though email doesn't actually exist) no telephone number because there is no mobile phone technology in Eorzea.

There is also the first post for Loreyna's Ticket Counter which establishes that the site is now live and a very brief post explaining what visitors to my site can achieve (the purchase of tickets).

[Header section](media/readme-images/fb-header.png)

[About Section](media/readme-images/fb-about.png)

[Images Section](media/readme-images/fb-images.png)

[First Post](media/readme-images/fb-first-post.png)

Social media also provides the owners of the site to apply for paid ads for their products; Repeating the release of ads and editing them with promotions that will then be displayed in prominent places on the websites they frequesntly use.

Social media also adheres to Influencer Marketing; by getting social media users with a high number of followers to post news and updates, reviews and ratings of your site, they can also provide you with steady visits from other people to your site and then they themsleves may pass on the word and other people will also come to see your site.

As well as influencers and paid ads, you can also pay commisions to others sites with similar products to add your adverts and links to your site into their products or confirmation emails, therefore spreading the word further through the use of other poeple. This is less beneficial as usually the fees are determined by the people you want posting your links and site in their products, so they can charge very hgh fees.

Other platforms that may be popular would also be reddit; based on the content for my site (video game locations) people looking for information on where the best places to go would be quite popular with adventure seekers. This also can be linked and shared and feature on different people's timelines.

### Content Research

I have been researching other sites that deal with either ticket selling or travel sites and have created a document for the research I have completed;

[Content Research](media/readme-images/content-research.png)

### Email marketing

I have included a mail chimp newsletter sign-up form at the bottom of my home page so that people can receive notifications when the admins have updated the website with new areas, districts, or destinations. The form is displayed in the same style as the other two button zones on the home page, with a slightly transparent gold background with a blue button with a custom font.

[MailChimp Signup Form](media/readme-images/ss-mailchimp-form.png)

## Credits

- https://levelup.gitconnected.com/django-customize-404-error-page-72c6b6277317 - This page helped me to build a custom 404 HTML page to make the user experience much improved.
- All of the amazing team members working at the tutor team for the Code Institute, without which, I would be a blubbering mess!
- My mentor Chris Quinn has provided me with sound guidance and direction from the inception of Loreyna's Ticket Counter.
- All of the learning materials I have been studying are provided by the Code Institute.
- Final fantasy images and location names are used for educational purposes only and the information and images are taken from a google search for the specific destinations. This site is completely non-profit and is not used for the marketing of any kind.
- Google and wordtracker.com for research tips and information to improve my site's search engine optimisation