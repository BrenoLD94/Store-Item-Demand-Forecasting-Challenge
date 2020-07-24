# Store-Item-Demand-Forecasting-Challenge

__Objetivo__: Prever a venda nos próximos 3 meses.

Link: https://www.kaggle.com/c/demand-forecasting-kernels-only/data

__Descrição dos Dados__:

* data - data dos dados de venda. Não há efeitos de férias ou fechamento de lojas.
* store - ID da loja.
* item - ID do item.
* vendas - Número de itens vendidos em uma loja específica em uma data específica.

__Contexto__:

Esta competição é fornecida como uma maneira de explorar diferentes técnicas de séries temporais em um conjunto de dados relativamente simples e limpo.

Você recebe 5 anos de dados de vendas de itens de loja e é solicitado a prever 3 meses de vendas para 50 itens diferentes em 10 lojas diferentes.

Qual é a melhor maneira de lidar com a sazonalidade? As lojas devem ser modeladas separadamente ou você pode agrupá-las? O aprendizado profundo funciona melhor que o ARIMA? Pode bater xgboost?

É uma grande competição para explorar diferentes modelos e aprimorar suas habilidades em previsão.

__Considerações__:
  A solução que adotei é simples e tem um resultado OK (private score = 15.92151 e public score = 16.53754). Meu principal intuito ao fazer esse desafio foi para treinar, praticamente, todas as etapas de um projeto de ciências de dados (bem simplificado). Fiz um app web para que a pessoa entre com o dataset de teste e o app gere as previsões. Tentei comentar todo meu raciocínio para a solução do problema.
  
Link do app: https://web-app-store-item.herokuapp.com/

obs: Devido as limitações do Heroku tive que sacrificar 'accurácia' do modelo para conseguir subir com o modelo para nuvem!
