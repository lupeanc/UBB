$(document).ready(function(){
    // delete - no longer use this. take from url instead
    // $("table").on('click', '.delete-button', function () {
    //     let id = $(this).closest('tr')[0].cells[0].innerText;
    //     // send delete req to php
    //     // $.post("delete.php",{'id': id});
    //
    //     //remove the row visually
    //     $(this).closest('tr').remove();
    // });


    // update
    $("table").on('click', '.selected-id', function () {
        let tableId = $(this).closest('tr')[0].cells[0].innerText;
        let tableUserId = $(this).closest('tr')[0].cells[1].innerText;
        let tableRoomId = $(this).closest('tr')[0].cells[2].innerText;
        let tableStart = $(this).closest('tr')[0].cells[3].innerText;
        let tableEnd = $(this).closest('tr')[0].cells[4].innerText;
        $(".update_form #id").val(tableId);
        $(".update_form #user_id").val(tableUserId);
        $(".update_form #room_id").val(tableRoomId);
        $(".update_form #start").val(tableStart);
        $(".update_form #end").val(tableEnd);
    });

});