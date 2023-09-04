# import os
# def shutdown_PC():
#     os.system("shutdown /s /t 10")
# shutdown_PC()

import os

def shutdown():
    if os.name == 'posix':  # Linux/Unix
        os.system("shutdown -h now")
    elif os.name == 'nt':  # Windows
        os.system("shutdown /s /t 0")
    else:
        print("Sorry, unsupported operating system.")

if __name__ == "__main__":
    shutdown()
