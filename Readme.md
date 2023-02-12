# Space Telegram #

Download photo from NASA nad post in Telegram channel with fixed frequence.

### How to install ###

Python3 should be already installed. Then use pip (or pip3, if there is a conflict with Python2) to install dependencies:

```python
pip install -r requirements.txt
```

U should put in .env correct infomation

``` NASA_API_KEY - Ur Nasa Api Key ```
``` SLEEP_TIMER - Period which u use for send_photo ```
``` TELEGRAM_TOKEN - Ur Telegram Token ```
``` CHAT_ID - ID of chat where u want to post pictures```

### How to use ###

Download EPIC:

```python
python fetch_epic.py
```

Download SpaceX:

```python
python fetch_spacex_images.py --id 5eb87d47ffd86e000604b38a
```
Module will download images of launch with id '5eb87d47ffd86e000604b38a'

Download APOD:

```python
python fetch_planetary.py --start 2023-02-05
```

Module will download images of APOD from '2023-02-05' till current date.

```python
python telebot.py
```

Module will post random images in telegram channel every 4 hours.
U can change period by changing SLEEP_TIMER in .env

```python
python send_photo.py --Image planetary_1.jpg
```

Module will post planetary_1.jpg in telegram channel.

### Project Goals ###
The code is written for educational purposes on online-course for web-developers dvmn.org.
