from asyncio import sleep


class T:
    def __init__(self):
        self.result = 1
        sleep()

    def set_r(self,v):
        self.result=v

    def __iter__(self):
        yield self
        return self.result

    def __await__(self):
        yield self
        return self.result

def fun1():
    yield 1
    return 'fun1 ok'


def fun2():
    print('s')
    print('-----')
    yield from fun1()
    print('-----')
    yield from fun1()
    print('e')


async def fun3(t):
    k = await t
    while k:
        k = await t
        print('1:',k)
    return 'fun3 done'
if __name__ == '__main__':
    t=T()
    b = fun3(t)