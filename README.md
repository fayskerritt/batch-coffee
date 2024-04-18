# **BATCH COFFEE**
## Milestone Project 4: Full Stack Frameworks with Django - Code Institute
## By Fay Skerritt

Batch Coffee is an online coffee retailer offering single origin coffee from all over the world. Batch Coffee comes in four different grind categories and three different varieties to cater for all coffee lovers.

To test the site you will need the below test credit card numbers from the [Stripe Docs](https://stripe.com/docs/testing): 

Number: 4242 4242 4242 4242
Exp. Date: Anything (e.g. 02/24)
CVC: Anything (e.g. 007)

Visit the deployed site: puffins

# Deployed Site
Live demo can no longer be viewed as Heroku is no longer free - [old url](https://pad-plants.herokuapp.com/)


# UX
## Project Goals
The main goal of this project was to create a fully functional web store that sells single origin coffee to coffee lovers.
The web store must allow users to browse products, save any they like the look of, purchase them using a credit card and review their personal information including past order summaries.

## User Stories
### Viewing, Sorting and Searching

* As a shopper, I want to view all products so I can see what is available to purchase on the site
* As a shopper, I want to view details about a specific product so I can see the price, details and description of the product
* As a shopper, I want to view products in categories so I can see the range of products available
* As a shopper, I want to sort products by category so I can view the specific category I am interested in 
* As a shopper, I want to sort products by price so I can find the best prices
* As a shopper, I want to sort products by more than one category at the same time so I can view the prices of the categories I am interested in 
* As a shopper, I want to search for product by name or description so I can find a specific product I would like to purchase
* As a shopper, I want to see the search terms I used and how many results my search got so I can see whether the product I am interested in is available

### User Admin
* As a site user, I want to register for an account so I can be able to view my personal account
* As a site user, I want to login and logout of my account so I can access my account and information
* As a site user, I want to recover my password if I forget it so I can get back into my account if I have forgotten my password
* As a site user, I want to receive an email confirmation after registering so I can verify that my account registration was successful
* As a site user, I want to have access to a personalised user profile so I can view my order history, order confirmations and save my delivery and payment information

### Buying
* As a shopper, I want to choose the quantity of a product when purchasing so I can add more than one item to my bag at a time
* As a shopper, I want to view all items in my bag that I have added so I can see the total cost of the items I will receive
* As a shopper, I want to change the quantity of products in my bag so I can make changes to my bag before checkout
* As a shopper, I want to enter my personal details and payment details so I can quickly and easily checkout
* As a shopper, I want to feel that my personal information is secure so I can provide the required information confidently
* As a shopper, I want to see my order details confirming my order has been placed so I can make sure all information is correct
* As a shopper, I want to receive an order confirmation email once my order has been placed so I can keep the confirmation email for my records

### Store Admin
* As a store owner, I want to add a product so I can add new items to my online store
* As a store owner, I want to edit or update a product so I can change the price or details of any product to keep them up to date
* As a store owner, I want to delete a product so I can remove items from my online store I no longer sell

## Design
### **Colour Scheme**
* Dark green was chosen as a secondary colour as it is a natural colour that compliments white text on top of it.
* Below is a branding Cascading_Style_Sheets

![Branding](media/readmemedia/branding.png)

### **Typography**
* Spartan was chosen for the font on the site with a lot of uppercase text which looks nice and linear.

### **Imagery**
* The home page features two artistic images of coffee, which capture the eye and go well with the coffee theme.
* Font Awesome icons are used in areas to clearly label input fields, sections and headers.
* Each item has a item image which was created by myself adding Batch Coffee branding to an empty bag.

### **Wireframes**
**Laptop:**

* The laptop wireframes are very similar to the displayed site with container used to leave spaces near the outer edges of the screen on larger screens. 
* The only real difference is the profile page which I incorporated a side menu into to navigate the three account pages.
* 
![Laptop Wireframe](media/readmemedia/laptop1.png)
![Laptop Wireframe](media/readmemedia/laptop2.png)
![Laptop Wireframe](media/readmemedia/laptop3.png)
![Laptop Wireframe](media/readmemedia/laptop4.png)

**Ipad:**

* Certain pages went from two columns to one on the smaller screen to ensure everything is easily visible.
* It was decided against using imagery on all pages as the images became very large to still look good on wide screens.
![Laptop Wireframe](media/readmemedia/ipad1.png)
![Laptop Wireframe](media/readmemedia/ipad2.png)
![Laptop Wireframe](media/readmemedia/ipad3.png)

**Mobile:**

* Almost everything on mobile is 1 column minus the item card in the bag.
* The navbar and footer differ slightly in the deployed site to the wireframes due to ensuring it was responsive across all screen sizes.
![Laptop Wireframe](media/readmemedia/mobile1.png)
![Laptop Wireframe](media/readmemedia/mobile2.png)


### Database Structure
During the development of Batch Coffee the built-in SQLite3 database was used. Once deployed to Heroku the database was transferred over to a postgressql database which is used in the deployed site.
User authentication and permissions were managed by Django's authentication system as well as [Allauth](https://django-allauth.readthedocs.io/en/latest/overview.html) from Django which was installed.

The database below shows the links between all the tables 

![Laptop Wireframe](media/readmemedia/dbschema.png)

# Features
### Existing Features
#### Navbar
* Shop dropdown offers range of sortation methods to sort coffee
* Searchbar displayed in navbar for ease of use. Collapses down into an icon on mobile where the search box drops down when clicked.
* Fixed to top of screen for good accessibility
* Bag icon with number of items rendered next to it to show how many items in the shopping Bag
* Heart icon which takes user to their saved items

#### Home Page
* Big logo to show branding
* Use of images that help to explain what the site sells
Buttons that take the user straight to browse products or to the about page

#### Footer
* Fixed to bottom so never floating in the middle of the screens
* Links to social media

#### About Page
* Explanation of what Batch Coffee sell
* Extra information about products and service provided

#### Shop
* Sort bar to sort all products by Price, Strength, Grind Category and Name - both ascending and descending
* Breadcrumb to show what products you are currently viewing and if you are viewing all the Varieties as buttons to allow the user to view only one
* Display of how many items are being shown on screens
* List of products with basic info in card body, on hover the rest of the product info slides over image with description
* Each product has it's Category as a link so user can see all of that category if they wish
* Each product has a heart icon which allows the user to add it to their saved items list

#### Product Page
* Product displayed showing all relevant information with a nice sized image
* Breadcrumb also on product page to show the product name
* Quantity drop down for user to choose qty if they wish to purchase
* Button to add product to bag which will take the quantity selected
* Another button with a link back to shop
* Save icon on product page also for user to add to their saved items
* Comments section at the bottom of each product page for users who are signed in to leave a comment about the product
* Users are able to delete their own comments

#### Shopping bag
* Table format shopping bag clearly labelled
* Quantity selector allows user to adjust quantity of items in Bag
* When quantity selector is changed javascript shows two buttons, one to submit the update of quantity or the other to cancel, revert the quantity back to the original quantity and hide the buttons using javascript again
* Table showing current totals of shopping bag with sub-total, discount if user has spent over threshold, delivery and grand total.
* Discount with message is shown if bag sub-total is above discount threshold
* Message telling user how much more they need to spend to get the discount if the sub-total is below threshold
* One button to take user back to shop and one to proceed to checkout

#### Checkout
* Summary of items in bag
* Form with placeholders to show personal details, delivery information and payment information needed from user
* Autofill of user details if they have them saved in their account
* Checkbox to give users who are logged in the otion to save their details to their account
* Stripe payment input that responds quickly to invalid card details
* Button to submit form labelled Pay Now
* Confirmed amount that will be charged to card just above pay button
* Button to go back to bag if user has changed their mind

#### Successful Checkout
* Message to let user know they have been sent an order confirmation to their email address
* Summary of their order details including the address it is being sent to and the estimated delivery date
* Sum of total number of items on the order with brief grid of items
* Side menu that gives user other account related options or to go back to shop

#### Login and Regsiter pages
* Users can register for an account, they will need an email which will require an email confirmation, a username and a password that they will need to confirm to ensure they match
* Password reset available if needed

#### My Account
* User can view their saved delivery details and update them if required
* User can view order history with the status of the order 
* User can view their saved items which they can then choose to remove from saved list by clicking the heart icon again

#### Store Admin
* Site owners are able to add products using a form with a dropdown for category and variety, seletors for strength and price and an image field
* Site owners are able to edit any product from the product page, during editing the image will be shown as a thumbnail for better visibility
* Site owners are able to delete any product from the product pages
* Site ownsers are able to log in to the django admin and can create, edit and delete products, users, comments, saved lists and items from the database


### Defensive Programming
* Links to user account and saved items hidden if user not logged in, only links to login or register.
* Save icon on products is greyed out if user not logged in and if hovered a tooltip will tell them to login to save and if they do click they will be redirected to the login page
* Messages will display in toasts to notify user of an issue or success of an action.
* Holding text if no items to ensure user knows it is not just an empty space
* Comment form not visible if user is not logged includes
* Loading spinner and overlay are shown once checkout form has been submitted, to ensure no information can be changed or the form resubmitted
* Comment delete button only visible to user who created it
* Edit and delete buttons on the product pages are only visible to superuser when logged includes
* Django decorator used to ensure users who are not superusers are unable to add, edit or delete products from the site


### Features to Implement in the Future
* Pagination on the shop page as the database grows, this will need to be specially added as to work with the filter and sorting functionality that currently exists
* Currently in the shopping bag the quantity field can only show up to 10 units due to the dropdown only going up to 10, there is an error message that notifies users of this but in future it will be impossible for the user to add more than 10 items to the shopping bag for stock reasons
* In the future an in/out of stock field will be added to the Product model so that products can be on the database but unable for purchase. Due to the nature of the product not having an extensive shelf-life this will be good for store staff to monitor sales
* 

# Technologies Used
### Databases
- [Sqlite3](https://www.sqlite.org/index.html)
- [postgresSQL](https://www.postgresql.org/)

### Coding Languages
- [CSS](https://www.w3.org/Style/CSS/)
- [HTML](https://html.spec.whatwg.org/multipage/)
- [Javascript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
- [Python](https://www.python.org/)

### Frameworks
- [Bootstrap](https://www.bootstrapcdn.com/)
- [Django](https://www.djangoproject.com/)
- [jQuery](https://jquery.com/)
### Libraries and Tools 
- [Figma](https://www.figma.com/)
- [Google Fonts](https://fonts.google.com/)
- [Font Awesome](https://fontawesome.com/)
- [Dj-Database-URL](https://pypi.org/project/dj-database-url/)
- [Django-Countries](https://pypi.org/project/django-countries/)
- [Django-Heroku](https://pypi.org/project/django-heroku/)
- [Django-Storages](https://django-storages.readthedocs.io/en/latest/)
- [Git](https://git-scm.com/)
- [GitHub](https://github.com/)
- [Gitpod](https://www.gitpod.io/)
- [Gunicorn](https://pypi.org/project/gunicorn/)
- [Pillow](https://pillow.readthedocs.io/en/stable/)
- [PIP](https://pip.pypa.io/en/stable/installing/)
- [Psycopg2](https://pypi.org/project/psycopg2/)
- [Stripe](https://stripe.com/gb)
- [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)
- [W3C – HTML Validation](https://validator.w3.org/)
- [W3C – CSS Validation](https://jigsaw.w3.org/css-validator/)
- [JS Hint](https://jshint.com/)
- [PEP8](http://pep8online.com/)

### Hosting
- [Heroku](https://www.heroku.com/)
- [AWS S3 Bucket](https://aws.amazon.com/)

# Testing
### Code Validation
* [W3C – HTML Validation](https://validator.w3.org/) - No errors found using url
* [W3C – CSS Validation](https://jigsaw.w3.org/css-validator/) - No errors found in custom css
* [JSHint](https://jshint.com/) - No issues found in javascript files
* [PEP8](http://pep8online.com) - No issues found in python files

### Testing User Stories

### Viewing, Sorting and Searching
* As a shopper, I want to view all products so I can see what is available to purchase on the site
    * Many ways to view all items, primarily from dropdown navbar there is a link to 'All Coffee'
    * Whilst on shop page breadcrumb always displays link to SHOP which displays all coffee
    * On the home and about pages there is a button to browse all coffee
* As a shopper, I want to view details about a specific product so I can see the price, details and description of the product
    * Product detail page displays all information about a product
    * From the shop page the user can click anywhere on the product image or name to get to the product detail page
    * A hover slide down feature on the shop page gives the user more information about the coffee for ease of use
* As a shopper, I want to view products in categories so I can see the range of products available
    * In the navbar the user has category dropdowns which enables them to view each grind category by variety and all of each grind category
    * In the shop menu the breadcrumb gives the user options to view all of either variety or category
* As a shopper, I want to sort products by category so I can view the specific category I am interested in
    * Again in the drop down shop nav there are options to sort by category and variety
    * The sort dropdown then gives the user the option to further sort each category
* As a shopper, I want to sort products by price so I can find the best prices
    * In the shop nav there is an option to view all coffee bt price which displays the coffees in ascending order
    * In the shop page the sort drop down allows the user to sort their current view by price either ascending or descending
* As a shopper, I want to sort products by more than one category at the same time so I can view the prices of the categories I am 
interested in 
    * If the user has searched for a category or variety from the shop nav these are then able to be further sorted by the sort dropdown
* As a shopper, I want to search for product by name or description so I can find a specific product I would like to purchase
    * The search bar in the navbar queries all coffee and will search within the name, description, category and variety field to ensure the search is successful
    * If no products found a message will be shown to the user
* As a shopper, I want to see the search terms I used and how many results my search got so I can see whether the product I am interested in is available
    * The search query of the user's search will be displayed with the number of items found at the top of the shop page

### User Admin
* As a site user, I want to register for an account so I can be able to view my personal account
    * If not already logged in the user will be able to navigate from the navbar user dropdown icon to the registration form
    * They will require an email, username and password to register and will receive an email from which they need to confirm their email address
* As a site user, I want to login and logout of my account so I can access my account and information
    * If user is logged in there will be a dropdown option in the user icon for them to logout with a confirm button that will show asking if they are sure they want to logout
    * If not already logged in the user will find the login dropdown from the user icon in the navbar where they will be required to enter either their username or email address and password to login
    * login_required decorator from django also used in places where actions require the user to be logged in which will redirect the user to the login page
* As a site user, I want to recover my password if I forget it so I can get back into my account if I have forgotten my password
    On the login page a 'forgotten password' link is present for the user to reset their password
* As a site user, I want to receive an email confirmation after registering so I can verify that my account registration was successful
    * An email from batchcoffee1@gmail.com will be received by the user with a link to confirm their email address on the site
* As a site user, I want to have access to a personalised user profile so I can view my order history, order confirmations and save my delivery and payment information
    * The user can navigate to their personalised account from the user dropdown in the menu once logged in
    * Their account page has a custom side menu with all account related options as well as a back to shop link
    * The user can view a form of their delivery details if they chose to save them when making a purchase or alternatively an empty form which they can fill in to save their details
    * The user can also view their order history which is displayed in a list newest at the top. Each order shows the order number, date email and expected delivery date with a progress bar showing where their order should be at that current time. The order number is also a link to take them to their full order Summary
    * Finally the user can navigate to their saved items page which displays all items they have added using the heart icon. They are able to remove any items from this list by clicking the heart icon again. They are also able to go to the product page if they decide to ourchase the item

### Buying
* As a shopper, I want to choose the quantity of a product when purchasing so I can add more than one item to my bag at a time
    * The quantity dropdown in the product detail page allows users to choose how many items they wish to add to their bag
* As a shopper, I want to view all items in my bag that I have added so I can see the total cost of the items I will receive
    * The bag icon in the navbar shows the total number of units in the shopping bag currently for the user to easily see how many items they have currently
    * If clicked the bag opens with each product on its own line stating the quantity of each
    * The shopping bag also has a total table which displays a sub-total of the products in the bag, this is the quantity of items * the item price. 
    * The sub-total also takes into consideration any discount applied if the user spends over the threshold, if so the discounted amount is shown also with a message letting the user know (or a message to tell them how far they are from the threshold)
    * The delivery price is also stated in the shopping bag
    * Finally a grand total with all the above considered
* As a shopper, I want to change the quantity of products in my bag so I can make changes to my bag before checkout
    * Each product in the shopping bag has its own quantity drop down which is editable
    * If the user changes the amount a button will appear to update the bag total
    * Also a cancel button will appear if the user decides they do not want to change the quantity and reverts the quantity back to its original value
    * A message will be displayed to let the user know the change of quantity
* As a shopper, I want to enter my personal details and payment details so I can quickly and easily checkout
    * At checkout the user must enter their personal details as well as delivery details and payment details to complete their order
    * The delivery details will be autofilled if the user is logged in and has saved their details in their account
    * A stripe input allows the user to input their credit card details that is quickly responsive if the card details are incorrect and will show the error to the user
* As a shopper, I want to feel that my personal information is secure so I can provide the required information confidently
* As a shopper, I want to see my order details confirming my order has been placed so I can make sure all information is correct
    * If the order is successful the user will be redirected to their order summary page
    * This page displays a message telling the user of the confirmation that has been sent stating the email address it has been sent to
    * The order number, date and estimated delivery date is also displayed with icons to make each field clear
    * The amount of items is shown with a brief overview of each item on the order including the quantity
    * A table shows the payment details including the delivery cost any duscount and the total spent.
* As a shopper, I want to receive an order confirmation email once my order has been placed so I can keep the confirmation email for my records
    * An email from batchcoffee1@gmail.com will be received by the user with a brief summary of their order, including delivery details and payment details

### Store Admin
* As a store owner, I want to add a product so I can add new items to my online store
    * If user is logged in with an admin/superuser login they will see the store admin dropdown in the user icon in the navbar
    * This link will take them to the add product page whuch displays a form requiring all the fields from the Product table highlighting whether each field is required
    * The form also has an option to upload an image file which will clearly show which file the user has to upload
* As a store owner, I want to edit or update a product so I can change the price or details of any product to keep them up to date
    * Again if logged in as an an admin/superuser two buttons will appear on every product detail page
    * The edit button that appears will take the user to an autofilled form showing the information of the product in it's current state with the options to change all fields and image
* As a store owner, I want to delete a product so I can remove items from my online store I no longer sell
    * If logged in as an admin/superuser the other of the two buttons that will appear on every product page is a delete button, this will delete the product from the database and site completely

### Manual Testing
#### Functionality
Navbar:
* All navbar links tested on every page and all work as they should.
* Nav Shop drodown tested to ensure javascript shows and hides information correctly.
* All nav dropdowns were tested to ensure each link displayed the correct information, this was checked against the display message that stated the categories and varieties and number of products showing.
* User dropdown tested to ensure it only displayed the login and register links to users who were not already logged in.
* Once logged in the user dropdown was tested to ensure it showed the my account and logout links.
* If logged in as a superuser, the user dropdown was tested to ensure it displayed the store admin option.
* If not logged in it was tested to ensure the my account and store admin links were not visible
* The shopping bag icon was tested to ensure it took the user to the bag and also tested to ensure the number next to it displayed the correct number relative to what was in the shopping bag.
* The saved items icon was tested to ensure it was only displayed to users who were logged in anf if logged in tested to ensure it took user to their saved items page.
* Search bar thouroughly tested with a combination of valid and invalid inputs to ensure working correctly and messages reflected isues.

Home page:
* Both internal links are clearly labelled and work correctly when clicked, these have both been tested.
* Both external links are clearly labelled, work correctly and open in a new tab, the two social media links have been tested in footer.

Shop:
* All nav dropdown options were testing with extra sorting from the sort dropdown on the shop page to ensure no mater what was being displayed it was always correctly sorted.
* All queries that displayed no products were checked to ensure a message let the user know this and was not just a blank page.
* Breadcrumb Shop link tested to ensure it always took user to all products.
* Breadcrumb category links tested to ensure always displayed all products of that category.
* Breadcrumb variety links tested to ensure always displayed all products of that variety.
* Sort dropdown tested for each value ascending and descending to ensure products were sorted correctly.
* All products render clearly with image and information that was checked against the database.
* Product cards were tested on all screen sizes and broswrs to ensure they are clear and are the correct size and position.
* Product card slide down overlay tested to ensure always displayed correct information and scroll was available if decription too long to fit inside card.
* Product category links on each product card tested to ensure took user to correct category.
* Saved buttons tested to ensure redirected user to login if not logged in.
* Saved button tested to ensure that if the item was not already on the users saved items list the heart logo was black and not solid and if clicked turned solid red and added the item to the user's saved item list. This was then checked in the database to ensure happened correctly.
* Saved button tested to ensure that if the item was already on the user's saved items list then it was displayed as solid and red and if clicked it turned black and not solid and was removed from the user's saved items list.

Product Page:
* Product images and information tested to ensure displayed correctly.
* Quantity dropdown tested to ensure the correct quantity was added to the bag depending on what was chosen.
* Add to bag button tested to ensure it took the user to the shopping bag and the quantity in the shopping bag was correct.
* Back to shop button tested to ensure it took user back to the all products page.
* Saved button tested in the exact same way as in the shop view to ensure the correct outcome whether the user was logged in or not as well as if the item was already in the user's aved items list or not.
* Breadcrumb links also tested to ensure worked the same as on the shop page.
* Comments tested to ensure if not logged in the comment form did not display.
* Comments tested to ensure if logged in the comments form displayed and the user was able to add a comment to the product which displayed the comment with the username and date and time stamp.
* If a comment was added this was then checked to see if correct in django admin.
* Comments tested to ensure if user logged in and it was their comment they were able to delete the comment and it was deleted from the admin also.
* Comments tested to ensure if the comment was not added by the logged in user they were unable to delete.
* For superuser only the edit and delete buttons were tested to ensure they worked correctly referencing the admin and were not accessible to non superuser users.

Shopping Bag:
* Product tables checked to ensure displayed correctly and information correct.
* Quantity dropdown thoroughly tested to ensure javascript worked correctly at hiding and showing the update and cancel buttons.
* Update button for changing quantity was tested to ensure the quantity in the shopping bag was updated correctly.
* Cancel button tested to ensure the quantity was not updated and the number in the dropdown returned to original quantity.
* Back to shop button checked to ensure it took user back to the all products page.
* Toast checked to ensure if quantity updated it didnt show bag summary as already on the bag page.
*  Order total tested to ensure all information correct.

Checkout:
* Forms tested to ensure validation working correctly, a combination or valid and invalid inputs were tested.
* Stripe test card number tested to ensure worked correctly.
* Form tested for logged in users as well as logged out users, if user was logged in the save information checkbox was tested and the autofill information was also checked against the user account.
* Once submitted the checkout success page was tested to ensure it matched the information that was in the shopping bag before checking out.
* Stripe webhooks tested to ensure they were working correctly, the form.save() line of code was commented out to test the webhook worked, which forced the order to be created by the webhook.
* Stripe dashboard was checked on each test order to ensure to errors.

Login/Logout/Signup:
* Logging in was tested with multiple users to ensure forms worked correctly.
* Logout was checked to ensure user was asked if they were sure to logout and then redirected to the home page.
* Cookies work correctly when logging in and logging out, this has been tested many times with a number of users.
* Signup was tested to ensure the form was validating correctly, a combination of valid and invalid inputs were used.
* Confirm email was tested multiple times to ensure the links in the emails worked consistely and redirected the user to the login page.

Account Page:
* Delivery details tested to ensure correct from checkout.
* Updating the details was tested to ensure validation worked properly and the information was correctly saved in the database.
* Order history was checked to ensure all info was correct and the order number links took the users to the correct order pages.
* Saved items page was tested to ensure only products in the user's saved items list were present
* Saved item buttons were tested in the same way they were in shop and product page exceot in saved items page once the solid red heart was clicked it was made sure that that products was removed from saved items list and then dissapeared from the page.

Store Admin:
* Add product form was tested to ensure it submitted data in the correct format for the database and provided the correct options for the user to choose from, checking the admin once submitted to ensure it was successful.
* Edit product page forms also tested in th same way the add product form was but also ensuring the autofilled data was correct, this was also checked against the admin to ensure udated information was successful.

#### Database
* All data inputs to the database follow the same format, whether they are added on the database or through the site.
* All updated data through the edit product view updates the database correctly.
* All user information is clearly and securely stored in the database, any non sensitive information can be viewed in the django admin.
* Once data submitted on the site it has been checked to ensure it is correct in the django admin.

#### Interface
* Each page of the web app has the same consistent layout.
* The navbar and footer display the same links on every page and each link has been tested on each page to ensure they all work and go to the same place.
* The navbar was checked to ensure it was fixed to the top of the screen at all times.
* The margin and padding added to elements to ensure nothing is hidden was checked on all screen sizes and broswers to ensure all information is visible on site at all times.
* The font, colour scheme and styling is consistent across the web app.
* All products are displayed in a similar format no matter of what page they are on for consistency, every page has been checked to ensure all information is rendered correctly.
* The site link hosted through Heroku displays everything correctly.

#### Security
* Incorrect login details returns an error message asking the user to try again, this has been tested with different users and different combinations of correct and incorrect details.
* Decorators for models that users need to be logged in to view have been tested to ensure the user is redirected to the login page.
* Links on the site have been tested to ensure they are hidden and unavailable to users who are not logged in. Also to ensure the correct error message is displayed.
* URL links have been tried when not logged in to ensure users do not have access to areas they shouldn't have and are redirected to the login page with the correct error message.
* Password confirmation when registering ensures users remember their login credentials and ensure the password match, this has been tested with a combination of correct and incorrect inputs to ensure the correct error messages are displayed.
* User passwords are hashed so the password that the user inputs when registering is never saved in the database, this has been checked in the admin to ensure no passwords visible.

#### Accessibility
* All images have been checked to ensure they have an alt attribute which explains the image for screen readers.
* All images have also been checked to ensure they have an aria label when the alt attribute is not available.
* Semantic markup is used for clear html structure, which has been checked thoroughly.
* Contrast of colours used across the site were checked in Google Dev Tools to ensure the contrast was AA meaning a score between 3.0 and 4.5.

#### Usability
* Styling and JavaScript are used to make the navbar interactive when hovering over each nav link to engage the user.
* All links in the navbar work correctly and take you to the correct page.
* The collapsible navbar works correctly on smaller screens with the hamburger button working to show the navbar links.
* Further dropdowns inside the collapsible navbar also work correctly.
* If an error occurs with the URL the 404.html page explains what has happened and displays a link back to the shop page.
* If an error occurs with the URL the 500.html page explains what has happened and displays a link back to the shop page.
* Messages are displayed in a toast near the top of the page on every page giving the user feedback or confirming an action.

#### Compatibility
* The web app was viewed on the following browsers and worked correctly on all; 
    * Google Chrome
    * Safari
    * Internet Explorer

#### Responsiveness
* The web app was viewed on the following devices and worked correctly on all;
    * MacBook
    * MacBook Pro
    * Dell Laptop
    * Desktop monitor
    * iPad Mini
    * iPhone 12 Pro Max
    * iPhone 11
    * Samsung S21
* Google Dev tools was also used to check the responsiveness of the site by changing the size of the screen and using the zoom feature.

#### Performance
* From Lighthouse in Chrome Devtools:
    * Performance - 65
    * Accessibility - 94
    * Best Practices - 93
    * SEO - 83

# Local Deployment

Documentation on how to clone a repo can be found on [Github](https://docs.github.com/en/free-pro-team@latest/github/creating-cloning-and-archiving-repositories/cloning-a-repository)

1. Navigate to the Mainpage of the repository
2. Click the "Code" button
3. Choose "Clone with HTTPs" and copy URL
4. Open the Terminal
5. Change the current working directory to your prefered location
6. Type git clone and past copied URL ```git clone https://github.com/fayskerritt/batch-coffee.git```
7. Press Enter to create local Clone - Make sure your environment supports python3 -
8. Type ```pip3 install -r requirements.txt``` into Terminal
9. Setup the environment variables. This process is differnet depending on the used IDE. Gitpod supports global Environments for the development process. Therefore they were stored in the settings. The following variables are needed:
    ```
    DEVELOPMENT=True   
    STRIPE_PUBLIC_KEY = <YOUR STRIPE_PUBLIC_KEY>
    STRIPE_SECRET_KEY = <YOUR STRIPE_SECRET_KEY>
    STRIPE_WH_SECRET = <YOUR STRIPE_WH_SECRET>
    ```
10. Migrate the models and create the database by typing the following commands into the terminal:
    - ```python3 manage.py makemigrations```  
    - ```python3 manage.py migrate```
11. Import the following fixtures: 
    - ```python3 manage.py loaddata productline```
    - ```python3 manage.py loaddata products```
    - ```python3 manage.py loaddata categories```
    - ```python3 manage.py loaddata proudctsize```
    - ```python3 manage.py loaddata productvariants```
    - ```python3 manage.py loaddata blog ```
    - ```python3 manage.py loaddata faq ```
12. Create a superuser for accessing the django admin view with the following command:
    - ```python3 manage.py createsuperuser``` You will need to enter an email address, username and password.
13. You should be able to use the command ```python3 manage.py runserver``` to run the project.
14. You can access the django admin view by adding ```~/admin``` to the end of your (local) URL.
## Deployment to Heroku
To deply to Heroku follow these steps:
1. Create/Log in to your Heroku account and create a new App.
2. Install Heroku Add-on Heroku Postgres from the Resources tab. Choose the free ```Hobby Dev``` version. Then click the Provision button to add it to your project.
3. Create a requirements.txt file using command ```pip3 freeze --local > requirements.txt```
4. Create a Procfile ```echo web: gunicorn puffins.wsgi:application > Procfile```
5. Commit changes to Git ```git add .``` followed by ```git commit -m "Deploy: Updated Procfile"```
6. Set the environment variables in Heroku Settings under Reveal Config Variables
    Enter the following variables:
    ```
    USE_AWS = TRUE
    AWS_ACCESS_KEY_ID = <YOUR AWS_ACCESS_KEY_ID>
    AWS_SECRET_ACCESS_KEY = <YOUR AWS_SECRET_ACCESS_KEY>
    DATABASE_URL = <YOUR DATABASE_URL> (Set by Heroku Postgres)
    EMAIL_HOST_USER = <YOUR EMAIL_HOST_USER>
    EMAIL_HOST_PASSWORD = <YOUR EMAIL_HOST_PASSWORD>
    DEFAULT_FROM_EMAIL = <YOUR DEFAULT_FROM_EMAIL>
    STRIPE_PUBLIC_KEY = <YOUR STRIPE_PUBLIC_KEY>
    STRIPE_SECRET_KEY = <YOUR STRIPE_SECRET_KEY>
    STRIPE_WH_SECRET = <YOUR STRIPE_WH_SECRET>
    ```
7. Get the DATABASE_URL from the Heroku Settings and add it to your local .env file.
8. To see if the Postgres database is connected to your IDE use the command ```python3 manage.py showmigrations```. This will show all migrations for all models.
9. Migrate the models and create the postgres database on heroku using the following commands:
     ```python3 manage.py makemigrations```  
     ```python3 manage.py migrate```
10. To setup the data in the database import the provided fixtures in the following order (copy&paste if you like): 
    - ```python3 manage.py loaddata categories```
    - ```python3 manage.py loaddata productline```
    - ```python3 manage.py loaddata products```
    - ```python3 manage.py loaddata proudctsize```
    - ```python3 manage.py loaddata productvariants```
    - ```python3 manage.py loaddata blog ```
    - ```python3 manage.py loaddata faq ```
11. Create a superuser for the Postgres database to acces the django admin view:
    ```python3 manage.py createsuperuser``` You will need to enter an email address, username and password.
12. Log in to heroku from your terminal ```heroku login -i```
13. Add exisitng repository to Heroku  ```heroku git:remote -a <your repository>```
14. Push changes to Heroku ```git push heroku master```
15. Now in your AWS S3 account. The bucket should contain a folder called ```static```. To upload product images create a new folder called ```media``` and upload images to this. Grant public read access to these objects. 
15. Finally, go to the heroku app url to see your live site.


# Credits
### Content
* Code Institute - Full Stack Frameworks with Django Boutique Ado project - Inspiration for project from here.
* 
* The developer is not responsible for any copyright of the images added by users.

### Media
* The photos used on the Home page are from [Unsplash](https://unsplash.com/).
    * First image on Home page - [ Unsplash]()
    * Second image on Home page - [ Unsplash]()
* The Logo in the header and footer was made by me.
* The favicon was also designed and created by me.
* The no-image.png image image was also designed and created by me.

### Acknowledgements
* Mentor sessions . 
* Tutor support for help with issues when i got django errors that didn't make sense to me!
