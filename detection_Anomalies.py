import matplotlib.pyplot as plt
import numpy as np

class detection_Anomalies:

    def __init__(self):
        print("Analyse des données")

    def methode(file,nom):

    # Ouverture du fichier de données
        f=open(file,"r")

        lines=f.readlines()

    #compter le nombre de données
        nombreDonnees=0
    # Normalisation du format des données
        newLines=[]
        for line in lines:
            newLine=line.replace("'","")
            newLine1=newLine.replace("\n","")
            newLine2=newLine1.split(',')
            nombreDonnees+=1
            newLines.append(newLine2)


    # Le nombre de données sans les 2 premières ligne du fichiers qui indiquent le type de données et l'unité de msure de la donnée
        nombreDonnees=nombreDonnees-2
        print("Données initiales : ","\n")

        for newLine in newLines:
            print(newLine)

        nom1 = str(nom)


        print("\n","Analyse des données de : ",nom1,"\n")

        borne_inf = 0
        borne_sup = 0
    #indice du champ de la température dans la liste
        if(nom=="Temperature"):
            indice=newLines[0].index("Tblood")
            borne_inf=36
            borne_sup=38
        if(nom=="saturation en oxygène"):
            indice=newLines[0].index("SpO2")
            borne_inf=95
            borne_sup=100

        if(nom=="battement de coeur"):
            indice =newLines[0].index("HR")
            borne_inf=60
            borne_sup=80
        if(nom=="Tension artérielle systolique"):
            indice=newLines[0].index("ABPsys")
            borne_inf=100
            borne_sup=140


        Valeurs = []





    #on récupère les valeurs de toutes les températures
        for line in newLines:
            t=line[indice]
            Valeurs.append(t)

    #On retire 2 premières valeurs indiquant le nom du champ (Tblood) et son unité de mesure
        del Valeurs[0]
        del Valeurs[0]

    #affichage de toutes les températures
        print("liste des valeurs : ",Valeurs,"\n")
        listeIndices=[]

        x1=Valeurs.__len__()




        Alerte=False
        moyenne=0
        moyenneNormale=0

        # somme qui exclut les valeurs abberantes
        somme=0

        # somme qui considère toutes les valeurs
        somme1=0

        # compteur du nombre de valeurs normales
        nbValeursNormales=0

        # listes de toutes les valeurs numériques
        valeursNumeriques=[]


        listeValeursIncoherentes=[]

        #indices des valeurs dans la liste
        i=0


        for val in Valeurs:

            valeurNumerique = float(val)
            valeursNumeriques.append(valeurNumerique)

            if (valeurNumerique >= borne_inf and valeurNumerique <=borne_sup):

                print(nom," normale : ",valeurNumerique)
                i+=1
                somme+=valeurNumerique
                somme1+=valeurNumerique
                nbValeursNormales+=1

            if(valeurNumerique<borne_inf):
                print(nom," incohérente", valeurNumerique)

                listeValeursIncoherentes.append(valeurNumerique)
                somme1+=valeurNumerique
                i+=1

                #if(valeursNumeriques[i-1]>=37 | valeursNumeriques[i-1]<=40):
                #   print("erreur : la temperature ne peut pas trop baisser d'un coup")

            if(valeurNumerique>borne_sup):

                print("valeur anormale ",valeurNumerique)
                somme1 += valeurNumerique
                i += 1
                listeValeursIncoherentes.append(valeurNumerique)

        print("\n")
        if(nbValeursNormales!=0):
            moyenneNormale=somme/nbValeursNormales
            print("moyenne des valeurs normales : ",moyenneNormale,"\n")
        else:
            print("Alerte aucune valeur normale : vérifier les autres paramètres !")


        #graphique

        plt.xlabel("temps")
        plt.ylabel(nom)
        y = np.array(valeursNumeriques)
        indices=[]
        for val in range (1,valeursNumeriques.__len__()+1):
            ind=str (val)
            ind1="t"+ind
            indices.append(ind1)

        x=np.array(indices)
        plt.plot(x,y)

        nom_fig = nom + ".png"
        plt.savefig(nom_fig)
        plt.show()



        moyenne=somme1/Valeurs.__len__()
        print("moyenne absolue : ",moyenne,"\n")

        print("liste des valeures abbérantes :")
        print(listeValeursIncoherentes,"\n")


        mediane=np.median(np.array(valeursNumeriques))
        print("mediane : ",mediane,"\n")
        longeur= len(valeursNumeriques)


        print("valeurs non triées : ",valeursNumeriques)
        valeursNumeriques.sort()
        print("valeurs triées :     ",valeursNumeriques)

        print("nombre de valeurs : ",x1)
        etendue=valeursNumeriques[longeur-1]-valeursNumeriques[0]
        print("entendue : ",etendue,"\n")

        quartile1=0
        quartile3=0
        if(longeur%2==0):
            indice1=longeur*0.25
            indice1=int (indice1)
            indice2=longeur*0.75
            indice2=int (indice2)
            if(indice1%2!=0):
                quartile1=valeursNumeriques[1+abs(indice1)]
                quartile3=valeursNumeriques[1+abs(indice2)]
            else:
                quartile1=(valeursNumeriques[(indice1)]+valeursNumeriques[1 + (indice1)])/2
                quartile3=(valeursNumeriques[(indice2)]+valeursNumeriques[1 + (indice2)])/2


        print("quartile 1 : ",quartile1)
        print("quartile 3 :",quartile3)
        etudue_inter_quartiles=quartile3-quartile1
        print("etendue inter-quartiles",etudue_inter_quartiles)

        extremite_superieur=quartile1+1.5*(etudue_inter_quartiles)
        max=valeursNumeriques[0]

        for val in valeursNumeriques:
            if(val<=extremite_superieur and val>max):
                max=val
        extremite_superieur=max
        print("extremité supérieur : ",extremite_superieur)

        extremite_inferieur=quartile1-1.5*(etudue_inter_quartiles)
        min=valeursNumeriques[0]
        if(extremite_inferieur<min):
            extremite_inferieur=min
        print("extremite inférieur : ",extremite_inferieur,"\n")

        for val in listeValeursIncoherentes:
            if(val<extremite_inferieur):
                print("valeur en dehors de la boite à moustache")
                print(val," < ",extremite_inferieur)
                ind=valeursNumeriques.index(val)
                if(ind<longeur-1):
                    suiv=valeursNumeriques[ind+1]
                    pred=valeursNumeriques[ind-1]
                    if(suiv in listeValeursIncoherentes):
                        print("Vérifier les autres paramètres de santé ")

                    else:
                        print("valeur incohérente car la valeur suivante est normale")
                        print("valeur suivante normale : ",suiv)
                    print("\n")

            if(val>extremite_superieur):
                print("valeur en dehors de la boite à moustache")
                print(val," > ",extremite_superieur)
                ind = valeursNumeriques.index(val)
                if (ind < longeur - 1):
                    suiv = valeursNumeriques[ind + 1]
                    if (suiv in listeValeursIncoherentes):
                        print("Vérifier les autres paramètres de santé ")
                    else:
                        print("valeur incohérente car la valeur suivante est normale")
                        print("valeur suivante normale : ", suiv)
                else:
                    print("la dernière valeur est anormale : vérifier les autres paramètres de santé")
                print("\n")
        plt.hist(valeursNumeriques)
        plt.xlabel(nom1)

        plt.ylabel("nombre de valeurs")
        nom_fig2="Histogramme "+nom+".png"
        plt.savefig(nom_fig2)
        plt.show()
