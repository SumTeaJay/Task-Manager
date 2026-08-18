import time

def type_text(text, delay=0.03):
    for symbol in text:
        print(symbol, end="", flush=True)
        time.sleep(delay)
    time.sleep(delay * 10)
    print()