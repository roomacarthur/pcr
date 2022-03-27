# Peer Code Review
![PCR Banner](https://github.com/roomacarthur/pcr/blob/main/documentation/images/pcr_banner.png)

The Live Site can be viewed on [Heroku](https://pcr-roo.herokuapp.com/)

# Overview

PCR(peer code review) is an application built to help all developers not just juniors on their journey. The aim of the application is to allow for users to submit projects that they are currently working to be reviewed by other site users.

Users can Create, Read, Update & Delete Posts and reviews, They can also like reviews and posts to show appreciation.

PCR will be developed using **HTML, CSS, JavaScript & Python.**

As the site will be deployed via heroku It will use the Heroku Postgres Database and this will be implemented from the very beginning of development as the project will be deployed instantly to keep on top of potential issues. 

# User Experience

## Target Audience

With the aim of PCR being to allow people to get a better understanding of their project and understand how people view it and what they think you can do better to increase the overall level of your project.

The main overarching target audience for PCR is that of people who are in Development no matter there level of experience, Ideally the main focus is to aid newcomers and junior developers in creating better projects.


### User Stories

Below are a list of user stories that are very basic and cover a lot of the user and admin needs for PCR. The following User Stories have been broken down into more detail following an Agile Workflow approach with the aid of GitHub **Projects**. A User Story template was created allowing for me to manage the user stories and add them to a precise workflow with some automation.

#### As a Site User:

1. I want to be able to understand the functionality of the application so I can decide if what the application offers is something I want.
2. I want to feel welcomed and find the site easy to navigate and view so that as a junior developer I don't feel out of depth.
3. I want to be able to sign up so that I can have my own profile and submit work for review and review other site users work.
4. I want to be able to post a project for review so that I can get a better understanding of my application.
5. I want to be able to easily submit a project for review so that I can do it quickly and efficiently.
6. I want to be able to like and unlike content.

#### As a Reviewer:

1. I want to be able to post a review on someones post.
2. I want to be able to edit my post after I have created it.
3. I want to be able to delete my post incase I'm no longer happy with it.

#### As a site admin:

1. I wan't to be able to edit user posted content from within the app. 
2. I wan't to be able to delete user posted content from within the app
3. I wan't to be able to navigate the Admin Panel with ease. 

## Strategy

Create an interactive and responsive app that allows for flawless utilisation for CRUD(Create, Read, Update & Delete) functionality. Users will be able to view content, but to interact fully they will need to sign up and be logged in. Code will be written in a way that allows for easy readability and future updates.

### Project Goals
 - Provide clear and simple data for users.
 - Constantly upgrade and progress the functionality of the app.
 - Allow for users to register
 - Allow for users to create, read, update & delete content. 

## Scope

As it stands PCR has an almost never ending scope and with this I predict there will be multiple iterations. For our intial release we will be focusing on getting an MVP(minimum viable product) to market, once the App is functioning we can start working on separate branches whilst not effecting the current live iteration. 

The first release(MVP) of PCR will be defined by the following features:

   - User authentication (sign up, log in, sign out)
   - Create Posts - Update & Delete
   - Create Reviews - Update & Delete
   - Bland yet effective styling.
   - All Links functional
   - CRUD functionality available on all content.
   - Ability to post code snippits.

Future releases of PCR may include the following:

   - Custom user model for profile customization. 
   - Search bar for users to search through content.
   - Review up/down vote system
   - User score, (posts+reviews+likes)

## Structure

The structure of the application focuses mainly on the content that will be displayed, simple yet clean and clear. A very minimalistic design will be implimented on all pages, base.html will carry 90% on the page styling with the individual view templates just referring to a content section on the page. 

- Header

   - Logo (links back to homapage)
   - Desktop navigation
   - Mobile navigation for smaller devices. 

- Messages

   - Display success messages
   - display content to user upon actions.

- Main

   - This is the block content so all other pages will be styled inside here.

- Footer

   - Links to socials
   - small site navigation. 


## Skeleton

### Wireframes

As with all my CSS work I opt for a mobile first approach, the initial planning behind the wireframes for PCR was to make the mobile layout easily adapt to larger screens, meaning the design is only done for mobile and desktop and the application is fully responsive in all screen sizes. Below are the mobile and desktop wireframes. 

Mobile:

- Landing View - [Here](https://github.com/roomacarthur/pcr/blob/main/documentation/images/wireframes/mobile/mobile_landing.png)
- Update View -  [Here](https://github.com/roomacarthur/pcr/blob/main/documentation/images/wireframes/mobile/mobiel_editview.png)
- Generic View - [Here](https://github.com/roomacarthur/pcr/blob/main/documentation/images/wireframes/mobile/mobiel_generic.png)
- Detail View - [Here](https://github.com/roomacarthur/pcr/blob/main/documentation/images/wireframes/mobile/mobile_detailview.png)
- IsAuth Menu - [Here](https://github.com/roomacarthur/pcr/blob/main/documentation/images/wireframes/mobile/mobile_authmenu.png)
- noAuth Menu - [Here](https://github.com/roomacarthur/pcr/blob/main/documentation/images/wireframes/mobile/mobile_noauthmenu.png)

Desktop:

- Landing View - [Here](https://github.com/roomacarthur/pcr/blob/main/documentation/images/wireframes/desktop/desktop_landing.png)
- Update View - [Here](https://github.com/roomacarthur/pcr/blob/main/documentation/images/wireframes/desktop/desktop_update.png)
- Generic View - [Here](https://github.com/roomacarthur/pcr/blob/main/documentation/images/wireframes/desktop/desktop_generic.png)
- Detail View - [Here](https://github.com/roomacarthur/pcr/blob/main/documentation/images/wireframes/desktop/desktop_detail.png)
- Navigation - [Here](https://github.com/roomacarthur/pcr/blob/main/documentation/images/wireframes/desktop/desktop_auth.png)

### Database

For the PCR application a relational databse was designed, to save both the Post and Review data. Both models are designed to optimise CRUD functionality. As the application will be deployed via heroku, the deployment will be done very early in development. Deploying early will mean we can access the [Heroku Postgres](https://elements.heroku.com/addons/heroku-postgresql) Database and avoid any issues later in development moving from Djangos built in SQL database to the heroku one. Below is the tamplate I will be using to build the models, the RichTextEdit fields will allow for a rich text editor from [CKEditor](https://ckeditor.com/) which inturn will allow for code snippets. 

![Database model template](https://github.com/roomacarthur/pcr/blob/main/documentation/images/model_template.png)


## Surface

### Typography

For PCR two fonts have been used [Robot](https://fonts.google.com/specimen/Roboto) and [Lato](https://fonts.google.com/specimen/Lato?query=lato), both from Google Fonts, They both use Sans Serif as a backup font. 

### Colours

![colours](https://github.com/roomacarthur/pcr/blob/main/documentation/images/color-palette.png)

A very basic, yet refreshing colour palette was picked for PCR, the above colours are used frequently throughout the project with a couple other colours being called for better defined :hover objects and Yes/No butons. The colour of #ff0000(Bright RED) was used for the lick button so it would stand out a lot more.

### Visuals

Across the application, box shadows are used to give depth to containers to make them stand out, all links, and interactive actions have a :hover object set in CSS with some transforming to a bigger scale and some changing to a more prominent colour. All clickable objects have cursor set to pointer. 
### Images

With the first release of PCR we will not be supporting images, but it is something we will be looking into in the future, as it stands our only image is our Favicon which is loaded via our static files. 

# Features

## Existing Features
   
   - User authentication (sign up, log in, sign out)
   - Create Posts - Update & Delete
   - Create Reviews - Update & Delete
   - Bland yet effective styling.
   - All Links functional
   - CRUD functionality available on all content.
   - Ability to post code snippits.

## Future Features

   - Custom user model for profile customization. 
   - Search bar for users to search through content.
   - Review up/down vote system
   - User score, (posts+reviews+likes)

# Technologies

- Vs Code
- Git
- Bash
- GitHub
- HTML5
- CSS3
- Python
- JavaScript
- jQuery
- Heroku

When working on pyhton projects I work within a virtual env and track all my packages in a requirements.txt file. 

Below is a list of all the python packages used for PCR and there version types.:
- asgiref==3.5.0
- bleach==4.1.0
- certifi==2021.10.8
- cffi==1.15.0
- charset-normalizer==2.0.12
- cryptography==36.0.1
- defusedxml==0.7.1
- dj-database-url==0.5.0
- Django==3.2.12
   - Django 3.2.12 was a specific use as there was security issues with previous 3.2 versions.
- django-allauth==0.49.0
- django-ckeditor==6.2.0
- django-crispy-forms==1.14.0
- django-js-asset==2.0.0
- gunicorn==20.1.0
- idna==3.3
- oauthlib==3.2.0
- packaging==21.3
- psycopg2==2.9.3
- pycparser==2.21
- PyJWT==2.3.0
- pyparsing==3.0.7
- python3-openid==3.2.0
- pytz==2021.3
- requests==2.27.1
- requests-oauthlib==1.3.1
- six==1.16.0
- sqlparse==0.4.2
- tzdata==2021.5
- urllib3==1.26.8
- webencodings==0.5.1
- whitenoise==6.0.0


# Testing

## Tests

### Generic Testing

Responsive layout testing along with page content was thoroughly tested and results where recorded in a spread sheet and saved into a PDF for easier viewing. 

[test sheet](https://github.com/roomacarthur/pcr/blob/main/documentation/testing_sheet.pdf)

All tests PASSED with some tests done over the phone with relatives. I have also had multiple friends test the site and no issues have been raised and all devices used have displayed the app exactly how it should be shown.

### Python tests:

1. Test: Test the NewPost(CreateView) by creating a new post.
   - Result: Successfully called the correct form, input data and successfully posted the new data to the DataBase.
   
   PASS

2. Test: Test the PostEdit(UpdateView) by editing a post.
   - Result: Successful get request for the stored data. Displayed in the PostForm, Edited data and a successful POST request was sent, adding the new updated data to the DataBase record.
   
   PASS

3. Test: Test the PostDelete(DeleteView) by deleting a post.
   - Result: Prompted with a message asking me to confirm deletion, deletion from DataBase was successful and redirected to homepage.

   PASS

4. Test: Test the NewReview(CreateView) by creating a new Review on a Post
   - Result: Only one field from the form is present, Successfully posted a Review with the view fetching my username and the creation date which is displayed along with my review.

   PASS

5. Test: Test the ReviewDelete(DeleteView) by deleting a review.
   - Result: Once clicking the delete button on the review, I am prompted with a screen to confirm I would like to delete the review. Upon clicking yes, I am redirected back to the original Post.

   PASS

6. Test: Test the ReviewEdit(UpdateView) by editing a review.
   - Result: redirected to a template with the ReviewForm data, where I can access my database record for this review, update and submit to the database. I am then redirected back to the original post.

   PASS

### JavaScript

1. Test: Via Chrome Dev panel, ensure that scripts are being called on all pages.
   - Result: HighlightsJS is being called along with CDN data from the head in base.html

   PASS

2. Test: Check jQuery is attaching placholders for the inputs on New Post page.
   - Result: Each field that is using jQuery to attach a placeholder is working correctly.

   PASS

### Google Chrome Lighthouse Tests

Lighthouse testing was completed in a fresh incognito Google Chrome window. 

Desktop:

   - [Desktop Landing](https://github.com/roomacarthur/pcr/blob/main/documentation/images/lighthouse/desktop/desktop_landing.png)
   - [Desktop Post Detail](https://github.com/roomacarthur/pcr/blob/main/documentation/images/lighthouse/desktop/desktop_postdetail.png)
   - [Desktop Update](https://github.com/roomacarthur/pcr/blob/main/documentation/images/lighthouse/desktop/desktop_update.png)

Mobile:

   - [Mobile Landing](https://github.com/roomacarthur/pcr/blob/main/documentation/images/lighthouse/mobile/mobile_landing.png)
   - [Mobile Post Detail](https://github.com/roomacarthur/pcr/blob/main/documentation/images/lighthouse/mobile/mobile_postdetail.png)
   - [Mobile Update](https://github.com/roomacarthur/pcr/blob/main/documentation/images/lighthouse/mobile/mobile_update.png)

All results from Lighthouse tests where great, with nearly all results finishing in the perfect category. 

## Bugs & Fixes

1. Success message not working for PostDelete(DeleteView). 
   - FIX: The stock CBV success message doesn't seem to work for DeleteViews. The fix was to get the objects data and then pass that through to format the string with the objects dictionary. Help from a Stack Overflow post. [Credit](https://stackoverflow.com/questions/24822509/success-message-in-deleteview-not-shown)

2. Content past through the rich text editor was displaying raw HTML data in the view. 
   - FIX: Passing the "| safe" tag into the view is allowing for the rich text to bew rendered. 

3. Major Databse Conflicts in early Development, preventing from any data to be passed back and forth. 
   - FIX: running "python manage.py migrate 'app' zero" Deleting all entries into /migrations apart from the __ init __ file and resetting the database in heroku, wiping the Database of all data fixed the issue. 

4. When completing the New Post form, the slug field was not being auto populated. 
   - FIX: With help from [Here](https://stackoverflow.com/questions/63053210/changing-id-field-to-slug-field-in-django) A save function was added to the model, to use slugify to post the new slug to the model upon form completion.

5. Rich Text editor not displaying in Post Review Form. 
   - No Fix was found within the allowed timeframe. 

# Deployment

This project will be deployed to [Heroku](https://heroku.com) using the following outlined steps:

## Setting up Heroku Deployment

1. Navigate to [Heroku](https://heroku.com).
2. Create an account or log in.
   - If creating an account select **Python** as the **_Primary development language_**
3. Click the **New** button found top right of page and select **Create New App** from the dropdown menu.
4. Provide an app name **_this has to be unique_**
5. Select your region.
6. Click **Create App**
7. Navigate to the **Deploy tab**
8. Scroll down the page until you come across **Deployment Method**
9. Click **GitHub**
   - Connect your GitHub account if this is your first time.
10. Search for your projects GitHub Repository and click **connect**

## Automatic Deployment

When it comes to deployment there are two options **Automatic Deployment** or **Manual Deployment**.

For this project I have opted for **Automatic Deployment** as this allows for Heroku to re run the build and update my deployment every time I push code to my GitHub Repository.

To activate this:

1. Navigate to the **Deploy Tab**
2. Scroll down until you come across **Automatic Deployment**
3. Ensure that the correct branch is selected.
   - In Most cases this will be either main or master
   - In my case it will be main
4. Click **Enable Automatic Deploys**

The project is now deployed and will automatically re-run the build and deploy every time I push code to GitHub.

## Environment Variables

Within my local files my Environmental Variables are set within a env.py file, the details of this file as confidential and are added to the _.gitignore_ file so that they aren't publicly available. But because these files are not pushed to GitHub we need to enable the same Variables within Heroku for the application to run successfully.

# Credits

Help with Class Based Views
- https://ccbv.co.uk/

Help with login_required method. 
- https://steemit.com/utopian-io/@duski.harahap/create-a-forum-application-using-django-6-crud-system-and-url-protection-redirect-system
Success message not working in UpdateView.
   note: Bizarre issue as normal success_message worked in DeleteView.
- https://stackoverflow.com/questions/39999956/django-how-to-send-a-success-message-using-a-updateview-cbv

- PostDetail view.
   help from CI walk through project, I Think Therefore I Blog
   https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+FST101+2021_T1/courseware/b31493372e764469823578613d11036b/c6a89f138afe4b209ee4fa6d6f1251a3/ 

Rich Text Field from CKEditor
- https://ckeditor.com/docs/ckeditor4/latest/index.html

- Code Institute - Support
