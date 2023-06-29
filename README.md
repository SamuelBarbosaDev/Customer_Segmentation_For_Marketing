# Customer Segmentation For Marketing:

### Índice

- [Customer Segmentation For Marketing:](#customer-segmentation-for-marketing)
    - [Índice](#índice)
    - [Contextualização:](#contextualização)
    - [Metodologia Aplicada:](#metodologia-aplicada)
  - [Entendimento do Negócio:](#entendimento-do-negócio)
  - [Entendimento dos Dados:](#entendimento-dos-dados)
    - [Variáveis:](#variáveis)
    - [Verificando as Dimensões do DataFrame:](#verificando-as-dimensões-do-dataframe)
    - [Describe:](#describe)
    - [Verificando Valores Nulos:](#verificando-valores-nulos)
    - [Verificando Tipos:](#verificando-tipos)
  - [Preparação dos Dados:](#preparação-dos-dados)
    - [Criando Uma Copia do DataFrame:](#criando-uma-copia-do-dataframe)
    - [Substituindo Valores:](#substituindo-valores)
    - [Substituindo Valores:](#substituindo-valores-1)
    - [Removendo nulos:](#removendo-nulos)
    - [Label Endcode:](#label-endcode)
    - [Convertendo Colunas:](#convertendo-colunas)
    - [Dummy:](#dummy)
    - [Removendo Colunas:](#removendo-colunas)
  - [Modelagem:](#modelagem)
  - [Avaliação:](#avaliação)
  - [Implantação:](#implantação)
  - [Pré-requisitos para executar o projeto:](#pré-requisitos-para-executar-o-projeto)
    - [Instale o Pacote Anaconda:](#instale-o-pacote-anaconda)
    - [Ambiente virtual e Dependências:](#ambiente-virtual-e-dependências)


### Contextualização:
Você foi contratado por uma empresa de e-commerce que está buscando entender
melhor o comportamento de seus clientes para personalizar as suas campanhas de
marketing. Para isso, a empresa disponibilizou uma base de dados em csv contendo
dados sobre clientes, produtos e transações da loja realizadas entre os anos de 2010 e
2011.

### Metodologia Aplicada:
A análise foi realizada utilizando o modelo CRISP-DM, o CRISP-DM (Cross Industry Standard Process for Data Mining) é um modelo padrão de processo para projetos de mineração de dados que define um conjunto de fases e tarefas que devem ser executadas para desenvolver soluções de mineração de dados efetivas.

![CRISP-DM](/core/img/CRISP-DM.png)

O modelo CRISP-DM é uma abordagem sistemática e estruturada para a mineração de dados que ajuda as empresas a desenvolver soluções de mineração de dados de maneira eficiente e eficaz, reduzindo o tempo e os custos do projeto.

## Entendimento do Negócio:
Com base nesses dados, você precisa agrupar os clientes em clusters com base em seu comportamento de compra. Isso irá permitir identificar padrões e características em comum entre os clientes, como:
Clientes que compram os mesmos produtos;
Clientes que possuem a mesma frequência de compras;
Clientes que gastam mais dinheiro em suas compras.
A partir desses clusters, gere insights para que a empresa possa segmentar melhor a sua base de clientes e personalizar as suas campanhas de marketing, direcionando promoções e ofertas aos clientes com base no comportamento de compras.

## Entendimento dos Dados:
### Variáveis:
![Data Frame](/core/img/dataframe.png)

### Verificando as Dimensões do DataFrame:
![Data Frame](/core/img/shape.png)

### Describe:
![Data Frame](/core/img/describe.png)

### Verificando Valores Nulos:
![Data Frame](/core/img/nulos.png)

### Verificando Tipos:
![Data Frame](/core/img/tipos.png)

## Preparação dos Dados:
### Criando Uma Copia do DataFrame:
![Data Frame](/core/img/copy.png)

### Substituindo Valores:
![Data Frame](/core/img/substituindo_valores.png)

### Substituindo Valores:
![Data Frame](/core/img/substituindo_valores.png)

### Removendo nulos:
![Data Frame](/core/img/removendo_nulos.png)

### Label Endcode:
![Data Frame](/core/img/label_endcode.png)

### Convertendo Colunas:
![Data Frame](/core/img/convertendo_colunas.png)

### Dummy:
![Data Frame](/core/img/dummy.png)

### Removendo Colunas:
![Data Frame](/core/img/removendo_colunas.png)

## Modelagem:

## Avaliação:
Com o objetivo de criar este estudo, buscamos identificar o perfil dos usuários que têm maior probabilidade de deixar a plataforma de streaming. Para isso, realizamos uma análise detalhada em busca de padrões entre os diferentes perfis de usuários que abandonam a plataforma, a fim de identificar possíveis casos de churn antes que ocorram. Dessa forma, buscamos reter esses clientes por mais tempo em nossa plataforma.

Utilizamos dois modelos de machine learning para identificar os perfis dos clientes: Regressão Logística e Random Forest. Durante a comparação entre os dois modelos, constatamos que o Random Forest obteve um desempenho superior, além de se adequar melhor à resolução do nosso problema.

## Implantação:
Iniciando a etapa de implementação do modelo em produção.

## Pré-requisitos para executar o projeto:
Abaixo, listarei os requisitos necessários para que o projeto funcione corretamente.

### Instale o Pacote Anaconda:
Você pode baixá-lo em: <https://www.anaconda.com/download/> 

### Ambiente virtual e Dependências:
Criando ambiente virtual:
```
conda create -n .cluster
```

Entrando no ambiente virtual:
```
conda activate .cluster
```

Instale as dependências:
```
conda install --file core/requirements.txt
```

---
Linkedin: <https://www.linkedin.com/in/samuel-barbosa-dev/> 

E-mail: <samueloficial@protonmail.com>