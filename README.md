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
    - [Verificando Tipos:](#verificando-tipos)
    - [Describe:](#describe)
    - [Verificando Valores Nulos:](#verificando-valores-nulos)
    - [Verificando Valores duplicados:](#verificando-valores-duplicados)
    - [Verificando As Variáveis Com Boxplot:](#verificando-as-variáveis-com-boxplot)
    - [Verificando Distribuição:](#verificando-distribuição)
  - [Preparação dos Dados:](#preparação-dos-dados)
    - [Criando Uma Copia do DataFrame:](#criando-uma-copia-do-dataframe)
    - [Removendo nulos:](#removendo-nulos)
    - [Convertendo a coluna 'CustomerID' para str:](#convertendo-a-coluna-customerid-para-str)
    - [Convertendo a coluna 'InvoiceDate' para Datetime::](#convertendo-a-coluna-invoicedate-para-datetime)
    - [Análise RFV:](#análise-rfv)
    - [Recency:](#recency)
    - [Frequency:](#frequency)
    - [Monetary:](#monetary)
    - [Merge:](#merge)
    - [RFV Boxplot:](#rfv-boxplot)
    - [RFV - Distribuição Recency:](#rfv---distribuição-recency)
    - [RFV - Distribuição Frequency:](#rfv---distribuição-frequency)
    - [RFV - Distribuição Monetary:](#rfv---distribuição-monetary)
    - [Data Preparetion:](#data-preparetion)
    - [Testando técnicas de remoção de outliers:](#testando-técnicas-de-remoção-de-outliers)
    - [RFV Boxplot Limpo:](#rfv-boxplot-limpo)
    - [RFV Distribuição:](#rfv-distribuição)
  - [Modelagem:](#modelagem)
    - [KMeans:](#kmeans)
    - [Gráfico Kelbow Visualizer:](#gráfico-kelbow-visualizer)
    - [Criando os clusters::](#criando-os-clusters)
    - [Gráfico Scatterplot3d:](#gráfico-scatterplot3d)
    - [Grupos:](#grupos)
    - [Clusters:](#clusters)
    - [Dataframe Clusters:](#dataframe-clusters)
    - [gráfico\_heatmap:](#gráfico_heatmap)
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

### Verificando Tipos:
![Data Frame](/core/img/tipos.png)

### Describe:
![Data Frame](/core/img/describe.png)

### Verificando Valores Nulos:
![Data Frame](/core/img/nulos.png)

### Verificando Valores duplicados:
![Data Frame](/core/img/duplicados.png)

### Verificando As Variáveis Com Boxplot:
![Data Frame](/core/img/boxplot1.png)

### Verificando Distribuição:
![Data Frame](/core/img/distribuição.png)

## Preparação dos Dados:
### Criando Uma Copia do DataFrame:
![Data Frame](/core/img/copy.png)

### Removendo nulos:
![Data Frame](/core/img/removendo_nulos.png)

### Convertendo a coluna 'CustomerID' para str:
![Data Frame](/core/img/CustomerID.png)

### Convertendo a coluna 'InvoiceDate' para Datetime::
![Data Frame](/core/img/InvoiceDate.png)

### Análise RFV:
![Data Frame](/core/img/RFV.png)

### Recency:
![Data Frame](/core/img/Recency.png)

### Frequency:
![Data Frame](/core/img/Frequency.png)

### Monetary:
![Data Frame](/core/img/Monetary.png)

### Merge:
![Data Frame](/core/img/Merge.png)

### RFV Boxplot:
![Data Frame](/core/img/rfv_boxplot.png)

### RFV - Distribuição Recency:
![Data Frame](/core/img/distribuição_Recency.png)

### RFV - Distribuição Frequency:
![Data Frame](/core/img/distribuição_Frequency.png)

### RFV - Distribuição Monetary:
![Data Frame](/core/img/distribuição_Monetary.png)

### Data Preparetion:
![Data Frame](/core/img/data_preparetion.png)

### Testando técnicas de remoção de outliers:
![Data Frame](/core/img/outliers.png)

### RFV Boxplot Limpo:
![Data Frame](/core/img/rfv_boxplot_limpo.png)

### RFV Distribuição:
![Alt text](/core/img/rfv_distribuição.png)

## Modelagem:
### KMeans:
![Alt text](/core/img/kmeans.png)

### Gráfico Kelbow Visualizer:
![Alt text](/core/img/gráfico_kelbow_visualizer.png)

### Criando os clusters::
![Alt text](/core/img/criando_os_clusters.png)

### Gráfico Scatterplot3d:
![Alt text](/core/img/gráfico_clusters_scatterplot3d.png)

### Grupos:
![Alt text](/core/img/grupos.png)

### Clusters:
![Alt text](/core/img/clusters.png)

### Dataframe Clusters:
![Alt text](/core/img/dataframe_clusters.png)

### gráfico_heatmap:
![Alt text](/core/img/corr.png)

## Avaliação:
Com o objetivo de identificar e segmentar os perfis dos clientes com base em seu padrão de compra, a fim de promover campanhas de marketing mais personalizadas, chegamos a 5 grupos distintos, representando 5 perfis de clientes.

- Perfil 1: O perfil 1 apresenta a pior recência em relação aos demais, indicando que esses clientes estão afastados de nossa plataforma há mais tempo. No entanto, o perfil 1 não difere muito dos perfis 4 e 5 em relação à recência. Além disso, a frequência de acesso à nossa plataforma por parte desse perfil também é baixa, sendo a segunda mais baixa, ficando atrás apenas do perfil 5.

- Perfil 2: O perfil 2 é composto por clientes que tiveram interações muito recentes em nossa plataforma. Portanto, é importante manter esses clientes interessados em nosso e-commerce, seja por meio de anúncios de produtos relevantes que possam resolver seus problemas ou proporcionar diversão. Em resumo, o perfil 2 apresenta excelente recência, frequência adequada e gastos moderados.

- Perfil 3: O perfil 3 também é composto por clientes que entraram em contato recentemente com nossa plataforma. Eles possuem excelente recência, frequência adequada e gastos moderados.

- Perfil 4: O perfil 4 é o perfil de cliente mais engajado que temos. Apresenta recência adequada, frequência excelente e gastos consideráveis. Em suma, o perfil 4 é extremamente valioso, e cada centavo investido nesse grupo vale a pena.

- Perfil 5: O perfil 5 representa nosso perfil de cliente mais inativo. Possui recência satisfatória, frequência baixa e gastos reduzidos. Trata-se de um perfil de cliente com pouca interação e, consequentemente, baixo volume de compras.

Conclusão: Nosso principal objetivo é criar uma campanha de marketing mais personalizada, lembrando que, no final, tudo se resume a vender. Um padrão identificado foi que os clientes que mais gastam em nossa plataforma são aqueles que a frequentam com mais regularidade. Portanto, uma ideia interessante seria criar estratégias para incentivar o cliente a visitar nossa plataforma e interagir. Por exemplo, podemos oferecer um desconto de 25% a partir da compra do 3º item ou promover descontos especiais nas sextas-feiras para clientes fiéis, a fim de fidelizá-los.

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