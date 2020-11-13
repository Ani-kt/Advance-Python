"""
When we want a specific module to be in first place always then we will use __name__ variable.
Refer file name-special_variable__name__1
Date-9th Nov 2020
"""
print("abc:")
print("def")
def info():
    print("Hello:"+__name__)
    print("World"+__name__)
def sub():
    print("hi")   

def main():
    info()
    sub()
if __name__=="__main__":
    main()        