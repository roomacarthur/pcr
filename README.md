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

## Strategy

### User Stories

Below are a list of user stories that are very basic and cover a lot of the user and admin needs for PCR. The following User Stories have been broken down into more detail following an Agile Workflow approach with the aid of GitHub **Projects**. A User Story template was created allowing for me to manage the user stories and add them to a precise workflow.

#### As a Site User:

Maybe just link to GitHub Project...

1. I want to be able to understand the functionality of the application so I can decide if what the application offers is something I want.
2. I want to feel welcomed and find the site easy to navigate and view so that as a junior developer I don't feel out of depth.
3. I want to be able to sign up so that I can have my own profile and submit work for review and review other site users work.
4. I want to be able to post a project for review so that I can get a better understanding of my application.
5. I want to be able to easily submit a project for review so that I can do it quickly and efficiently.

#### As a Reviewer:

1.
2.
3.

#### As a site admin:

1.
2.
3.

will include user stories here.

## Scope

## Structure

## Skeleton

### Wireframes

As with all my CSS work I opt for a mobile first approach, the initial planning behind the wireframes for PCR was to make the mobile layout easily adapt to larger screens, meaning the design is only done for mobile and desktop and the application is fully responsive in all screen sizes. Below are the mobile and desktop wireframes. 

Mobile:

Landing View - [Here]()
Update View -  [Here](https://github.com/roomacarthur/pcr/blob/main/documentation/images/wireframes/mobile/mobiel_editview.png)
Generic View - [Here](https://github.com/roomacarthur/pcr/blob/main/documentation/images/wireframes/mobile/mobiel_generic.png)
Detail View - [Here](https://github.com/roomacarthur/pcr/blob/main/documentation/images/wireframes/mobile/mobile_detailview.png)
IsAuth Menu - [Here](https://github.com/roomacarthur/pcr/blob/main/documentation/images/wireframes/mobile/mobile_authmenu.png)
noAuth Menu - [Here](https://github.com/roomacarthur/pcr/blob/main/documentation/images/wireframes/mobile/mobile_noauthmenu.png)

Desktop:

Landing View - [Here](https://github.com/roomacarthur/pcr/blob/main/documentation/images/wireframes/desktop/desktop_landing.png)
Update View - [Here](https://github.com/roomacarthur/pcr/blob/main/documentation/images/wireframes/desktop/desktop_update.png)
Generic View - [Here](https://github.com/roomacarthur/pcr/blob/main/documentation/images/wireframes/desktop/desktop_generic.png)
Detail View - [Here](https://github.com/roomacarthur/pcr/blob/main/documentation/images/wireframes/desktop/desktop_detail.png)
Navigation - [Here](https://github.com/roomacarthur/pcr/blob/main/documentation/images/wireframes/desktop/desktop_auth.png)

## Surface

colours, Typography,

# Features

## Existing Features

## Future Features

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

- Django
- Django-allauth
- Gunicorn
- Psycopg2
- dj_database_url

- Heroku

# Testing






## Tests

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



## Bugs & Fixes

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
   help from CI walkthrough project: 

Rich Text Field from CKEditor
- https://ckeditor.com/docs/ckeditor4/latest/index.html