const url = "http://127.0.0.1:8000/"

function create_loader(){
  const container_loader = document.createElement('div')
  container_loader.classList.add('loader')
  container_loader.id = "loader"

  return container_loader
}

function hidden_loader(){
  const loader = document.querySelectorAll("#loader")
  for (let i = 0; i < loader.length; i++) {
    loader[i].classList.add('hidden')
  }
  
  return loader
}

const insertPost = async function(data, url_request) {
  let response = await fetch(url_request, {
    method: 'POST',
    headers : {
      'Content-Type': 'application/json',
      'X-CSRFToken' : getCookie('csrftoken'),
    },
    body: JSON.stringify(data)
  })
  let responsedata = await response.json()
  if (response.ok) {
    return responsedata
  } else {
    console.log(response.status)
  }
}

const request = async function (url_request) {
  try {
      let test = 1
      let response = await fetch(url_request)
      if (response.ok) {
        let data = await response.json()

        return data
      } else {
        console.error('retour du serveur : ', response.status)
      }
    } catch (e) {
      console.log(e)

    }
}

function create_like(type_like, nbs_like, type_class){
    const container_simple_like = document.createElement('div')
    container_simple_like.classList.add("col-3", type_class)
    const i_like = document.createElement('i')
    i_like.classList.add("fas", type_like)
    container_simple_like.append(i_like)
    i_like.after(nbs_like)

    return container_simple_like

}

function event_like_article(like, pseudo, id_article){
  like.addEventListener('click', (e) => {
    const data = {
      "reaction" : like.id
    }
    const post_article = insertPost(data, url + "api/articles/postlikearticle/" + id_article + "/" + pseudo)
    post_article.then(data => {
      const elt_element = like.parentNode
      elt_element.firstChild.firstChild.nextSibling.nextSibling.textContent = data.nbs_likes[1]
      elt_element.firstChild.nextSibling.firstChild.nextSibling.nextSibling.textContent = data.nbs_likes[2]
      elt_element.firstChild.nextSibling.nextSibling.firstChild.nextSibling.nextSibling.textContent = data.nbs_likes[3]
      elt_element.firstChild.nextSibling.nextSibling.nextSibling.firstChild.nextSibling.nextSibling.textContent = data.nbs_likes[4]
    })
  })

  return like
}

function create_article(id_user, id_article, src_image, pseudo, date, title, content, nbs_love, nbs_like, nbs_dislike, nbs_fucklike){
    const container_section = document.createElement('section')
    container_section.classList.add("content_user_articles")

    const article_container = document.createElement("article")
    article_container.classList.add("post_user")
    container_section.append(article_container)

    const div_container = document.createElement("div")
    div_container.classList.add("row", "box_pseudo_date")
    article_container.append(div_container)

    const link_user = document.createElement('a')
    link_user.href = url + "user/account/" + id_user
    div_container.append(link_user)

    const img_user = document.createElement("img")
    img_user.src = "/static/assets/img/" + src_image
    img_user.classList.add("col-4", "image_user_article")
    img_user.alt = "image user"
    link_user.append(img_user)

    const container_pseudo_date = document.createElement("div")
    container_pseudo_date.classList.add("col-7")
    div_container.append(container_pseudo_date)

    const container_pseudo = document.createElement("div")
    container_pseudo.classList.add("pseudo_comments")
    container_pseudo.textContent = pseudo
    container_pseudo_date.append(container_pseudo)

    const container_date = document.createElement("div")
    container_date.classList.add("date_comments")
    container_date.textContent = date
    container_pseudo_date.append(container_date)

    const link_article = document.createElement('a')
    link_article.href = url + "articles/" + id_article
    article_container.append(link_article)

    const container_title = document.createElement("div")
    container_title.classList.add("title_post")
    container_title.textContent = title
    link_article.append(container_title)

    const container_post = document.createElement("div")
    container_post.classList.add("content_post")
    container_post.textContent = content
    article_container.append(container_post)

    const container_like = document.createElement("div")
    container_like.classList.add("row", "like_user")
    container_like.id = id_article
    article_container.append(container_like)

    let love_like = create_like("fa-heart", nbs_love, "love_like")
    love_like.id = 1
    love_like = event_like_article(love_like, pseudo, id_article)
    container_like.append(love_like)

    let like = create_like("fa-thumbs-up", nbs_like, "like")
    like.id = 2
    like = event_like_article(like, pseudo, id_article)
    container_like.append(like)
    
    let dislike = create_like("fa-thumbs-down", nbs_dislike, "dislike")
    dislike.id = 3
    dislike = event_like_article(dislike, pseudo, id_article)
    container_like.append(dislike)

    let fuck_like = create_like("fa-hand-middle-finger", nbs_fucklike, "fuck_like")
    fuck_like.id = 4
    fuck_like = event_like_article(fuck_like, pseudo, id_article)
    container_like.append(fuck_like)
   
    return container_section

}

function ManageArticle(data){
  for (let i = 0; i < data.length; i++){
    hidden_loader()
    const place_article = document.getElementById('place_article')
    place_article.append(create_article(
      data[i].info_user.id_user,
      data[i].id,
      data[i].info_user.photo,
      data[i].info_user.pseudo,
      data[i].date_article,
      data[i].title,
      data[i].content_article,
      data[i].nbs_likes[1] = (data[i].nbs_likes[1] === undefined) ? 0 : data[i].nbs_likes[1],
      data[i].nbs_likes[2] = (data[i].nbs_likes[2] === undefined) ? 0 : data[i].nbs_likes[2],
      data[i].nbs_likes[3] = (data[i].nbs_likes[3] === undefined) ? 0 : data[i].nbs_likes[3],
      data[i].nbs_likes[4] = (data[i].nbs_likes[4] === undefined) ? 0 : data[i].nbs_likes[4],
    ))
  }
}

function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== '') {
      const cookies = document.cookie.split(';');
      for (let i = 0; i < cookies.length; i++) {
          const cookie = cookies[i].trim();
          // Does this cookie string begin with the name we want?
          if (cookie.substring(0, name.length + 1) === (name + '=')) {
              cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
              break;
          }
      }
  }
  return cookieValue;
}

function infinite(item, action){
  let i = 1
  let observer = new IntersectionObserver(function (observables) {
    observables.forEach(function (observable) {
      if (observable.intersectionRatio > 0) {
        i++
        action(i)

      }
    })
  }, {
    threshold: [0] // 100% has to be visible
  })

  observer.observe(item)
  
}

export {
    infinite,
    ManageArticle,
    insertPost,
    hidden_loader,
    create_article,
    request,
    create_loader,
    url,
}