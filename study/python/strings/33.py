# 33. Leia uma cadeia de caracteres no formato “DD/MM/AAAA” e copie o dia, mes e ano para
# 3 variaveis inteiras. Antes disso, verifique se as barras estao no lugar certo, e se DD, MM
# e AAAA sao numericos.


import re

result = "Data 01.02.2019, outra data 20.11.2018, data 15.03.1980"

r = re.compile(r'\d{2}\.\d{2}\.\d{4}')
print(r.findall(result))