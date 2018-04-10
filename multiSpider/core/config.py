from multiprocessing.managers import ListProxy, DictProxy, ValueProxy

managerConfig = {
    'address': ('', 8001),
    'authkey': 'asd'.encode()
}

managerAction=[
    {
        'typeid':'getUrl',
        'proxytype':ValueProxy,
    }
]


