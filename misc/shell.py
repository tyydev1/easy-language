import easy
import time

last_interrupt_time = 0
INTERRUPT_TIMEOUT = 1  # seconds

print("""\n
    _________   _______  __
   / ____/   | / ___/\ \/ /
  / __/ / /| | \__ \  \  / 
 / /___/ ___ |___/ /  / /  
/_____/_/  |_/____/  /_/   \n
""")

print("Easy 1.0.0 Universal Version - Initial release")
print("Welcome to Easy! This is the first published version of the Easy language.")

while True:
    try:
        text = input('>>> ').strip()
        if text == "": continue
        result, error = easy.run('<stdin>', text)

        if error is not None:
            print(error.as_string())
        elif result is not None:
            if isinstance(result, easy.Quit):
                print("Goodbye!")
                break
            if hasattr(result, 'elements'):
                if len(result.elements) == 1:
                    print(repr(result.elements[0]))
                else:
                    print(repr(result))
            else:
                print(repr(result))
    except KeyboardInterrupt:
        current_time = time.time()
        if current_time - last_interrupt_time < INTERRUPT_TIMEOUT:
            print("\nGoodbye!")
            break
        last_interrupt_time = current_time
        print("\nUse 'quit' or press Ctrl+C again within 1 second to exit")
    except EOFError:
        break