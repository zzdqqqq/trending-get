# trending-get

### Motivation
Automatically watching top10 trending articles.

### Configuration
Download trending-get.py.

Download chrome driver from [[here](https://chromedriver.chromium.org/downloads)].

Put chromedriver file and trending-get.py in same directory.

In your bash:
```bash
cd [to the folder contains trending-get.py]
virtualenv env --python=python3
source ./env/bin/activate
pip install -r requirements.txt

```

### Usage
In your bash:
```bash
python3 trending-get.py ["github username"] ["github password"]
```
Wait a couple seconds, you will get the results.

### Help
```bash
python3 trending-get.py -h
```
```bash
usage: trending-get.py [-h] username password

Trending-get Tool

positional arguments:
  username
  password

```