import pandas.io.clipboard as cb
import argparse


def vstrans(x):
    if x < 16:
        x = x + 0XFE00
    else:
        x = x - 16 + 0xE0100
    return x


def hex_a(x, len_):
    y = hex(x)[2:]
    res = '0' * (len_ - len(y)) + y
    return res


def encoder(s):
    b = s.encode()
    c = [vstrans(i) for i in b]
    res = '😀'.encode('unicode_escape')  # unicode of 😀
    for cc in c:
        res = res + b'\\U' + bytes(hex_a(cc, 8), 'utf-8')
    print(res.decode('unicode_escape'))
    return res.decode('unicode_escape')


def encode(s, head='😀'):
    b = s.encode()
    c = [vstrans(i) for i in b]
    res = head.encode('unicode_escape')
    for cc in c:
        res = res + b'\\U' + bytes(hex_a(cc, 8), 'utf-8')
    #print(res.decode('unicode_escape'))
    return res.decode('unicode_escape')


def decode(s):
    b = s.encode('unicode_escape')
    secs = b.split(b'\\U')
    out = []
    for sec in secs:
        if len(sec) == 8:
            num = int(sec, 16)
            if 0 <= num - 0XFE00 < 16:
                out.append(num - 0XFE00)
            if 0 <= num - 0xE0100 < 256 - 16:
                out.append(num - 0xE0100 + 16)
    return bytes(out).decode()


def cbencode(head='😀'):
    s = cb.paste()
    e = encode(s, head=head)
    print(e)
    cb.copy(e)


def cbdecode():
    s = cb.paste()
    e = decode(s)
    print(e)
    cb.copy(e)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='none')
    parser.add_argument('--encode', '-e', action='store_true')
    parser.add_argument('--decode', '-d', action='store_true')
    parser.add_argument('--bunker', '-b', type=str, help='bunker text, default is 😀', default=r'😀')

    par = parser.parse_args()
    if par.encode:
        cbencode(head=par.bunker)
    elif par.decode:
        cbdecode()
