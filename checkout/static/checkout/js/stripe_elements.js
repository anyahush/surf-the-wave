// Declare variables
var stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
var clientSecret = $('#id_client_secret').text().slice(1, -1);
var stripe = Stripe(stripePublicKey);
var elements = stripe.elements();

var style = {
    base: {
        iconColor: '#aab7c4',
        color: '#000',
        fontWeight: '500',
        fontFamily: 'Roboto, Open Sans, Segoe UI, sans-serif',
        fontSize: '16px',
        fontSmoothing: 'antialiased',
        ':-webkit-autofill': {
            color: '#fce883',
        },
        '::placeholder': {
            color: '#aab7c4',
        },
    },
    invalid: {
        iconColor: '#dc3545',
        color: '#dc3545',
    }
};

var card = elements.create('card', {style: style});
card.mount('#card-element');

// Create change event and displays error message
// if error occurs
card.addEventListener('change', function(event) {
    var errorDiv = document.getElementById('card-errors');
    if(event.error) {
        var html = `
        <span rold="aler">
            <i class="fas fa-times></i>
        </span>
        <span>${event.error.message}</span>`
    } else {
        errorDiv.textContent = '';
    }
});

// Handle form submit
var form = document.getElementById('payment-form');

form.addEventListener('submit', function(ev) {
    ev.preventDefault();
    card.update({ 'disbaled': true});
    $('#submit-button').attr('disabled', true);
    stripe.confirmCardPayment(clientSecret, {
        payment_method: {
            card: card,
        }
    }).then(function(result) {
        if(result.error) {
            var errorDiv = document.getElementById('card-errors');
            var html = `
                <span rold="aler">
                <i class="fas fa-times></i>
                </span>
                <span>${event.error.message}</span>`;
            $(errorDiv).html(html);
            card.update({ 'disbaled': false});
            $('#submit-button').attr('disabled', false);
        } else {
            if (result.paymentInten.status === 'succeeded') {
                form.submit();
            }
        }
    })
})