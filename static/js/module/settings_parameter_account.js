function event_submit() {
    document.getElementById('img_user').addEventListener('submit', (e) => {
        e.preventDefault()
        document.getElementById('img_user').submit()
    })
}


function validateAndUpload(input){
    const URL = window.URL || window.webkitURL;
    const file = input.files[0];

    if (file) {
        const image = new Image();

        image.onload = function() {
            if (this.width) {
                const src = URL.createObjectURL(file)
                const preview = document.querySelector('.image_user_change_pic')
                preview.src = src
                event_submit()
            }
        }
        image.src = URL.createObjectURL(file);
        
    }
}


export {
    validateAndUpload,
}