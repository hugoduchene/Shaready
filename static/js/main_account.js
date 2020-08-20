import { url, request, create_loader, ManageArticle, insertPost } from './module/settings.js'
import { infinite_scroll_article_user, infinite_articles_user } from './module/settings_account.js'

/* Put articles at the good place */

const place_article = document.getElementById('place_article')
const url1 = new URL(window.location.href)
const id_user = url1.pathname.split('/')[3]

place_article.append(create_loader())
const request_articles_user = request(url + "api/articles/getarticleuser/"+ id_user +"/1")
request_articles_user.then(data => {
    ManageArticle(data)
}).catch((error => {
    console.log(error)
}))

/* infinite scroll */

window.addEventListener("DOMContentLoaded", (event) => {
    let item = document.getElementById('end_body')
    infinite_articles_user(item, infinite_scroll_article_user, id_user)
  });


/* Subscribe button configuration */

document.querySelector('.follow_button').addEventListener('click', (e) => {
    const pseudoUser = document.querySelector(".name_user").textContent
    const data = {
        "id_receiving" : id_user
    }
    const request_subscribe = insertPost(data , url + "api/user/postsubscription/" + pseudoUser)
    request_subscribe.then(data => {
        document.getElementById("nbs_follows").textContent = data.nbs_follows

        if (data.already_follow == 1) {
            document.querySelector('.follow_button').classList.add('already_follow')
            document.querySelector('.follow_button').textContent = 'Followed'
        } else {
            document.querySelector('.follow_button').classList.remove('already_follow')
            document.querySelector('.follow_button').textContent = 'Follow'
        }
    })
})
