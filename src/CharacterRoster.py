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
                speed=12
            ),
            Character(
                name="Mage", 
                hp=80, 
                min_damage=3,
                max_damage=12, 
                critical_chance=15, 
                fumble_chance=10,
                speed=10
            ),
            Character(
                name="Paladin", 
                hp=150, 
                min_damage=1,
                max_damage=8, 
                critical_chance=5, 
                fumble_chance=5,
                speed=8
            ),
            Character(
                name="Voleur", 
                hp=90, 
                min_damage=2,
                max_damage=10, 
                critical_chance=20, 
                fumble_chance=5,
                speed=21
            ),
            Character(
                name="Chevalier", 
                hp=130, 
                min_damage=2,
                max_damage=9, 
                critical_chance=8, 
                fumble_chance=7,
                speed=11
            ),
            Character(
                name="Vampire", 
                hp=100, 
                min_damage=2,
                max_damage=9, 
                critical_chance=10, 
                fumble_chance=8,
                speed=14
            ),
            Character(
                name="Archer", 
                hp=85, 
                min_damage=1,
                max_damage=12, 
                critical_chance=25, 
                fumble_chance=15,
                speed=20
                
            ),
            Character(
                name="Berserker", 
                hp=110, 
                min_damage=4,
                max_damage=10, 
                critical_chance=15, 
                fumble_chance=10,
                speed=20
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