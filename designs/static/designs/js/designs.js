/* jshint esversion: 6 */
let canvas = new fabric.Canvas('tshirt-canvas');

function updateTshirtImage(imageURL) {
    fabric.Image.fromURL(imageURL, function (img) {
        img.scaleToHeight(100);
        img.scaleToWidth(100);
        canvas.centerObject(img);
        canvas.add(img);
        canvas.renderAll();
    });
}

// Update the TShirt color according to the selected color by the user
document.getElementById("tshirt-color").addEventListener("change", function () {
    document.getElementById("tshirt-div").style.backgroundColor = this.value;
}, false);

// When the user clicks on upload a custom picture
document.getElementById('tshirt-custompicture').addEventListener("change", function (e) {
    var reader = new FileReader();

    reader.onload = function (event) {
        var imgObj = new Image();
        imgObj.src = event.target.result;

        // When the picture loads, create the image in Fabric.js
        imgObj.onload = function () {
            var img = new fabric.Image(imgObj);

            img.scaleToHeight(100);
            img.scaleToWidth(100);
            canvas.centerObject(img);
            canvas.add(img);
            canvas.renderAll();
        };
    };

    // If the user selected a picture, load it
    if (e.target.files[0]) {
        reader.readAsDataURL(e.target.files[0]);
    }
}, false);

// When the user selects a picture that has been added and press the DEL key
// The object will be removed !
document.addEventListener("keydown", function (e) {
    var keyCode = e.key;

    if (keyCode == 46) {
        console.log("Removing selected element on Fabric.js on DELETE key !");
        canvas.remove(canvas.getActiveObject());
    }
}, false);

// Define as node the T-Shirt Div

var node = document.getElementById('tshirt-div');
var saveBtn = document.getElementById('saveDesignBtn');

var designCount = 0;
saveBtn.addEventListener('click', function(e){
    designCount += 1;

    domtoimage.toPng(node).then(function (dataUrl) {
        console.log(dataUrl);

        var img = new Image();
        img.src = dataUrl;
        sessionStorage.setItem('design', dataUrl);
    }).catch(function (error) {
        console.error('oops, something went wrong!', error);
    });
    
});