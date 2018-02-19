# #!/usr/bin/python
#
# def main():
#     print "I am in main"
#
# main()

import webbrowser
import time

my_urls = ['https://www.facebook.com','https://www.youtube.com']

def open_urls(urls):
    for url in urls:
        webbrowser.open_new_tab(url)


def main():
    webbrowser.open("https://www.google.com", new=2, autoraise=True)
    time.sleep(10)
    open_urls(my_urls)

if __name__ == "__main__":
    main()