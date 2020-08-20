import {url , request } from './module/settings.js'

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

