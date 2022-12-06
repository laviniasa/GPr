def valida_string(s, mín, máx):
    tamanho = len(s)
    return mín <= tamanho <= máx


input(valida_string("", 1, 5))
