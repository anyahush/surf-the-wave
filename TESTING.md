# Testing

## Table of Contents
---
1. [Code Validation]()
    * [HTML Validation]()
    * [CSS Validation]()
    * [JavaScript Validation]()
    * [Python Validation]()
2. [Testing User Stores]()
3. [Responsiveness]()
4. [Browser Compatibility]()
5. [Performance]()
6. [Manual Testing]()
7. [Bugs]()
    * [Found and Fixed]()
    * [Existing]()


### Code Validation

### Testing User Stories

- As a first time visitor:
    1. I want to easily navigate throughout the site.
        - Across all device screen sizes there is a navbar with options to get around the site. 
        ![Mobile Nav](readme/assets/user-story-testing-images/mobile-nav.png)
        ![Main Nav](readme/assets/user-story-testing-images/navbar.png)
    2. I want to understand the purpose of the site easily.
        - On the home page the images, name of site and navbar options clearly indicate that it is a surf shop
        - The image gallery and text make the user aware of the latest stock and blogs
        ![Home page](readme/assets/user-story-testing-images/mobile-home.png)
    3. I expect an attractive site that contributes to my good experience. -ADD ONCE LIGHTHOUSE TESTING DONE
    4. I want the site to be accessible. - ADD ONCE LIGHTHOUSE TESTING DONE
    5. I want the site to be responsive across all devices.
        - Throughout development responsiveness has been considered. Using Bootstrap and media queries the site is accessible across all devices.


- As an unregistered visitor:
    1. I want to be able to search and filter products easily and efficiently.
        - A searchbar input field allows users to search by product, description or category
        ![Searchbar](readme/assets/user-story-testing-images/searchbar.png)
        - Product category badges allow users to filter which category they want to look at
        ![Category badges](readme/assets/user-story-testing-images/product-categories.png)
        - Navbar dropdown menus have categories listed so users can easily filter which products they want to look at
        ![Navbar dropdown](readme/assets/user-story-testing-images/navbar-dropdown.png)
    2. I want to be able to sort and view products according to type, price and name.
        - The sort selector dropdown allows users to sort products based on price, name or category
        ![Sort selector](readme/assets/user-story-testing-images/sort-products-selector.png)
    3. I want to be able to be able to view product detail so I can find information about price, size and description.
        - The product detail page displays product information clearly for the user
        ![Product detail](readme/assets/user-story-testing-images/product-detail.png)
    4. I want to be able to add products to my shopping basket.
        - On the product detail page an 'Add to basket' button allows users to add products to their bags.
        ![Add to basket button](readme/assets/user-story-testing-images/add-to-basket-button.png)
    5. I want to be able to view my shopping basket.
        - Users can click on shopping basket icon in navbar or 'Proceed to basket' button on toast message
        - The basket page displays all products added to basket and an order summary
        ![Basket page](readme/assets/user-story-testing-images/shopping-basket.png)
    6. I want to be able to edit my shopping basket.
        - A quantity selector dropdown allows users to change the quantity and use the update link to update the amount
        - The remove link allows users to remove item completely from their basket
        ![Quantity selector](readme/assets/user-story-testing-images/quantity-selector.png)
    7. I want to be able to view the total cost of my basket.
        - In the shopping basket page the total cost with breakdown of order total and delivery cost are displayed
        - Total cost of basket is also displayed in toast messages if the user is not on the basket or profile pages
    8. I want to be able to complete the checkout process and be able to enter payment information easily.
        - The checkout page displays checkout form. This is clearly labelled with input labels and placeholders
        - Stripe card payment section is available for card payments
        ![Checkout page](readme/assets/user-story-testing-images/checkout.png)
    9. I want to be able to view a confirmation of my order once the checkout process is complete.
        - The checkout success page displays an order confirmation for the user
        ![Order confirmation](readme/assets/user-story-testing-images/order-confirmation.png)
    10. I want to be able to received an email confirmation of my order.
        - Following a successful order an orde confirmation email is sent
        ![Order confirmation email](readme/assets/user-story-testing-images/order-confirmation-email.png)
    11. I want to be able to register easily for an account.
        - In the user dropdown menu, users can select to register for an account
        - The register account form is simple and clearly labelled
        ![Register dropdown](readme/assets/user-story-testing-images/dropdown-menu.png)
        ![Register form](readme/assets/user-story-testing-images/register-form.png)
    12. I want to be able to access the blog posts.
        - Following the blog navlink, it takes users to the blogs page. All users can view blog posts
        ![Blogs page](readme/assets/user-story-testing-images/blogs-page.png)
        ![Blog Post](readme/assets/user-story-testing-images/blog-post.png)

