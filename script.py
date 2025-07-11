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

activite_principale = '52.10B'
name_file = '5210B'
requetebase = f"https://recherche-entreprises.api.gouv.fr/search?page=1&per_page=25&categorie_entreprise=PME&departement=69,01,38,42&section_activite_principale=H&tranche_effectif_salarie=NN,00,01,02,03,11,12,21&etat_administratif=A&activite_principale={activite_principale}"
data = requests.get(requetebase)
response = data.json()


index=1    
for a in range(int(response['total_pages'])):
    print(f'------------   Début de la page N°{index} ----------------------')
    requete = f"https://recherche-entreprises.api.gouv.fr/search?page={index}&per_page=25&categorie_entreprise=PME&departement=69,01,38,42&section_activite_principale=H&tranche_effectif_salarie=NN,00,01,02,03,11,12,21&etat_administratif=A&activite_principale={activite_principale}"
    data_fetch_loop = requests.get(requete)
    response_loop = data_fetch_loop.json()
    
    for i in response_loop['results'] :
        with open(f'./results{name_file}.txt','a') as w:
            if i['nom_raison_sociale'] != None:
                dirigeants_valides = [
                    f"{d.get('nom','')},{d.get('prenoms','')}"
                    for d in i.get('dirigeants', [])
                    if 'nom' in d and 'prenoms' in d
                ]
                if dirigeants_valides:
                    print(f"Raison Entreprise :{i['nom_raison_sociale']} | Dirigeants :  {' | '.join(dirigeants_valides)}\n")
                    w.write(f"Raison Entreprise :{i['nom_raison_sociale']} | Dirigeants :  {' | '.join(dirigeants_valides)}\n")
                else : 
                    print(f"Raison Entreprise :{i['nom_raison_sociale']} | Dirigeants : Pas de noms de dirigeants...\n")
                    w.write(f"Raison Entreprise :{i['nom_raison_sociale']} | Dirigeants : Pas de noms de dirigeants...\n")

                # noms_dirigeant = [a for a in i['dirigeants']]
                # print(f"Raison Entreprise :{i['nom_raison_sociale']} ---- Dirigeants :  {' | '.join([f"{d['nom']},{d['prenoms']}" for d in noms_dirigeant if 'nom' in d and 'prenoms' in d])}\n")
                # w.write(f"Raison Entreprise :{i['nom_raison_sociale']} ---- Dirigeants :  {' | '.join([f"{d['nom']},{d['prenoms']}" for d in noms_dirigeant if 'nom' in d and 'prenoms' in d])}\n")

    print(f'------------   Fin de la page N°{index} ----------------------')
    index += 1

    time.sleep(1)


# return_data = response['results']

# for i in return_data :
#     print(i['nom_raison_sociale'])