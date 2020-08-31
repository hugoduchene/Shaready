import { insertPost, url } from './settings.js'

function create_like_comment(type_like, nbs_like) {
    const container_like = document.createElement('div')
    container_like.classList.add('col-6', 'like_comments')

    const icon = document.createElement('i')
    icon.classList.add('fas', type_like, 'like_comments')
    container_like.append(icon)
    icon.after(nbs_like)

    return container_like
}

function event_like_comment(obj, id_comments, pseudoUser, reaction) {
    obj.addEventListener('click', (e) => {
        const data_request = { "reaction_comment" : reaction }
        const request_like = insertPost(data_request, url + "api/comments/createlike/"+ id_comments +"/"+ pseudoUser)
        request_like.then(data => {
            const elt_element = obj.parentNode
            elt_element.firstChild.firstChild.nextSibling.nextSibling.textContent = data.nbs_likes[1]
            elt_element.firstChild.nextSibling.firstChild.nextSibling.nextSibling.textContent = data.nbs_likes[2]
        })
    })

    return obj
}


function create_comment(id_user_comment, src_img, pseudo, date, content_comment, nbs_like, nbs_dislike, id_comment) {
    const container_comments = document.createElement('section')
    container_comments.classList.add('box_comments')
    container_comments.id = id_comment

    const container_other_comments = document.createElement('div')
    container_other_comments.classList.add('comments_other_user')
    container_comments.append(container_other_comments)

    const container_row = document.createElement('div')
    container_row.classList.add('row')
    container_other_comments.append(container_row)

    const container_img = document.createElement('div')
    container_img.classList.add('col-2', 'container_image_comments')
    container_row.append(container_img)

    const container_link_img = document.createElement('a')
    container_link_img.href = "/user/account/" + id_user_comment
    container_img.append(container_link_img)

    const img_user = document.createElement('img')
    img_user.src = '/static/assets/img/' + src_img
    img_user.classList.add('image_comments')
    img_user.alt = "Image User"
    container_link_img.append(img_user)

    const container_info_user = document.createElement('div')
    container_info_user.classList.add('col-10')
    container_row.append(container_info_user)

    const container_pseudo = document.createElement('div')
    container_pseudo.classList.add('pseudo_comments')
    container_pseudo.textContent = pseudo
    container_info_user.append(container_pseudo)

    const container_date = document.createElement('div')
    container_date.classList.add('date_comments')
    container_date.textContent = date
    container_info_user.append(container_date)

    const container_like_comments = document.createElement('div')
    container_like_comments.classList.add('col-12', 'comments')
    container_like_comments.textContent = content_comment
    container_row.append(container_like_comments)

    const container_like  = document.createElement('span')
    container_like.classList.add('row')
    container_row.append(container_like)

    const like = event_like_comment(
        create_like_comment('fa-thumbs-up', nbs_like), 
        id_comment,
        pseudo,
        1,
    )
    container_like.append(like)

    const dislike = event_like_comment(
        create_like_comment('fa-thumbs-down', nbs_dislike),
        id_comment,
        pseudo,
        2,
    )
    container_like.append(dislike)

    return container_comments
}

export {
    create_comment,
}