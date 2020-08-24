import { get_button_edit, get_modal_class } from './module/popup_make_message.js';
import { infinite, url, request, create_loader, hidden_loader, insertPost, ManageArticle } from './module/settings.js'
import { infinite_scroll_article_categories } from './module/FeedSettings.js'

/* create trends articles */
if (document.querySelector("#see_categories").value == "trends") {
  place_article.append(create_loader())
  const request_trends = request(url + "api/articles/gettrends/")
  request_trends.then(data => {
    ManageArticle(data)
    if (data.length == 0) {
      hidden_loader()
    }
  })
}

/* Manage pop up to create a article */

get_button_edit().addEventListener("click", function onclick(e) {
  get_modal_class().classList.toggle("visible");
  get_modal_class().classList.toggle("invisible");
});

get_modal_class().onclick = function(e) {
  const target = e.target;
  
  if (target === get_modal_class()) {
    get_modal_class().classList.toggle("visible");
    get_modal_class().classList.toggle("invisible");
  }
}

/* display of the articles according to their category */

document.querySelector("#see_categories").addEventListener("click", function(e){
  const place_article = document.getElementById('place_article')
  place_article.innerHTML = ""
  place_article.append(create_loader())
  const value_id = document.getElementById('see_categories').value
  if (value_id == "trends") {
    const trends = request(url + "api/articles/gettrends/")
    trends.then(data => {
      ManageArticle(data)
      if (data.length == 0) {
        hidden_loader()
      }
    })
  } else if (value_id == "subscription") {
    const articles_subscription = request(url + "api/articles/getarticlessubscribed" + "/1")
    articles_subscription.then(data => {
      ManageArticle(data)
      if (data.length == 0) {
        hidden_loader()
      }
    })
  } else {
    const articles_categories = request(url + "api/articles/getarticlecategory/" + value_id + "/1")
    articles_categories.then(data => {
      ManageArticle(data)
    })

  }

  let item = document.getElementById('end_body')
  infinite(item, infinite_scroll_article_categories)
  
});

/* Manage counter of character count */

document.getElementById('content_article').addEventListener('keydown', (e) => {
  let nbs_character = document.getElementById('content_article').value.length
  document.getElementById('number_character').textContent = nbs_character
  if (nbs_character > 850) {
    document.getElementById('number_character').style.color = 'red'
  } else if (nbs_character < 850) {
    document.getElementById('number_character').style.color = 'rgb(124, 124, 124)'
  }

  

})

/* create article */

document.getElementById('button_create_post').addEventListener("click", function(e){
  if (document.getElementById('title').value.length > 0 && document.getElementById('content_article').value.length > 0 && document.getElementById('content_article').value.length < 850) {
    const data = {
      "title" : document.getElementById('title').value,
      "content_article" : document.getElementById('content_article').value,
      "id_category" : document.getElementById('add_in_categories').value
    }
    insertPost(data, url + "api/articles/postcreatearticle")
    get_modal_class().classList.toggle("invisible");
  } else {
    console.log("error")
  }
})

