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
        let element = event.target;
        let elementClist = element.classList;
        targetIdNumber(element.id);
        //alert(targetId(event));
        if (elementClist.contains("closed")) {
            elementClist.remove("closed");
            elementClist.add("open");
        } else if (elementClist.contains("open")) {
            elementClist.remove("open");
            elementClist.add("closed");
        }
    });

    function targetId(element) {
        return element.target.id;
    }

    function targetIdNumber(elementId) {
        let elementSplit = elementId.split("_");
        return elementSplit[1];
    }

    function toggleSubsectionBlocks(parent) {
        if (parent.contains("closed")) {
            parent.remove("closed");
            parent.add("open");
        } else if (parent.contains("open")) {
            parent.remove("open");
            parent.add("closed");
        }
    }
});