/* jshint esversion: 6 */

/* Adjusted from: https://github.com/Code-Institute-Solutions/boutique_ado_v1/blob/master/products/templates/products/includes/quantity_input_script.html */

/* 
    * Disable +/- buttons outside 1-99 range.
    * If no size is passed to the function, the parameter will have a value of undefined by default,
    * which prevents any errors 
*/
function handleEnableDisable(itemId, size) {
    var currentValue;
    if (size) {
        currentValue = partseInt($(`.size_${itemId}_${size}`).val());
    } else {
        currentValue = parseInt($(`.id_qty_${itemId}`).val());
    }

    var minusDisabled = currentValue < 2;
    var plusDisabled = currentValue > 98;

    if (size) {
        $(`.decrement-size_${itemId}_${size}`).prop('disabled', minusDisabled);
        $(`.increment-size_${itemId}_${size}`).prop('disabled', plusDisabled);
    } else {
        $(`.decrement-qty_${itemId}`).prop('disabled', minusDisabled);
        $(`.increment-qty_${itemId}`).prop('disabled', plusDisabled);
    }
}

// Ensure proper enabling/disabling of all inputs on page load
var allQtyInputs = $('.qty_input');
for(var i = 0; i < allQtyInputs.length; i++){
    var itemId = $(allQtyInputs[i]).data('item_id');
    var size = $(allQtyInputs[i]).data('size');
    handleEnableDisable(itemId, size);
}

// Check enable/disable every time the input is changed
$('.qty_input').change(function() {
    var itemId = $(this).data('item_id');
    var size = $(this).data('size');
    handleEnableDisable(itemId, size);
});

// Increment quantity
$('.increment-qty').click(function(e) {
    e.preventDefault();
    var itemId = $(this).data('item_id');
    var size = $(this).data('size');
    var closestInput = $(this).closest('.input-group').find('.qty_input')[0];
    if (size) {
        allQuantityInputs = $(`.input-group-${itemId} input[data-size='${size}']`);
    } else {
        allQuantityInputs = $(`.input-group-${itemId} input[name='quantity']`);
    }
    var currentValue = parseInt($(closestInput).val());
    var allQuantityInputs;
    
    currentValue = parseInt($(closestInput).val());
    $(allQuantityInputs).val(currentValue + 1);
    handleEnableDisable(itemId, size);
});

// Decrement quantity
$('.decrement-qty').click(function(e) {
    e.preventDefault();
    var itemId = $(this).data('item_id');
    var size = $(this).data('size');
    var closestInput = $(this).closest('.input-group').find('.qty_input')[0];
    if (size) {
        allQuantityInputs = $(`.input-group-${itemId} input[data-size='${size}']`);
    } else {
        allQuantityInputs = $(`.input-group-${itemId} input[name='quantity']`);
    }
    var currentValue = parseInt($(closestInput).val());
    var allQuantityInputs;
    
    currentValue = parseInt($(closestInput).val());
    $(allQuantityInputs).val(currentValue - 1);
    handleEnableDisable(itemId, size);
});