
print("="*35)
# IMPORTAÇÕES BIBLIOTECAS
# 
import os                         # carrega a biblioteca nativa, permitindo interação com o sistema operacional.
import pandas as pd               # leitura do CSV e manipulação dos dados
from pathlib import Path          # construção do caminho dos arquivos 
import seaborn as sns             # visualização estatística para EDA
import matplotlib.pyplot as plt   # necessária para exibir/salvar os gráficos quando se usa o seaborn
import sweetviz as sv             # gera relatórios interativos em HTML com gráficos e estatísticas


print("="*50)
print("PROJETO AVALIATIVO FINAL — MÓDULO 1 — SEMANA 13")
print("Disciplina : Visualização de Dados e Business Intelligence")
print("SENAI/SC – Lab 365 – Turma: T1")
print("Aluno: Cláudia Maria Duarte Ramos")
print("Data final: 20/07/2026")
print("Base de dados sugerida: Human Resources (HR) disponível em: https://freesql.com/") 



print("="*35)
print("CAMINHOS DOS ARQUIVOS")
# Definição dos arquivos de entrada e saída, organização e estrutura do projeto 

# QUERY 01
ARQUIVO_ENTRADA_Q1 = Path(
    r"C:\Projeto_Final\Queries\query_01.csv"
)

ARQUIVO_Q1_OUTLIERS = Path(
    r"C:\Projeto_Final\dados\clean\query_01_outliers.csv"
)

ARQUIVO_Q1_SEM_OUTLIERS = Path(
    r"C:\Projeto_Final\dados\clean\query_01_sem_outliers.csv"
)

# QUERY 02
ARQUIVO_ENTRADA_Q2 = Path(
    r"C:\Projeto_Final\Queries\query_02.csv"
)

ARQUIVO_Q2_OUTLIERS = Path(
    r"C:\Projeto_Final\dados\clean\query_02_outliers.csv"
)

ARQUIVO_Q2_SEM_OUTLIERS = Path(
    r"C:\Projeto_Final\dados\clean\query_02_sem_outliers.csv"
)

# Cria automaticamente a pasta caso não exista
ARQUIVO_Q1_OUTLIERS.parent.mkdir(parents=True, exist_ok=True)
ARQUIVO_Q2_OUTLIERS.parent.mkdir(parents=True, exist_ok=True)

print("="*35)
print("LEITURA DO ARQUIVO CSV - QUERY_01")
# Importação das consultas SQL (Query_01 e Query_02) para df do Pandas. 

query_01 = pd.read_csv(
    ARQUIVO_ENTRADA_Q1,
    sep=",",
    encoding="utf-8-sig",
    quotechar='"'
)

print("Colunas QUERY_01:", query_01.columns.tolist())
print(query_01.head())

print("="*35)
print("LEITURA DO ARQUIVO CSV - QUERY_02")

query_02 = pd.read_csv(
    ARQUIVO_ENTRADA_Q2,
    sep=",",
    encoding="utf-8-sig",
    quotechar='"'
)

print("Colunas QUERY_02:", query_02.columns.tolist())
print(query_02.head())

print("="*35)
print("PADRONIZAÇÃO DAS COLUNAS")
# Uniformização dos nomes das colunas, removendo espaços e convertendo para letras minúsculas.
# Evita inconsistências durante as análises. 

query_01.columns = (
    query_01.columns
        .str.strip()
        .str.lower()
)
print("Colunas padronizadas:", query_01.columns.tolist())


query_02.columns = (
    query_02.columns
        .str.strip()
        .str.lower()
)
print("\nColunas padronizadas:", query_02.columns.tolist())


print("="*35)
print("DIAGNÓSTICO INICIAL — INTEGRIDADE DOS DADOS")
# Avalia a qualidade dos dados (estrutura, tipos de dados, dimensões, valores ausentes, duplicidades)

print("Dimensões QUERY_01 (linhas, colunas):", query_01.shape)
print("Dimensões QUERY_02 (linhas, colunas):", query_02.shape)

