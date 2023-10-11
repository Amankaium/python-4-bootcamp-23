def print_info(**kwargs):
    for key in kwargs:
        print(key, kwargs[key])

profile = {
    'name': "Kaium",
    "code": "python"
}

# print_info(name="Kaium", code="python")

def universal_function(*args, **kwargs):
    print(args)
    print(kwargs)

universal_function(4, 7)
universal_function(9, n=100000)
