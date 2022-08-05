import time

import webview


RUN_N = 1


def window_loaded():
    global RUN_N
    time.sleep(3)
    RUN_N += 1

    for window in webview.windows:
        window.destroy()


def run_window():
    webview.create_window('Woah dude!', html='<h1>Woah dude!<h1>')
    webview.start(window_loaded)


def main():
    run_window()

    run_window()


if __name__ == '__main__':
    main()
