function generateResponse() {

    const responseBox = document.getElementById("responseText");

    responseBox.value =
`Guten Tag Herr Müller,

vielen Dank für Ihre Nachricht.

Es tut uns leid zu hören, dass Ihre Heizung nicht funktioniert.

Wir prüfen gerne, ob wir morgen einen Techniker zu Ihnen nach Heidelberg schicken können.

Wir melden uns schnellstmöglich mit einem Termin bei Ihnen.

Viele Grüße
Ihr Handwerk-Team`;

    responseBox.focus();
}


function editResponse() {

    const responseBox = document.getElementById("responseText");

    responseBox.focus();

    responseBox.select();
}


function approveResponse() {

    const responseBox = document.getElementById("responseText");

    if (responseBox.value.trim() === "") {

        alert("Please generate a response first.");

        return;
    }

    const confirmed = confirm(
        "Are you sure you want to approve and send this response?"
    );

    if (confirmed) {

        alert(
            "Response approved! Email sending will be connected to FastAPI next."
        );

    }
}