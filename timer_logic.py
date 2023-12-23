from time import localtime, strftime, time
from ui.tracker_windows import get_window

def get_date_formatted():
    what_time_is_it = localtime()
    date_with_format = strftime("%A %d, %B %Y", what_time_is_it)
    return date_with_format

def start_timer():
    return time()

def stop_timer():
    return time()
    
def main():
    start = start_timer()

    # This is a test for the timer
    while get_window():
        print("☑️")

    
    stop = stop_timer()
        
    # Measure time for each iteration
    elapsed_time = stop - start
    print(f"Time taken for write the correct name {elapsed_time} seconds.")
    
    return "Correct name written."

print(main())