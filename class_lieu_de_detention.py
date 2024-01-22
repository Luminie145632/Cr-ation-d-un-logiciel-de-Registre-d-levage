# Définition de la classe lieu_de_detention
class LieuDeDetention:
    # Constructeur de la classe lieu_de_detention
    def __init__(self, denomination, adresse, type_activite, plan_du_lieu_de_detention, SIRE, particulier, professionnel, personne_physique, personne_morale, code_APE, statut_juridique, responsable_de_la_tenue_du_registre, coordonnées_du_detenteur, tel, portable, mail):
        # Attributs de la classe
        self.denomination = denomination
        self.adresse = adresse
        self.type_activite = type_activite
        self.plan_du_lieu_de_detention = plan_du_lieu_de_detention
        self.SIRE = SIRE
        self.particulier = particulier
        self.professionnel = professionnel
        self.personne_physique = personne_physique
        self.personne_morale = personne_morale
        self.code_APE = code_APE
        self.statut_juridique = statut_juridique
        self.responsable_de_la_tenue_du_registre = responsable_de_la_tenue_du_registre
        self.coordonnées_du_detenteur = coordonnées_du_detenteur
        self.tel = tel
        self.portable = portable
        self.mail = mail

        # Phrase qui donne les caractéristiques du lieu de détention où se trouve le cheval du propriétaire.
        print(f"Si le propriétaire est {self.personne_morale}, alors c'est un {self.professionnel} et le lieu où se trouve le cheval a une {self.statut_juridique}. Si le propriétaire est {self.particulier}. Le lieu où est gardé le cheval du propriétaire est {self.denomination}, situé à {self.adresse}. Pour vous y rendre, suivez le plan du lieu de détention : {self.plan_du_lieu_de_detention}. Cet endroit propose des activités liées aux {self.type_activite}, il a un {self.statut_juridique}, il a aussi pour SIRE {self.SIRE} et son code APE est {self.code_APE}. Le responsable de la tenue du registre a pour coordonnées son téléphone {self.tel}, son portable {self.portable} et son e-mail {self.mail}")

# Exemple d'utilisation de la classe
lieu_detention_cheval = LieuDeDetention("Stable de l'Étoile", "123 Rue des Écuries", "cours d'équitation", "123456789", "1234Z", False, True, True, False, "0123456789", "SAS", "Responsable Nom", "Coordonnées", "0123456789", "0612345678", "responsable@domaine.com")
