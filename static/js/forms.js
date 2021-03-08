'use strict';

$('#new-itinerary').click(function(){
    $('#itinerary-form').toggle();
});

$('#edit-itinerary').click(function(){
    $('#edit-form').toggle();
});


$('#edit-entry').click(function () {
    $('#entry-form-edit').show('slow', function() {

    });
});

$('#delete-entry').on('click', (evt) => {
    evt.preventDefault();

    const deleteEntryInfo = {
        id: $('#delete-confirmed').val()
    };

    console.log(deleteEntryInfo)
    console.log(`/api/delete-entry/${deleteEntryInfo['id']}`)

    $.post(`/api/delete-entry/${deleteEntryInfo['id']}`, deleteEntryInfo, (res) => {

    })

    window.location.replace('/profile')
})