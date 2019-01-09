# todo-list


# Requirements: #

1. App might be run on any web server which is congigured to server CGI (Apache with cgi module enabled)
1. Python3



**Main script is index.py. Apache or another web server shoud call it first**


## How To ##

1. Place all script in DocRoot
1. Run createdb.py from console (**python3 createdb.py**)
1. That's it



## Apache config example ##
```sh
<VirtualHost *:80>
ServerName  test.local


DocumentRoot  /home/vladimir/dev/tasklist
    ServerAdmin webmaster@localhost
AddDefaultCharset utf-8
    ErrorLog ${APACHE_LOG_DIR}/error.log
    CustomLog ${APACHE_LOG_DIR}/access.log combined
ScriptAlias /cgi-bin/ /home/vladimir/dev/tasklist/
<Directory "/home/vladimir/dev/tasklist/">
Require all granted
Options +Indexes
Options +ExecCGI
AllowOverride All
AddHandler cgi-script .cgi .py
</Directory>

</VirtualHost>
```


###How to enable module###

> a2enmod cgi

> service apache2 reload