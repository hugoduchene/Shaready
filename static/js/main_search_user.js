import { url ,request, hidden_loader, create_loader} from './module/settings.js'
import { manage_box_user, } from './module/SearchUserSettings.js'

document.querySelector('#searchUser').addEventListener('submit', function (e) {
    e.preventDefault()
    if (document.getElementById('InsearchUser').value.length > 0) {
        e.preventDefault()
        document.getElementById('PlaceUser').innerHTML = ""
        document.getElementById('PlaceUser').append(create_loader())
        const valueInput = document.getElementById('InsearchUser').value
        const requestUser = request(url + "api/user/getresearchuser/" + valueInput)
        requestUser.then(data => {
            manage_box_user(data, document.getElementById('PlaceUser'))
            document.getElementById('InsearchUser').value
            hidden_loader()
        })
    }
    
});