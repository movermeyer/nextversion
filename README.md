# nextversion
A Python package to increments module verision numbers.

```python
from nextversion import nextversion
nextversion('1.0a2')   # => '1.0a3'
nextversion('v1.0a2')  # => '1.0a3'  (normalized to compatible version with PEP 386)
nextversion('foo.0.3')  # => None    (impossible to normalize)
```

If original version number does not match [PEP 386](//www.python.org/dev/peps/pep-0386/),

1. Next version compatible with [PEP 386](//www.python.org/dev/peps/pep-0386/) is returned if possible,
1. If impossible, `None` is returned.

## Install
### Install from PyPI
```bash
$ pip install nextversion
```

### Install from Github repo
```bash
$ git clone https://github.com/laysakura/nextversion.git
$ cd nextversion
$ ./setup.py install
```

## See also
- [PEP 386](//www.python.org/dev/peps/pep-0386/)
- [Version::Next](//search.cpan.org/perldoc?Version::Next)

## Author
Sho Nakatani <lay.sakura@gmail.com>, a.k.a. @laysakura
