# Fac¸a um programa para ler uma tabela contendo os nomes dos alunos de uma turma de
# 5 alunos. O programa deve solicitar ao usuario os nomes do aluno, sempre perguntando ´
# se ele deseja inserir mais um nome na lista. Uma vez lidos todos os alunos, o usuario ´
# ira indicar um nome que ele deseja verificar se est ´ a presente na lista, onde o programa ´
# deve procurar pelo nome (ou parte deste nome) e se encontrar deve exibir na tela o nome
# completo e o ´ındice do vetor onde esta guardado este nome.

todos_nomes = []
a = 0 
while a == 0 :
    alunos = input("digite um nome: ")
    if alunos == 'x':
        break
    else:
        todos_nomes.append(alunos)
print(todos_nomes)
new_name = input('digite um nome')
for nome in todos_nomes:
    if nome == new_name:
        print(new_name)
    else:
        print('o nome não está na lista')

