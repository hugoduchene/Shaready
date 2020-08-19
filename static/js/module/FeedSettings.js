import { url, request, create_loader, hidden_loader, ManageArticle } from './settings.js'

function create_categories(name_place ,id_category, name_category) {
    const place_categories = document.getElementById(name_place)
    const option = document.createElement('option')
    option.value = id_category
    option.id = id_category
    option.textContent = name_category
    place_categories.append(option)

    return place_categories
}

function infinite_scroll(i){
    const place_article = document.getElementById('place_article')
    const value_id = document.getElementById('see_categories').value
    if (value_id == "trends") {
      //pass
    } else if (value_id == "subscription") {
      const articles_subscribed = request(url + "api/articles/getarticlessubscribed" + "/" + i)
      articles_subscribed.then(data => {
        ManageArticle(data)
        hidden_loader()
      })
    } else {
      const articles_categories = request(url + "api/articles/getarticlecategory/" + value_id + "/" + i)
      articles_categories.then(data => {
        ManageArticle(data)
        hidden_loader()
      })
    }
  }

export {
    create_categories,
    infinite_scroll,
}