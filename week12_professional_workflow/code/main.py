## lazy import

def process_data(data):
    import time
    time.sleep(2)
    return data * 2

print(process_data(10))