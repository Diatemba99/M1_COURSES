class Employe:
    def __init__(self, matr, nom, prenom, salbase):
        self.__matr=matr
        self.__nom=nom
        self.__prenom=prenom
        self.__salbase=salbase


    #Starting of getters bloc
    def getMatr(self):
        return self.__matr

    def getNom(self):
        return self.__nom

    def getPrenom(self):
        return self.__prenom            

    def getSalbase(self):
        return self.__salbase


    #Starting setters bloc

    def setMatr(self, matr):
        self.__matr=matr 

    def setNom(self, nom):
        self.__nom=nom 

    def setPrenom(self, prenom):
        self.__prenom=prenom 

    def setSalbase(self, salbase):
        self.__matr=salbase                    