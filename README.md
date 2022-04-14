# <div align="center">crypto-articles-api</div>
### DESCRIPTION

Aim of this project is to abandon API's from internet for project <a href="https://github.com/Aldmors/Exchange">Exchange</a> and generate own articles about cryptocurrencies in a way of scraping site (https://theconversation.com/uk/topics/cryptocurrency-8321) with Python, then making it available at Flask API.

### USED TECHNOLOGIES
<img src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=darkgreen"/> <img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white"/>

### HOW TO
First install dependencies
````
pip install -r requirements.txt
````
Change host/port in `/server.py` if needed
````
7   app = Flask(__name__)
8   cors = CORS(app)
9   app.config['CORS_HEADERS'] = 'Content-Type'
10  host = "127.0.0.1"                         <- here
11  port = 4000                                <- here
````
Export FLASK_APP
````
export FLASK_APP=server
````

Run <strong>ONE</strong> of those commands to start server
````
python server.py
````
````
flask run
````

On host adress you will get list of objects (max 20) => every with data about article and article formatted with basic HTML
````
GET => 127.0.0.1:4000/articles (host:port/articles)
[
  {
    "articleUrl":"Link to article",
    "author":"Name of the author",
    "content":"Article itself,formatted with HTML",
    "data":"Date of publication of the article",
    "description":"Short description of article",
    "iconUrl":"Link to small icon from the article",
    "imgUrl":"Link to big img from the article",
    "title":"Title of article"
  },
  {
    "articleUrl":"http://example.com",
    "author":"ArZi ArziPL",
    "content":"Lorem ipsum dolor sit amet, consectetur adipiscing elit. In ultricies mollis odio sit amet condimentum. Donec non metus sollicitudin, scelerisque nibh vitae, placerat leo. Pellentesque vel accumsan mauris. Suspendisse porta lacinia orci vel venenatis. Aliquam auctor eros enim, et ultrices erat luctus eu.",
    "data":"April 14, 2022",
    "description":"Example article from crypto-articles-api",
    "iconUrl":"http://example.com",
    "imgUrl":"http://example.com",
    "title":"How this API works and why it's cool"
  }
]

````
***

<div align="center">Hope you had a good time here. If you liked the project, leave a ⭐ and visit <a href="https://github.com/ArziPL">my profile</a> to send feedback, check other projects, or make something cool together</p></div> 
