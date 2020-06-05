# Test task
_author: vladisa88_
## With this simple django project you can upload images by url or choose it locally. Also you can resize images.

### To start:
`git clone https://github.com/vladisa88/image_test`

`cd image_test`

`pip3 install -r requirments.txt && python3 manage.py migrate && python3 manage.py runserver`

### How to deploy:
1) pip freeze or use Pipfile
1) Create Dockerfile for our proj
2) Set up database (Postgres or sometheng else)
4) Set up project static
4) Set up heroku app (for heroku deployment)
3) Create heroku.yaml file (for heroku deployment)
5) git push heroku master :)

### Solutions:
Мне кажется, что решение с ресайзом через html очень элегантно, буду очень рад услышать от Вас фидбэк по проекту, может быть, что-то доделать.