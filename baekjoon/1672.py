n = int(input())
gene = input()

gene_list = ['A', 'G', 'C', 'T']
new_gene = []
for g in gene:
    new_gene.append(gene_list.index(g))
change = [[0, 2, 0, 1], [2, 1, 3, 0], [0, 3, 2, 1], [1, 0, 1, 3]]

while len(new_gene) > 1:
    a = change[new_gene[-2]][new_gene[-1]]
    new_gene.pop(-1)
    new_gene.pop(-1)
    new_gene.append(a)
    
print(gene_list[a])