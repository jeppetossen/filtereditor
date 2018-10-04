$(document).ready(function () {
    $(".group-header").on('click', function (event) {
        let target_parent = $(event.target).parent().find(".container-group-content");
        if (target_parent.css("display") === "none") {
            target_parent.css("display", "flex");
        } else {
            target_parent.css("display", "none");
        }
    });

    $(".ps-colorpicker").spectrum({
        preferredFormat: "rgb",
        showInput: true,
        allowEmpty: true,
        showAlpha: true,
        clickoutFiresChange: true,
        move: function (tinycolor) {
            $(this).val( tinycolor.toRgbString() );
        }
    });
});