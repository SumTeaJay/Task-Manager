import time
from rich.console import Console
from rich.theme import Theme

def type_text(text, delay=0.03):
    custom_theme = Theme({"repr.number": "#62a874"})
    bold_concole = Console(style="bold", theme=custom_theme)
    for symbol in text:
        bold_concole.print(symbol, end="")
        time.sleep(delay)
    time.sleep(delay * 10)
    print()