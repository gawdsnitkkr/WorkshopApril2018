# WorkshopApril2018

## Setup

* Install common modules
```bash
pip install -r requirements.txt
```

* If using Windows, then also run:
```bash
pip install -r windows_requirements.txt
```
## Setting up virtual enviornment

### installing Prerequisites(UBUNTU)
```
$ sudo apt-get install python3 python3-pip virtualenvwrapper
```
### Creating Virtual Enviornment
    * move to the project directory *

```
$ virtualenv -p /usr/bin/python3 env
$ source env/bin/activate
$ pip install requirements.txt
```