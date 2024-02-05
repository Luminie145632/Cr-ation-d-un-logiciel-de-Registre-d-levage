class Professionnel:
   def __init__(self,num_siret, code_ape, statut_juridique, denomination  ):#,nom, prenom, adresse, numero_telephone ,num_siret, code_ape, statut_juridique, denomination):
        
  #      super().__init__(self, nom, prenom, adresse, numero_telephone)
        self._num_siret = num_siret
        self._code_ape = code_ape
        self._statut_juridique = statut_juridique
        self._denomination = denomination
        
    # Accesseurs
   def get_num_siret(self):
        return self._num_siret

   def get_code_ape(self):
        return self._code_ape

   def get_statut_juridique(self):
        return self._statut_juridique

   def get_denomination(self):
        return self._denomination

    # Mutateurs
   def set_num_siret(self, num_siret):
        self._num_siret = num_siret

   def set_code_ape(self, code_ape):
        self._code_ape = code_ape

   def set_statut_juridique(self, statut_juridique):
        self._statut_juridique = statut_juridique
#yoouuuupi
   def set_denomination(self, denomination):
        self._denomination = denomination

# Exemple d'utilisation
if __name__ == "__main__":
    # Création d'une instance de la classe Professionnel
    professionnel = Professionnel(12345678901234, 1234, "SAS", "Nom Entreprise")

    # Utilisation des accesseurs
    print("Numéro de SIRET:", professionnel.get_num_siret())
    print("Code APE:", professionnel.get_code_ape())
    print("Statut juridique:", professionnel.get_statut_juridique())
    print("Dénomination:", professionnel.get_denomination())

    # Utilisation des mutateurs
    professionnel.set_num_siret(98765432109876)
    professionnel.set_code_ape(5678)
    professionnel.set_statut_juridique("SARL")
    professionnel.set_denomination("Nouvelle Entreprise")

    # Affichage des valeurs mises à jour
    print("\nValeurs mises à jour:")
    print("Numéro de SIRET:", professionnel.get_num_siret())
    print("Code APE:", professionnel.get_code_ape())
    print("Statut juridique:", professionnel.get_statut_juridique())
    print("Dénomination:", professionnel.get_denomination())