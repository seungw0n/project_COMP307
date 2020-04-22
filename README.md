# django-marketplace
A basic marketplace web app to learn Django.
To run this website on django, you need to have a version on python of at least 3.6. 
In the setting.py, you need to change the MEDIA_ROOT to you own computer directory.

You need install widget_tweaks :
- pip install django-widget-tweaks

You need to install channels and redis to run this app. 
On mac you can install it using:
- brew install openssl
- python3 –m pip install -U channels
- brew install redis
- python3 -m pip install channels_redis
- brew services start redis

We also used stripe, you need to download it then:
- pip3 install stripe




