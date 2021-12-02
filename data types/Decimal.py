#decimal ,python standard livery theke import korte hoy
from decimal import *
a=Decimal(3.4)
print(a)
print(a.quantize(Decimal('0.00')))#nirdisto sokhok output pete quantize funtion use hoy
b=Decimal(2.2)
print(a.quantize(Decimal('0.0')))
