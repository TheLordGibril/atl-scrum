from src.Character import Character

class CharacterRoster:
    @staticmethod
    def get_all_characters():
        """Retourne la liste de tous les personnages disponibles avec différentes stats"""
        return [
            Character(
                name="Guerrier", 
                hp=120,
                strength= 10,
                critical_chance=10, 
                fumble_chance=5,
                speed=12,
                armor=8,
                weapon=5
            ),
            Character(
                name="Mage", 
                hp=80,
                strength= 1,
                critical_chance=15, 
                fumble_chance=10,
                speed=10,
                armor=3,
                weapon=1
            ),
            Character(
                name="Paladin", 
                hp=150, 
                strength= 1,
                critical_chance=5, 
                fumble_chance=5,
                speed=8,
                armor=15,
                weapon=1
            ),
            Character(
                name="Voleur", 
                hp=90,
                strength= 5,
                critical_chance=20, 
                fumble_chance=5,
                speed=21,
                armor=5,
                weapon=5
            ),
            Character(
                name="Chevalier", 
                hp=130, 
                strength= 5,
                critical_chance=8, 
                fumble_chance=7,
                speed=11,
                armor=10,
                weapon=3
            ),
            Character(
                name="Vampire", 
                hp=100,
                strength= 10, 
                critical_chance=10, 
                fumble_chance=8,
                speed=14,
                armor=6,
                weapon=8
            ),
            Character(
                name="Archer", 
                hp=85,
                strength= 3, 
                critical_chance=25, 
                fumble_chance=15,
                speed=20,
                armor=4,
                weapon=6
            ),
            Character(
                name="Berserker", 
                hp=110,
                strength= 5, 
                critical_chance=15, 
                fumble_chance=10,
                speed=20,
                armor=0,
                weapon=10
            )
        ]
    
    @staticmethod
    def get_character_description(index):
        """Retourne la description d'un personnage basé sur son index"""
        descriptions = [
            "Guerrier: Robuste et équilibré. Bon rapport entre HP et dégâts. Vitesse moyenne.",
            "Mage: Faible en défense mais fort en attaque. Vitesse moyenne.",
            "Paladin: Très résistant, dégâts moyens mais fiable. Vitesse lente.",
            "Voleur: Rapide et agile, spécialiste des coups critiques. vitesse ultra rapide.",
            "Chevalier: Bon équilibre entre attaque et défense. Vitesse moyenne.",
            "Vampire: Équilibré dans toutes les statistiques. Vitesse élevée.",
            "Archer: Précis mais fragile, peut faire beaucoup de dégâts ou rater complètement. Bonne vitesse.",
            "Berserker: Fort en attaque, dégâts minimums élevés. Vitesse ultra rapide."
        ]
        return descriptions[index]