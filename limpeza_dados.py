import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print("1. Carregando todas as bases necessárias...")
df_pedidos = pd.read_csv('data/olist_orders_dataset.csv')
df_itens = pd.read_csv('data/olist_order_items_dataset.csv')
df_clientes = pd.read_csv('data/olist_customers_dataset.csv')

# Conversão das datas
colunas_data = ['order_purchase_timestamp', 'order_delivered_customer_date', 'order_estimated_delivery_date']
for coluna in colunas_data:
    df_pedidos[coluna] = pd.to_datetime(df_pedidos[coluna])

# Filtrando pedidos entregues válidos
df_entregues = df_pedidos[(df_pedidos['order_status'] == 'delivered') & (df_pedidos['order_delivered_customer_date'].notnull())].copy()

# Calculando tempos de entrega e atraso
df_entregues['tempo_entrega_dias'] = (df_entregues['order_delivered_customer_date'] - df_entregues['order_purchase_timestamp']).dt.days
df_entregues['dias_diferenca_estimada'] = (df_entregues['order_delivered_customer_date'] - df_entregues['order_estimated_delivery_date']).dt.days
df_entregues['houve_atraso'] = df_entregues['dias_diferenca_estimada'].apply(lambda x: 1 if x > 0 else 0)

print("2. Unificando as tabelas (Merge)...")
df_intermediario = pd.merge(df_entregues, df_itens, on='order_id', how='inner')
df_final = pd.merge(df_intermediario, df_clientes, on='customer_id', how='inner')

print("3. Agrupando os dados por Estado...")
analise_estados = df_final.groupby('customer_state').agg(
    frete_medio=('freight_value', 'mean'),
    tempo_entrega_medio=('tempo_entrega_dias', 'mean'),
    taxa_atraso_percentual=('houve_atraso', lambda x: x.mean() * 100)
).reset_index()

# Ordenando pelos estados com maior taxa de atraso
analise_estados = analise_estados.sort_values(by='taxa_atraso_percentual', ascending=False)

# =========================================================================
# EXPORTAR OS RESULTADOS (CSV)
# =========================================================================
print("4. Salvando os arquivos CSV limpos...")
df_final.to_csv('data/olist_vendas_limpo.csv', index=False)
analise_estados.to_csv('data/analise_atrasos_estados.csv', index=False)

# =========================================================================
# GERAR E SALVAR O GRÁFICO AUTOMATICAMENTE (.PNG)
# =========================================================================
print("5. Gerando gráfico de performance logística...")

# Configurando o estilo do gráfico
plt.figure(figsize=(12, 6))
sns.set_theme(style="whitegrid")

# Criando o gráfico de barras para os top 10 estados com mais atraso
grafico = sns.barplot(
    data=analise_estados.head(10),
    x='customer_state',
    y='taxa_atraso_percentual',
    hue='customer_state',       # Define que a cor muda por estado
    palette='Reds_r',
    legend=False                # Remove a legenda lateral para não poluír
)

# Detalhes visuais do gráfico
plt.title('Top 10 Estados com Maior Taxa de Atraso nas Entregas (Olist)', fontsize=14, fontweight='bold')
plt.xlabel('Estado do Cliente', fontsize=12)
plt.ylabel('Pedidos com Atraso (%)', fontsize=12)

# Adicionando os valores em cima de cada barra
for p in grafico.patches:
    grafico.annotate(f"{p.get_height():.1f}%",
                     (p.get_x() + p.get_width() / 2., p.get_height()),
                     ha='center', va='center',
                     xytext=(0, 9),
                     textcoords='offset points', fontsize=10, fontweight='bold')

plt.tight_layout()

# SALVA O GRÁFICO COMO IMAGEM DE ALTA QUALIDADE
plt.savefig('data/grafico_top10_atrasos.png', dpi=300)
print("Sucesso total! Verifique a pasta 'data' no seu PyCharm.")