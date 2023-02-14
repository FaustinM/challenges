import itertools
from math import comb

joueurs = [
    "Joueur 1", "Joueur 2", "Joueur 3", "Joueur 4", "Joueur 5",
    "Joueur 6", "Joueur 7", "Joueur 8", "Joueur 9", "Joueur 10",
    "Joueur 11", "Joueur 12", "Joueur 13", "Joueur 14", "Joueur 15"
]

vote_joueurs = {
    "Joueur 1" : ("Joueur 2", "Joueur 3"),
    "Joueur 2" : ("Joueur 2", "Joueur 3"),
    "Joueur 3" : ("Joueur 2", "Joueur 3"),
    "Joueur 4" : ("Joueur 2", "Joueur 3"),
    "Joueur 5" : ("Joueur 2", "Joueur 3"),
    "Joueur 6" : ("Joueur 11", "Joueur 12"),
    "Joueur 7" : ("Joueur 2", "Joueur 3"),
    "Joueur 8" : ("Joueur 2", "Joueur 3"),
    "Joueur 9" : ("Joueur 2", "Joueur 3"),
    "Joueur 10" : ("Joueur 2", "Joueur 3"),
    "Joueur 11" : ("Joueur 2", "Joueur 3"),
    "Joueur 12" : ("Joueur 2", "Joueur 3"),
    "Joueur 13" : ("Joueur 2", "Joueur 3"),
    "Joueur 14" : ("Joueur 2", "Joueur 3"),
    "Joueur 15" : ("Joueur 2", "Joueur 3"),
}

combinaisons_joueurs = list(itertools.combinations(joueurs, 5))


def check_if_combi_possible(combi, conditionsCombi):
    for conditionCombi in conditionsCombi:
        for joueur in conditionCombi:
            if joueur in combi:
                return False
    return True

def list_combi_possible(allCombi, conditionsCombi):
    combinaison_possible = []
    for combi in allCombi:
        if check_if_combi_possible(combi, conditionsCombi): 
            combinaison_possible.append(combi)
    return combinaison_possible

def calculer_score_equipe(equipe, votes):
    point = 0
    for joueur in equipe:
        for vote in votes[joueur]:
            if vote in equipe: point = point + 1
    return point

def calculer_score_combi(combi, votes):
    return sum([calculer_score_equipe(e, votes) for e in combi])

def trouver_meilleur_combi_equipe(equipes, votes):
    max_score = -1
    max_combi = None
    for combi in list(itertools.product(*equipes)):
        score_combi = calculer_score_combi(combi, votes)
        if score_combi > max_score:
            max_score = score_combi
            max_combi = combi
    return max_combi

def trouve_meilleur(allCombi, votes, nbEquipe):
    meilleur_combi = None
    meilleur_score = -1
    for combi in allCombi:
        equipes = [combi]
        for i in range(1, nbEquipe):
            equipes.append(list_combi_possible(allCombi, equipes))
        
        equipes[0] = [equipes[0]]
        print(list(itertools.product(*equipes))[-1], '\n')

def generer_combi(allCombi, parents, n):
    return {
        
    }
            
    

combi = list_combi_possible(combinaisons_joueurs, [combinaisons_joueurs[0]])
combi_2 = list_combi_possible(combinaisons_joueurs, [combinaisons_joueurs[0], combi[0]])

# print(combinaisons_joueurs[120], calculer_score_equipe(combinaisons_joueurs[120], vote_joueurs))
# print(trouver_meilleur_combi_equipe([combinaisons_joueurs, combi, combi_2], vote_joueurs))

trouve_meilleur(combinaisons_joueurs, vote_joueurs, 3)