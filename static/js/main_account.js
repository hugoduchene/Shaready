import { infinite, url, request, create_loader, ManageArticle } from './module/settings.js'
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