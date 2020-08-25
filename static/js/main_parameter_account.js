import { validateAndUpload } from './module/settings_parameter_account.js'

/* manages the change of photo */

const file = document.getElementById('file')

file.addEventListener('change', (e) => {
    validateAndUpload(file)
})