- As a registered visitor:
    * I want to be able to receive a confirmation email upon registration.
        - Users receive a confirmation email to verify their email address
        ![Email verification](readme/assets/user-story-testing-images/verify-email.png)
    * I want to be able to view my personalised profile.- ADD ONCE LIGHTHOUSE done
    * I want to be able to save and edit personal information on my profile. -ADD ONCE LIGHTHOUSE done
    * I want to be able to view my order history.
        - On the users profile page, users can view their order history
        ![Order history](readme/assets/user-story-testing-images/order-history.png)
    * I want to be able to login and logout with ease.
        - Users select the dropdown to login, which takes them to the login form
        ![Login form](readme/assets/user-story-testing-images/login-form.png)
        - Users can select the dropdown to logout, or if on the profile page their is a logout button
        ![Logout]()
    * I want to be able to leave reviews on products.
        - Logged in users can leave one review per product
        ![Product review](readme/assets/user-story-testing-images/product-review.png)
    * I want to be able to edit or delete my reviews.
        - Users can edit or delete their own reviews
        ![Edit and delete buttons]()
    * I want to be able to leave comments on the blog posts.
        - Logged in users can leave one comment per blog post
        ![Blog comments](readme/assets/user-story-testing-images/blog-comments.png)
    * I want to be able to edit or delete comments on blog posts.
        - Users can edit or delete their own comments
        ![Edit and delete buttons](readme/assets/user-story-testing-images/blog-comment.png)
    * I want to be able to delete my account.
        - Under 'My Account' on the profile page, users can delete their account
        -![Delete account]()
    * I want to be able to change my password to keep my account secure.
        - Under 'My Account' on the profile page, users can change their password 
        ![Change password]()
    * I want to be able to reset my password if I forget it.
        - On the login page, users can click a link to reset their password if they have forgotten it
        ![Forgot password]()

- As a returning visitor:
    * I want to be able to find social media links.
        - In the footer, across all pages, users can find links to the sites social media accounts
        ![Social media accounts](readme/assets/user-story-testing-images/social-media-links.png)
    * I want to be able to contact the site owner if I have any queries.
        - In the footer, across all pages, their is a link to the contact form
        ![Contact link](readme/assets/user-story-testing-images/contact-us-link.png)
        ![Contact Form](readme/assets/user-story-testing-images/contact-form.png)
    * I want to enjoy using the site without never ending scrolling.
        - In the footer, across all pages, their is a 'Back to top' link
        ![Back to top link](readme/assets/user-story-testing-images/back-to-top-link.png)

- As a superuser:
    * I want to be able to add new products.
        - From the navbar dropdown or in the profile page, superusers can add new products
        ![Add product form](readme/assets/user-story-testing-images/add-product-form.png)
    * I want to be able to edit or delete existing products.
        - On the products page and each product detail page, edit and delete links allow superusers to edit or delete products
        ![Edit and delete links](readme/assets/user-story-testing-images/blog-edit-delete-links.png)
        ![Edit product form](readme/assets/user-story-testing-images/edit-product-form.png)
    * I want to be able to add new categories.
        - In the admin portal, accessed from the admin navlink, superusers can add new categories
        ![New category](readme/assets/user-story-testing-images/add-category.png)
        ![New category form](readme/assets/user-story-testing-images/add-category-form.png)
    * I want to be able to add new blog posts.
        - From the navbar dropdown or in the profile page, superusers can add new blogs
        ![Add blog form](readme/assets/user-story-testing-images/add-blog-form.png)
    * I want to be able to edit or delete existing blog posts.
        - On the blogs page and each blog detail page, edit and delete links allow superusers to edit or delete blogs
        ![Edit and delete links]()
        ![Edit blog form](readme/assets/user-story-testing-images/edit-blog-form.png)
    * I want to be able to delete blog comments left by users.
        - A delete comment button is displayed for superusers to delete any comment left
        ![Delete comment button]()
    * I want to be able to delete user reviews left on products.
        - A delete review button is displayed for superusers to delete any review left
        ![Delete review button]()
    * I want to be able to access the Django admin portal easily
        - In the superuser user option dropdown there is a link to the admin portal
        ![Admin dropdown](readme/assets/user-story-testing-images/admin-dropdown-menu.png)
    * I want to be able to delete a user.
        - In the admin portal, superusers can delete any user
        ![Delete user](readme/assets/user-story-testing-images/delete-user.png)
    * I want to be able to make another user admin.
        - In the admin portal, superusers can make other users admin
        ![Admin user](readme/assets/user-story-testing-images/make-superuser.png)




### Responsiveness

### Browser Compatibility

### Performance

### Manual Testing

### Bugs

#### Found and Fixed

- Whilst setting up webhooks there was issues with the webhook being sent back from Stripe. With investigation and searching on Slack and through web searches I found that I hadn't changed the port to public, so Stripe wasn't able to connect.
    * Solution: Port was changed to public.
- Once the webhook handler for payment_intent_succeeded had been updated to be able to get or create orders to be stored, I found an issues with street_address2. The webhook was failing and displaying a 'NOT NULL constraint' error. I discovered that in the Order model I had set null=False, instead of null=True. 
    * Solution: Order model updated with street_address2, null=True

#### Existing
