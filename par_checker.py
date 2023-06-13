import sys

from stack import Stack


def par_checker():
    s = Stack()
    input_string = input('')

    for c in input_string:
        try:
            if c == '(':
                s.push(c)
            elif c == ')':
                s.pop()
        except Exception:
            print('有未匹配的\')\'')
            sys.exit()
    if s.is_empty():
        print('匹配')
    else:
        print('仍有未匹配的\'(\'')


if __name__ == '__main__':
    par_checker()
