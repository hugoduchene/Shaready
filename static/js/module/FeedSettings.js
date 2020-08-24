import { url, request, hidden_loader, ManageArticle } from './settings.js'

function infinite_scroll_article_categories(i){
    const place_article = document.getElementById('place_article')
    const value_id = document.getElementById('see_categories').value
    if (value_id == "trends") {
      //pass
    } else if (value_id == "subscription") {
      const articles_subscribed = request(url + "api/articles/getarticlessubscribed" + "/" + i)
      articles_subscribed.then(data => {
        ManageArticle(data)
        
      })
    } else {
      const articles_categories = request(url + "api/articles/getarticlecategory/" + value_id + "/" + i)
      articles_categories.then(data => {
        ManageArticle(data)
        
      })
    }
  }

export {
    infinite_scroll_article_categories,
}