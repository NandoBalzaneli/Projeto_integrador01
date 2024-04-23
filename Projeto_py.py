from tabulate import tabulate

print('PROGRAMA PARA CADASTRAR PRODUTOS, CALCULAR PREÇO DE VENDA E CLASSIFICAR LUCRO')

produto = input('Qual produto deseja cadastrar: ')
ca = float(input('Digite o custo do produto: '))
cf = float(input('Digite o custo fixo do produto: '))
cv = float(input('Digite o valor da comissão de vendas: '))
iv = float(input('Digite o valor dos impostos (sobre a venda) do produto: '))
ml = float(input('Digite a margem de lucro do produto: '))

pv = ca / (1 - ((cf + cv + iv + ml) / 100))


rc = (pv - ca)
oc = ((cf * pv) / 100) + ((cv * pv) / 100) + ((iv * pv) / 100)
rt = (rc - oc)


lucro_pct = (pv - ca - (cf + cv + iv)) / pv * 100

if lucro_pct >= 50:
    classificacao = 'Alto'
elif lucro_pct >= 20:
    classificacao = 'Médio'
elif lucro_pct >= 0:
    classificacao = 'Equilíbrio'
elif lucro_pct > -20:
    classificacao = 'Baixo'
else:
    classificacao = 'Prejuízo'

lista_desc = [
    ['Descrição', 'Valor', '%'],
    ['Produto', produto, ''],
    ['A. Preço de venda', pv, '100%'],
    ['B. Custo de Aquisição (Fornecedor)', ca, (ca / pv) * 100],
    ['C. Receita Bruta', pv - ca, ((pv - ca) / pv) * 100],
    ['D. Custo Fixo/Administrativo', (cf * pv) / 100, cf],
    ['E. Comissão de Vendas', (cv * pv) / 100, cv],
    ['F. Impostos', (iv * pv) / 100, iv],
    ['G. Outros Custos', oc, (oc / pv) * 100],
    ['H. Rentabilidade', rt, (rt / pv) * 100],
    ['I. Classificação de Lucro', classificacao, '']
]


print()

print(tabulate(lista_desc, headers='firstrow'))

print()
