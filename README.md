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
View the deployed site here - [Batch Coffee](https://pad-plants.herokuapp.com/)

![Mockup](static/img/readme/mockup.png)

# UX
## Project Goals
The main goal of this project was to create a fully functional web store that was capable of 



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
* As a shopper, I want to choose the size of a product when purchasing so I can add the correct size to my bag
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
* A range of greens were chosen for different attributes:


![Mockup](static/img/readme/colourscheme.png)

### **Typography**
* Roboto was chosen for the font to go with the linear pattern of the site. It was thought that anything too fancy wouldn't have gone well with the house plant images.

### **Imagery**
* The home page features two artistic images of houseplants, which capture the eye and go well with the green colour theme.
* The profile and 404 pages also feature artistic imagery of houseplants which are in keeping with the theme.
* Font Awesome icons are used in areas to clearly label input fields and headers.
* Each plant has an image at the top of the card which shows the user exactly what the plant looks like.

### **Wireframes**
**Home page:**

* 2 column structure on larger screens which changes to 1 on smaller screens. Had to use a Bootstrap row-reverse class to switch the second image and text to show opposite to the top whilst still showing text - image - text - image on a mobile device.
    * Figma screenshot - [Home](https://raw.githubusercontent.com/fayskerritt/padplants/master/static/img/readme/homewireframe.png)

**Plants page:**

* Wireframe shows a hero image but during development the page looked too busy with an image so left that out.
    * Figma screenshot - [Plants](https://raw.githubusercontent.com/fayskerritt/padplants/master/static/img/readme/plantswireframe.png)

**Profile page:**

* Image added to the side of the Username as page looked quite bare for new users.
    * Figma screenshot - [Profile](https://raw.githubusercontent.com/fayskerritt/padplants/master/static/img/readme/profilewireframe.png)

**Add Plant page:**

* Page copied to create Edit page by filling in the inputs from the database
* Font Awesome icons used to represent the 3 different light conditions; Shade, Light & Shade and Direct Sunlight. Also to represent the 5 rooms; Bathroom, Bedroom, Living Room, Study and Kitchen.
    * Figma screenshot - [Add Plant](https://raw.githubusercontent.com/fayskerritt/padplants/master/static/img/readme/addwireframe.png)

**Login page:**

* Simple form, ended up adding Font Awesome icons to the Username and Password Labels
    * Figma screenshot - [Login](https://raw.githubusercontent.com/fayskerritt/padplants/master/static/img/readme/loginwireframe.png)

**Register page:**

* Same form layout as Login page with extra input to confirm password, this was to prevent an error when entering their password first time round.
    * Figma screenshot - [Register](https://raw.githubusercontent.com/fayskerritt/padplants/master/static/img/readme/registerwireframe.png)

### Database Structure
#### Creation of database on MongoDB:
* Once registered and logged in to [MongoDB](https://www.mongodb.com/) a database was created named 'pad-plants' and a document was added to the Plant collection with the following 'key: value' pairs:

    `_id:` (str)\
    `name:` (str)\
    `botanical_name:` (str)\
    `description:` (str)\
    `watering:` (str)\
    `size:` (str)\
    `light_needed:` (str)\
    `room:` (str)\
    `img_url:` (str)

* These keys were used when adding any more plants to the database.
* The other collection used was Users which had the 'key: value' pairs:

    `_id:` (str)\
    `username:` (str)\
    `password:` (str)

* The password string is hashed when the user inputs it using the Werkzeug generate_password_hash method, so is stored as a string.



# Features
### Existing Features
* Registration - Creating a profile using a unique username and password which is stored in the database, the password will be hashed for better security.
* Displaying database of plants on the Plants page - Pulling the data from MongoDB to display the list of all plants in the database with all fields displayed nicely in their own individual cards.
* Adding a plant - Creating a plant and adding it to the database using the Add Plant form. This allows the user to input the name, botanical name and a description. There are two drop downs for the user to choose the size and how often the plant needs watering. There are also two lots of radio checkboxes that the user can choose how much light the plant needs and which room the plant goes best in. Finally there is an input for the user to add a URL for an image, however if the URL doesn't work then the image displayed will be a default image.
* Editing a plant you have added - An edit button will be available to edit the fields of a plant you have added, the previously chosen fields will be auto filled on the Edit page. The Admin user profile has access to edit all plants.
* Deleting a plant you have added - A delete button will be available to delete a plant that you have added. The Admin user profile has access to delete all plants.
* Viewing all plants you have added on your Profile page - Pulling data from MongoDB to display the plants that have been added by the user that is logged in, this uses the 'created by' field.
* Searching the database - 
    * The search has the option of a text input, which searches the plant name, botanical name and description fields. 
    * Two drop down menus that allow the user to search by room and by size. 
    * Two check boxes that allow the user to filter the list by plants that are happy in low light and plants that do not need watering very often. 
    * You can combine all these search fields to find the perfect plant for you.
* Different buttons and options visible depending on logged in status - 
    * Register and Login options in the navbar are visible before logging in, which are hidden to show the Logout option once logged in. 
    * Register button on the home page changes to Browse once logged in. 
    * Edit and Delete buttons are only visible against plants that the logged in user has created.
    * Edit and Delete buttons are visible on all plants to the Admin user.
* Visible buttons when no search results found - 
    * If no plants are found when using the search functionality then a message will show and an Add button will be visible.
    * If no plants have been added yet by the current user, a message and Add button will show on the profile page.
* Responsiveness - As can be seen in the mockup at the top of this README the site is responsive across all sizes of device. The Bootstrap Grid framework was used to enable this.
* Defensive Programming - A modal is used to ask the user if they are sure they want to delete a plant when the Delete button is clicked.
* To ensure user is always able to read the whole description overflow was set to scroll in css in case of zoomed in font sizes on different devices.
* Interactive Navbar that displays a bottom border when hovering as well as bolder font on the page that is active.
* An external link is present on the home page with the option to buy plants, this sends users to an Amazon page currently.
* Social Media links in the footer - Links to social media pages increase engagement with users.


### Features to Implement in the Future
* Pagination on the Plants page as the database grows.
* A link to an active selling page to be added to the home page to gain sales from community members.
* A link option on each plant card to send the user to a site where the plant is available to buy.

# Technologies Used

* [HTML5](https://en.wikipedia.org/wiki/HTML5) - To build templates for website pages.
* [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets) - To style the HTML content to make the site look nice and display nicely on the page.
* [Python3](https://www.python.org/) - To write scripts that get and post data to the MongoDb Database.
* [jQuery](https://jquery.com/) - To simplify DOM manipulation for Bootstrap
* [MongoDB](https://www.mongodb.com/) - To create a plant database that stores information entered from the Pad Plants web app.
* [Flask](https://flask.palletsprojects.com/en/1.1.x/) - To create a flask app in Python that is backed by MongoDB and allows for routing to be coded for the different pages and functions of the web app.
* [Jinja](https://palletsprojects.com/p/jinja/) - Templating used in HTML files as a link for the Python expressions and functions.
* [Werkzeug](https://pypi.org/project/Werkzeug/) - To debug code when an error is highlighted, also for password hashing as a security helper.
* [Pymongo](https://pypi.org/project/pymongo/) - To simplify the communications between the flask app and the Mongo database.
* [Python.OS](https://docs.python.org/3/library/os.html) - To set the default environment variables for the web app.
* [BSON.ObjectId](https://docs.mongodb.com/manual/reference/method/ObjectId/) - To find documents in MongoDB by rendering the ObjectId.
* [GitHub](https://github.com/) - To store the project once pushed from Gitpod.
* [Git](https://git-scm.com/) - For Version control by using the Gitpod terminal to add, commit and push the code to GitHub.
* [Bootstrap](https://getbootstrap.com/) - Template used to ensure site is responsive as well as for styling objects as a base for own CSS.
* [Figma](https://www.figma.com/file/HC618UdxHcbhAvexrrO5Hp/Milestone-2-Wireframes) - To create wireframes, logo, favicon and the colour chart for README.
* [Google Fonts](https://fonts.google.com/) - Roboto font used for all pages of web app.
* [Font Awesome](https://fontawesome.com/) - To display icons used for better readability.


# Testing
### Code Validation
* [HTML Validator](https://validator.w3.org/nu/?doc=https%3A%2F%2Fpad-plants.herokuapp.com%2F) - No errors found
* [CSS Validator](https://jigsaw.w3.org/css-validator/validator) - No errors found 
* [JSHint](https://jshint.com/) - No issues found 
* [PEP8](http://pep8online.com) - No issues found

### Testing User Stories
#### New User
* As a new user, I want to understand the main purpose of the site, so I can learn more about the site’s features.
    * Once loaded, the home page clearly explains the sites purpose and prompts the user to register via a button so that they can "discover the best houseplants for your home and share your favourites with others", when clicked, the register button takes the user to the Registration page.
    * Tested on different browsers and devices and the layout works well on all, collapsing from 2 columns to 1 on smaller devices.
    * The register button was tested on all browsers and devices by either clicking or touching depending on device, the registration form successfully loaded on all.
* As a new user, I want to see the plants featured on the website, so I can learn more about plants.
    * When clicked, the clearly labelled "Plants" tab in the Navbar or the "Browse" button on the homepage takes the user to the plants.html page where all plants in the database are displayed once loaded. This list is displayed in a card grid format and can be scrolled through to view all plants, or alternatively use the search form to search using the different inputs.
    * Tested on different browsers and devices and the grid is responsive depending on screen size, looks good on all and displays all information clearly on all.
* As a new user, I want to be shown where I can buy plants, so I can purchase a house plant.
    * On the home page there is a link to the "plant store", this stands out on a clear green background and when clicked, the link takes the user to an Amazon 'Houseplants' search in a new tab, which in the future will be set up to a Pad Plants store.
    * Tested on different devices and browsers to ensure it always opened in a new tab which it did.

#### Returning User
* As a returning user, I want to register to the site, so I have my own profile to store my information.
    * On the home page, when clicked, the "Register" button takes the user to the registration page, this page displays a form that requires the user to enter a username and password, then to re-enter the password to ensure the user has correctly entered their desired password. The form has 3 required inputs which will flag with an exclamation mark if the entry is not valid. The username is required to be between 5 and 15 characters and the following characters are allowed; A-Z a-z 0-9 ! @ # $ % ^ & * _ = + - this is the same for the password fields.
    * Tested by using different formats of username and password including one with lots of symbols and one with none, some with only numbers and all worked fine.
    * Also tested by leaving some of the inputs blank as well as clicking register without filling anything in. Every time a pop up appeared telling the user to fill in the missing field.
* As a returning user, I want to add plants to the database, so I can share my plant knowledge with the community.
    * Create functionality provides the user with a form to add in details about the plant. 
    * There are three text input fields; "Name" which is required and must be between 3 and 30 characters, "Botanical Name" which is not required and must also be between 3 and 30 characters then "Description" which is required and must be between 5 and 200 characters. 
    * Two drop down select options allow the user to choose the watering schedule and size of plant.
    * Tested by adding plants making sure to test all possible selections and options.
    * Also tested by leaving some required fields blank, this caused a pop up to appear telling the user to fill in the missing field. It was decided when developing that the check boxes would not be required as to not put off users who did not know this information.
* As a returning user, I want to have access to all plants added by other members, so I can benefit from other people's knowledge.
    * All plants are visible to all users on the Plants page, in descending order so a returning user can view most recently added plants.
    * As above, this was tested on different browsers and devices, page is fully responsive to changes in size.
* As a returning user, I want to be able to logout of my profile, so I can keep my data safe.
    * Logout option in the navbar will delete session cookies for that user and take them back to the login page where they will need to re-enter their credentials again to log back in.
    * Tested by logging in and using the logout button with the dev tools open to ensure session cookies was deleted. Successful every time.

#### Frequent User
* As a frequent user, I want to edit my added plants, so I can keep the information current.
    * Every plant that the currently logged in user has added will have an edit button, which will take the user to an edit form which will fill in the form with the current data from the database and will allow the user to edit each input then save, or alternatively cancel if they decide to no longer edit.
    * Tested by changing the inputs multiple times and checking each time after clicking save that the data has been updated on MongoDB, which was successful every time.
    * Also tested by taking the URL of the edit page and logging out then trying to view the URL, this shows an error message telling the user they are not authorised to edit the plant and a cancel button that returns you to the plants page for security reasons.
* As a frequent user, I want to search for specific plants, so I can find information about plants I own.
    * The Plants page includes a search bar which allows the user to search any word and will search within the database from the name, botanical name and description keys.
    * This was tested by searching the database using words that I knew were in the database, these all displayed the correct plants.
    * It was also tested using words that are not present in the database which brought up the no plants found text.
* As a frequent user, I want to be able to delete my added plants, so I can ensure no duplicates in the database.
    * Every plant that the currently logged in user has added will have a delete button, which will remove the plant from the database. If clicked there is a pop up that requires the user to confirm deletion to prevent accidental deleting.
    * To test this 5 test plants were added and 3 were deleted from the plants page and 2 from the profile page. The id in the URL was checked for each and Mongodb was also checked to ensure the data had been deleted. All worked fine.
* As a frequent user, I want to view all plants with specific filters, so I can choose a new house plant to suit my needs.
    * As mentioned above there is a search bar which searches the name, botanical name and description of all plants in the database.
    * There are also two drop down options which allow the user to choose a room and/or a size. Finally there are two checkboxes; one which will display plants that do not require a lot of light and/or the other which will display plants that do not require frequent watering. 
    * Each input can be searched on its own or they can be combined to create an advanced search of the list of plants from the database.
    * This was tested by searching the database with every possibility of search:
        * Individual input search, so tried searching by all 5 rooms on their own, all sizes on their own and each check box checked on its own. Worked fine
        * Two inputs selected, this was trialled with; room & size, room and light, room and water, size and light, size and water, light and water all worked fine and showed correct findings, or none found.
        * Three inputs selected, this was trialled on all rooms with a size selected then each checkbox selected, all worked fine or showed the none found text.
        * All inputs selected; this was trialled with all selected which only showed results for certain rooms, but all were correct.
        * Finally all of the above were tested with a text input as well, all tests worked fine and showed correct list of plants.

#### Site Owner/Developer
* As the owner/developer, I want to expand my database of plants, so I can broaden my knowledge.
    * The site is simple to use, users are directed to the register page from the home page as well as if they search for a plant and there are no results.
    * Logging into the site is easy and when registering you have to confirm your password, so users are less likely to forget their credentials.
    * Adding a plant is also easy, the botanical name is not required so even if users don't have that information, they are still able to add a plant.
    * This was tested by friends and relatives who tested the site for me.
* As the owner/developer, I want to redirect users to a store, so I can gain sales from people interested in plants.
    * The link to a store is clearly visible to all users on the homepage with a clear green background.
    * This was tested by clocking the link and ensuring the page opened in a new tab.
* As the owner/developer, I want to grow my community of plant lovers, so I have an audience of potential customers.
    * The site looks nice and is inviting with nice images and a good layout, which will attract users to explore further as well as make them more likely to return.
    * This was tested by asking family and friends for feedback, which was all very positive.


### Manual Testing
#### Functionality
* All internal links are clearly labelled and work correctly when clicked.
* All external links are clearly labelled, work correctly and open in a new tab.
* All buttons are clearly labelled and work correctly.
* All forms submit data in the correct format for the database and provide the correct options for the user to choose from.
* All inputs, dropdown menus and checkboxes work correctly and submitting these displays the correct results.
* Cookies work correctly when logging in and logging out.
* All photos render clearly and the correct size and position.
* All plant information renders clearly and the correct size and position.

#### Database
* All data inputs to the database follow the same format, whether they are added on the database or through the web app.
* All updated data through the edit plant button updates the database correctly.
* All user information is clearly and securely stored in the database.

#### Interface
* Each page of the web app has the same consistent layout.
* The font, colour scheme and styling is consistent across the web app.
* All queries from the database display the plant data clearly and well formatted across both the plant page and profile page.
* The site link hosted through Heroku displays everything correctly.

#### Security
* Incorrect login details returns a generic error message and reloads the page.
* Users can only update and delete plants that they have added, jinja templating is used to hide information from any users that are not authorised.
* Password confirmation when registering ensures users remember their login credentials.
* Password is hashed so the password that the user inputs when registering is never saved in the database.

#### Accessibility
* All images have an alt attribute which explains the image for screen readers.
* Aria labels are also used when the alt attribute is not available.
* Semantic markup is used for clear html structure.
* Contrast of colours used across the site were checked in Google Dev Tools to ensure the contrast was AA meaning a score between 3.0 and 4.5.

#### Usability
* Styling and JavaScript are used to make the navbar interactive when hovered over to engage the user.
* The active page is bold in the navbar to tell the user which page they are on.
* All links in the navbar work correctly and take you to the correct page.
* The collapsible navbar works correctly on smaller screens with the hamburger button working to show the navbar links.
* If an error occurs with the URL the 404 page explains what has happened and displays a link back to the plants page.
* Flash messages are displayed in a banner near the top of the page which is the same on every page giving the user feedback or confirming an action.

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
* Also Google Dev tools was used to check the responsiveness of the site by changing the size of the screen and using the zoom feature.

#### Performance
* From Lighthouse in Chrome Devtools:
    * Performance - 59 (lower metrcis due to the size of the images on the home page causing load time to increase)
    * Accessibility - 92
    * Best Practices - 93
    * SEO - 100

#### Bugs
* Search functionality was coded incorrectly to start with using elif to check if the select inputs and checkboxes had been filled in, which meant that as soon as one of the expressions was true then it would ignore the rest of the elifs. This was fixed by changing it to an if statement for each input area.
* Add Plant button was visible when no plants could be found when using the search bar, even if the user was not logged in. This was fixed by adding in a jinja if statement to only show the add button if the user was logged in and to show the register button if they were not.
* Modal pulled ID of first plant in the list, so when trying to delete a specific plant it would delete the first plant instead. This was fixed by adding in a jinja reference to the plant ID in the ID attribute of the modal html element, which fixed the bug. 
* When adding in plants the URL was not pasted in correctly which caused there to be no photo of the plant, therefor an onerror attribute was added to the plant cards so that a default image was shown instead.
* When testing in safari the description scroll positioning cut the top line of the description off so a margin was added to the paragraph as well as a min-width to the card to fix this.
* Images on homepage cause a higher load time, however I do not want to affect the quality of the images as they are a bit part of the aesthetics, so this would be something I would look into in the future.

# Deployment

### Deploy App to Heroku
*In Gitpod:*

* Once the Flask App is created, the following OS default environment variables were set in the `env.py` file:
    * "IP", with the IP address you want the app to run on.
    * "PORT", with the specified port.
    * "SECRET_KEY", with a value generated from a random key generator.
    * "MONGO_URI", with the connection string from MongoDB.
    * "MONGO_DBNAME", with the database name

* This file along with all other sensitive files were added to the `.gitignore` file.
* To specify the Python package dependencies to Heroku the requirements.txt file was created using the command `pip3 freeze --local > requirements.txt`.
* The Procfile was also created using the command `echo web: python app.py` to tell Heroku that the `app.py` file uses the Python language.

*In Heroku:*

* A new app was created with the name 'pad-plants'.
* In the 'Deploy Tab' GitHub was connected using the repository name.
* In the 'Settings' tab of Heroku, the Configuration Variables were added (these are the 'key: value' pairs that were declared in the `env.py` file).
* Back in the 'Deploy' tab the 'Enable Automatic Deployment' button was clicked to allow automatic updates from GitHub.
* The branch was then deployed from the master.

*In Gitpod:*

* The Mongo database is then wired up to the Flask app by adding the Mongo links to the default environment variables.

### Local Deployment
* On the [GitHub Repository](https://github.com/fayskerritt/padplants), click on the '↓ Code' button.
* Copy the link to clone the repository using the HTTPS tab.
* In your preferred IDE CLI, navigate to the directory you would like to clone to.
* Type `git clone ` followed by the URL you copied from step 3 and press enter.
* Once cloned, all files from workspace will be visible.
* You will need to create an `env.py` that had previously been added to the `.gitignore` file.
* To test type `python3 app.py` into the CLI and open the 8080 port.
* Finally using git you can push this to your own GitHub repository.


# Credits
### Content
* Code Institute - Backend Development Mini Project - Inspiration for code layout and functionality learnt here.
* Details about plants added was sourced from the web and written in the user's own words.
* The developer is not responsible for any copyright of the images added by users.

### Media
* The photos used on the Home page, Profile page and 404 page are all from [Unsplash](https://unsplash.com/).
    * First image on Home page - [Igor Son from Unsplash](https://unsplash.com/photos/FV_PxCqgtwc)
    * Second image on Home page - [Ergita Sela from Unsplash](https://unsplash.com/photos/OFrc0b8ruts)
    * Profile page image - [Annie Spratt from Unsplash](https://unsplash.com/photos/S7viz8JWxwY)
    * 404 page image - [Annie Spratt from Unsplash](https://unsplash.com/photos/zPktb9QkcGY)
* The Logo in the header and footer was made by me.
* The favicon was also designed and created by me.
* The default plant image was also designed and created by me.
* The photo URLs used for each plant in the database are from a google search, images added by developer are listed below:
    * Mother in Law's Tongue from [cloudinary.com](https://res.cloudinary.com/patch-gardens/image/upload/c_fill,f_auto,h_840,q_auto:good,w_840/v1563812091/products/snake-plant-e0fb21.jpg)
    * Swiss Cheese Plant from [cloudfront.net](https://d6p0gevo8s9lm.cloudfront.net/media/catalog/product/cache/1/image/9df78eab33525d08d6e5fb8d27136e95/m/o/monstera-deliciosa-1.jpg)
    * ZZ Plant from [shopify.com](https://cdn.shopify.com/s/files/1/0350/5665/products/5N8A2459_web_600x600.jpg?v=1579563579)
    * Calathea Medallion from [cloudinary.com](https://res.cloudinary.com/patch-gardens/image/upload/c_fill,f_auto,h_840,q_auto:good,w_840/v1539774938/products/calathea-19d9d9.jpg)
    * Parlour Palm from [smartgardenguide.com](https://smartgardenguide.com/wp-content/uploads/2019/05/how-to-care-for-a-parlor-palm-chamaedorea-elegans-11-681x1024.jpg)
    * Snake Plant from [plnts.com](https://plnts.com/wp-content/uploads/2020/03/sku_Sansevieria-Fernwood-Mikado_potCR_M_144274-s.jpg)
    * String of Hearts from [redd.it](https://i.redd.it/7zymycxc7v951.jpg)
    * Peace Lily from [etsystatic.com](https://i.etsystatic.com/15265690/r/il/9c7e6c/1211862072/il_570xN.1211862072_3kuo.jpg)
    * Rubber Plant from [cloudinary.com](https://res.cloudinary.com/patch-gardens/image/upload/c_fill,f_auto,h_840,q_auto:good,w_840/v1526658099/products/rubber-plant-f432b4.jpg)
    * Devil's Ivy from [shopify.com](https://cdn.shopify.com/s/files/1/0758/3437/products/Devils_Ivy_j_1024x.jpg?v=1588073704)
    * Spider Plant from [shopify.com](https://cdn.shopify.com/s/files/1/0268/0029/1885/products/GD_Spider_H_White_SM_Plant_2.jpg?v=1597093748)
    * Spotted Begonia from [smartgardenguide.com](https://smartgardenguide.com/wp-content/uploads/2019/10/begonia-maculata-care-12.jpg)
    * Bird of Paradise from [crocdn.co.uk](https://img.crocdn.co.uk/images/products2/pl/20/00/03/44/pl2000034452.jpg?width=940&height=940)
    * Corn Plant from [cloudinary.com](https://res.cloudinary.com/patch-gardens/image/upload/c_fill,f_auto,h_840,q_auto:good,w_840/v1539776737/products/corn-plant-214138.jpg)
    * Mini Swiss Cheese Plant from [plnts.com](https://plnts.com/wp-content/uploads/2020/03/PL_M_014_Monstera-Adansonii_potCR_M_1027719.jpg)
    * Red Chinese Evergreen from [cloudinary.com](https://res.cloudinary.com/patch-gardens/image/upload/c_fill,f_auto,h_840,q_auto:good,w_840/v1581949716/cyxonbr7h6zt8umiukts.jpg)

### Acknowledgements
* Mentor sessions helped me figure out how to fix my search functionality to combine checked boxes with text. 
* Tutor support for help with issues when attempting to add in jinja templating to html and getting red errors in gitpod.