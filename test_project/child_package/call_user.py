# Try commenting out this line, run this py file again.
import auto_syspath3  # noqa: F401
from config import env
from utils import add, sub

if __name__ == '__main__':
    print(env.userName)
    print(env.token)
    print(add(1, 2))
    print(sub(3, 4))
