import {url , request, insertPost } from './module/settings.js'

/* get number of notifications */

const request_nbs_notif = request(url + "api/notification/getnbsnotifications")
request_nbs_notif.then(data => {
   const nbs_notif = data.all_notification
   const place_notifs = document.querySelectorAll(".nbs_notif")
   for (let i = 0; i < place_notifs.length; i++) {
       if (data.all_notification > 9) {
        place_notifs[i].textContent = "9+"
       } else {
        place_notifs[i].textContent = data.all_notification
       }
    }
   
})

/* read notification */
const place_click_notifs = document.querySelectorAll('#button_notif')
for (let i = 0; i < place_click_notifs.length; i++) {
    place_click_notifs[i].addEventListener('click', (e) => {
        const read_notif = insertPost({}, url + "api/notification/postmanagenotification")
        
    })
}