print("\nTipos de dado QUERY_01:")
print(query_01.dtypes)


print("\nTipos de dado QUERY_02:")
print(query_02.dtypes)


print("\nValores ausentes por coluna: QUERY_01")
print(query_01.isnull().sum())


print("\nValores ausentes por coluna: QUERY_02")
print(query_02.isnull().sum())


print("\nRegistros duplicados: QUERY_01", query_01.duplicated().sum())
print("\nRegistros duplicados: QUERY_02", query_02.duplicated().sum())


print("\n5 primeiras linhas: QUERY_01")
print(query_01.head(5))

print("\n5 primeiras linhas: QUERY_02")
print(query_02.head(5))



print("="*35)
print("ANÁLISE EXPLORATÓRIA AUTOMATIZADA — SWEETVIZ QUERY_01 e QUERY_02")
# Geração de relatório automatizado com estatísticas descritivas,
#  distribuição das variáveis e diagnóstico da qualidade dos dados.

relatorio = sv.analyze(query_01)
relatorio.show_html(r"C:\Projeto_Final\dados\clean\relatorio_query_01.html")
print(">>> SWEETVIZ <<<")

relatorio = sv.analyze(query_02)
relatorio.show_html(r"C:\Projeto_Final\dados\clean\relatorio_query_02.html")
print(">>> SWEETVIZ <<<")


print("="*35)
print("EDA — 1. FUNCIONÁRIOS POR DEPARTAMENTO - QUERY_02")
# Apresenta a distribuição/concentração dos colaboradores por departamento. 

func_por_departamento = (
    query_02.groupby("departamento")["funcionario"]
    .count()
    .sort_values(ascending=False)
)
print(func_por_departamento)



print("="*35)
print("EDA — 2. DEPARTAMENTO COM MAIOR MÉDIA SALARIAL - QUERY_01")
# Identifica quais áreas apresentam as maiores remunerações. 

media_salario = (
    query_01.groupby("departamento")["salario_base"]
    .mean()
    .sort_values(ascending=False)
)

print(media_salario.head(1))



print("="*35)
print("EDA — 3. CONCENTRAÇÃO DE FUNCIONÁRIOS POR REGIÃO - QUERY_02")
# Distribuição geográfica. 

func_por_regiao = (
    query_02.groupby("regiao")["funcionario"]
    .count()
    .sort_values(ascending=False)
)

print(func_por_regiao)



print("="*35)
print("EDA — 4. LOCALIZAÇÃO COM MAIS DEPARTAMENTOS - QUERY_02")
# Localidades que concentram maior quantidade de deptos. cadastrados. 

departamentos_local = (
    query_02.groupby("localizacao")["departamento"]
    .nunique()
    .sort_values(ascending=False)
)

print(departamentos_local)



print("="*35)
print("EDA — 5. FUNCIONÁRIO COM MAIOR SALÁRIO - QUERY_02")
# Identifica o funcionário com a maior remuneração da base de dados.

print(query_02.loc[
    query_02["salario"].idxmax()
])


print("="*35)
print("EDA — 6. ONDE SE CONCENTRA MAIOR PARTE DOS SALÁRIOS QUERY_01")
print(query_01["salario_base"].describe())
# retorna o resumo estatístico descritivo da coluna "salario_base_query_01"(mínimo, quartis,  
# mediana, média e máximo), para compreender a distribuição salarial. 

print("="*35)
print("EDA — 6. ONDE SE CONCENTRA MAIOR PARTE DOS SALÁRIOS QUERY_02")
print(query_02["salario"].describe())
# retorna o resumo estatístico descritivo da coluna "salario_query_02"(mínimo, quartis, mediana, 
# média e máximo), para compreender a distribuição salarial.

print("="*35)
print("ESTATÍSTICAS BÁSICAS - SALÁRIO BASE POR DEPARTAMENTO - QUERY_01")
print("MÉDIA DO SALÁRIO BASE POR CARGO - QUERY_01")
# Compara salários entre diferentes cargos.

