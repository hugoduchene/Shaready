import { url, request, hidden_loader, ManageArticle } from './settings.js'


function infinite_scroll_article_user(i, id_user) {
    const articles_user = request(url + "api/articles/getarticleuser/"+ id_user + "/" + i)
    articles_user.then(data => {
        ManageArticle(data)
    }).catch((error) => {
      console.log(error)
    })
}

function infinite_articles_user(item, action, id_user){
    let i = 1
    let observer = new IntersectionObserver(function (observables) {
      observables.forEach(function (observable) {
        if (observable.intersectionRatio > 0) {
          i++
          action(i, id_user)
          
  
        }
      })
    }, {
      threshold: [0] // 100% has to be visible
    })
  
    observer.observe(item)
    
  }

export {
    infinite_articles_user,
    infinite_scroll_article_user,
}