import plotly.express as px
import pandas as pd
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

figure3 = px.bar(
    ca_produit,
    x='produit',
    y='CA',
    title="Chiffre d'affaires par produit",
    text='CA',
    color='produit',
    color_discrete_map={
        'Produit A' :  'green',
        'Produit B' : 'blue',
        'Produit C' : 'red',
    }
)


figure3.write_html('ca-par-produit.html')
print('Chiffre d\'affaire par produit généré avec succès')

# ====================================
# le chiffre d'affaire par produit 
# ====================================


