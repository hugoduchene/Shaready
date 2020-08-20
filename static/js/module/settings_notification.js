import {url, request, create_loader, hidden_loader} from './settings.js'

function create_notification(id_user, img_src, pseudo, date, text_notif){
    const container_notif = document.createElement('div')
    container_notif.classList.add('row', 'box_notification')

    const container_img_user = document.createElement('div')
    container_img_user.classList.add('col-4')
    container_notif.append(container_img_user)

    const container_link_img = document.createElement('a')
    container_link_img.href = url + "user/account/" + id_user
    container_img_user.append(container_link_img)

    const img_user = document.createElement('img')
    img_user.classList.add('img_notifications')
    img_user.src = "/static/assets/img/" + img_src
    img_user.alt = "image user"
    container_link_img.append(img_user)

    const container_infos_user = document.createElement('div')
    container_infos_user.classList.add('col-8')
    container_notif.append(container_infos_user)

    const container_pseudo = document.createElement('div')
    container_pseudo.classList.add('pseudo_notifications')
    container_pseudo.textContent = pseudo
    container_infos_user.append(container_pseudo)

    const container_date = document.createElement('div')
    container_date.classList.add('date_notifications')
    container_date.textContent = date
    container_infos_user.append(container_date)

    const container_content_notif = document.createElement('p')
    container_content_notif.classList.add('text_notifications')
    container_content_notif.textContent = pseudo + text_notif
    container_notif.append(container_content_notif)

    return container_notif
}

function manage_notification(i){
    document.querySelector(".content_notifications").append(create_loader())
    const request_all_notif = request(url + "api/notification/getallnotification/" + i)
    request_all_notif.then(data => {
        for (let i = 0; i < data.length; i++) {
            const date_notif = data[i].date_notification.split('T')[0]
            let notif_content = data[i].type_notification
            
            switch (notif_content) {
                case "1":
                    notif_content = " is one of your most loyal fans, it's your turn to respect his subscription by writing a great article!"
                    break;
                case "2":
                    notif_content = " likes one of your articles, keep it up and you'll be more popular than justin bibier !"
                    break;
                case "3":
                    notif_content = " likes one of your comments, congratulations, you're relevant!"
                    break;
                case "4":
                    notif_content = " had the courage to comment one of your articles, don't deny your fans !"
                    break;
            }
            document.querySelector(".content_notifications").append(create_notification(
                data[i].infos_user.id_user,
                data[i].infos_user.image_profile,
                data[i].infos_user.pseudo,
                date_notif,
                notif_content,
            ))
        }
    })
    hidden_loader()
}

export {
    create_notification,
    manage_notification,
}