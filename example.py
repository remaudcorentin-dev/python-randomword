
from randomword import RandomWord

rw = RandomWord()

for i in range(0, 5):
    result = rw.get()
    print("# %s : %s" % (result['word'], result['definition']))
