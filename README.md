<h1 align="center">BlackSheep Printing</h1>

[View the live project here.](https://ci-ms4-blacksheepprint.herokuapp.com/)

Two user types' credentials have been included below:
| User type | Username | Password |
| --- | --- | --- |
| Admin | Admin | Django2022 |
| General | User1 | Django22 |
(Case sensitive)

For Stripe payment user testing, use card details from ![here](https://ci-ms4-blacksheepprint.s3.eu-central-1.amazonaws.com/readme/stripe_payment_test.png)

With this website, users are able to buy pre-created clothing, or create custom clothing from uploaded images.

![mockup](https://ci-ms4-blacksheepprint.s3.eu-central-1.amazonaws.com/readme/amiresponsive.png)

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

With this website, users customise templates for clothing and apparel with uploaded images, or choose from pre-designed clothing.

Users can track their order from start to finish - designing*, submitting, paying, and tracking status.

'* only when creating a custom item of clothing.

### Target audience

- Anyone looking to order a custom clothing.
- Anyone looking to add their designs to clothing.

## 1.2 Scope Plane

### 1.2.1 Requirements and functional specifications

- Header and Footer
  - Header is split into teaser bar (special offer to qualify for free delivery), company name above logo, image logo that returns to landing page, navbar with links to design and (pre-designed) products page, buttons for user account and shopping basket with total.
  - On small and medium device sizes: Text and image logo, icons for user account, shopping card and total and search menu, with hamburger menu for design and products pages.
  - Products button navigates to:
    - Categories (men, ladies, kids, other)
    - Sub-categories under each (t-shirts, sweatshirts, etc.)
  - User account button navigates to:
    - Super User only: Admin View;
    - Logged In User: Profile, Log Out;
    - Logged Out User: Log In and Register.
  - Footer with icons, navigates to Terms and Conditions, Twitter, FaceBook and Pinterest.
- Landing page
  - Visible whether signed in or signed out
- Admin View
  - Navigates to products or designs add / edit pages
  - Removes products or design templates
- Products page
  - Visible to all site visitors
  - Navigates to product detail, (superuser) edit and delete pages
- Design page
  - Visible to all site visitors
  - Navigates to design page, (superuser) edit and delete templates (mockups)
  - Upload of content only for registered for users
  - Template with a canvas area, where customisation occurs
  - Control panel for customising chosen apparel
- User profile page
  - Only available to signed in users
  - Contains personal information (contact details), editable
  - Shows order history, with option to reorder
- User authentication
  - Sign in required to get access to user profile area
  - Sign in required as super user for administration
  - Sign out
  - Register new credentials
  - Register / sign up with Google account
  - Reset password from Sign in page
- Shopping cart
  - Checkout as guest
  - Sign in to register
- Checkout
  - Pay online with secure payment
- Contact form with options to report bugs, make suggestions or other.

### 1.2.2 User Stories

#### Site Visitor Goals

  1. As a Site Visitor, I want to easily navigate the website's pages from the header and footer.
  2. As a Site Visitor, I want to be able to browse through available products.
  3. As a Site Visitor, I want to be able to upload and move images for my designs.
  4. As a Site Visitor, I want to be able to view my past orders.
  5. As a Site Visitor, I want to be able to edit my contact details.
  6. As a Site Visitor, I want to be able to pay for my order securely.
  7. As a Site Visitor, I want to be able to add products to and edit contents of my shopping cart.
  8. As a Site Visitor, I want to be able to search through products.
  9. As a Site Visitor, I want to be able to filter products by category, price and name.

#### Site Owner Goals

  10. As the Site Owner, I want to restrict content uploads to registered users.
  11. As the Site Owner, I want to view a record of orders in various states.
  12. As the Site Owner, I want to be able to easily add or edit design templates. and details.
  13. As the Site Owner, I want to be able to easily add or edit products and details.

## 1.3 Structure Plane

### Website pages

The website consists of the following pages:

- Landing page: First web page and home page.
- Register page: Register username and password.
- Sign in page: Allows returning (registered) visitors to sign in, choice between email, or Google login.
- Admin page: Restricted to super user - view all orders, edit content and fonts, edit orders.
- Product page: Preview of categories and subcategories.
- Design page: Page with template, canvas and controls for custom content.
- Shopping cart page: Overview of order with link to checkout.
- Checkout page: Add delivery details and payment credentials, call from profile if registered and signed in.
- Checkout success page: Confirmation of order completion and payment.
- Profile page: Contact details, previous orders and saved designs.
- Order history page: Detailed overview of past orders.
- Contact page: Contact form with subject options.
- 404 error page: Displays when incorrect URL entered.
- 400 and 500 error pages: Display when errors occur on the website.

### Code Structure

- Django Framework used to construct / build the website.
- Project structure (apps):
  - Home - Landing page, adapted from Code Institute's Boutique Ado walkthrough project.
  - Product - Product overview, Product details, Product admin (edit, delete), adapted from Code Institute's Boutique Ado walkthrough project.
  - Design - Design overview, Design customisation, Design template admin (edit, delete), adapted from Code Institute's Boutique Ado walkthrough project.
  - Profile - Contact details, order tracking, adapted from Code Institute's Boutique Ado walkthrough project, and admin view.
  - Checkout - Checkout, checkout success, adapted from Code Institute's Boutique Ado walkthrough project.
  - Cart - Shopping cart, adapted from Code Institute's Boutique Ado walkthrough project.

- Additional content:
  - Manage.py
  - Templates - base.html, allauth, includes (headers and footers)
  - Static
    - CSS
    - JS
  - Media - locally stored images
  - Custom storage - AWS
  - Google oauth app - files for Google oauth login
  - Procfile - required to run application
  - Requirements.txt - required apps to run
  - Pipfile and Pipfile.lock - required apps to run
  - Readme - readme documentation
  - Testing - testing documentation

### Database

- Front-end consists of HTML5, CSS3, supplemented wtih Bootstrap 5 and JavaScript.
- Back-end consists of Python-based Django framework and Postgres database for Heroku deployed site.

- Local development database: [SQLite3](https://www.sqlite.org/index.html)
- Deployed site database: [PostgreSQL](https://www.postgresql.org/)

#### Database model

![Overview of tables, fields and data types in models](https://ci-ms4-blacksheepprint.s3.eu-central-1.amazonaws.com/readme/db-model.png)

#### Models

##### User Model

- Forms part of allauth model.
- Fields included:
  - username
  - password
  - first name
  - last name
  - email address
  - (is) active
  - staff status
  - superuser status

#### User Profile Model

- Forms part of user profile model
- Fields included:
  - user
  - default phone number
  - default street address 1
  - default street address 2
  - default town or city
  - default county
  - default postcode
  - default country

#### Order Model

- Contains past order information
- Fields included:
  - order number
  - user profile
  - full name
  - email
  - phone number
  - street address 1
  - street address 2
  - town or city
  - county
  - postcode
  - country
  - order date
  - delivery cost
  - order total
  - grand total
  - original cart
  - stripe pid

#### Order Line Items Model

- Contains details at each order line
- Fields included:
  - order (number)
  - product
  - product size
  - quantity
  - line item total

#### Category Model

- Contains product category list
- Fields included:
  - (category) name
  - friendly name

#### Product Model

- Contains products and details
- Fields included:
  - category
  - stock code
  - (product) name
  - (product) description
  - has sizes
  - price
  - image url
  - image

#### Design Model

- Contains templates
- Fields included:
  - (template) name
  - friendly name
  - image url
  - image
  - base price
  - has sizes

## Amazon Web Services S3 bucket

Images uploaded by users and readme images are stored in AWS S3. Header image and favicon have been locally saved for faster loading.

Steps taken integration:

1. Created user account with AWS
2. Created an IAM user -  [detailed steps](https://docs.aws.amazon.com/AmazonS3/latest/userguide/setting-up-s3.html)
![S3_IAM](https://ci-ms4-blacksheepprint.s3.eu-central-1.amazonaws.com/readme/AWS_S3_2.png)
3. Created S3 bucket named ms3recipebundle - [detailed steps](https://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-bucket.html)
![S3_landing](https://ci-ms4-blacksheepprint.s3.eu-central-1.amazonaws.com/readme/AWS_S3_1.png)
4. Imported Python library, [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html), as console to create, configure and manage AWS services.
5. Assigned s3 variables (bucket name, url, access and security keys) in util.py file.

## 1.4 Skeleton Plane

### 1.4.1 Navigation

- Page header navigates to Landing page, Admin page (Admin user only), Collection page and Sign Out page (if signed in), Sign In page and Register page (if not signed in).
- Sign In page navigates to Register page and Reset page.
- Sign Out page navigates to Register page.
- Page footer navigates to terms and conditions of usage.

### 1.4.2 Wireframes

| App | Page | Link |
| ---- | ---- | ---- |
| Home | Index | [view](https://ci-ms4-blacksheepprint.s3.eu-central-1.amazonaws.com/readme/index_v2.png) |
| Products | Overview | [view](https://ci-ms4-blacksheepprint.s3.eu-central-1.amazonaws.com/readme/products_v2.png) |
| Products | Detail | [view](https://ci-ms4-blacksheepprint.s3.eu-central-1.amazonaws.com/readme/products_detail_V1.png) |
| Designs | Overview | [view](https://ci-ms4-blacksheepprint.s3.eu-central-1.amazonaws.com/readme/design_V2.png) |
| Designs | Detail | [view](https://ci-ms4-blacksheepprint.s3.eu-central-1.amazonaws.com/readme/design_detail_V1.png) |
| Checkout | Checkout | [view](https://ci-ms4-blacksheepprint.s3.eu-central-1.amazonaws.com/readme/checkout_V1.png) |
| Checkout | Checkout Success | [view](https://ci-ms4-blacksheepprint.s3.eu-central-1.amazonaws.com/readme/checkout_success_V1.png) |
| Cart | Shopping Cart | [view](https://ci-ms4-blacksheepprint.s3.eu-central-1.amazonaws.com/readme/cart_V1.png) |
| Profiles | Profile | [view](https://ci-ms4-blacksheepprint.s3.eu-central-1.amazonaws.com/readme/profile_V1.png) |
| Profiles | Admin Overview | [view](https://ci-ms4-blacksheepprint.s3.eu-central-1.amazonaws.com/readme/admin_overview_V1.png) |

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
- [Python 3.10](https://www.python.org/)
- [Django](https://djangoproject.com/)

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

### - [Snipping Tool 11.2109.37.0](https://support.microsoft.com/en-us/windows/use-snipping-tool-to-capture-screenshots-00246869-1843-655f-f220-97299b865f6b)

- Used for screenshots during testing.

### - [Lunapic](https://www2.lunapic.com/editor/)

- Used to create products.

### - [colormind.io](http://colormind.io/image/)

- Used to generate colour palette for website.

### [dbdiagram](https://dbdiagram.io/)

- Used to generate database schematic.

### [TempMail](http://temp-mail.org/en/)

- Used temporary email for testing.

# 3. Features

## 3.1 Existing Features

- Responsive on all device sizes
- User authentication (Sign in, Sign out, Reset Password and Register)
- Interactive elements

## 3.2 Features Left to Implement

- Adding text to designs
- Being able to view order at different statuses
- Being able to access previous designs
- Being able to order from previous designs
- Contact form for special print jobs or to report bugs / issues

# 4. Testing

## [Click here to go to testing](TESTING.md)

# 5. APIs

- Fabric.js for t-shirt customisation
- DomToImage for exporting t-shirt canvas to png file
- Stripe for online payments management
- Google OAuth api

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
    os.environ.setdefault("SECRET_KEY", [user input])
    os.environ.setdefault("AWS_ACCESS_KEY_ID",  [user input])
    os.environ.setdefault("AWS_SECRET_ACCESS_KEY", [user_input])
    os.environ.setdefault("SECRET_KEY",  [user input])
    os.environ.setdefault("DATABASE_URL",  [user input])
    os.environ.setdefault("EMAIL_HOST_PASS",  [user input])
    os.environ.setdefault("EMAIL_HOST_USER",  [user input])
    os.environ.setdefault("STRIPE_PUBLIC_KEY",  [user input])
    os.environ.setdefault("STRIPE_SECRET_KEY",  [user input])
    os.environ.setdefault("STRIPE_WH_SECRET",  [user input])
    os.environ.setdefault("USE_AWS",  True)

- Install packages per requirements.txt file

- Run application in remote environment (PIPENV or VENV) with command python3 manage.py runserver

## 6.2 - Heroku

Heroku is a free hosting service for hosting small projects.

### Deploy to Heroku

- Create a Heroku account
- Install Python (3.10 at time of creation) locally.
- Install Heroku CLI (first install Git CLI if you don't already have it installed).
- Log in to Heroku from CLI.
- Prepare and clone app - clone Github Repository.
- Deploy with heroku create and git push heroku main.
- Create a Procfile, containing:
 web: gunicorn blacksheep.wsgi:application
- Declare app dependencies in requirements.txt (pip install -r requirements.txt)
- In Heroku > Resources > Add-ons: Heroku Postgres
- Get url for remote database: Heroku config
- In settings.py:
  Copy Databases and comment out (ctrl + /) first
  Replace {} with dj_database_url.parse(<postgres://…>)
  Import dj_database_url
- Python3 manage.py showmigrations, then python3 manage.py migrate
- Create new application with unique name.
- Navigate to Deploy, and connect to GitHub. Select repo, and then branch.
- Configure Config Vars - same parameters as in env.py file mentioned above.
- Deploy from dashboard.
- Open App.
- For more [details, visit here](https://devcenter.heroku.com/articles/getting-started-with-python)

### Deployed to AWS (Amazon Web Services)

1. Create an account on aws.amazon.com
2. In S3 application, create S3 bucket named 'blacksheepprint' (same as Heroku app name)
3. Make public by unchecking "Block all public access setting"
4. Adjust settings:
  4.1 Properties > Static website hosting > Use this bucket to host a website
  4.2 Permissions > CORS configuration > ![https://ci-ms4-blacksheepprint.s3.eu-central-1.amazonaws.com/readme/aws_cors_config.png]
  4.3 Permissions > Bucket policy editor > Policy generator >
  ![https://ci-ms4-blacksheepprint.s3.eu-central-1.amazonaws.com/readme/aws_cors_config.png]
  Paste into Bucket Policy
  4.4 Add "/*" to end of Resource details
  4.5 Change Actions to GetObjects
  4.6 Permissions > Access Control List > Everyone (public access) > List
5. Set up AWS IAM

For details on how to set up AWS S3, [see](https://docs.aws.amazon.com/AmazonS3/latest/userguide/GetStartedWithS3.html)

For details on who to set up AWS IAM, [see](https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-started.html)

# 7. Credits

## 7.1. Code

- Bootstrap 5.1: Bootstrap Library used to make the site responsive using the Bootstrap Grid System
- [Form autocomplete](https://www.chromium.org/developers/design-documents/form-styles-that-chromium-understands)
- [AWS file uploading](https://gist.github.com/leongjinqwen/9d9a2d58bf2fb923658820559a88a5ec)
- [Using FabricJS for t-shirt printing website](https://ourcodeworld.com/articles/read/1016/how-to-create-your-own-t-shirt-designer-using-fabricjs-in-javascript)
- [Setting up Google OAuth](https://devnote.in/how-to-set-up-google-authentication-with-django/)

## 7.2. Content

- Created favicon from logo using [favicon.cc](https://www.favicon.cc/)
- Address [coolgenerator](https://www.coolgenerator.com/nl-address-generator)
- Terms and conditions [policymaker.io](https://policymaker.io/)

## 7.3. Media

- [Font Awesome](http://fontawesome.com)
- [Google Fonts](https://fonts.google.com/)
- [Pexels](https://www.pexels.com/)
- [Testing and ReadMe example](https://github.com/pmeeny/CI-MS4-LoveRugby)
- [Placeholder image](https://www.freeiconspng.com/img/23499)
- [Templates and Products created with mockups from](https://www.pngegg.com/)

## 7.4. Other

- [Deploying to Postgres](https://dev.to/giftedstan/heroku-how-to-deploy-a-django-app-with-postgres-in-5-minutes-5lk)
- [Customising 404 page](https://levelup.gitconnected.com/django-customize-404-error-page-72c6b6277317)
- [Using Pipenv](https://docs.python-guide.org/dev/virtualenvs/)
- [Understanding AllAuth](https://learndjango.com/tutorials/django-allauth-tutorial)
- [Understanding AllAuth social apps](http://www.sarahhagstrom.com/2013/09/the-missing-django-allauth-tutorial/#Create_and_configure_a_Facebook_app)
- [Understanding X-Frame](https://docs.djangoproject.com/en/3.2/ref/clickjacking/#how-to-use-it)
- [Django cookies](https://stackoverflow.com/questions/1622793/django-cookies-how-can-i-set-them)

## 7.5. Acknowledgements

- My mentor for guidance and support.
- My partner for advice and patience.
- My brothers for their pep-talks and positivity.
- My mother for all her words of love and encouragement.
- My manager, for support and holding me accountable for my wellbeing.