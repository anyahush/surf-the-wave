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
