import { url } from './settings.js'

function create_box(src_image, pseudo, id_user) {
    const container_box_user = document.createElement('div')
    container_box_user.classList.add("col-sm-3")

    const container_box_user_search = document.createElement('div')
    container_box_user_search.classList.add('box_user_search')
    container_box_user.append(container_box_user_search)

    const container_img = document.createElement('a')
    container_img.classList.add('col-12')
    container_img.href = url + "user/account/" + id_user
    container_box_user_search.append(container_img)

    const img_user = document.createElement('img')
    img_user.classList.add('little_image_search_user')
    img_user.src = "/static/assets/img/" + src_image
    img_user.alt = "Image User"
    container_img.append(img_user)

    const container_pseudo = document.createElement('div')
    container_pseudo.classList.add('col-12', 'pseudo_search_user')
    container_pseudo.textContent = pseudo
    container_box_user_search.append(container_pseudo)

    return container_box_user
}

function manage_box_user(data, elt) {
    for (let i = 0; i < data.length; i++) {
        elt.append(create_box(data[i].image_profile, data[i].username, data[i].id))
    }

}

export {
    manage_box_user,
}