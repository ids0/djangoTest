def test(name):
    print(f'hello {name}')
    def testinner(x):
        print(x)

    PublicAPI = {'key':testinner}
    return PublicAPI

ivan = test

ivan['key'](x)
