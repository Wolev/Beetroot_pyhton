import time


spinner_items = "\\|/—"


for _ in range(50):
    for item in spinner_items:
        print(item, end = "", flush=True)
        time.sleep(0.2)
        print('\b', end="", flush=True)

