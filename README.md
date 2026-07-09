# Análise de Performance Logística e Impacto Financeiro (E-commerce Olist)

Análise exploratória desenvolvida em Python para auditar dados de uma operação real de e-commerce, mapear gargalos logísticos estaduais e mensurar o impacto financeiro dos atrasos de entrega para o cliente final.

## 📌 Contexto do Projeto
Em operações de e-commerce, a última milha (*last mile*) é crucial para a retenção do cliente. Utilizando o dataset público da Olist, este projeto realiza o ciclo completo de dados (Data Pipeline): desde a carga, passando por uma limpeza rigorosa de dados nulos e inconsistências de tipos, até a geração de inteligência de negócio e visualização de dados.

## 🛠️ Tecnologias Utilizadas
* **Python 3.12**
* **Pandas:** Limpeza, manipulação, cruzamento de tabelas (`merge`) e agregações (`groupby`).
* **Seaborn & Matplotlib:** Geração de gráficos estatísticos e visuais de alta fidelidade.
* **PyCharm IDE & Git/GitHub:** Controle de versão e ambiente de desenvolvimento.

## 📈 Principais Insights de Negócio

A análise cruzada entre os dados de entrega, localização geográfica dos clientes e valores financeiros revelou diagnósticos críticos para a diretoria:

1. **O Gargalo de Alagoas (AL):** Lidera o ranking nacional com **20.8% de taxa de atraso**. Praticamente 1 a cada 5 clientes do estado recebe seu produto fora do prazo estimado, enfrentando uma espera média de 24 dias.
2. **A Anomalia Operacional do Rio de Janeiro (RJ):** Estados do Norte e Nordeste justificam tempos longos pela distância dos polos de distribuição (Sudeste) e fretes elevados. No entanto, o **Rio de Janeiro figura em 7º lugar no ranking de atrasos (11.6%)**, mesmo apresentando um frete barato (R$ 20.91) e proximidade geográfica. Isso aponta para uma ineficiência puramente operacional na distribuição local ou problemas de segurança urbana na malha fluminense.
3. **Penalização Financeira:** Clientes com entregas severamente atrasadas (mais de 50 dias) pagaram, em média, **39.8% a mais pelo frete** (R$ 27.82 vs R$ 19.90) comparado a entregas normais. O cliente mais prejudicado pela logística foi o que mais pagou pelo serviço.

---

## 📊 Visualização dos Dados (Gargalos Estaduais)

O gráfico abaixo foi gerado automaticamente pelo script Python e exportado em alta resolução, destacando os 10 estados com piores índices de pontualidade:

![Top 10 Estados com Maior Taxa de Atraso](dados/grafico_top10_atrasos.png)

---

## 📁 Estrutura do Repositório
* `limpeza_dados.py`: Script Python com o pipeline completo de engenharia e análise.
* `dados/grafico_top10_atrasos.png`: Gráfico gerado para o relatório executivo.
* `.gitignore`: Configuração para impedir o upload dos datasets pesados (.csv) originais.
