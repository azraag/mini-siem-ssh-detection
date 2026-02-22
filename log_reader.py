import time

def follow(file):
    file.seek(0, 2)  # dosyanın sonuna git

    while True:
        line = file.readline()
        if not line:
            time.sleep(1)
            continue
        yield line
