from time import localtime, strftime, time

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

    attempts = 3

    # This is a test for the timer
    while attempts > 0:
        name = input("Write my name:\n ")

        if name != "Sebastian":
            attempts = attempts - 1
        else:
            break

    
    stop = stop_timer()
        
    # Measure time for each iteration
    elapsed_time = stop - start
    print(f"Time taken for write the correct name {elapsed_time} seconds.")
    
    return "Correct name written."

print(main())