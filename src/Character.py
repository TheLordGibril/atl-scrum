from typing import Self
import random

# Codes couleur ANSI
COLORS = {
    "RESET": "\033[0m",
    "RED": "\033[91m",
    "BLUE": "\033[94m",
    "GREEN": "\033[92m",
    "YELLOW": "\033[93m",
    "BOLD": "\033[1m"
}
def strip_ansi_codes(text):
    """Retire les codes ANSI d'une chaîne de caractères pour les logs texte"""
    import re
    ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
    return ansi_escape.sub('', text)

class Character:
    def __init__(self, name: str = "Character", team_color: str = "BLUE", 
                 hp: int = 100, min_damage: int = 0, max_damage: int = 10, 
                 critical_chance: int = 10, fumble_chance: int = 5,
                 speed: int = 10):
        self.name: str = name
        self.hp: int = hp
        self.max_hp: int = hp
        self.min_damage: int = min_damage
        self.max_damage: int = max_damage
        self.critical_chance: int = critical_chance  # Pourcentage de chance d'infliger des dégâts doubles
        self.fumble_chance: int = fumble_chance      # Pourcentage de chance de rater l'attaque
        self.speed: int = speed                      # Vitesse du personnage pour l'initiative
        self.is_dead: bool = False
        self.team_color: str = team_color
        self.message_log: list = []
        self.initiative_roll = 0        # Pour le jet d'initiative principal
        self.tiebreaker_roll = 0 
    
    def roll_initiative(self):
        """Lance un dé d'initiative pour départager les égalités de vitesse"""
        self.initiative_roll = random.randint(1, 20)
        return self.initiative_roll
    
    def get_colored_name(self):
        """Retourne le nom du personnage avec sa couleur d'équipe"""
        return f"{COLORS[self.team_color]}{self.name}{COLORS['RESET']}"
    
    def attack(self, enemy: Self):
        if not self.is_dead:
            # Vérification si l'attaque rate (fumble)
            if random.randint(1, 100) <= self.fumble_chance:
                fumble_msg = f"{self.get_colored_name()} rate complètement son attaque contre {enemy.get_colored_name()} !"
                self.message_log.append(fumble_msg)
                return
            
            # Calcul des dégâts aléatoires
            base_damage = random.randint(self.min_damage, self.max_damage)
            
            # Vérification d'un coup critique
            is_critical = random.randint(1, 100) <= self.critical_chance
            damage_dealt = base_damage * 2 if is_critical else base_damage
            
            if is_critical:
                attack_msg = f"{self.get_colored_name()} assène un {COLORS['YELLOW']}COUP CRITIQUE{COLORS['RESET']} à {enemy.get_colored_name()} pour {damage_dealt} points de dégâts!"
            else:
                attack_msg = f"{self.get_colored_name()} lance un dé a {self.max_damage} faces et obtient un {base_damage} ! Il attaque {enemy.get_colored_name()} pour {damage_dealt} points de dégâts"
            
            self.message_log.append(attack_msg)
            enemy.receive_damage(damage_dealt)
        else:
            death_msg = f"{self.get_colored_name()} ne peut pas attaquer car il est mort"
            self.message_log.append(death_msg)

    def receive_damage(self, damage: int):
        self.hp -= damage
        remaining_hp = max(0, self.hp)
        hp_percent = int((remaining_hp / self.max_hp) * 100)
        
        damage_msg = f"{self.get_colored_name()} reçoit {damage} points de dégâts ({remaining_hp}/{self.max_hp} HP - {hp_percent}%)"
        self.message_log.append(damage_msg)
        
        if self.hp <= 0:
            death_msg = f"{COLORS['BOLD']}{COLORS['RED']}{self.name} est mort !{COLORS['RESET']}"
            self.message_log.append(death_msg)
            self.is_dead = True
    
    def get_status_bar(self, width: int = 20):
        """Retourne une barre de progression visuelle des points de vie"""
        hp_percent = max(0, self.hp) / self.max_hp
        bar_length = int(width * hp_percent)
        
        if hp_percent > 0.7:
            color = COLORS["GREEN"]
        elif hp_percent > 0.3:
            color = COLORS["YELLOW"]
        else:
            color = COLORS["RED"]
        
        hp_bar = f"{color}{'█' * bar_length}{' ' * (width - bar_length)}{COLORS['RESET']}"
        return f"{self.get_colored_name()}: [{hp_bar}] {int(hp_percent*100)}%"
    
    def get_stats_display(self):
        """Affiche les statistiques du personnage"""
        return (f"{self.get_colored_name()}: {self.hp} HP, {self.min_damage}-{self.max_damage} DMG, "
                f"{self.critical_chance}% Crit, {self.fumble_chance}% Fumble, {self.speed} Vitesse")
    
    def clear_messages(self):
        """Vide le journal de messages et retourne les messages effacés"""
        messages = self.message_log.copy()
        self.message_log = []
        return messages