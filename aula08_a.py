#import math
from math import sqrt
num = int(input('Digite um número: '))
#raiz = math.sqrt(num) #caso utilize import math
raiz = sqrt(num) # não é preciso utilizar a referância math._ quando aplico forma from math import _
print('A raiz quadrada de {} é {:.2f}.'.format(num, raiz))
