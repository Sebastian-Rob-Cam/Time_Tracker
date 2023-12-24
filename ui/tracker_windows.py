import pygetwindow as gw

def get_window():
    try:
        active_window = gw.getActiveWindow()

        while True:
            tracking = gw.getActiveWindow()

            if active_window != tracking:
                return False, active_window.title
    except KeyboardInterrupt:
        print("Tracking stopped.")