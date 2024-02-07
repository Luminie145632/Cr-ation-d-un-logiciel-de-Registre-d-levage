class LiaisonPages:
    def __init__(self, application):
        self.application = application

    def afficher_page_mouvement_temporaire(self):
        self.application.gestionnaire_pages.select(0)

    def afficher_page_particulier_professionnel(self):
        self.application.gestionnaire_pages.select(1)

    def afficher_page_accueil(self):
        self.application.gestionnaire_pages.select(2)
