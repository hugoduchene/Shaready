# Shaready <img src="https://travis-ci.com/hugoduchene/Shaready.svg?branch=master">
<img align="center" src="https://github.com/hugoduchene/Shaready/blob/dev/static/assets/img/logo_nav.svg"/>

Shaready is a social information network aiming to conquer the magnificent market of communication and knowledge.

<h1 id="future"> The future of Shaready</h1>

<ul>
  <li><a href="https://github.com/hugoduchene/Shaready/projects/2">V1 Shaready</a></li>
  <li><a href="https://github.com/hugoduchene/Shaready/projects/3">V2 Shaready</a></li>
  <li><a href="https://github.com/hugoduchene/Shaready/projects/4">V3 Shaready</a></li>
</ul>

# API docs

The api is divided into 4 distinct parts, there are :

<ul>
  <li><a href="#articles_api">/api/articles/</a></li>
  <li><a href="#comments_api">/api/comments/</a></li>
  <li><a href="#notification_api">/api/notification/</a></li>
  <li><a href="#user_api">/api/user/</a></li>
</ul>

<dl>
  <dt><h3 id="auth_api">Authentication of api's</h3></dt>
  <dd>- For some endpoints, the api requires a per-session verification to interact with the shaready database.</dd>
  <dd>- For the api to accept your post request, you have to take the "csrf-token" using the getCookie function, here is an example: <a href="https://docs.djangoproject.com/fr/3.1/ref/csrf/">https://docs.djangoproject.com/fr/3.1/ref/csrf/</a></dd>

  ```js
  const insertPost = async function(data, url_request) {
  let response = await fetch(url_request, {
    method: 'POST',
    headers : {
      'Content-Type': 'application/json',
      'X-CSRFToken' : getCookie('csrftoken'),
      'credentials' : 'same-origin',
    },
    body: JSON.stringify(data)
  })
  ```
  <dd>To request the endpoints that have permissions you must add in the header of your requests the cookies with "credentials".</dd>
  
  ```js
  fetch('https://example.com:1234/users', {
  credentials: 'include'
  })

  fetch('/users', {
  credentials: 'same-origin'
  })
  ```
  
</dl>

<dl>
  <dt><h3 id="articles_api">Api articles</h3></dt>
  <dd>This part of the api manages all the interactions that the system needs to read or create articles, all the endpoints available in this part of the api are below :</dd>
  
  <h5><dd>To get all the categories of the application</dd></h5>

```
Get : /api/articles/categories
```

  <h5><dd>To get all the articles in a category</dd></h5>
  
```
Get : /api/articles/getarticlecategory/<idCategory>/<idPage>
```

  <h5><dd>To get all the articles of a user</dd></h5>

```
Get : /api/articles/getarticleuser/<idUser>/<idPage>
```

  <h5><dd>To take all the items of your subscriptions, you must <a href="#auth_api">authenticate</a> yourself to access this endpoint.</dd></h5>
  
```
Get : /api/articles/getarticlessubscribed/<int:idPage>
````

  <h5><dd>To get all the articles of the trends</dd><h5>
  
```
Get : /api/articles/gettrends/
```

  <h5><dd>To create an article, you must <a href="#auth_api">authenticate</a> yourself to access this endpoint.</dd><h5>
  
```
Post : /api/articles/postcreatearticle

const data = {
      "title" : <your tilte>,
      "content_article" : <your content>,
      "id_category" : <id's category>
    }
```

<h5><dd>To create a like on an article, you must <a href="#auth_api">authenticate</a> yourself to access this endpoint.</dd><h5>
  
```
Post : /api/articles/getarticleuser/<idUser>

const data = {
    "reaction" : 1 = Goldlike, 2 = Like, 3 = Dislike
  }
```
</dl>

<dl>
  <dt><h3 id="comments_api">Api comments</h3></dt>
  <dd>This part of the api manages all the interactions that the system needs to read or create comments, all the endpoints available in this part of the api are below :</dd>
  
  <h5><dd>To get all the comments of an article</dd><h5>
  
```
Get : /api/comments/getall/<idArticle>/<idPage>
```

<h5><dd>To create a comment on an article, you must <a href="#auth_api">authenticate</a> yourself to access this endpoint.</dd><h5>
  
```
Post : /api/comments/createcomment/<idArticle>/<pseudoUser>

const data = { "content_comment" : content_comment }
```

<h5><dd>To create a like on a comment, you must <a href="#auth_api">authenticate</a> yourself to access this endpoint.</dd><h5>
  
```
Post : /api/comments/createlike/<idComment>/<pseudoUser>

const data = { "content_comment" : content_comment }
```
</dl>
  
</dl>

<dl>
  <dt><h3 id="notification_api">Api notification</h3></dt>
  <dd>This part of the api manages all the interactions that the system needs to read notifications, all the endpoints available in this part of the api are below :</dd>
  
  <h5><dd>To get the number of unread notifications, you must <a href="#auth_api">authenticate</a> yourself to access this endpoint.</dd><h5>
  
```
Get : /api/notification/getnbsnotifications
```

<h5><dd>To get all your notifications, you must <a href="#auth_api">authenticate</a> yourself to access this endpoint.</dd><h5>
  
```
Get : /api/notification/getallnotification/<idPage>
```

<h5><dd>To change the status of your notifications from unread to read, you must <a href="#auth_api">authenticate</a> yourself to access this endpoint.</dd><h5>
  
```
Post : /api/notification/postmanagenotification

const data = {}
```
</dl>

<dl>
  <dt><h3 id="user_api">Api user</h3></dt>
  <dd>This part of the api manages all the interactions that the system needs to manage user system, all the endpoints available in this part of the api are below :</dd>
  
  <h5><dd>To find users</dd><h5>
  
```
Get : /api/user/getresearchuser/<userResearch>
```

  <h5><dd>To get all the information of a user</dd><h5>
  
```
Get : /api/user/getallinfouser/<idUser>
```

  <h5><dd>To search the list of your subscriptions, you must <a href="#auth_api">authenticate</a> yourself to access this endpoint.</dd><h5>
  
```
Get : /api/user/alreadysubscribe/<idReceiving>
```

<h5><dd>To subscribe to a user, you must <a href="#auth_api">authenticate</a> yourself to access this endpoint.</dd><h5>
  
```
Post : /api/user/postsubscription/<pseudoUser>

const data = {
        "id_receiving" : <id_user>
    }
```