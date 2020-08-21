import { url, request ,post_like, infinite, insertPost } from './module/settings.js'
import { create_comment } from './module/settings_article_only.js'

/* Event on like in article_only */

const all_reaction = ['.love', '.like', ".dislike"]
const pseudo_author = document.querySelector('#pseudo_author').textContent
const id_article = new URL(window.location.href).pathname.split('/')[2]
let place_nbs_like = document.querySelectorAll('.nbs_like')

for (let i = 0; i < all_reaction.length; i++) {
    const elt = document.querySelector(all_reaction[i])
    elt.addEventListener('click', (e) => {
        post_like(elt, pseudo_author, id_article).then(data => {
            for (let x = 0; x < place_nbs_like.length; x++) {
                place_nbs_like[x].textContent = data.nbs_likes[x+1]
                
            }
        })
    })
    
}

/* manages the display of comments */

function infinite_comments(i) {
    const place_comment = document.querySelector('.place_comment')
    const request_comment = request(url + "api/comments/getall/" + id_article + "/" + i)
    request_comment.then(data => {
        for (let x = 0; x < data.length; x++) {
            place_comment.append(create_comment(
                data[x].info_user.photo, 
                data[x].info_user.pseudo, 
                data[x].date_comment, 
                data[x].content_comment, 
                data[x].nbs_likes[1] = (data[x].nbs_likes[1] === undefined) ? 0 : data[x].nbs_likes[1], 
                data[x].nbs_likes[2] = (data[x].nbs_likes[2] === undefined) ? 0 : data[x].nbs_likes[2],
                data[x].id
            ))
        }
    })
}

/* display of the first items */

infinite_comments(1)

/* display of the following items */

const item = document.getElementById('end_body')
infinite(item, infinite_comments)

/* create comment */

document.getElementById('button_comments').addEventListener('click', (e) => {
    e.preventDefault()
    let content_comment = document.querySelector('.input_comment').value
    if (content_comment.length > 0) {
        let data = { "content_comment" : content_comment }
        const request_create_comment = insertPost(data, url + "api/comments/createcomment/" + id_article + "/" + pseudo_author)
        document.querySelector('.input_comment').value = ""
        request_create_comment.then(data => {
            const new_comment = create_comment(
                data.info_user.image_profile,
                data.info_user.pseudo,
                data.info_user.date.split('T')[0],
                data.content_comment,
                0,
                0,
            )

            const place_comment = document.querySelector('.place_comment')
            place_comment.insertBefore(new_comment, place_comment.firstChild)
        })
    }



})
