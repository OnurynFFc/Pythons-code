from time import gmtime, strftime
'''
n = int(input(print("qual sua idade?:")))
an = int('%y', gmtime()) - n
if an < n:
  d = an * (-1)
print("vc nasceu em", d,"A.C")
print("vc nasceu em", an,"d.c")
'''
strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
print(strftime)