<h1 align="center">Recipe Bundle</h1>

[View the live project here.](#)

Two user types' credentials have been included below:
| User type | Username | Password |
| --- | --- | --- |
| Admin | Admin | Admin |
| General | User1 | User1 |
(Case sensitive)

With this website, users are able to create custom clothing. From standard templates, users can add content from a library of images, their own text, or even upload their own designs to use.

![mockup](https://ms3recipebundle.s3.eu-central-1.amazonaws.com/readme/amiresponsive.png)

## Contents <!-- omit in toc -->

- [1. User Experience (UX)](#1-user-experience-ux)
  - [1.1 Strategy Plane](#11-strategy-plane)
    - [Target audience](#target-audience)
  - [1.2 Scope Plane](#12-scope-plane)
    - [1.2.1 Requirements and functional specifications](#121-requirements-and-functional-specifications)
    - [1.2.2 User Stories](#122-user-stories)
      - [Site Visitor Goals](#site-visitor-goals)
      - [Site Owner Goals](#site-owner-goals)
  - [1.3 Structure Plane](#13-structure-plane)
    - [Structure](#structure)
  - [1.4 Skeleton Plane](#14-skeleton-plane)
    - [1.4.1 Navigation](#141-navigation)
    - [1.4.2 Wireframes](#142-wireframes)
  - [1.5 Surface Plane](#15-surface-plane)
    - [Colour scheme](#colour-scheme)
    - [Typography](#typography)
    - [Imagery](#imagery)
- [2. Technologies Used](#2-technologies-used)
  - [2.1 Language Used](#21-language-used)
  - [2.2 Frameworks, Libraries & Programs Used](#22-frameworks-libraries--programs-used)
- [3. Features](#3-features)
      - [3.1 Existing Features](#31-existing-features)
      - [3.2 Features Left to Implement](#32-features-left-to-implement)
- [4. Testing](#4-testing)
      - [Click here to go to testing](#click-here-to-go-to-testing)
- [5. Deployment](#5-deployment)
  - [5.1. GitHub Pages](#51-github-pages)
  - [5.2. Forking the GitHub Repository](#52-forking-the-github-repository)
  - [5.3. Making a Local Clone](#53-making-a-local-clone)
- [6. Credits](#6-credits)
  - [6.1. Code](#61-code)
  - [6.2. Content](#62-content)
  - [6.3. Media](#63-media)
  - [6.4. Acknowledgements](#64-acknowledgements)

# 1. User Experience (UX)

## 1.1 Strategy Plane

With this website, users customise templates for clothing and apparel with images from a library or self-upload, or text with the available fonts.

Users can track their order from start to finish - designing, submitting, paying, tracking status and saving designs to order again at a later time.

### Target audience

- Anyone looking to order a customised t-shirt.
- Anyone looking to make a personalised printed gift.

## 1.2 Scope Plane

### 1.2.1 Requirements and functional specifications

- Header and Footer
  - Header is split into teaser bar (special offer for no shipping fees), text and image logo that returns to landing page, navbar with links to about, design and products page, buttons for user account and shopping basket with total.
  - On small and medium device sizes: Text and image logo, icons for user account, shopping card and total and search menu, with hamburger menu for about, design and products pages.
  - Products button navigates to:
    - Categories (men, ladies, kids, other)
    - Sub-categories under each (t-shirts, sweatshirts, etc.)
  - User account button navigates to:
    - Super User only: Admin;
    - Logged In User: Profile, Orders, Saved Designs, Log Out;
    - Logged Out User: Log In and Register.
  - Footer with icons, navigates to Twitter, FaceBook and Pinterest.
- Landing page
  - Visible when signed out or signed out
- Administrator
  - Maintain content
  - Track order status
  - Manage orders
- Products page
  - Visible to all site visitors
  - Splits 4 categories
  - Further split into sub-categories
  - Navigates to design page
- Design page
  - Visible to all site visitors
  - Upload of content only for registered for users - prompt to sign up / in
  - Template with a canvas area, where customisation occurs
  - Control panel for customising chosen apparel
- User profile page
  - Only available to signed in users
  - Contains personal information (contact details), editable
  - Shows order history, with option to reorder
  - Saved design
- User authentication
  - Sign in required to get access to user profile area
  - Sign in required to upload custom designs
  - Sign in required as super user for administration
  - Sign out
  - Register new credentials
  - Register / sign up with Google account
  - Register / sign up with Facebook account
  - Reset password from Sign in page
- Shopping cart
  - Checkout as guest
  - Sign in to register
- Contact form with options to report bugs, make suggestions or other.

### 1.2.2 User Stories

#### Site Visitor Goals

  1. As a Site Visitor, I want to easily navigate the website's pages from the header and footer.
  2. As a Site Visitor, I want to be able to browse through examples of previously completed work.
  3. As a Site Visitor, I want to be able to search through images to select for my designs.
  4. As a Site Visitor, I want to be able add my designs to a template for visual confirmation.
  5. As a Site Visitor, I want to be able to track the status of my orders.
  6. As a Site Visitor, I want to be able to edit my contact details.
  7. As a Site Visitor, I want to be able to contact site owners.

#### Site Owner Goals

  8. As the Site Owner, I want to make it easy and convenient for users to send suggestions for improvement or bug reports to a dedicated mailbox, thereby improving the chances of them returning.
  9. As the Site Owner, I want to restrict content uploads to registered users.
  10. As the Site Owner, I want to view a record of orders in various states.
  11. As the Site Owner, I want to be able to easily add new images or fonts.

## 1.3 Structure Plane

### Website pages

The website consists of the following pages:

- Landing page: First web page and home page.
- Register page: Register username and password.
- Sign in page: Allows returning (registered) visitors to sign in, choice between email, Facebook or Google login.
- Admin page: Restricted to super user - view all orders, edit content and fonts, edit orders.
- Product page: Preview of categories and subcategories.
- Product design page: Page with template, canvas and controls for custom content.
- Shopping cart page: Overview of order with link to checkout.
- Checkout page: Add delivery details and payment credentials, call from profile if registered and signed in.
- Checkout success page: Confirmation of order completion and payment.
- Profile page: Contact details, previous orders and saved designs.
- Saved designs page: Detailed view of previous designs, option to edit (redirect to design page).
- Order history page: Detailed overview of past orders.
- Contact page: Contact form with subject options.
- 404 error page: Displays when incorrect URL entered.
- 400 and 500 error pages: Display when errors occur on the website.

### Code Structure:

- Django Framework used to construct / build the website.
- Project structure (apps):
  - Home - Landing page.
  - Product - Product overview, Product design.
  - Profile - Contact details, order tracking, saved designs.
  - Checkout - Shopping cart, checkout, checkout success.

- Additional content:
  - Manage.py
  - Templates - base.html, allauth, includes (headers and footers)
  - Static
    - CSS
    - JS
  - Custom storage - AWS
  - Procfile - required to run application
  - Requirements.txt - required apps to run

### Database

- Deployed to a [SQLite](https://www.sqlite.org/index.html) database


## Amazon Web Services S3 bucket

Images uploaded by users and readme images are stored in AWS S3. Header image and favicon have been locally saved for faster loading.

Steps taken integration:

1. Created user account with AWS
2. Created an IAM user -  [detailed steps](https://docs.aws.amazon.com/AmazonS3/latest/userguide/setting-up-s3.html)
![S3_IAM](https://ms3recipebundle.s3.eu-central-1.amazonaws.com/readme/AWS_S3_2.png)
3. Created S3 bucket named ms3recipebundle - [detailed steps](https://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-bucket.html)
![S3_landing](https://ms3recipebundle.s3.eu-central-1.amazonaws.com/readme/AWS_S3_1.png)
4. Imported Python library, [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html), as console to create, configure and manage AWS services.
5. Assigned s3 variables (bucket name, url, access and security keys) in util.py file.

## 1.4 Skeleton Plane

### 1.4.1 Navigation

- Page header navigates to Landing page, Admin page (Admin user only), Collection page and Sign Out page (if signed in), Sign In page and Register page (if not signed in).
- Sign In page navigates to Register page and Reset page.
- Sign Out page navigates to Register page.
- Page footer navigates to social media links (Pinterest, FaceBook and Twitter).

### 1.4.2 Wireframes

- Home / Landing page ![view](https://ci-ms4-blacksheepprint.s3.eu-central-1.amazonaws.com/readme/index_v1.png)
- Products page ![view](https://ci-ms4-blacksheepprint.s3.eu-central-1.amazonaws.com/readme/products_v1.png)
- Design page ![view](https://ci-ms4-blacksheepprint.s3.eu-central-1.amazonaws.com/readme/design_v1.png)

## 1.5 Surface Plane

### Colour scheme

- The colour scheme was generated from the header image.

- The main colours for the themes were generated with the [colormind.io](http://colormind.io/) Website Colors tool 
  - #F4F4EE Pampas - Light background colour and light-on-dark text
  - #7DA074 Amulet - Light accent, used for teaser banner
  - #2CC4D5 Scooter - Main brand colour, used for header and footer
  - #855682 Strikemaster - Dark accent
  - #386477 Oracle - Dark-on-light text and dark background
  - Snapshot of palette images ![mockup](https://ci-ms4-blacksheepprint.s3.eu-central-1.amazonaws.com/readme/colour-palette.png)

### Typography

- For the fonts, I searched for the best fonts for an ecommerce website. I chose the following complementary fonts from [this article](https://rocketium.com/academy/20-best-fonts-for-ecommerce-businesses/):

  - Main font: [Alegreya](https://fonts.google.com/specimen/Alegreya#standard-styles)
  - Complementary font: [Alegreya Sans](https://fonts.google.com/specimen/Alegreya+Sans)

- While the fonts are very similar, the complementary font is used to keep elements separate.

### Imagery

- Since the focus should be on the design feature, I wanted to keep the background and header simple. To achieve this, I opted to limit additional "standard" imagery on all pages:
  - The landing page has a full-page cover, with a lady pointing at a t-shirt with a design for a playful feel.
  - The products page have images to visually identify the categories
  - No additional images in the product design page

# 2. Technologies Used

## 2.1 Languages Used

- [HTML 5](https://en.wikipedia.org/wiki/HTML5)
- [CSS](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
- [Python](https://www.python.org/)

## 2.2 Frameworks, Libraries & Programs Used

### - [Bootstrap 5.1:](https://getbootstrap.com/docs/5.1/getting-started/introduction/) <!-- omit in toc -->

- Bootstrap was used to assist with the responsiveness and styling of the website

### - [Google Fonts:](https://fonts.google.com/) <!-- omit in toc -->

- Imported (fonts)] fonts from Google Fonts into the style.css file used on all pages throughout the website.
  
### - [Font Awesome:](https://fontawesome.com/) <!-- omit in toc -->

- Font Awesome was used on all pages throughout the website to add icons for aesthetic and UX purposes.

### - [jQuery:](https://jquery.com/) <!-- omit in toc -->

- jQuery in conjunction with Bootstrap make the navbar and accordion responsive.

### - [Jinja](https://jinja.palletsprojects.com/en/3.0.x/) <!-- omit in toc -->

- Template engine for Python programming language.

### - [Git:](https://git-scm.com/) <!-- omit in toc -->

- Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.

### - [GitHub:](https://github.com/) <!-- omit in toc -->

- GitHub is used to store the projects code after being pushed from Git.

### - [Visual Studio Code:](https://code.visualstudio.com/) <!-- omit in toc -->

- IDE used to write code for this project.

### - [Balsamiq:](https://balsamiq.com/) <!-- omit in toc -->

- Balsamiq was used to create the wireframes during the design process.

### - [Am I Responsive:](http://ami.responsivedesign.is/) <!-- omit in toc -->

- Used to create mockups for README file.

### - [Resizing.app:](https://resizing.app/features/resize-png/) <!-- omit in toc -->

- Resize PNG to reduce README file sizes.

### - [PolicyMaker](https://policymaker.io/) <!-- omit in toc -->

- Terms for register form obtained from free template [from](https://policymaker.io/terms-conditions-ready)

### - [Paint 11.2110.0.0](https://support.microsoft.com/en-us/windows/get-microsoft-paint-a6b9578c-ed1c-5b09-0699-4ed8115f9aa9)

- Used to create placeholder image and user testing files.

### - [Snipping Tool 11.2109.37.0](https://support.microsoft.com/en-us/windows/use-snipping-tool-to-capture-screenshots-00246869-1843-655f-f220-97299b865f6b)

- Used for screenshots during testing.

### - [colormind.io](http://colormind.io/image/)

- Used to generate colour palette for website.

# 3. Features

## 3.1 Existing Features

- Responsive on all device sizes
- User authentication (Sign in, Sign out, Reset Password and Register)
- Interactive elements

## 3.2 Features Left to Implement

# 4. Testing

## [Click here to go to testing](TESTING.md)

# 5. APIs

# 6. Deployment

## 6.1 - GitHub

### Forking the GitHub Repository

A fork is a copy of the repository, allowing you to experiment with changes without affecting the original project.

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/ElrieM/MS3_RecipeBundle).
2. In the banner above the Repository, click on the "Fork" button.
3. If you have succeeded, you now have a copy of the original repository in your GitHub account.

Alternatively, click [here](https://docs.github.com/en/github/getting-started-with-github/quickstart/fork-a-repo) for a guide to fork a repository.

### Making a Local Clone

A clone allows you to create a local copy of a repository on your computer and sync between your computer and the GitHub repository.

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/ElrieM/MS3_RecipeBundle)
2. Click on Code, click on the copy button next to HTTPS to copy the URL.
3. Open Git Bash.
4. Change the current working directory to the location where the cloned directory should be stored.
5. Type "git clone', then paste the URL copied in step 2.
6. Press Enter to create a local clone.

Alternatively, click [here](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository-from-github/cloning-a-repository) for a guide to clone a repository.

### Create env.py

- Create env.py file in root folder, with the following parameters
    os.environ.setdefault("IP", [user input])
    os.environ.setdefault("PORT",  [user input])
    os.environ.setdefault("SECRET_KEY",  [user input])
    os.environ.setdefault("MONGO_URI",  [user input])
    os.environ.setdefault("MONGO_DBNAME",  [user input])
    os.environ.setdefault("AWS_ACCESS_KEY_ID",  [user input])
    os.environ.setdefault("AWS_SECRET_ACCESS_KEY",  [user input])

- Install packages per requirements.txt file

- Run application with CLI (PIP / PIPENV, depending on environment, run)  python3 app.py

## 6.2 - Heroku

Heroku is a free hosting service for hosting small projects.

### Deploy to Heroku

- Create a Heroku account
- Install Python (3.10 at time of creation) locally.
- Install Heroku CLI (first install Git CLI if you don't already have it installed).
- Log in to Heroku from CLI.
- Prepare and clone app - clone Github Repository.
- Deploy with heroku create and git push heroku main.
- Define a Procfile.
- Declare app dependencies in requirements.txt (pip install -r requirements.txt)
- Create new application with unique name.
- Navigate to Deploy, and connect to GitHub. Select repo, and then branch.
- Configure Config Vars - same parameters as in env.py file mentioned above.
- Deploy from dashboard.
- Open App.
- For more [details, visit here](https://devcenter.heroku.com/articles/getting-started-with-python)

### Deploy to AWS (Amazon Web Services)

1. Create AWS user account [here](https://aws.amazon.com/).
2. Create new user on IAM console [here](https://console.aws.amazon.com/).
3. Set AmazonS3FullAccess for user and note AWS Access and Secret keys.
4. On AWS S3 console, create a new bucket. Bucket name can be updated in the util.py file.
5. Set bucket policy, [see here](https://docs.aws.amazon.com/AmazonS3/latest/userguide/bucket-policies.html) for details and to generate policies. There is also an option to have policies generated from the bucket policies page.
6. Update util.py variables with bucket details from AWS:

    s3_bucket_name = "ms3recipebundle"
    s3_bucket_url = "http://ms3recipebundle.s3.amazonaws.com/"

### Set up MongoDB

1. Create new user account [here](https://www.mongodb.com/).
2. Create data cluster, see [here](https://docs.mongodb.com/manual/tutorial/getting-started/) for details.
3. Click on "Browse Collections", then create 5 collections:
   - users
   - cuisines
   - types
   - diet
   - recipes
4. Under Security > Database Access, create user with read and write access.
5. Under Security > Network Access, allow network access from the application's IP address.
6. Under Deployment > Database, click on Connect. Database is now connected to app.
7. In env.py, update MONGO_URI, MONGO_DBName and SECRET key and deploy to Heroku.

# 7. Credits

## 7.1. Code

- Bootstrap 5: Bootstrap Library used to make the site responsive using the Bootstrap Grid System
- [Form autocomplete](https://www.chromium.org/developers/design-documents/form-styles-that-chromium-understands)
- [AWS file uploading](https://gist.github.com/leongjinqwen/9d9a2d58bf2fb923658820559a88a5ec)
- [Using FabricJS for t-shirt printing website](https://ourcodeworld.com/articles/read/1016/how-to-create-your-own-t-shirt-designer-using-fabricjs-in-javascript)

## 7.2. Content

- Created favicon from logo using [favicon.cc](https://www.favicon.cc/)

## 7.3. Media

- [Font Awesome](http://fontawesome.com)
- [Google Fonts](https://fonts.google.com/)
- [Pexels](https://www.pexels.com/)
- [Testing and ReadMe example](https://github.com/pmeeny/CI-MS3-https://github.com/pmeeny/CI-MS3-FootballMemories)overview/why-cypress)
- [Header image](https://github.com/ElrieM/MS3-RecipeBundle/blob/3eb943e1db8a44dc72540c3f1a523e6976ab4384/README.md#L465)
- [Placeholder image](https://www.freeiconspng.com/img/23499)

## 7.4. Acknowledgements

- My mentor for guidance and support.
- My partner for advice and patience.
- My brothers for their pep-talks and positivity.
- My mother for all her words of love and encouragement.
- My manager, for support and holding me accountable for my wellbeing.