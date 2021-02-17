"use strict"

$('#get-user').on('submit'), (evt) => {
  evt.preventDefault();

  const formData = {login_email: $('#login-email').val(),};
    
  $.get('/login-user', formData, (res) => {
    %('#flash').append(res)
  })
}