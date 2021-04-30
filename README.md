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


