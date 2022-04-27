import matplotlib.pyplot as plt
import numpy as np
import time

def detection_Anomalies(file):
    f = open(file, "r")

    lines = f.readlines()

    newLines = []
    for line in lines:
        newLine1 = line.split(',')
        # print(newLine1)
        newLines.append(newLine1)
    i = 0

    error=0

    for line in newLines:
        i += 1

        attaque = False

        #Backdoor
        #Voici une règle qui caractérise une attaque backdoor

        if ((line[4] == "tcp") and (line[3] == "80" or line[3] == "8080") and (line[5] == "-" or line[5] == "smb") and (line[9] == "REJ") ):

            #On va vérifier qu'on à bien à faire à une attaque backdoor
            label = "backdoor\n"
            if (label != line[16]):

                #Si on a pas d'attaque on va incrémenter le nombre d'erreur
                print("erreur")
                error += 1
            else:
                print("backdoor "+ str(i))
                attaque = True





        if (line[4] == "tcp" and (line[9] == "S0" or line[9]=="REJ") and ((int(line[3]) > 100) and (line[3]!="8080"))):
            label = "scanning\n"
            if (label != line[16]):
                print("erreur");
                error += 1
            else:
                print("Scanning " + str(i));
                attaque = True






        if ((line[3] == line[1] and (int(line[3]) >= 11) and (int(line[3]) <= 79)) and line[4] == "tcp" and (line[9] == "REJ"or line[9]=="RSTO")):
            label = "dos\n";
            if (label != line[16]):
                print("erreur "+str(i) );
                error += 1
            else:
                print("dos");
                attaque = True
        if (line[3] == "19" and line[4] == "tcp" and line[9] == "SO"):

            label = "dos\n";
            if (label != line[16]):
                print("erreur");
                error += 1
            else:
                print("dos");
                attaque = True

        if(line[4]=="udp" and line[5]=="dns" and line[9]=="SF" and (line[14]=="broker.hivemq.com" )):

            label="dos\n"

            if (label != line[16]):
                print("erreur");
                error += 1
            else:
                print("dos");
                attaque = True





        if (line[3] == "80" and line[4] == "tcp" and line[5] == "http" and line[9] == "SF"):

            label = "injection\n"
            label2="password\n"
            if (label != line[16] and label2 !=line[16]):
                print("erreur");
                error += 1
            else:
                print("injection or password " + str(i));
                attaque = True

        if (line[3] == "80" and line[4] == "tcp" and line[5] == "-" and line[9] == "S2"):

            # Permet de vérifier qu'on a bien une attaque informatique
            label = "injection\n";
            if (label != line[16]):
                print("erreur");
                error += 1
            else:
                print("injection");
                attaque = True





        if ((line[3] == "80" or line[3] == "443") and (line[4] == "tcp") and (line[9] == "S1" or line[9] == "S3") ) or  (line[14]=="testphp.vulnweb.com/listproducts.php.hub" or line[14]=="testphp.vulnweb.com/listproducts.php"):
            label = "ddos\n "
            if (label != line[16]):
                print("erreur" + str(i));
                error += 1
            else:
                print("DDOS "+ str(i))
                attaque = True

        if(line[3]=="8080" and line[4]=="tcp" and (line[9]=="SF" or line[9]=="OTH")):

            label = "ddos\n"
            if (label != line[16]):
                print("erreur");
                error += 1
            else:
                print("DDOS " + str(i))
                attaque = True








        if (line[3] == "21" and line[3]!=line[1] and line[4] == "tcp" and line[5] == "-" and line[9] == "REJ"):
            label = "password\n";
            if (label != line[16]):
                print("erreur");
                error += 1
            else:
                print("password "+str(i));
                attaque = True




        if (line[3] == "80" and line[4] == "tcp" and (line[5] == "http" or line[5] == "-") and (
                (line[9] == "SH") or (line[9] == "SO") or (line[9] == "SHR") or (line[9] == "S3") or line[9] == "RSTR"  )):

            label = "xss\n"
            if (label != line[16]):
                print("erreur")
                error += 1
            else:
                print("XSS")
                attaque = True

        if ((line[5] == "dns") and (line[4] == "udp") and (line[9] == "SF") and (
                line[14] == "testphp.vulnweb.com" or line[14] == "www.mqtt-dashboard.com")):

            label = "1"
            if (label != line[15]):
                print("erreur");
                error += 1
            else:
                print("XSS");
                attaque = True

        if ((line[3] == "4444" or line[1] == "4444") and line[4] == "tcp" and line[9] == "OTH"):

            label = "ransomware\n";
            if (label != line[16]):
                print("erreur");
                error += 1
            else:
                print("ransomware");
                attaque = True
        if (line[3] == "445" and line[4] == "tcp" and line[9] == "OTH"):
            label = "ransomware\n";
            if (label != line[16]):
                print("erreur");
                error += 1
            else:
                print("ransomware");
                attaque = True
        if (line[3] == "135" and line[4] == "tcp" and (
                line[9] == "OTH" or line[9] == "SO" or line[9] == "SH" or line[9] == "SHR")):
            label = "ransomware\n";

            if (label != line[16]):
                print("erreur");
                error += 1
            else:
                print("ransomware");
                attaque = True
        if ((line[3] == "7870" or line[1] == "7870") and line[4] == "tcp" and line[9] == "OTH"):
            label = "ransomware\n";
            if (label != line[16]):
                print("erreur");
                error += 1
            else:
                print("ransomware");
                attaque = True


        if ((line[5] == "dns") and (line[4] == "udp") and (line[9] == "SF") and (
                line[14] == "detectportal.firefox.com" or line[14] == "detectportal.firefox.com.hub")):
            label = "mitm\n"
            if (label != line[16]):
                print("erreur")
                error += 1
            else:
                print("MITM ")
                attaque = True


        if ((line[3] == "443") and line[4] == "tcp" and line[5] == "ssl" and (line[9] == "RSTR" or line[9] == "SF")):
            label = "mitm\n"
            if (label != line[16]):
                print("erreur");
                error += 1
            else:
                print("MITM ");
                attaque = True


        if (line[4] == "icmp" and line[9] == "OTH"):
            label = "mitm\n"
            if (label != line[16]):
                print("erreur")
                error += 1
            else:
                print("MITM ")
                attaque = True

        if ((line[3] == "443") and line[4] == "tcp" and (line[9] == "RSTOS0" or line[9] == "RSTO")):
            label = "mitm\n"
            if (label != line[16]):
                print("erreur")
                error += 1
            else:
                print("MITM ")
                attaque = True

        else:
            if(attaque == False):
                label = "0"
                if (label != line[15]):
                    print("erreur " + str(i))
                    error+=1
                else:
                    print("normal "+ str(i))



    # On va calculer le taux d'erreur de notre algorithme qui est le nombre d'erreur divisé le nombre total de records.
    len=newLines.__len__()
    errorRate=error/len
    print("taux d'erreur : ",errorRate)


file = "C:\\Users\micka\OneDrive\Bureau\TER\\algo 2\\network_filtre.csv"

detection_Anomalies(file)