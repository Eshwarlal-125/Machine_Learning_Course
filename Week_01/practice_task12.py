# 12. Write a function build_profile(name, **kwargs) that accepts arbitrary keyword arguments and prints them as key-value pairs.
def build_profile(name,**kwargs):
    print(name)
    for key,value in kwargs.items():
        print(key,value)

build_profile("Ali",age=20,city="Lahore",course="ML")