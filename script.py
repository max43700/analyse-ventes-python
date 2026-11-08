import plotly.express as px
import pandas as pd
from numpy.ma.core import size
from plotly.graph_objs.layout import xaxis, yaxis

# ====================================
# Exemple fourni dans l'ennoncé
# ====================================

données = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vSC4KusfFzvOsr8WJRgozzsCxrELW4G4PopUkiDbvrrV2lg0S19-zeryp02MC9WYSVBuzGCUtn8ucZW/pub?output=csv')

figure = px.pie(données,
                values='qte',
                names='region',
                title='quantité vendue par région')

figure.write_html('ventes-par-region.html')
print('ventes-par-région.html généré avec succès !')


# ====================================
# Fin de l'exemple
# ====================================


# ====================================
# les ventes par produit
# ====================================

données['CA'] =  données['prix'] * données['qte']
ca_produit = données.groupby('produit', as_index=False,) ['CA'].sum()

figure2 = px.bar(
    ca_produit,
    x='produit',
    y='CA',
    title="Chiffre d'affaires par produit",
    text='CA',
    color='produit',
    color_discrete_map={
        'Produit A' : '#6A9C78',
        'Produit B' : '#648ACB',
        'Produit C' : '#D98278',
    }
)


figure2.update_layout(
    xaxis_title='Produit',
    yaxis_title='Chiffre d\'affaire (€)',
    font={'size' : 26},
)

figure2.write_html('ca-par-produit.html')
print('Chiffre d\'affaire par produit généré avec succès')

# ====================================
# Quantité vendu par produit
# ====================================


qteProduit =  données.groupby('produit', as_index=False,) ['qte'].sum()

figure3 = px.bar(
    qteProduit,
    x='produit',
    y='qte',
    title='Quantités vendu par produit',
    text = 'qte',
    color='produit',
    color_discrete_map={
        'Produit A' : '#6A9C78',
        'Produit B' : '#648ACB',
        'Produit C' : '#D98278',
    }
)

figure3.update_layout(
    xaxis_title='Produit',
    yaxis_title='Quantité vendu',
    font={'size' : 26},
    showlegend=False,
)

figure3.write_html('quantite-par-produit.html')

print('Graphique des quantités généré avec succès !')



