# novnc-proxy-django
a simple novnc-django demo

### requirements

- django
- websockify

### How to use

- chdir /path/to/novnc-proxy-django
- python manage.py migrate
- python manage.py createsuperuser
- python manage.py runserver

- websockify 127.0.0.1:6080 --target-config=/path/to/config_path/vnc_tokens

### More Details
[novnc远程控制的简单实现](http://blog.missuor.com/blogs/1132/detail)

