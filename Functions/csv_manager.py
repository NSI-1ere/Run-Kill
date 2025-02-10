import csv, os

class CSVManager:
    def __init__(self):
        self.chemin_repertoire = os.path.dirname(os.path.abspath(__file__))
        os.makedirs(self.chemin_repertoire + r'.\Save', exist_ok=True)
        self.csv_file = self.chemin_repertoire + r'.\Save\save.csv'

    def write_save_file(self, xp: int, inventory: list):
        with open(self.csv_file, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["xp", "inventory"])  # Header du .csv
            writer.writerow([xp, ";".join(inventory)])  # Autre ligne pour save les données

    def fetch_save_file(self):
        if not os.path.exists(self.csv_file):
            return 0, []  # Si le fichier existe pas

        with open(self.csv_file, mode="r", newline="", encoding="utf-8") as file: # r = read, on lit le fichier
            reader = csv.reader(file)
            next(reader, None)  # On skip le header

            try:
                xp, inventory = next(reader)  # On lit la première ligne (là où on stocke les données)
                return int(xp), inventory.split(";") if inventory else [] #.split crée une liste à partir d'un string (ex: "1;2;3".split(";") = [1, 2, 3])
            except StopIteration:
                return 0, []  # Si le fichier est vide

    def update_save_file(self, new_xp: int = None, new_inventory: list = None):
        """Sert à n'update qu'une seule valeur, pas les 2"""
        current_xp, current_inventory = self.fetch_save_file()

        # Utiliser les nouvelles valeurs fournies, sinon on garde les anciennes
        updated_xp = new_xp if new_xp is not None else current_xp
        updated_inventory = new_inventory if new_inventory is not None else current_inventory

        self.write_save_file(new_xp, updated_inventory)  # On sauvegarde