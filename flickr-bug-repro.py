#!/usr/bin/python3

import urllib.request

URL = "https://farm9.staticflickr.com/8174/7912860138_2fc6744d84_q.jpg"

def save_image(image, filename):
    fp = open(filename, "wb")
    fp.write(image)
    fp.close()

def fetch_image(user_agent):
    headers = { "User-Agent": user_agent }
    request = urllib.request.Request(url=URL, headers=headers)
    f = urllib.request.urlopen(request)
    image = f.read()
    print("%d bytes in image when U-A is %s" % (len(image), user_agent))
    # uncomment to save the images
    # save_image(image, "%s.jpg" % user_agent.replace("/", "_"))
    
fetch_image("Python-urllib/3.4")
fetch_image("Python-not-urllib/3.4")
