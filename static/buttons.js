var lock_button = $("#lock_button");
lock_button.click(function() {
    $.ajax({
        url: "/lock_door",
        type: "post",
        success: function(response) {
            console.log(response);
        }
    });
});

var unlock_button = $("#unlock_button");
unlock_button.click(function() {
    $.ajax({
        url: "/unlock_door",
        type: "post",
        success: function(response) {
            console.log(response);
        }
    });
});

var light_on_button = $("#light_on_button");
light_on_button.click(function() {
    $.ajax({
        url: "/light_on",
        type: "post",
        success: function(response) {
            console.log(response);
        }
    });
});

var light_off_button = $("#light_off_button");
light_off_button.click(function() {
    $.ajax({
        url: "/light_off",
        type: "post",
        success: function(response) {
            console.log(response);
        }
    });
});