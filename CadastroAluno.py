turma = []
continuar = 'S'

while continuar == 'S':
    aluno = {}
    aluno['nome'] = input('Nome do aluno: ')
    prova = float(input('Digite a nota da prova: ').replace(',', '.')) # tratamento da retirada da virgula substituida por ponto.
    teste = float(input('Digite a nota do teste: ').replace(',', '.'))
    nota_final = prova + teste
    aluno['nota_final'] = nota_final

    if aluno['nota_final'] >= 7.0:
        aluno['situacao'] = 'Aprovado'
    else:
        aluno['situacao'] = 'Reprovado'

    turma.append(aluno)
    #controle de continuidade de WHILE e conversão de 
    #tratamento de retirada de espaços acidentais.srip()
    #.upper(): Converte a letra digitada para maiúscula, para aceitar tanto 's' minusculo como 'S' maiusculo!
    continuar = input('Deseja continuar? [S/N] ').strip().upper()

print('\n--- RELATÓRIO DA TURMA ---')
for alunos in turma:
    #Mostra a média formatada em 2 casas decimais (.2f)
    print(f"Aluno: {alunos['nome']} | Nota final: {alunos['nota_final']:.2f} | Situação: {alunos['situacao']}")