#!/usr/bin/env python
# coding: utf-8

# In[5]:


import streamlit as st
import numpy as np
import pprint
import pandas as pd
import time
# import plotly.graph_objects as go

# empty dataframe hidden until user inputs data
df = pd.DataFrame()


st.title('CSE Calcul ASC 2026')
st.write('')

# add some space between photo and instructions
st.write('')
st.subheader('vous pouvez saisir vos informations pour le calcul ASC')


# create placeholders to clear inputs when clicking "start over" button
placeholder_c = st.empty()
placeholder_s = st.empty()



# In[9]:


# have user input the amount they have for each coin

userRFF = placeholder_c.number_input('Revenu fiscal de reference 2026 (sur les revenus 2025) en euros: ', min_value= 0, value=100000)
userNBPart = placeholder_s.number_input('Nombre de parts ', min_value= 1.,format="%.2f", step=0.5)



# In[ ]:


# tell user how much they have in gold pieces

QF = (userRFF / userNBPart / 12) 
QF = round(QF)

st.write(f'Votre Quotient Familial {QF:,d} .')


# In[ ]:


st.write('')

# Afficher l'enveloppe 
if QF > 2300:
    st.subheader('Vous avez l\'enveloppe standard de 200 euros.')
    st.write('Pas besoin de venir nous voir :) ')
elif 2050 < QF <= 2300 :
    st.subheader('Vous avez une enveloppe de 250 euros.')
    st.write('Vous pouvez venir nous voir!! :) ')
    st.write('Nous avons besoin de votre avis d\'imposition pour valider cette enveloppe. ')
elif 1800 < QF <= 2050 :
    st.subheader('Vous avez une enveloppe de 300 euros.')
    st.write('Vous pouvez venir nous voir!! :) ')
    st.write('Nous avons besoin de votre avis d\'imposition pour valider cette enveloppe. ')
elif 1550 < QF <= 1800:
    st.subheader('Vous avez une enveloppe de 350 euros.')
    st.write('Vous pouvez venir nous voir!! :) ')
    st.write('Nous avons besoin de votre avis d\'imposition pour valider cette enveloppe. ')
elif 1300 < QF <= 1550:
    st.subheader('Vous avez une enveloppe de 400 euros.')
    st.write('Vous pouvez venir nous voir!! :) ')
    st.write('Nous avons besoin de votre avis d\'imposition pour valider cette enveloppe. ')
elif QF <= 1300:
    st.subheader('Vous avez une enveloppe de 450 euros.')
    st.write('Vous pouvez venir nous voir!! :) ')
    st.write('Nous avons besoin de votre avis d\'imposition pour valider cette enveloppe. ')
else: 
    st.write('Vous avez une enveloppe bonifiée.')
    st.write('Vous pouvez venir nous voir!! :) ')

# Afficher un message d'explication si l'utilisateur dépasse l'enveloppe
if QF < 2300:
    st.subheader('Ceci est le montant total auquel vous avez droit, il inclut')
    st.write(' - Les demandes de remboursement pour un maximum de 200€')
    st.write(' - Une carte cadeau du montant de l\'enveloppe auquel est soustrait le montant déjà demandé en remboursement (ici aussi il y a un maximum de 200€)')
    st.write(' - Une ou plusieurs carte enfant du surplus si le montant maximum est atteint pour la carte cadeau (maximum de 200€ par enfant)')
    st.write(' - Une carte culture du surplus si le montant maximum des cartes cadeaux précédentes est atteint')
    st.write('')
    st.write('Si vous disposez de plus de l\'enveloppe par défaut de 200€, pour en bénéficier, veuillez apportez votre justificatif (Relevé d\'impots de l\'année précédente) à une permanence de votre CSE ET veuillez ajouter vos éventuels enfants comme ayant droit dans Swile.')
else: 
    st.subheader('Ceci est le montant total auquel vous avez droit, il inclut')
    st.write(' - Les demandes de remboursement pour un maximum de 200€')
    st.write(' - Une carte cadeau du montant de l\'enveloppe, à savoir 200€, auquel est soustrait le montant déjà demandé en remboursement.')



# In[ ]:


# create dividing line to separate calculations from reset
st.write('-------------------------')