media_salario = (
    query_01
    .groupby("cargo")["salario_base"]
    .mean()
    .sort_values(ascending=False)
    .round(2)
)
print(media_salario)

print("="*35)
print("MEDIDAS ESTATÍSTICAS BÁSICAS da QUERY_02 POR REGIÃO")
# Compara salários entre diferentes regiões.
# Permite avaliar possíveis diferenças salariais geográficas.

media_regiao = query_02.groupby("regiao")["salario"].mean().round(2)

print("="*35)
print("Estatísticas Básicas — Salário por Região QUERY_02")

print(media_regiao)

print("="*35)
print("BOXPLOT GERAL — VISUALIZAÇÃO DOS OUTLIERS - QUERY 02")
# Apresenta a distribuição salarial e identifica possíveis valores discrepantes (outliers).
# Representação visual do critério IQR descrito abaixo. 

print(">>> GERA BOXPLOT GERAL — OUTLIERS - QUERY_01 <<<")
plt.figure(figsize=(8, 5))
sns.boxplot(data=query_01, x="salario_base")
plt.title("Distribuição Geral de Salário — Identificação de Outliers")
plt.xlabel("Salário")
plt.tight_layout()
plt.savefig("boxplot_outliers.png", dpi=200)
plt.show()
plt.close()

# Cálculo do IQR = Define os limites estatísticos utilizados na identificação dos outliers.

Q1 = query_01["salario_base"].quantile(0.25)
Q3 = query_01["salario_base"].quantile(0.75)
IQR = Q3 - Q1

limite_inferior = Q1 - 1.5 * IQR
limite_superior = Q3 + 1.5 * IQR

print(f"Q1 (25%): {Q1:.2f}")
print(f"Q3 (75%): {Q3:.2f}")
print(f"IQR: {IQR:.2f}")
print(f"Limite inferior: {limite_inferior:.2f}")
print(f"Limite superior: {limite_superior:.2f}")

# Identificação, separação e exportação dos resultados: 
# Separação dos registros em dois DataFrames: com e sem outliers.

query_01_outliers = query_01[
    (query_01["salario_base"] < limite_inferior) |
    (query_01["salario_base"] > limite_superior)
]

query_01_sem_outliers = query_01[
    (query_01["salario_base"] >= limite_inferior) &
    (query_01["salario_base"] <= limite_superior)
]

print(f"\nTotal de registros: {len(query_01)}")
print(f"Outliers identificados: {len(query_01_outliers)}")
print(f"Registros sem outliers: {len(query_01_sem_outliers)}")

print("\nRegistros classificados como outliers:")
print(query_01_outliers[["cargo", "departamento", "salario_base"]])


query_01_outliers.to_csv(
    ARQUIVO_Q1_OUTLIERS,
    index=False,
    encoding="utf-8-sig"
)

query_01_sem_outliers.to_csv(
    ARQUIVO_Q1_SEM_OUTLIERS,
    index=False,
    encoding="utf-8-sig"
)

print(f"\nArquivo de outliers salvo em: {ARQUIVO_Q1_OUTLIERS}")
print(f"Arquivo sem outliers salvo em: {ARQUIVO_Q1_SEM_OUTLIERS}")


print("="*35)
print("BOXPLOT GERAL — VISUALIZAÇÃO DOS OUTLIERS - QUERY 02")
# Representação visual do critério IQR  


print(">>> GERA BOXPLOT GERAL — OUTLIERS - QUERY_02 <<<")
plt.figure(figsize=(8, 5))
sns.boxplot(data=query_02, x="salario")
plt.title("Distribuição Geral de Salário — Identificação de Outliers")
plt.xlabel("Salário")
plt.tight_layout()
plt.savefig("boxplot_outliers.png", dpi=200)
plt.show()
plt.close()

print("="*35)

