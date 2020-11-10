class Setup:
	def __init__(self, prix, stock, config, marque, GPU, CPU):
		self.prix = prix
		self.stock = stock
		self.config = config
		self.marque = marque
		self.GPU = GPU
		self.CPU = CPU
gaming = Setup(2500, 10,"Gaming", "Asus","Rtx-3070", "i7-8700k")
print (gaming.GPU, gaming.CPU, "est au prix de", gaming.prix, "euros, il en reste", gaming.stock,"et c'est une config", gaming.config, "Il est de la marque", gaming.marque)

gaming = Setup(3500, 10,"Gaming", "MSI", "Rtx-3080 TI", "i9-9900k")
print (gaming.GPU, gaming.CPU, "est au prix de", gaming.prix, "il en reste", gaming.stock,"et c'est une config", gaming.config, "Il est de la marque", gaming.marque)