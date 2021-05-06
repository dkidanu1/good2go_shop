# Good2Go

![Responsiveness](static/img/responsive.png)


The live website can be found [Good2Go](https://goodtogo1.herokuapp.com/).


# Contents
1. About the Site
2. Strategy Plane
    - User Stories 
3. Scope Plane
    - Features Planned
    - Features and Django Apps
    - Additional Functionality
4. Structure Plane
    - Database Design
5. Skeleton Plane
6. Surface Plane
7. Design
8. Technologies Used
9. Testing
10. Deployment
11. Credit

## About the Site: 

The Good2Go site has been designed in the scope of the Code Institute Full Stack Frameworks with Django Project to give users a seamless way to view, select, and order meals and produce at a discounted rate. All the items present on the site have been saved from disposal. The user will have limited access to the site without registering an account, but will have full view of the meal and produce items. The idea of the site is to make all the content relevant to sustainability, easy accessibility and great experience. 

## Strategy Plane

The GoodtoGo site is an ecommerce platform created to showcase knowledge gained throughout the Full Stack course. The project aims to provide an exciting user experience for those interested in ordering meals that have been rescued. Users can successfully purchase items, and have them delivered to their home. For more user interaction a blog was created and a review section was added. Users are encouraged to reach out to GoodtoGo through a contact form. The site was inspired by the UK company Too Good Too Go.

User Stories: 

As an e-commerce site owner I would like to …
- Have access to site super user and admin to view and maintain site 
- View products, transaction, reviews and identify any inconsistencies 
- Add products and new items to my store
- Edit/ Delete products in my store
- Accept and/or reject reviews from customers
- Add/ Edit/ Delete Blog posts 

As a shopper I would like to …
- View products in distinct categories
- View product details of the products selected 
- Easily add products/ items to my bag
- View products in bad and the total easily
- Register for a site account 
- Receive a confirmation email after registering 
- Easily log in and logout
- View my personalised user account
- Sort through available products by category, price etc…
- Search for product by name 
- Easily select the portion size and quantity of a product when purchasing 
- Simply add payment information safely and securely 
- View an order confirmation after checkout
- Receive an email confirmation after checking out 

## Scope Plane 
In designing GoodtoGo, the idea was for the user to have a positive and easy experience through a simple and usable web-site. The user is able to navigate through the navigation bar that is always visible and by links in the footer. They can go from any part of the web-site to any other part. Simple to navigate and intuitive.

### Features Planned

The GoodtoGo site was developed with dynamic products including appropriate restrictions. Features like create, read, update, and delete, are available for admins and shop users, which users are able to edit reviews made once they sign up.

-	Responsive Design – site should function on mobile, tablet and desktop/laptop devices
-	Navigation across all pages
-	Clearly display information on website which is supplemented by entering the About Us page.
-	A standard e-commerce feed for products with the option to search, sort products and filter them by category name.
-	Every product can be added to the cart immediately and links to a product detail page where the user can read more about it.
-	About Us page informs the user of information about the company owners and informational blogs for their education.
-	Blog page containing blog posts all bout sustainability and the process of saving meals.
-	Contact information and form to easily contact the store.
-	Options for the customers to leave a review on a product.
- Footer Section

### Features and Django Apps

GoodtoGo is a Django project that consists of 8 Django applications, they are all listed below. As explained in Django's documentation - a Django application describes a Python package that provides some set of features. Applications may be reused in various projects.
* `about`
* `bag`
* `blog`
* `checkout`
* `contact`
* `home`
* `products`
* `profiles`
* `reviews`

### Additional functionality:
-	Search functionality: Search box at the top of the nav bar which is accessible across all pages on mobile this is found in the collapsible under the search symbol
-	Toasts: Small snippet messages for success, info, warning and error.
-	Django- all auth: Python package addressing authentication of user, it allows for features such as signup logout and password change. 

## Structure Plane

The website will have a few pages accessible to a non-registered user and additional 2 pages that will be accessible only after registration. There are a total of 5 page to navigate to and an additional shopping bag and my account section for users registered:

-	Home: Provides a simple landing page for users to get the look and feel of Good2Go before navigating to other pages.
-	About us: Provides the user with information about Good2Go and context for their use of the site. Additionally, the Good2Go blog is accessible on the about us page. 
-	Products: User can view all products available for order and sort through them through specific filters.
-	Meals: User can search through available meals on the site for ordering. 
-	Fresh Produce: User can search through available fresh produce on the site for ordering.
-	Contact us: User can see location and address of GoodtoGo additionally they can contact the company through a contact form.  
-	My Account: User can view profile, log in and out or manage products if they are an admin. 
-	Shopping bag: User can view items in shopping bag, checkout and pay for their items as well as input address for delivery. 

The pages consist of different sections unique to their functionality. A navigation bar which will be adapted accordingly for the mobile version, will be static on the top of the website. This will allow the user to move to any other section easily without scrolling or searching for the navigation. 

### Database Design

#### Profiles App

| Name | Database Key | Field Type | Type Validation |
| :-------------: |:----------------:| :--------------: | :---------: |
|User | user |	OneToOneField 'User'| on_delete=models.CASCADE
|Default Phone Number |	default_phone_number | CharField | max_length=20, null=True, blank=True
|Default Country | default_country | CountryField | blank_label='country', null=True, blank=True
|Default Postcode | default_postcode | CharField | max_length=20, null=True, blank=True
|Default Town or City | default_town_or_city | CharField | max_length=40, null=True, blank=True
|Default Street Address1 | default_street_address1 | CharField | max_length=80, null=True, blank=True
|Default Street Address2 | default_street_address2 | CharField | max_length=80, null=True, blank=True

#### Products App

`Category` model

| Name | Database Key | Field Type | Type Validation |
| :-------------: |:----------------:| :--------------: | :---------: |
|Name | name | CharField | max_length=254
|Friendly Name | friendly_name | CharField | max_length=254, null=True, blank=True

`Product` model

| Name | Database Key | Validation | Field Type|
| :-------------: |:----------------:| :--------------: | :---------: |
|Product id | id | primary_key=True | AutoField
|Name | name | default='', max_length=254 | CharField
|SKU | sku | max_length=254, null=True, blank=True | CharField
|Description | content | blank=False | TextField
|Price | price | max_digits=6, decimal_places=2 | DecimalField
|Image| image| blank=False | ImageField
|Rating | rating | blank=True | DecimalField

#### Review

| Name | Database Key | Validation | Field Type|
| :-------------: |:----------------:| :--------------: | :---------: |
|User | user | on_delete=models.CASCADE | ForeignKey
|Product| product | Product, related_name="review" | ForeignKey
|Title | title | max_length=50 | CharField
|Description| description | description | TextField
|Rating | rating | choices=RATE | IntegerField
|Upvotes | upvotes | default=0 | IntegerField
|Downvotes| downvotes | default=0 | IntegerField
|date_posted | date_posted | auto_now_add=True| DateTimeField


## Skeleton Plane 
The Goodtogo website will have a consistent colour pallet consisting of greys and maroons., this will include consistent typography, sizing, colour and look/feel.



## Testing
### Validating Code
- HTML code is validated through W3 validator.
- CSS code is validated through W3 Jigsaw.
- JavaScript code is validated through JS Hint.
- Python code is validated through PEP8.
- Flake8
A number of issues were identified and rectified utilizing Flake8, it was also chosen to not address a number of identified issues as they were not detrimental to the project as a whole. 


### Navigation

| Functionality | Expected Outcome | Actual Outcome | Pass/Fail |
| :-------------: |:----------------:| :--------------: | :---------: |
| Clicking on G2G Logo  | Opens "About Us" page | As Expected | Pass |
| Clicking on `Product` link | Opens dropdown tab with links | As expected | Pass |
| Clicking on `Meals and Fresh Produce` link | Opens dropdown tab with links | As expected | Pass |
| Clicking on `My Account` link | Opens dropdown tab with links for Log In | As expected | Pass |
| Clicking on `Register` link | Opens Register page | As expected | Pass |
| Clicking on `my account` link | Opens dropdown tab with links | As expected | Pass |
| Clicking on `log Out` link | Logs out user and redirects to log in page | As expected | Pass |

### Footer

| Functionality | Expected Outcome | Actual Outcome | Pass/Fail |
| :-------------: |:----------------:| :--------------: | :---------: |
| Clicking on `Facebook` icon | Opens Facebook website in new tab | As expected | Pass |
| Clicking on `Instagram` icon | Opens Instagram website in new tab | As expected | Pass |
| Clicking on `Twitter` icon | Opens Twitter website in new tab | As expected | Pass |
| Clicking on nav menu links | Opens the appropriate web page | As expected | Pass |

## About us

| Functionality | Expected Outcome | Actual Outcome | Pass/Fail |
| :-------------: |:----------------:| :--------------: | :---------: |
| Clicking on `Read more` blog button | Opens the full blog post on new page | As expected | Pass |

## Product

| Functionality | Expected Outcome | Actual Outcome | Pass/Fail |
| :-------------: |:----------------:| :--------------: | :---------: |
| Clicking on product cards | Opens the selected product detail | As expected | Pass |
| Clicking on `Add to Bag` button | Opens the products page | As expected | Pass |
| Clicking on `Email` icon | Opens email modal to contact site owner | As expected | Pass |
| Clicking on filter button | Show products under that category | As Expected | Pass
| Clicking on product | Show product details info on a new page | As Expected | Pass
| Selecting the number in input and clicking "Add" | Adds the selected quantity of the item to cart and then opens "View Bag" page |As Expected | Pass

### Reviews

| Functionality | Expected Outcome | Actual Outcome | Pass/Fail |
| :-------------: |:----------------:| :--------------: | :---------: |
| Clicking on `Submit` button without filling all the forms | Displays Validation to tell the user to enter all the forms | As Expected | Pass |
| After clicking on `Add` button | User is redirected to "Products" page with their review now sucessfully showing | As Expected | Pass |
| Clicking on `Edit` symbol | User is redirected to "Edit your review" modal with previous information showing | As Expected | Pass |
| Clicking on `Delete` symbol | user is directed to modal to delete their review | As Expected | Pass |

### Registration

| Functionality | Expected Outcome | Actual Outcome | Pass/Fail |
| :-------------: |:----------------:| :--------------: | :---------: |
| Clicking on Register button | Registers the user and redirects to confirm email address. If registration form is incomplete, shows Please fill out this field | As Expected | Pass

### Sign in

| Functionality | Expected Outcome | Actual Outcome | Pass/Fail |
| :-------------: |:----------------:| :--------------: | :---------: |
| Clicking on `Log In` with correct username and password | Directs user to the index page | As Expected | Fail |
| Clicking on `Log In` with Incorrect username and password | flash message to user showing incorrect username or password | As Expected | Pass |
| Clicking on Forgot password | Opens "Forgot password" page | As Expected | Pass

### Log Out

| Functionality | Expected Outcome | Actual Outcome | Pass/Fail |
| :-------------: |:----------------:| :--------------: | :---------: |
| clicking on `Shop` button | Shows "Shop" page | As Expected | Pass
| Clicking on `log Out` button | Logs out user and redirects to index page | As expected | Pass |

### Checkout

| Functionality | Expected Outcome | Actual Outcome | Pass/Fail |
| :-------------: |:----------------:| :--------------: | :---------: |
| clicking on `bag` button | Shows "bag" page | As Expected | Pass
| Clicking on `- or +` buttons | Adds or Decreases quantity of items | As expected | Pass |
| Clicking on `Remove or Update` buttons | changes the shopping bag accordingly | As expected | Pass |

