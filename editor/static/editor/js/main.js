/*$(document).ready(function () {

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
    $(".SpectrumColorPicker").spectrum({
        preferredFormat: "rgb",
        showInput: true,
        allowEmpty: true,
        showAlpha: true,
        clickoutFiresChange: true,
        move: function (tinycolor) {
            $(this).val( tinycolor.toRgbString() );
        }
    });

    // TODO: Clean up and make it less repeatable code
    $(".Subsection").on('click', function (event) {
        let element = event.target;
        let elementClist = element.classList;
        let elementIdNumber = element.id.split("_")[1];
        let subsectionContent = targetElementById(elementIdNumber).classList;
        if (elementClist.contains("closed")) {
            subsectionContent.remove("closed");
            subsectionContent.add("open");
            elementClist.remove("closed");
            elementClist.add("open");
        } else if (elementClist.contains("open")) {
            subsectionContent.remove("open");
            subsectionContent.add("closed");
            elementClist.remove("open");
            elementClist.add("closed");
        }
    });

    $(".BlockSubsection").on('click', function (event) {
        let element = event.target;
        let elementClist = element.classList;
        let elementIdNumber = element.id.split("_")[1];
        let subContent = targetElementByIdBlock(elementIdNumber).classList;
        if (elementClist.contains("closed")) {
            subContent.remove("closed");
            subContent.add("open");
            elementClist.remove("closed");
            elementClist.add("open");
        } else if (elementClist.contains("open")) {
            subContent.remove("open");
            subContent.add("closed");
            elementClist.remove("open");
            elementClist.add("closed");
        }
    });

    function targetId(element) {
        return element.id;
    }

    function targetIdNumber(elementId) {
        let elementSplit = elementId.split("_");
        return elementSplit[1];
    }

    // TODO: Make a cleaner solution
    function targetElementById(elementId) {
        return document.getElementById("SubsectionBlockContent_" + elementId);
    }
    function targetElementByIdBlock(elementId) {
        return document.getElementById("BlockSubsectionContent_" + elementId);
    }
});