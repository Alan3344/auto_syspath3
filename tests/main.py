from config import env
from utils import add, sub


def main():
    print(env.userName)
    print(env.token)
    print(add(1, 2))
    print(sub(3, 4))


if __name__ == '__main__':
    print('call_user.py: ', __file__)
    main()
