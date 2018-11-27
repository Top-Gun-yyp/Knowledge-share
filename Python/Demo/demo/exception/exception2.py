import pdb
try:

    print('try...')
    s = 10
    if s>0:
        print(s)
    r = 10 / int('1')
    print('result:', r)
except ValueError as e:
    print('ValueError:', e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:', e)
finally:
    print('finally...')
print('END')
