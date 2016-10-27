# raspberryPi

Let's see if can build a weather station on the Pi.


Download the source code of the project with git:
```bash
git clone <repo url>
cd raspberryPi/www

Then install the  virtualenv:

```bash
sudo pip install virtualenv
source env/bin activate

Then install the required packages, see the list below:

```bash
sudo pip install flask
sudo pip install gevent
sudo pip install uwsgi
sudo pip install greenlet
sudo pip install geventwebsocket 
sudo pip install gevent-websocket