# 4. Testing

- The website was tested on Google Chrome and Microsoft Edge.

- The website was viewed on a variety of devices, including:

| Name | Type | Browser | Version | Nature |
| --- | --- | --- | --- | --- |
| Xioami Mi 10T Lite | Mobile | Chrome | Chrome 96.0.4664.45 | Physical |
| iPhone 11s | Mobile | Chrome simulation | | Emulator |
| iPhone 5/SE | Mobile | Chrome simulation |  | Emulator |
| Galaxy Note 3 | Mobile | Chrome simulation | | Emulator |
| iPad | Tablet | Chrome simulation | | Emulator |
| Surface Duo | Tablet | Chrome simulation | | Emulator |
| Toshiba Satellite L850-F33V | Desktop | Chrome | Version 95.0.4638.69 (Official Build) (64-bit) | Physical |
| Dell Inspiron 15 5515 with 24" Dell monitor | Desktop | Chrome | Version 95.0.4638.69 (Official Build) (64-bit) | Physical |
| Dell Inspiron 15 5515 with 24" Dell monitor | Desktop | Firefox | 91.0.1 (64-bits)| Physical |
| Dell Inspiron 15 5515 with 24" Dell monitor | Desktop | Microsoft Edge | Version 95.0.1020.53 (Official build) (64-bit) | Physical |

- Friends and family were asked to review the site and documentation to point out bugs and /or user experience issues.