# Identificação, separação e exportação dos resultados: 
# Separação dos registros em dois DataFrames: com e sem outliers.

Q1 = query_02["salario"].quantile(0.25)
Q3 = query_02["salario"].quantile(0.75)
IQR = Q3 - Q1

limite_inferior = Q1 - 1.5 * IQR
limite_superior = Q3 + 1.5 * IQR

print(f"Q1 (25%): {Q1:.2f}")
print(f"Q3 (75%): {Q3:.2f}")
print(f"IQR: {IQR:.2f}")
print(f"Limite inferior: {limite_inferior:.2f}")
print(f"Limite superior: {limite_superior:.2f}")

query_02_outliers = query_02[
    (query_02["salario"] < limite_inferior) |
    (query_02["salario"] > limite_superior)
]

query_02_sem_outliers = query_02[
    (query_02["salario"] >= limite_inferior) &
    (query_02["salario"] <= limite_superior)
]


print(f"\nTotal de registros: {len(query_02)}")
print(f"Outliers identificados: {len(query_02_outliers)}")
print(f"Registros sem outliers: {len(query_02_sem_outliers)}")

print("\nRegistros classificados como outliers:")
print(query_02_outliers[["funcionario", "departamento", "regiao", "salario"]])

query_02_outliers.to_csv(
    ARQUIVO_Q2_OUTLIERS,
    index=False,
    encoding="utf-8-sig"
)
query_02_sem_outliers.to_csv(
    ARQUIVO_Q2_SEM_OUTLIERS,
    index=False,
    encoding="utf-8-sig"
)

print(f"\nArquivo de outliers salvo em: {ARQUIVO_Q2_OUTLIERS}")
print(f"Arquivo sem outliers salvo em: {ARQUIVO_Q2_SEM_OUTLIERS}")


print("="*35)
print("HISTOGRAMA QUERY_01")
# Gera figura para visualização de distribuição
# Apresenta graficamente a distribuição dos valores de salário_base e a frequência


print(">>> GERA HISTOGRAMA - QUERY_01 <<<")
plt.figure(figsize=(8, 5))

sns.histplot(data=query_01, x="salario_base", bins=20, kde=True)

plt.title("Distribuição dos salários")
plt.xlabel("Salário_base")
plt.ylabel("Frequência")
plt.tight_layout()

plt.savefig("histograma_salario_base.png", dpi=200)
plt.show()
plt.close()



print("="*35)
print("HISTOGRAMA QUERY_02")
# Gera figura para visualização de distribuição
# Apresenta graficamente a distribuição dos valores de salário e a frequência


print(">>> GERA HISTOGRAMA - QUERY_02 <<<")
plt.figure(figsize=(8, 5))

sns.histplot(data=query_02, x="salario", bins=20, kde=True)

plt.title("Distribuição dos salários")
plt.xlabel("Salário")
plt.ylabel("Frequência")
plt.tight_layout()

plt.savefig("histograma_salario.png", dpi=200)
plt.show()
plt.close()

print("="*35)

print("="*35)
print(" BOXPLOT QUERY_01")
# Gera figura que compara grupos e identifica outliers 
# Compara categorias entre si e não só uma distribuição isolada 


print(">>> GERA BOXPLOT QUERY_01 <<<")
plt.figure(figsize=(8, 5))
sns.boxplot(data=query_01, x="cargo", y="salario_base")
plt.title("Distribuição de Salário base por cargo")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("boxplot_salario_por_cargo.png", dpi=200)
plt.show()

print("="*35)

print("="*35)
print("BOXPLOT QUERY_02")
# Gera figura que compara grupos e identifica outliers 
# Compara categorias entre si e não só uma distribuição isolada 


print(">>> GERA BOXPLOT QUERY_02 <<<")
plt.figure(figsize=(8, 5))
sns.boxplot(data=query_02, x="departamento", y="salario")
plt.title("Distribuição de Salário por departamento")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("boxplot_salario_por_departamento.png", dpi=200)
plt.show()

print("="*35)

