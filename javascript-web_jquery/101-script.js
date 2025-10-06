$(document).ready(function () {
    // Add an element to the list
    $('DIV#add_item').click(function () {
        $('UL.my_list').append('<li>Item</li>');
    });

    // Remove last element from the list
    $('DIV#remove_item').click(function () {
        $('UL.my_list li:last-child').remove();
    });

    // Clear all elements from the list
    $('DIV#clear_list').click(function () {
        $('UL.my_list').empty();
    });
});