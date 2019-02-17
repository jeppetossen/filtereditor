$(document).ready(function ()
{
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

    $(".Subsection").on('click', function (event)
    {
        let element = event.target;
        let elementClist = element.classList;
        let elementIdNumber = element.id.split("_")[1];
        let subsectionContent = targetElementById(elementIdNumber).classList;

        if (elementClist.contains("closed")) {
            subsectionContent.replace("closed", "open", );
            elementClist.replace("closed", "open", );
        } else if (elementClist.contains("open")) {
            subsectionContent.replace("open", "closed");
            elementClist.replace("open", "closed");
        }
    });

    $(".BlockSubsection").on('click', function (event)
    {
        let element = event.target;
        let elementClist = element.classList;
        let elementIdNumber = element.id.split("_")[1];
        let subContent = targetElementByIdBlock(elementIdNumber).classList;

        if (elementClist.contains("closed")) {
            subContent.replace("closed", "open");
            elementClist.replace("closed", "open");
        } else if (elementClist.contains("open")) {
            subContent.replace("open", "closed");
            elementClist.replace("open", "closed");
        }
    });

    function targetId(element)
    {
        return element.id;
    }

    function targetIdNumber(elementId)
    {
        let elementSplit = elementId.split("_");
        return elementSplit[1];
    }

    // TODO: Make a cleaner solution
    function targetElementById(elementId)
    {
        return document.getElementById("SubsectionBlockContent_" + elementId);
    }
    function targetElementByIdBlock(elementId)
    {
        return document.getElementById("BlockSubsectionContent_" + elementId);
    }
});