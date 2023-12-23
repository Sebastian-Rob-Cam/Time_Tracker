import pygetwindow as gw

def get_window():
    try:
        while True:
            active_window = gw.getWindowsWithTitle(gw.getActiveWindow().title)

            if active_window:
                print(f"Active Window: {active_window[0].title}")
            else:
                return False
    except KeyboardInterrupt:
        print("Tracking stopped.")