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


$('#add-entry').click(function () {
    $('#new-entry-form').show('slow', function(){

    });
});

$('#submit-entry').on('submit'), (evt) => {
    evt.preventDefault();
    
    const entryData = $('#entry-form').serialize();
    const url = '/api/new-entry'
    console.log(entryData)
    $.post(url, entryData, (res) => {

    });

    window.location.reload();
}

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