# Renew letsencrypt certificates on a machine

### Installing certbot

```
sudo apt-get update
sudo apt-get install software-properties-common
sudo add-apt-repository -y ppa:certbot/certbot
sudo apt-get update
sudo apt-get install -y python-certbot-nginx 
```

### Renewing the certificates

First stop nginx. If it is running from Docker, stop it with
``docker stop NAME`` where ``NAME`` is the name of the container,
certainly something like ``****_nginx_1``, you can get all container
names with ``docker ps``.

Then get new certificates from Letsencrypt with ``certbot renew``, which
requires [``certbot`` installed](https://certbot.eff.org/lets-encrypt/ubuntuxenial-nginx).

It will tell you that the new certificates have been downloaded in
``/etc/letsencrypt/...``. If your nginx configuration (see nginx.conf) expects
another folder, ``cp`` it at the right place.

```
cp /etc/letsencrypt/live/design.emmadb.genomefoundry.org/*.pem /cert/
```

Don't forget to restart your nginx:

```docker start *****_nginx_1```


