from Class_Setup import Setup
from Class_Client import Client

gaming = Setup(2500, 10,"Gameur", "Asus","Rtx-3080", "i7-8700k")
print (gaming.GPU, gaming.CPU, "est au prix de", gaming.prix, "euros, il en reste", gaming.stock,"et c'est une config", gaming.config, "Il est de la marque", gaming.marque)

gaming1 = Setup(3500, 10,"Gaming", "MSI", "Rtx-3080 TI", "i9-9900k")
print (gaming1.GPU, gaming1.CPU, "est au prix de", gaming1.prix, "il en reste", gaming1.stock,"et c'est une config", gaming1.config, "Il est de la marque", gaming1.marque)

client1 = Client(int(len(input(""))), int(len(input(""))), int(len(input(""))))