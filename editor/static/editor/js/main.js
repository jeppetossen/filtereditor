/*$(document).ready(function () {
    $(".group-header").on('click', function (event) {
        let target_parent = $(event.target).parent().find(".container-visual-content");
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
});*/

$(document).ready(function () {
    $(".Subsection").on('click', function (event) {
        let element = event.target.classList;
        //alert(element);
        if (element.contains("closed")) {
            element.remove("closed");
            element.add("open");
        } else if (element.contains("open")) {
            element.remove("open");
            element.add("closed");
        }
    });

    function toggleContentElements(event) {

    }
});