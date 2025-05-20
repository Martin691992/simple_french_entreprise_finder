import requests
import time

# requète sur recherche entreprises
## doc de l'api sur : https://recherche-entreprises.api.gouv.fr/docs/#section/Bienvenue-sur-la-documentation-interactive-d'API-Recherche-d'entreprises-!/Infolettre

#   entreprise : PME
#   départements : 69,01,42,38
#   Activité : transport
#   effectif : jusqu'a 200 personnes
#   actif
#   Code NAF : 
#     49.41A	Transports routiers de fret interurbains
#     49.41B	Transports routiers de fret de proximité
#     52.10A	Entreposage et stockage frigorifique	Entreposage et stockage frigorifique	Entreposage et stockage frigorifique
#     52.10B	Entreposage et stockage non frigorifique	Entreposage et stockage non frigorifique	Entreposage et stockage non frigorifique
#     52.21Z	Services auxiliaires des transports terrestres

#     52.29A	Messagerie, fret express
#     52.29B	Affrètement et organisation des transports 

#   49.41A,49.41B,52.10A,52.10B,52.21Z,52.29A,52.29B
#
#

requetebase = "https://recherche-entreprises.api.gouv.fr/search?page=1&per_page=25&categorie_entreprise=PME&departement=69,01,38,42&section_activite_principale=H&tranche_effectif_salarie=NN,00,01,02,03,11,12,21&etat_administratif=A&activite_principale=52.29A"
data = requests.get(requetebase)
response = data.json()


index=1    
for a in range(int(response['total_pages'])):
    print(f'------------   Début de la page N°{index} ----------------------')
    requete = f"https://recherche-entreprises.api.gouv.fr/search?page={index}&per_page=25&categorie_entreprise=PME&departement=69,01,38,42&section_activite_principale=H&tranche_effectif_salarie=NN,00,01,02,03,11,12,21&etat_administratif=A&activite_principale=52.29A"
    data_fetch_loop = requests.get(requete)
    response_loop = data_fetch_loop.json()
    
    for i in response_loop['results'] :
        print(i['nom_raison_sociale'])
        with open('./results5229A.txt','a') as w:
            if i['nom_raison_sociale'] != None:
                w.write(f"{i['nom_raison_sociale']}\n")
    print(f'------------   Fin de la page N°{index} ----------------------')
    index += 1

    time.sleep(1)


# return_data = response['results']

# for i in return_data :
#     print(i['nom_raison_sociale'])