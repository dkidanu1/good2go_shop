// --- Call function for email.js ---
(function(){emailjs.init("user_xrIf5Dia8Ng6JpCHdTsuT");})();

// --- Sends e-mail to set up service on email.js 
document.getElementById('contactForm').addEventListener('submit', function (event) {
    event.preventDefault();
    emailjs.send("gmail", "goodtogo", {
        "from_name": contactForm.name.value,
        "from_email": contactForm.emailaddress.value,
        "contact_request": contactForm.message.value
    })
        .then(
            function success() {
                notification();
                setTimeout(refresh, 2500);
            },
            function failure() {
                failToSend();
            }
        );
    return false;
});

// --- Change text to notify user of successful send (200)  ---
function notification() {
    $("#submit").text("Your message has been submitted successfully");
}

// --- Refresh Form ---
function refresh() {
    $("#submit").text("Submit");
    document.getElementById("contactForm").reset();
}

// --- E-mail failed to sent (404) ---
function failToSend(){
    $("#submit").text("Failed to submit. please refresh page and try again");
}
