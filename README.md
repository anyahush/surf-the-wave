# Surf the Wave
![Mock-up of site]()

Surf the Wave is a fictional e-commerce site that sells surf equipment and surfwear for all those who love surfing or are curious to try! This is the fourth milestone project as part of my Diploma with Code Institute. This project focuses on the development of a full-stack e-commerce site that uses a centrally-owned dataset by using HTML, CSS, JavaScript, Python+Django, relational database(Postgres), stripe payments and AWS.

Deployed website can be viewed [here]().

## Table of Contents
---
1. [Project Goals]()
2. [UX]()
3. [Strategy Plane]()
    * [User Stories]()
4. [Scope Plane]()
    * [Existing Features]()
    * [Features Left to Implement]()
5. [Structure Plane]()
6. [Skeleton Plane]()
7. [Surface Plane]()
8. [Technologies]()
9. [Testing]()
10. [Deployment]()
11. [Credits]()
12. [Acknowledgements]()

---

## UX Design

## Strategy Plane

### Site Owner Goals
- Promote surf shop buisness and increase sales of surf boards and equipment
- Increase online status and promote the site on social media
- Encourage the uptake of surfing, amongst all ages and genders, through blog posts and social media

### Demograghic
- All genders and ethnicities
- All levels of surfing
- Ages 7+


### User Stories

- As a first time visitor:
    * I want to easily navigate throughout the site.
    * I want to understand the purpose of the site easily.
    * I expect an attractive site that contributes to my good experience.
    * I want the site to be accessible.
    * I want the site to be responsive across all devices.

- As an unregistered visitor:
    * I want to be able to search and filter products easily and efficiently.
    * I want to be able to sort and view products according to type, price and name.
    * I want to be able to be able to view product detail so I can find information about price, size and description.
    * I want to be able to add products to my shopping basket.
    * I want to be able to view my shopping basket.
    * I want to be able to edit my shopping basket.
    * I want to be able to view the total cost of my basket.
    * I want to be able to complete the checkout process and be able to enter payment information easily.
    * I want to be able to view a confirmation of my order once the checkout process is complete.
    * I want to be able to received an email confirmation of my order.
    * I want to be able to register easily for an account.
    * I want to be able to access the blog posts.

- As a registered visitor:
    * I want to be able to receive a confirmation email upon registration.
    * I want to be able to view my personalised profile.
    * I want to be able to save and edit personal information on my profile.
    * I want to be able to view my order history.
    * I want to be able to login an logout with ease.
    * I want to be able to leave reviews on products.
    * I want to be able to edit or delete my reviews.
    * I want to be able to leave comments on the blog posts.
    * I want to be able to delete my account.
    * I want to be able to change my password if I forget it.

- As a returning visitor:
    * I want to be able to find social media links.
    * I want to be able to contact the site owner if I have any queries.
    * I want to enjoy using the site without never ending scrolling.

- As a superuser:
    * I want to be able to add new products.
    * I want to be able to edit or delete existing products.
    * I want to be able to add new categories.
    * I want to be able to add new blog posts.
    * I want to be able to edit or delete existing blog posts.
    * I want to be able to delete blog comments left by users. 
    * I want to be able to delete user reviews left on products.
    * I want to be able to delete a user.
    * I want to be able to make another user admin.
    * I want to inform users of products that are out of stock, and prevent users from purchasing them.



## Scope Plane

### **Existing Features**

During the initial strategy planning, the opportunities of the site were determined and values were given according to their imporance and viability ranking between 1 and 5. Below are the list of features that were valued important and viable at this stage. The remaining features have been recorded in Features Left to Implement.

#### Design
- Responsive design
- Accessible
- Easy navigation throughout, nav links clearly labelled or icons used in navbar. Sidenav used for smaller devices.
- Site logo - returns user to the home page
- Nav link options will change depending on status of user eg. unregistered, registered or admin
- On the home page a selection of photos will be displayed that link to different sections of the site, aimed to promote certain products or lines that are in season

#### Products
- Users are able to search and filter products depending on what they are looking for
- Users can add products to shopping basket
- Users can update or delete products from shopping basket
- Users can securely purchase product(s) from the site
- Order confirmation will be displayed to user and subsequent confirmation email sent.
- If a product is 'Out of Stock', this will be displayed to the user and the add to basket button will be hidden
- Registered users can leave reviews on products
- Registered users can edit or delete their reviews

#### Register, Login and Logout
- Users are able to register for an account
- Registered users can login and logout of account
- Users will receive confirmation emails for registering, order summary and deleting account
- Registered users can change their password if forgotten
- Registered users can view profile containing personal information and order history
- Registered users can save and update personal information on their profile

