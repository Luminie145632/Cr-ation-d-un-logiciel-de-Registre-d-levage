import tkinter as tk
from tkinter import messagebox
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

class FenetrePrincipale(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Génération de PDF")

        self.setup_ui()

    def setup_ui(self):
        self.text_widget = tk.Text(self, wrap=tk.WORD)
        self.text_widget.pack(expand=True, fill=tk.BOTH)

        self.generate_pdf_button = tk.Button(self, text="Générer PDF", command=self.generate_pdf)
        self.generate_pdf_button.pack()

    def generate_pdf(self):
        content = self.text_widget.get("1.0", tk.END)
        if not content.strip():
            messagebox.showwarning("Avertissement", "Le contenu est vide.")
            return

        filename = "output.pdf"
        try:
            pdf_canvas = canvas.Canvas(filename, pagesize=letter)
            pdf_canvas.drawString(100, 750, content)
            pdf_canvas.save()
            messagebox.showinfo("Succès", "PDF généré avec succès : {}".format(filename))
        except Exception as e:
            messagebox.showerror("Erreur", "Une erreur est survenue lors de la génération du PDF : {}".format(str(e)))

if __name__ == "__main__":
    app = FenetrePrincipale()
    app.mainloop()
