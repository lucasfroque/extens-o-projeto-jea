import pandas as pd
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('dados_jea.csv')


plt.figure(figsize=(8, 6))
sns.histplot(df['Idade'], bins=5, kde=True)
plt.title('Distribuição de Idades dos Usuários')
plt.xlabel('Idade')
plt.ylabel('Número de Usuários')
plt.show()

plt.figure(figsize=(8, 6))
sns.barplot(x='Nome', y='Membros na Família', data=df)
plt.title('Número de Membros na Família por Usuário')
plt.xlabel('Usuário')
plt.ylabel('Membros na Família')
plt.show()

plt.figure(figsize=(8, 6))
sns.countplot(x='Necessidades Básicas', data=df)
plt.title('Necessidades Básicas da Comunidade')
plt.xlabel('Necessidade')
plt.ylabel('Número de Usuários')
plt.show()