#### Admin
- Admin users can add, update and delete products
- Admin users can create new categories
- Admin users can add, update and delete blog posts
- Admin users can delete user comments on blog posts
- Admin users can delete user reviews on products
- Admin users can delete users
- Admin users can make other users admin

#### Other
- Users can contact site owner through contact form
- If user is logged in, contact form will pre-populate
- Social media links displayed
- Back to top button in footer, to prevent unnecessary scrolling
- All users can view blog posts, if logged in users can leave comments
- Deletion confirmation before anything is deleted, to prevent accidental deletion
- Cancel buttons on all edit pages, incase user changes their mind



### **Features Left to Implement**

- A wishlist section for logged in users to save products for future purchase
- Expand further product lines and product ranges
- A rating and comment section for products


## Structure Plane 

### Database 

## Skeleton Plane

### Wireframes
The wireframes for this project were developed using [Balsamiq](https://balsamiq.com/).

| Mobile | Tablet| Desktop|
--------------------|--------------------|--------------------------|
| [Mobile](readme/assets/wireframes/mobile.png) | [Tablet](readme/assets/wireframes/tablet.png) | [Desktop](readme/assets/wireframes/desktop.png) |


### Changes to Wireframes



## Surface Plane

During initial stages of development, I carried out research to explore what other surf websites looked like. From what I found, most surf websites are fairly simple in design, following standard layouts of e-commerce sites. In particular, I found two sites that I have taken inspiration from in the design and colour schemes; [Surfdome](https://www.surfdome.com/) and [Shore](https://www.shore.co.uk/).

### Colour Scheme

As mentioned above, I used inspiration from other surf websites whilst choosing the colour schemes. I decided that blue, an obvious choice with the correlation to water, and yellow, due to its bright and uplifting colour and it can represent the sun. 

Initially I chose two colours that I wanted to use. They are Yellow Orange and Cornflower Blue.

![Yellow Orange colour](readme/assets/readme-images/yellow-orange.png)

![Cornflower Blue colour](readme/assets/readme-images/cornflower-blue.png)

Following this, I used [Coolers](https://coolors.co/) to create a palette of complimentary colours.

![Colour palette](readme/assets/readme-images/colour-palette.png)


### Images

Initially a logo, created using [Adobe](https://www.adobe.com/express/create/logo), was going to be used. During initial stages of development I felt the logo did not fit well with the aesthetic of the site and decided to remove this. The brand logo was created using 'Source Sans Pro' font from Google Fonts.



### Typography

To ensure easy reading, consistency and a good user experience, I have chosen Akshar font from [Google Fonts](https://fonts.google.com/).

## Technologies

### Languages
- HTML
- CSS3
- JavaScript
- Python

### Frameworks and Libraries

- [Am I Responsive?](http://ami.responsivedesign.is/) was used to create the mock ups.
- [Balsamiq](https://balsamiq.com/) was used to create the wireframes.
- [Bootstrap 5.1.3](https://getbootstrap.com/) was used to contribute to responsiveness and styling of the site.
- [Font Awesome](https://fontawesome.com/) was used for button icons.
- Git was used for version control ad to push code to GitHub.
- [GitHub](https://github.com/) was used to store the repository.
- [GitPod](https://www.gitpod.io/) was used as the IDE to develop the project.
- [Google Fonts](https://fonts.google.com/) were used to select fonts for the site.
- [Lambdatest](https://www.lambdatest.com/) was used to check browser compatibility.
- [Online JavaScript Beautifier](https://beautifier.io/) was used to standardise HTML, CSS and JavaScript files.



## Testing

The testing process can be viewed [here]().

## Deployment



## Credits

### Content


#### Code Content
* README layout and style used from previous [project](https://github.com/anyahush/protect-our-planet-quiz).
* [Code Institute's Boutique Ado](https://github.com/Code-Institute-Solutions/boutique_ado_v1) walkthrough project was used throughout as a guide.
* Image hover effect on image gallery modified from [W3 Schools Tutorial](https://www.w3schools.com/howto/tryit.asp?filename=tryhow_css_image_overlay_opacity) and [Shore's website](https://www.shore.co.uk/).
* The shopping basket page modiefied code from [Surfdome](https://www.surfdome.com/).


### Media

#### Images


## Acknowledegments
- Code Institute tutors and Slack community for help and guidance
- My mentor Precious Ijege for his help and guidance throughout
- My mini-Feb group on Slack for moral support and feedback


