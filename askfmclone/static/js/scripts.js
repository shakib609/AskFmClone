(function() {
    alert_messages = $('.alert-success');
    $('[data-toggle="tooltip"]').tooltip();

    if (alert_messages)
        setTimeout(function() {
            alert_messages.fadeOut(200);
        }, 10000);
})();
