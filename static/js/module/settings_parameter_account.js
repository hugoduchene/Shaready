import { insertPost } from './settings.js'

function event_submit() {
    document.getElementById('img_user').addEventListener('submit', (e) => {
        e.preventDefault()
        document.getElementById('img_user').submit()
    })
}
 

function cropped_image() {
    const cropButton = document.getElementById('button_img')
    const img = document.getElementById('img_user_pic')

    let cropper = new Cropper(img, {
        aspectRatio: 1 / 1,
        minCropBoxWidth:150,
        minCropBoxHeight:150,
        maxCropBoxWidth:150,
        maxCropBowHeight:150,
        scalable: false,
        cropBoxResizable: false,
        responsive: true,
        crop(event) {
            const canvas = this.cropper.getCroppedCanvas()
            const data_img = canvas.toDataURL("image/jpeg")
            img.src = data_img

            document.querySelector("#cropped_img").value = data_img
            event_submit()
        }
    })
}


function validateAndUpload(input){
    const URL = window.URL || window.webkitURL;
    let file = input.files[0];

    if (file) {
        const image = new Image();

        image.onload = function() {
            if (this.width) {
                const src = URL.createObjectURL(file)
                const preview = document.querySelector('.image_user_change_pic')
                preview.src = src
                cropped_image()
            }
        }
        image.src = URL.createObjectURL(file);
        
    }
}


export {
    validateAndUpload,
}