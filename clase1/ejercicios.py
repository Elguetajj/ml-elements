print("Hello World!!")


list = [1,2,3,4,5]

def squares(plist:list):
    return [x*x for x in list]


def squares2(plist):
    return [*map(lambda x: x**2, plist)]


def gen_transformer(transformation):
    def transformer(plist):
        return [transformation(i) for i in plist]
    return transformer

square3 = (gen_transformer(lambda i: i**2))

def gen_transform(transformation):
    return lambda plist: [*map(transformation,plist)]

cube = gen_transform(lambda i: i**3)

print(squares(list))

print(squares2(list))

print(square3(list))

print(cube(list))