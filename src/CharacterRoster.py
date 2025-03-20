from src.Character import Character

class CharacterRoster:
    @staticmethod
    def get_all_characters():
        """Retourne la liste de tous les personnages disponibles avec différentes stats"""
        return [
            Character(
                name="Guerrier", 
                hp=120, 
                min_damage=2,
                max_damage=10, 
                critical_chance=10, 
                fumble_chance=5,
                armor=8
            ),
            Character(
                name="Mage", 
                hp=80, 
                min_damage=3,
                max_damage=12, 
                critical_chance=15, 
                fumble_chance=10,
                armor=3,
            ),
            Character(
                name="Paladin", 
                hp=150, 
                min_damage=1,
                max_damage=8, 
                critical_chance=5, 
                fumble_chance=5,
                armor=15,
            ),
            Character(
                name="Voleur", 
                hp=90, 
                min_damage=2,
                max_damage=10, 
                critical_chance=20, 
                fumble_chance=5,
                armor=5,
            ),
            Character(
                name="Chevalier", 
                hp=130, 
                min_damage=2,
                max_damage=9, 
                critical_chance=8, 
                fumble_chance=7,
                armor=10,
            ),
            Character(
                name="Vampire", 
                hp=100, 
                min_damage=2,
                max_damage=9, 
                critical_chance=10, 
                fumble_chance=8,
                armor=6,
            ),
            Character(
                name="Archer", 
                hp=85, 
                min_damage=1,
                max_damage=12, 
                critical_chance=25, 
                fumble_chance=15,
                armor=4,
            ),
            Character(
                name="Berserker", 
                hp=110, 
                min_damage=4,
                max_damage=10, 
                critical_chance=15, 
                fumble_chance=10,
                armor=0,
            )
        ]
    
    @staticmethod
    def get_character_description(index):
        """Retourne la description d'un personnage basé sur son index"""
        descriptions = [
            "Guerrier: Robuste et équilibré. Bon rapport entre HP et dégâts.",
            "Mage: Faible en défense mais fort en attaque.",
            "Paladin: Très résistant, dégâts moyens mais fiable.",
            "Voleur: Rapide et agile, spécialiste des coups critiques.",
            "Chevalier: Bon équilibre entre attaque et défense.",
            "Vampire: Équilibré dans toutes les statistiques.",
            "Archer: Précis mais fragile, peut faire beaucoup de dégâts ou rater complètement.",
            "Berserker: Fort en attaque, dégâts minimums élevés."
        ]
        return descriptions[index]