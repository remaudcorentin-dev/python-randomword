# python-randomword

##### v1.0.3

Simple API python to get random word with definition (offline usage)

### Installation

`pip install python-randomword`


### Usage

```python

from randomword import RandomWord

rw = RandomWord()

for i in range(0, 5):
    result = rw.get()
    print("# %s : %s" % (result['word'], result['definition']))

```

or simply :

```python
>>> from randomword import RandomWord
>>> print( RandomWord() )
# sluggard : lazy slow-moving person
```