- [4. Testing](#4-testing)
  - [4.1 Manual testing](#41-manual-testing)
    - [4.1.1 HTML - W3C Markup Validator](#411-html---w3c-markup-validator)
    - [4.1.2 CSS - W3C CSS Validator](#412-css---w3c-css-validator)
    - [4.1.3 Accessibility - WAVE Web Accessibility Evaluation Tool](#413-accessibility---wave-web-accessibility-evaluation-tool)
    - [4.1.4 Performance - Chrome Lighthouse](#414-performance---chrome-lighthouse)
    - [4.1.5 JSHint](#415-jshint)
    - [4.1.6 User Experience testing](#416-user-experience-testing)
  - [4.2 Automated testing](#42-automated-testing)
    - [Tested page](#tested-page)
  - [4.3 Testing Bugs - Resolved](#43-testing-bugs---resolved)
  - [4.4 Known Bugs](#44-known-bugs)

## 4.1 Manual testing

The following tools were used to validate every page of project to ensure there were no syntax errors in the project:

### 4.1.1 HTML - W3C Markup Validator

- Pages tested:
  
| App | Page | Outcome | Link |
| --- | --- | --- | --- |
| Home | Index | No errors | [view](https://ci-ms4-blacksheepprint.s3.eu-central-1.amazonaws.com/readme/html_index.png) |
| Home | Terms | No errors | [view](https://ci-ms4-blacksheepprint.s3.eu-central-1.amazonaws.com/readme/html_terms.png) |
| Product | Overview | No errors | [view](https://ci-ms4-blacksheepprint.s3.eu-central-1.amazonaws.com/readme/html_products.png) |
| Products | Detail | No errors | [view](https://ci-ms4-blacksheepprint.s3.eu-central-1.amazonaws.com/readme/html_product_detail.png) |
| Products | Add | No errors | [view](https://ci-ms4-blacksheepprint.s3.eu-central-1.amazonaws.com/readme/html_add_product.png) |
| Products | Edit | No errors | [view](https://ci-ms4-blacksheepprint.s3.eu-central-1.amazonaws.com/readme/html_edit_product.png) |
| Designs | Overview | No errors | [view](https://ci-ms4-blacksheepprint.s3.eu-central-1.amazonaws.com/readme/html_designs.png) |
| Designs | Detail | No errors | [view](https://ci-ms4-blacksheepprint.s3.eu-central-1.amazonaws.com/readme/html_design_mockup.png) |
| Designs | Add | No errors | [view](https://ci-ms4-blacksheepprint.s3.eu-central-1.amazonaws.com/readme/html_add_mockup.png) |
| Designs | Edit | No errors | [view](https://ci-ms4-blacksheepprint.s3.eu-central-1.amazonaws.com/readme/html_edit_mockup.png) |
| Checkout | Checkout | No errors | [view](https://ci-ms4-blacksheepprint.s3.eu-central-1.amazonaws.com/readme/html_checkout.png) |
| Checkout | Checkout Success | No errors | [view](https://ci-ms4-blacksheepprint.s3.eu-central-1.amazonaws.com/readme/html_checkout_success.png) |
| Cart | Shopping Cart | No errors | [view](https://ci-ms4-blacksheepprint.s3.eu-central-1.amazonaws.com/readme/html_cart.png) |
| Profiles | Profile | No errors | [view](https://ci-ms4-blacksheepprint.s3.eu-central-1.amazonaws.com/readme/html_profile.png) |
| Profiles | Admin View | No errors | [view](https://ci-ms4-blacksheepprint.s3.eu-central-1.amazonaws.com/readme/html_admin.png) |

### 4.1.2 CSS - W3C CSS Validator

- All errors / warnings relate to Bootstrap template CSS.
- Summary of result:
- No errors or warnings from CSS style file unrelated to Bootstrap;
- Errors from Bootstrap 5.1 (unused / unrecognised errors); and
- Report can be found [here](https://ci-ms4-blacksheepprint.s3.eu-central-1.amazonaws.com/readme/css.png).
  
### 4.1.3 Accessibility - WAVE Web Accessibility Evaluation Tool

- Pages tested:
  
| App | Page | Result - Errors | Result - Warnings | Link |
| --- | --- | --- | --- | --- |
| Home | Index | No errors | No warnings | [view](https://ci-ms4-blacksheepprint.s3.eu-central-1.amazonaws.com/readme/wave_index.png) |
| Home | Terms | No errors | Missed heading level, redundant link (ref for attribution) | [view](https://ci-ms4-blacksheepprint.s3.eu-central-1.amazonaws.com/readme/wave_terms.png) |
| Product | Overview | No errors | Missed heading level warning, ignored for aesthetic | [view](https://ci-ms4-blacksheepprint.s3.eu-central-1.amazonaws.com/readme/wave_products.png) |
| Products | Detail | No errors | Missed heading level and redundant link for login  prompt (ignored) | [view](https://ci-ms4-blacksheepprint.s3.eu-central-1.amazonaws.com/readme/wave_product_detail.png) |
| Products | Add | Missing form label | Missing heading level and skipped heading level | [view](https://ci-ms4-blacksheepprint.s3.eu-central-1.amazonaws.com/readme/wave_add_product.png) |
| Products | Edit | No errors | Missed heading level and skipped heading level, redundant link to product details - ignored | [view](https://ci-ms4-blacksheepprint.s3.eu-central-1.amazonaws.com/readme/wave_edit_product.png) |
| Designs | Overview | No errors | [view](https://ci-ms4-blacksheepprint.s3.eu-central-1.amazonaws.com/readme/wave_designs.png) |
| Designs | Detail | No errors | Missed heading level and skipped heading level, redundant link to product details - ignored | [view](https://ci-ms4-blacksheepprint.s3.eu-central-1.amazonaws.com/readme/wave_design_mockup.png) |
| Designs | Add | Missing form label | Missing heading level and skipped heading level | [view](https://ci-ms4-blacksheepprint.s3.eu-central-1.amazonaws.com/readme/wave_add_mockup.png) |
| Designs | Edit | Missing form label | Missing heading level and skipped heading level | [view](https://ci-ms4-blacksheepprint.s3.eu-central-1.amazonaws.com/readme/wave_edit_mockup.png) |
| Checkout | Checkout | Missing form label, empty heading | Missed and skipped heading level | [view](https://ci-ms4-blacksheepprint.s3.eu-central-1.amazonaws.com/readme/wave_checkout.png) |
| Checkout | Checkout Success | No errors | Missing first level heading | [view](https://ci-ms4-blacksheepprint.s3.eu-central-1.amazonaws.com/readme/wave_checkout_success.png) |
| Cart | Shopping Cart | Missing form label, empty table header (ignored) | Missed and skipped heading level | [view](https://ci-ms4-blacksheepprint.s3.eu-central-1.amazonaws.com/readme/wave_cart.png) |
| Profiles | Profile | Missing form label - ignored (Django crispy forms) | missing label, missing first heading level | [view](https://ci-ms4-blacksheepprint.s3.eu-central-1.amazonaws.com/readme/wave_profile.png) |
| Profiles | Admin View | No errors | Missed heading level, redundant link (ignored, goes to different page) | [view](https://ci-ms4-blacksheepprint.s3.eu-central-1.amazonaws.com/readme/wave_admin.png) |

### 4.1.4 Performance - Chrome Lighthouse

- Pages tested (mobile and desktop tested on each):

| App | Page | Scores - Desktop | Scores - Mobile |
| --- | --- | --- |  --- |
| Home | Index | [view](https://ci-ms4-blacksheepprint.s3.eu-central-1.amazonaws.com/readme/lighthouse_desktop_index.png) | [view](https://ci-ms4-blacksheepprint.s3.eu-central-1.amazonaws.com/readme/lighthouse_mobile_index.png) |
| Home | Terms | [view](https://ci-ms4-blacksheepprint.s3.eu-central-1.amazonaws.com/readme/lighthouse_desktop_terms.png) | [view](https://ci-ms4-blacksheepprint.s3.eu-central-1.amazonaws.com/readme/lighthouse_mobile_terms.png) |
| Product | Overview | [view](https://ci-ms4-blacksheepprint.s3.eu-central-1.amazonaws.com/readme/lighthouse_desktop_products.png) | [view](https://ci-ms4-blacksheepprint.s3.eu-central-1.amazonaws.com/readme/lighthouse_mobile_products.png) |
| Products | Detail | [view](https://ci-ms4-blacksheepprint.s3.eu-central-1.amazonaws.com/readme/lighthouse_desktop_product_detail.png) | [view](https://ci-ms4-blacksheepprint.s3.eu-central-1.amazonaws.com/readme/lighthouse_mobile_product_detail.png) |
| Products | Add | [view](https://ci-ms4-blacksheepprint.s3.eu-central-1.amazonaws.com/readme/lighthouse_desktop_add_product.png) | [view](https://ci-ms4-blacksheepprint.s3.eu-central-1.amazonaws.com/readme/lighthouse_mobile_add_product.png) |
| Products | Edit | [view](https://ci-ms4-blacksheepprint.s3.eu-central-1.amazonaws.com/readme/lighthouse_desktop_edit_product.png) | [view](https://ci-ms4-blacksheepprint.s3.eu-central-1.amazonaws.com/readme/lighthouse_mobile_edit_product.png) |
| Designs | Overview | [view](https://ci-ms4-blacksheepprint.s3.eu-central-1.amazonaws.com/readme/lighthouse_desktop_designs.png) | [view](https://ci-ms4-blacksheepprint.s3.eu-central-1.amazonaws.com/readme/lighthouse_mobile_designs.png) |
| Designs | Detail | [view](https://ci-ms4-blacksheepprint.s3.eu-central-1.amazonaws.com/readme/lighthouse_desktop_design_mockup.png) | [view](https://ci-ms4-blacksheepprint.s3.eu-central-1.amazonaws.com/readme/lighthouse_mobile_design_mockup.png) |
| Designs | Add | [view](https://ci-ms4-blacksheepprint.s3.eu-central-1.amazonaws.com/readme/lighthouse_desktop_add_mockup.png) | [view](https://ci-ms4-blacksheepprint.s3.eu-central-1.amazonaws.com/readme/lighthouse_mobile_add_mockup.png) |
| Designs | Edit | [view](https://ci-ms4-blacksheepprint.s3.eu-central-1.amazonaws.com/readme/lighthouse_desktop_edit_mockup.png) | [view](https://ci-ms4-blacksheepprint.s3.eu-central-1.amazonaws.com/readme/lighthouse_mobile_edit_mockup.png) |
| Checkout | Checkout | [view](https://ci-ms4-blacksheepprint.s3.eu-central-1.amazonaws.com/readme/lighthouse_desktop_checkout.png) | [view](https://ci-ms4-blacksheepprint.s3.eu-central-1.amazonaws.com/readme/lighthouse_mobile_checkout.png) |
| Checkout | Checkout Success | [view](https://ci-ms4-blacksheepprint.s3.eu-central-1.amazonaws.com/readme/lighthouse_desktop_checkout_success.png) | [view](https://ci-ms4-blacksheepprint.s3.eu-central-1.amazonaws.com/readme/lighthouse_mobile_checkout_success.png) |
| Cart | Shopping Cart | [view](https://ci-ms4-blacksheepprint.s3.eu-central-1.amazonaws.com/readme/lighthouse_desktop_cart.png) | [view](https://ci-ms4-blacksheepprint.s3.eu-central-1.amazonaws.com/readme/lighthouse_mobile_cart.png) |
| Profiles | Profile | [view](https://ci-ms4-blacksheepprint.s3.eu-central-1.amazonaws.com/readme/lighthouse_desktop_profile.png) | [view](https://ci-ms4-blacksheepprint.s3.eu-central-1.amazonaws.com/readme/lighthouse_mobile_profile.png) |
| Profiles | Admin View | [view](https://ci-ms4-blacksheepprint.s3.eu-central-1.amazonaws.com/readme/lighthouse_desktop_admin.png) | [view](https://ci-ms4-blacksheepprint.s3.eu-central-1.amazonaws.com/readme/lighthouse_mobile_admin.png) |

### 4.1.5 JSHint

- Pages tested (mobile and desktop tested on each):

| App | Page | Results | Link |
| --- | --- | --- | --- |
| Products | products.js |No issues | [results](https://ci-ms4-blacksheepprint.s3.eu-central-1.amazonaws.com/testing/jshint_products.png) |
| Profiles | countryfield.js |No issues | [results](https://ci-ms4-blacksheepprint.s3.eu-central-1.amazonaws.com/testing/jshint_countryfield.png) |
| Designs | designs.js |No issues | [results](https://ci-ms4-blacksheepprint.s3.eu-central-1.amazonaws.com/testing/jshint_designs.png) |
| Checkout | stripe_elements.js |No issues | [results](https://ci-ms4-blacksheepprint.s3.eu-central-1.amazonaws.com/testing/jshint_stripe_elements.png) |
| Cart | cart.js |No issues | [results](https://ci-ms4-blacksheepprint.s3.eu-central-1.amazonaws.com/testing/jshint_cart.png) |

### 4.1.6 PEP8 testing

PyLint was installed and problems continuously monitored in terminal.

| Errors found: | Comments |
| --- | --- |
| Class ... has no 'objects' member | Related to database content, no further action required |
| Catching too general exception Exception | No action required, intention to catch errors |
| Unused Http404 imported from django.http | No action required, import for custom error pages |
| Missing module docstring | Ignored, docstrings included where relevant |

### 4.1.7User Experience testing  

#### User Story 1. As a Site Visitor, I want to easily navigate the website's pages from the header and footer <!-- omit in toc -->

1.1 Header with Navigation Bar

- Requirements considered:
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

- Tests

| Step | Expected Result | Devices | Test Result |
| --- | --- | --- | --- |
| Click on logo (navbrand) | Navigates to Home page | Desktop, Tablet, Mobile| All passed |
| Click on Products > View All | Navigates to Products page | Desktop, Tablet, Mobile| All passed |
| Click on Designs | Navigates to Designs page | Desktop, Tablet, Mobile| All passed |
| Click on Account > select Register | Navigates to Register page | Desktop, Tablet, Mobile| All passed |
| Click on Account > Login | Navigates to Login page | Desktop, Tablet, Mobile| All passed |
| Sign in as Admin, Click on Admin View | Navigates to Administration page, not visible to "general" users | Desktop, Tablet, Mobile| All passed |
| Sign in as User1 | No Administration page option to click | Desktop, Tablet, Mobile| All passed |
| Click on Collection | Navigates to recipe Collection page | Desktop, Tablet, Mobile| All passed |
| Click on Account > Sign Out | Signs out and redirects to home page | Desktop, Tablet, Mobile| All passed |

1.2 Footer with navigation links

- Requirements considered
  - Footer with icons, navigates to Twitter, FaceBook and Pinterest and terms and conditions.

- Tests
  | Step | Expected Result | Devices | Test Result |
  | --- | --- | --- | --- |
  | Click on Twitter icon | Opens new browser with Twitter landing page | Desktop, Tablet, Mobile| All passed |
  | Click on Pinterest icon | Opens new browser with Pinterest landing page | Desktop, Tablet, Mobile| All passed |
  | Click on FaceBook icon | Opens new browser with FaceBook landing page | Desktop, Tablet, Mobile| All passed |
  | Click on Terms | Opens on Terms page in same browser | Desktop, Tablet, Mobile | All passed |

1.3 Landing page

- Requirements considered
  - Visible when signed out or signed out.

- Tests
  | Step | Expected Result | Devices | Test Result |
  | --- | --- | --- | --- |
  | Sign in as Admin, Click on Home | Navigates to landing page | Desktop, Tablet, Mobile| All passed |
  | Sign in as User1 | Navigates to landing page | Desktop, Tablet, Mobile| All passed |

    [Results](https://ci-ms4-blacksheepprint.s3.eu-central-1.amazonaws.com/testing/user_story-1.png)

#### As a Site Visitor, I want to be able to browse through available products.<!-- omit in toc -->

- Requirements considered
  - Products page
    - Visible to all site visitors
    - Navigates to product detail, (superuser) edit and delete pages

- Tests
  | Step | Expected Result | Devices | Test Result |
  | --- | --- | --- | --- |
  | All Users (signed in / not), click on Products > View All page | See overview of all products with links to detailed pages | Desktop, Tablet, Mobile| All passed |
  | Signed in as Admin, click on Products > View All page | See buttons to Edit or Remove at the bottom of each product | Desktop, Tablet, Mobile| All passed |
  | Signed in as User1, click on Products > View All page | No buttons to Edit or Remove at the bottom of each product | Desktop, Tablet, Mobile| All passed |
  | All Users, click on a product to view details | See product image or placeholder image, price, description, add to cart, add between 1 and 99 items to cart from page | Desktop, Tablet, Mobile | All passed |
  | All Users, click on cart | See products added in cart with images or placeholder images, quantity and prices | Desktop, Tablet, Mobile | All passed |

    [Results](https://ci-ms4-blacksheepprint.s3.eu-central-1.amazonaws.com/testing/user_story-2.png)

#### User Story 3. As a Site Visitor, I want to be able to upload and move images for my designs. <!-- omit in toc -->

- Requirements considered
  - Design page
    - Visible to all site visitors
    - Navigates to design page, (superuser) edit and delete templates (mockups)
    - Upload of content only for registered for users
    - Template with a canvas area, where customisation occurs
    - Control panel for customising chosen apparel

- Tests
  | Step | Expected Result | Devices | Test Result |
  | --- | --- | --- | --- |
  | All Users (signed in / not), click on Design page | See overview of templates with links to customisation pages | Desktop, Tablet, Mobile| All passed |
  | Signed in as Admin, click on Design page | See buttons to Edit or Remove at the bottom of each template | Desktop, Tablet, Mobile| All passed |
  | Signed in as User1, click on Design page | No buttons to Edit or Remove at the bottom of each template | Desktop, Tablet, Mobile| All passed |
  | All users, click on template | See template, buttons to upload or change colour, price, add to cart, add between 1 and 99 items to cart from page | Desktop, Tablet, Mobile | All passed |
  | All Users, click on cart | See designs added in cart with images or placeholder images, quantity and prices | Desktop, Tablet, Mobile | Added product instead of design, to be resolved in future version |

 [Results](https://ci-ms4-blacksheepprint.s3.eu-central-1.amazonaws.com/testing/user_story-3.png)

#### User Story 4. As a Site Visitor, I want to be able to view my past orders. <!-- omit in toc -->

- Requirements considered
  - User profile page
    - Only available to signed in users
    - Shows order history, with option to reorder

- Tests
  | Step | Expected Result | Devices | Test Result |
  | --- | --- | --- | --- |
  | Signed in user, click on Account > User Profile | Display list of previous orders | Desktop, Tablet, Mobile| All passed |
  | Signed in user, on User Profile page > select a past order | See order details | Desktop, Tablet, Mobile| All passed |
  | User not signed in, attempt to navigate to User Profile URI | Error and redirect link to landing page | All passed |

  [Results](https://ci-ms4-blacksheepprint.s3.eu-central-1.amazonaws.com/testing/user_story-4.png)

#### User Story 5. As a Site Visitor, I want to be able to edit my contact details. <!-- omit in toc -->

- Requirements considered
  - User profile page
    - Only available to signed in users
    - Contains personal information (contact details), editable

- Tests
  | Step | Expected Result | Devices | Test Result |
  | --- | --- | --- | --- |
  | Signed in user, click on Account > User Profile | Display saved details | Desktop, Tablet, Mobile| All passed |
  | Signed in user, on User Profile page > edit details, click save | Changed details saved | Desktop, Tablet, Mobile| All passed |
  | User not signed in, attempt to navigate to User Profile URI | Error and redirect link to landing page | All passed |

[Results](https://ci-ms4-blacksheepprint.s3.eu-central-1.amazonaws.com/testing/user_story-5.png)

#### User Story 6.  As a Site Visitor, I want to be able to pay for my order securely. <!-- omit in toc -->

- Requirements considered
  - Checkout
    - Pay online with secure payment

- Tests
  | Step | Expected Result | Devices | Test Result |
  | --- | --- | --- | --- |
  | Any user, from cart page > click Secure Checkout | | Desktop, Tablet, Mobile| All passed |
  | Any user,  Using test card details (see Readme for details), click on Complete Order | Order summary, showing order details, error if incorrect card details used | Order summary doesn't show order details |

  [Results](https://ci-ms4-blacksheepprint.s3.eu-central-1.amazonaws.com/testing/user_story-6.png)

#### User Story 7.As a Site Visitor, I want to be able to add products to and edit contents of my shopping cart. <!-- omit in toc -->

- Requirements considered
  - Contact form with options to report bugs, make suggestions or other.

Tested as part of User Story 2 and User Story 3.

#### 8. As a Site Visitor, I want to be able to search through products. <!-- omit in toc -->

- Tests
  | Step | Expected Result | Devices | Test Result |
  | --- | --- | --- | --- |
  | Any user, from Products page > enter search term | | Desktop, Tablet, Mobile| Search initially worked, insufficient time to resolve |

#### 9. As a Site Visitor, I want to be able to filter products by category, price and name. <!-- omit in toc -->

- Tests
  | Step | Expected Result | Devices | Test Result |
  | --- | --- | --- | --- |
  | Any user, from Products page > selection all options from Filter to test | Filter by price ascending / descending, category etc. | Desktop, Tablet, Mobile| All passed |

## User Story 10. As the Site Owner, I want to restrict content uploads to registered users. <!-- omit in toc -->

- Requirements considered
  - Add, Edit or Remove cuisine type options
  - Add, Edit or Remove diet type options
  - Add, Edit or Remove meal type options

 | Step | Expected Result | Devices | Test Result |
  | --- | --- | --- | --- |
 | From Designs detail page | Login prompt if not signed in, else button to upload content | Desktop, Tablet, Mobile| All passed |

 [Results](https://ci-ms4-blacksheepprint.s3.eu-central-1.amazonaws.com/testing/user_story-10.png)

## User Story 11. As the Site Owner, I want to view a record of orders in various states. <!-- omit in toc -->

Currently limited to viewing, statuses in future version.

## User Story 12. As the Site Owner, I want to be able to easily add or edit design templates. <!-- omit in toc -->

Tested as part of User Story 3.

## User Story 13. As the Site Owner, I want to be able to easily add or edit products and details. <!-- omit in toc -->

Tested as part of User Story 2.
## 4.2 Automated testing

All tests performed manually.

## 4.3 Testing Bugs - Resolved

| Bug Found | Solution |
| --- | ---- |
| CSS not loading | env field added |

## 4.4 Known Bugs

- The website is not optimised for Internet Explorer. No additional work was performed to optimise the site for IE as (extended) support has ended for customers since January 2020 and no further development of IE is expected.
- Order success page does not show order details after successful completion, but does show it from profile > past orders view.
- Google authentication failure
- Adding designs to cart adds Product equivalent instead
- Product search not working
- Allauth pages not loading, defaults to standard
- Verification and emails not working
- Quantity buttons not working on cart
