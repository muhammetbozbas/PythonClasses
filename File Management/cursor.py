f = open("msg.txt")

print(f.read())


# >>> f = open("msg.txt")
# >>> f.read()
# 'first line\nsecond line\nthird line\nfourth line\nfifth line\n'
# >>> f.read()
# ''
# >>> f.seek(0)
# 0
# >>> f.read()
# 'first line\nsecond line\nthird line\nfourth line\nfifth line\n'
# >>> f.readline()
# ''
# >>> f.seek(0)
# 0
# >>> f.readline()
# 'first line\n'
# >>> f.readline()
# 'second line\n'
# >>> f.readline()
# 'third line\n'
# >>> f.seek(0)
# 0
# >>> f.readlines()
# ['first line\n', 'second line\n', 'third line\n', 'fourth line\n', 'fifth line\n']
# >>> f.seek(0)
# 0
# >>> lines = f.readlines()
# >>> lines
# ['first line\n', 'second line\n', 'third line\n', 'fourth line\n', 'fifth line\n']
# >>> lines[0]
# 'first line\n'
# >>> lines[2]
# 'third line\n'
# >>> f.closed   ==> "dosya kapalı mı?"
# False
# >>> f.close()  ===> "dosyayı kapat!"
# >>> f.closed
# True
# >>> f.seek(0) ===> kapalı dosyada işlem yapamazsın.
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#     f.seek(0)
#     ~~~~~~^^^
# ValueError: I/O operation on closed file.
# >>> 