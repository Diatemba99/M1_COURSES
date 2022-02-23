import employe

def cree_liste():
    liste=[]
    return liste

def ajouterEmploye(liste, emp):
    liste.append(emp)


def afficherListe(liste):
    pass


def statistique(liste):
    pass



def main():
    choix=0
    liste=cree_liste()
    while choix!=0:
        print("1- Ajouter un employe")
        print("2- Lister les employes")
        print("3- Statistiques")
        print("4- Quitter")
        print(" Votre choix :")
        choix = int(input(" Mettez votre choix :"))
        if choix ==1:
            matr=int(input("Matricule ?"))
            prenom=int(input("Prenom ?"))
            nom=int(input("nom ?"))
            salbase=int(input("salaire de base ?"))
            emp = employe.Employe(matr,prenom, nom, salbase)
            ajouterEmploye(liste, emp)
        else:
                


main()

