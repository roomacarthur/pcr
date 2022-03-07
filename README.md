# Peer Code Review

## intro

PCR is a social space for users to request code/project reviews and review other peoples projects.

# Table of Contents:

1. [Overview](#overview)
2. [User Experience(UX)](#user-experience-UX)
   1. [Target Audience](#target-audience)
   2. [Strategy](#strategy)
   3. [Scope](#scope)
   4. [Structure](#structure)
   5. [Skeleton](#skeleton)
      1. [Wireframes](#wireframes)
   6. [Surface](#surface)
      1. [Colours](#colours)
      2. [Typography](#typography)
      3. [Images & Icons](#images-&-icons)
3. [Features](#features)
   1. [Existing Features](#existing-features)
   2. [Future Features](#future-features)
4. [Technologies](#technologies)
5. [Testing](#testing)
   1. [Tests](#tests)
   2. [Bugs & Fixes](#bugs-&-fixes)
6. [Deployment](#deployment)
7. [Credits](#credits)

# Overview

PCR is an application built to help all developers not just juniors on their journey. The aim of the application is to allow for users to submit projects that they are currently working to be reviewed. The community is the driving force as they are the ones that will do the reviewing.

People who contribute by reviewing will be acknowledged and for each positively voted review they leave they will gain a point on the Reviewer Leader board.

PCR will be developed using **HTML, CSS, JavaScript & Python.**
It will use a PostgreSQL database to handle the back-end of the application. The application will be deployed using Heroku.

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

wireframes will be here.

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
