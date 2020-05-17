# test for function notation
def helloworld(txt:dict(type=str,help='input text')):
    print(txt)


if __name__ == '__main__' :
    helloworld('hawken')
    print(helloworld.__annotations__)