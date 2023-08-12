### 1.使用方法:

1. 安装

```bash
git clone https://github.com/Alan3344/auto_syspath3.git
cd auto_syspath3
python setup.py install
```
或者
```bash
pip install git+https://github.com/Alan3344/auto_syspath3.git
```

2. 使用

不用再在每个文档的开头加上这两行了，因为这会招来烦人的`Flake8`提示`Flake8(E402)`

```python
import sys
sys.path.extend(['./', '../'])
import selfpkg1
import selfpkg2
```

现在只需要直接在自定义包前面加上这一行就可以了,如果你不喜欢`Flake8`提示未使用,可以在后面加上 `# noqa`

- 根据`python`导入模块的特性,这个`__init__.py`文件会自动执行,所以也不需要再写`add_path()`函数了

```python
import os
import auto_syspath3 # noqa
import selfpkg1
import selfpkg2
```

### 2.拒绝`Flake8`提示检测: module level import not at top of file Flake8(E402)

- 原因: 为了让这个文件可以单独运行, 所以把`import`放到了函数里面

### 3.编写这个模块的原因:

我使用`VSCode`编写`python`代码的,但是`VSCode`导入是正确提示,但是`Flake8`提示错误
可能使用`PyCharm`不会有这个问题,但是他需要设置为`source root`,我不喜欢这样

1. 这个函数原本的样子,每次引用,都得复制一遍
2. 其次这个文件主要是放在`site-packages`目录,打包后发给别人使用会缺少这个文件
3. 我在`pypi`上有找到类似的包,但是未能达到我的预期,所以自己写了一个
4. 重要的是,使用这个包后,自定义的包在任何一个终端都可以使用,不需要设置`source root`

```python
def add_path(path=__file__, deep=0):
    """Add a path to the sys.path if it is not already there."""
    paths = []
    path = os.path.abspath(path)
    dirname = os.path.dirname(path)
    for i in range(deep):
        dirname = os.path.dirname(dirname)
    d(f'dirname: {dirname}')
    for p in os.walk(dirname):
        p0 = p[0].replace(dirname, '')
        if p0.startswith('/.') or '__pycache__' in p0:
            continue
        elif not p[0] in sys.path:
            paths.append(p[0])
            sys.path.insert(0, p[0])
            d(f'add path: {p[0]}')
    return paths
```
