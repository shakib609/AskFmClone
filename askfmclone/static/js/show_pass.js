(function() {
    password_field = $('#id_password');
    show_pass = $('#show_pass')

    show_pass.on('change', function(e) {
        if (this.checked)
            password_field.attr({type: 'text'})
        else
            password_field.attr({type: 'password'})
    })
})();
