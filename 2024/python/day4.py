class PrettyLogger:
    i = 0
    reset = '\033[0m'

    def colors():
        prefix = '\033[38;5;'
        numbers = [1,2,3,4,5,6,196,154,228,27,]
        return [f"{prefix}{number}m" for number in numbers]
    
    def pretty(text, color):
        print(f"{color}{text}{PrettyLogger.reset}")

    def log(text):
        greens = PrettyLogger.colors()
        PrettyLogger.pretty(text, greens[PrettyLogger.i % len(greens)])
        PrettyLogger.i = PrettyLogger.i+1

log = PrettyLogger.log

for i in range(35):
    log("hello")