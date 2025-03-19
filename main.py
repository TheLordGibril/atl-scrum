from src.Character import Character, COLORS, strip_ansi_codes
from src.CharacterRoster import CharacterRoster
import time
import os
import shutil
import random
import datetime
import sys
import threading
import queue
import keyboard

def clear_screen():
    """Nettoie l'écran du terminal"""
    os.system('cls' if os.name == 'nt' else 'clear')

def get_terminal_size():
    """Retourne la largeur et hauteur du terminal"""
    columns, lines = shutil.get_terminal_size()
    return columns, lines

# Générateur de noms médiévaux fantastiques
def generate_medieval_name():
    """Génère un nom aléatoire à consonance médiévale fantastique"""
    prefixes = [
        "Ael", "Aer", "Af", "Ak", "Al", "Am", "An", "Ar", "Arn", "Ash", "Az",
        "Bal", "Ban", "Bar", "Bel", "Ber", "Bol", "Bor", "Bran", "Brom", "Brun",
        "Cal", "Cam", "Cas", "Caw", "Cel", "Cen", "Crag", "Dain", "Dal", "Dan",
        "Dar", "Day", "Dor", "Duer", "Dun", "Dur", "Dwal", "Ed", "Ein", "El",
        "Elb", "Eld", "Eow", "Er", "Ere", "Erf", "Ern", "Estel", "Eth", "Fal",
        "Far", "Farin", "Fel", "Fen", "Fer", "Fin", "Flint", "Frar", "Frea", "Frerin",
        "Gal", "Gam", "Gan", "Gar", "Gem", "Gil", "Gim", "Gloin", "Glor", "Gob",
        "Gol", "Gor", "Gor", "Gram", "Gran", "Grim", "Grin", "Gry", "Gul",
        "Hal", "Har", "Hel", "Hen", "Hor", "Huor", "Hur", "Ig", "Il", "Is",
        "Jar", "Jor", "Kas", "Kaz", "Kel", "Khal", "Kil", "Kith", "Kol", "Lag",
        "Lam", "Leaf", "Leg", "Lin", "Lor", "Luth", "Mal", "Mar", "Mer", "Mir",
        "Mor", "Muir", "Mur", "Nag", "Nar", "Nef", "Nor", "Nyl", "Ob", "Oc",
        "Od", "Og", "Or", "Ow", "Pel", "Per", "Pyr", "Rag", "Ran", "Ray",
        "Ren", "Rol", "Roth", "Ry", "Sig", "Sin", "Skald", "Son", "Stone", "Storm",
        "Svar", "Syr", "Tal", "Tan", "Tar", "Tav", "Tel", "Thal", "Thor", "Thrain",
        "Thror", "Thur", "Tib", "Tor", "Ty", "Ul", "Ur", "Val", "Van", "Var", "Vil",
        "Von", "Vor", "War", "Wind", "Wulf", "Yew", "Yor", "Yrl", "Zar"
    ]
    
    suffixes = [
        "ac", "ail", "ain", "aire", "ald", "ale", "an", "and", "ar", "ard",
        "as", "ash", "at", "ath", "ayne", "azar", "bard", "barik", "bas", "bean",
        "bek", "bor", "born", "bur", "cas", "claw", "coil", "dain", "dar", "dark",
        "dil", "din", "dir", "dor", "doth", "dred", "drin", "dun", "dust", "fang",
        "far", "fast", "fel", "fin", "fire", "fist", "foot", "for", "frost", "fume",
        "fur", "gan", "gar", "gas", "gate", "gath", "gil", "gold", "gorn", "goth",
        "grim", "gun", "had", "hail", "hal", "hand", "har", "hawk", "heart", "helm",
        "horn", "ia", "ian", "ice", "il", "in", "iner", "ion", "ir", "is",
        "ith", "ka", "kath", "ki", "kil", "kin", "kith", "lan", "las", "ler",
        "ley", "li", "light", "lin", "loch", "lor", "lum", "mane", "mer", "mir",
        "mond", "mor", "more", "nar", "nath", "nir", "nor", "nus", "ny", "nyd",
        "or", "orn", "ory", "osh", "oth", "ow", "radoc", "rain", "rak", "ram",
        "ran", "rand", "ray", "ril", "rim", "rin", "rion", "rod", "roth", "rune",
        "ryl", "sam", "san", "sath", "say", "sel", "sgor", "shadow", "shek", "shield",
        "shin", "shir", "sil", "skin", "skull", "smith", "soil", "soul", "spear", "steel",
        "stone", "storm", "sun", "sword", "thal", "thalas", "thar", "thel", "thor", "thorne",
        "thul", "thus", "til", "ton", "tor", "tuk", "tur", "val", "van", "var",
        "veld", "ver", "vik", "vor", "wald", "ward", "wind", "wine", "wood", "wrath",
        "wyn", "xus", "yr", "yth", "zar", "zen", "zin", "zor", "zur"
    ]
    
    name_parts = []
    
    # Décide aléatoirement si on utilise 1 préfixe et 1 suffixe, ou 1 préfixe et 2 suffixes
    if random.random() < 0.7:  # 70% de chance d'avoir 1 préfixe et 1 suffixe
        name_parts.append(random.choice(prefixes))
        name_parts.append(random.choice(suffixes))
    else:  # 30% de chance d'avoir 1 préfixe et 2 suffixes
        name_parts.append(random.choice(prefixes))
        
        # Évite les doublons de suffixes
        first_suffix = random.choice(suffixes)
        second_suffix = random.choice([s for s in suffixes if s != first_suffix])
        
        name_parts.append(first_suffix)
        name_parts.append(second_suffix)
    
    return "".join(name_parts)


def print_logs(filename):
    f = open(filename,"r")
    contents = f.read()
    print(contents)


# Fonction pour quitter l'application
def exit_application():
    """Quitte l'application proprement"""
    print(f"\n{COLORS['YELLOW']}Fermeture de l'application...{COLORS['RESET']}")
    # Désactive tous les hooks de clavier avant de quitter
    keyboard.unhook_all()
    time.sleep(0.5)  # Donne le temps à l'utilisateur de voir le message
    sys.exit(0)

# Fonction pour configurer la touche Échap pour quitter
def setup_exit_key():
    """Configure la touche Échap pour quitter l'application"""
    keyboard.on_press_key("esc", lambda e: exit_application())

class BattleLogger:
    """Classe pour enregistrer et sauvegarder les logs de bataille"""
    def __init__(self):
        self.battle_log = []
        self.start_time = datetime.datetime.now()
    
    def add_log(self, message):
        """Ajoute un message au log avec horodatage"""
        timestamp = datetime.datetime.now().strftime("%H:%M:%S")
        clean_message = strip_ansi_codes(message)
        self.battle_log.append(f"[{timestamp}] {clean_message}")
    
    def add_round_separator(self, round_num):
        """Ajoute un séparateur de tour"""
        self.battle_log.append("\n" + "=" * 40)
        self.battle_log.append(f"ROUND {round_num}")
        self.battle_log.append("=" * 40)
    
    def save_to_file(self, team1_name, team2_name, winner):
        """Sauvegarde les logs dans un fichier"""
        # Crée un dossier logs s'il n'existe pas
        if not os.path.exists("logs"):
            os.makedirs("logs")
        
        # Nom du fichier avec date et heure
        date_str = self.start_time.strftime("%Y%m%d_%H%M%S")
        filename = f"logs/battle_{team1_name}_vs_{team2_name}_{date_str}.txt"
        
        with open(filename, "w", encoding="utf-8") as f:
            # En-tête
            f.write("=" * 60 + "\n")
            f.write(f"COMBAT : {team1_name} VS {team2_name}\n")
            f.write(f"Date: {self.start_time.strftime('%d/%m/%Y %H:%M:%S')}\n")
            f.write(f"Vainqueur: {winner}\n")
            f.write("=" * 60 + "\n\n")
            
            # Contenu du log
            for line in self.battle_log:
                f.write(line + "\n")
            
            # Pied de page
            f.write("\n" + "=" * 60 + "\n")
            f.write(f"FIN DU COMBAT - {datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
        
        return filename
    



class BattleSpeedController:
    """Classe pour contrôler la vitesse et la pause du combat"""
    def __init__(self):
        self.speed_factor = 1.0  # Normal
        self.paused = False
        self.speed_levels = {
            0.0: "PAUSE",
            0.5: "LENT",
            1.0: "NORMAL",
            2.0: "RAPIDE",
            5.0: "TRÈS RAPIDE",
            10.0: "TURBO"
        }
        self.speed_index = 2  # Index correspondant à 1.0 (normal)
        self.speed_values = list(self.speed_levels.keys())
        
        # Configuration des touches
        self.setup_keyboard_listeners()
    
    def setup_keyboard_listeners(self):
        """Configure les écouteurs de clavier"""
        keyboard.on_press_key("p", lambda e: self.toggle_pause())
        keyboard.on_press_key("right", lambda e: self.increase_speed())
        keyboard.on_press_key("left", lambda e: self.decrease_speed())
        # Ajoute la touche Échap pour quitter l'application
        keyboard.on_press_key("esc", lambda e: exit_application())
    
    def toggle_pause(self):
        """Basculer entre pause et reprise"""
        if self.paused:
            self.paused = False
            self.speed_factor = self.speed_values[self.speed_index]
        else:
            self.paused = True
            self.speed_factor = 0.0
    
    def increase_speed(self):
        """Augmente la vitesse"""
        if self.speed_index < len(self.speed_values) - 1:
            self.speed_index += 1
            self.speed_factor = self.speed_values[self.speed_index]
            self.paused = (self.speed_factor == 0.0)
    
    def decrease_speed(self):
        """Diminue la vitesse"""
        if self.speed_index > 0:
            self.speed_index -= 1
            self.speed_factor = self.speed_values[self.speed_index]
            self.paused = (self.speed_factor == 0.0)
    
    def get_speed_name(self):
        """Retourne le nom du niveau de vitesse actuel"""
        return self.speed_levels[self.speed_values[self.speed_index]]
    
    def wait(self, seconds):
        """Attend le temps spécifié, ajusté selon la vitesse et gère la pause"""
        adjusted_time = seconds / self.speed_factor if self.speed_factor > 0 else 0
        
        if self.paused:
            # Attente active pendant la pause
            print(f"\r{COLORS['YELLOW']}⏸️  PAUSE - Appuyez sur P pour reprendre{COLORS['RESET']}   ", end="", flush=True)
            while self.paused:
                time.sleep(0.1)
            print("\r" + " " * 50 + "\r", end="", flush=True)  # Efface le message de pause
        
        if adjusted_time > 0:
            time.sleep(adjusted_time)

def display_character_selection():
    """Affiche le menu de sélection des personnages"""
    clear_screen()
    width, _ = get_terminal_size()
    
    print(f"{COLORS['BOLD']}{'=' * width}{COLORS['RESET']}")
    print(f"{COLORS['BOLD']}{' SÉLECTION DES PERSONNAGES '.center(width, '=')}{COLORS['RESET']}")
    print(f"{COLORS['BOLD']}{'=' * width}{COLORS['RESET']}")
    
    characters = CharacterRoster.get_all_characters()
    
    for i, character in enumerate(characters):
        print(f"{COLORS['BOLD']}[{i+1}]{COLORS['RESET']} {character.name}")
        print(f"    {CharacterRoster.get_character_description(i)}")
        print(f"    HP: {character.hp} | Dégâts: {character.min_damage}-{character.max_damage}")
        print(f"    Critique: {character.critical_chance}% | Fumble: {character.fumble_chance}% | Vitesse: {character.speed}")
        print()
    
    return characters

def interactive_character_selection(characters, team_name, team_color, team_size):
    """
    Interface interactive pour sélectionner les personnages avec les flèches et Entrée
    Version corrigée pour mieux gérer les touches directionnelles
    """
    import keyboard
    import time
    
    team = []
    current_index = 0  # Personnage actuellement sélectionné
    
    # Désactive les hooks existants pour éviter les conflits
    keyboard.unhook_all()
    
    # Ajoute la touche Échap pour quitter l'application
    keyboard.on_press_key("esc", lambda e: exit_application())
    
    for char_num in range(team_size):
        current_index = 0
        selected = False
        exit_selection = False
        
        # Affiche l'écran initial
        clear_screen()
        display_selection_screen(characters, current_index, team_name, team_color, char_num, team_size, team)
        
        # Pour éviter les déclenchements trop rapides
        last_key_time = time.time()
        key_cooldown = 0.2  # secondes
        
        while not selected and not exit_selection:
            # Approche différente - vérification directe des touches
            current_time = time.time()
            
            # Vérification des touches avec délai pour éviter les répétitions trop rapides
            if current_time - last_key_time > key_cooldown:
                moved = False
                
                # Vérifie les différentes variantes des noms de touches pour plus de compatibilité
                if keyboard.is_pressed('down') or keyboard.is_pressed('down arrow'):
                    current_index = (current_index + 1) % len(characters)
                    moved = True
                    last_key_time = current_time
                    
                elif keyboard.is_pressed('up') or keyboard.is_pressed('up arrow'):
                    current_index = (current_index - 1) % len(characters)
                    moved = True
                    last_key_time = current_time
                    
                elif keyboard.is_pressed('enter') or keyboard.is_pressed('return'):
                    selected = True
                    last_key_time = current_time
                    
                elif keyboard.is_pressed('esc') or keyboard.is_pressed('escape'):
                    exit_selection = True
                    last_key_time = current_time
                
                if moved:
                    clear_screen()
                    display_selection_screen(characters, current_index, team_name, team_color, char_num, team_size, team)
            
            # Petite pause pour éviter de surcharger le CPU
            time.sleep(0.05)
        
        if exit_selection:
            # Si l'utilisateur appuie sur Échap pendant la sélection des personnages,
            # nous quittons l'application complètement
            exit_application()
        
        # Crée une copie du personnage choisi avec un nom médiéval aléatoire
        if selected:
            selected_char = characters[current_index]
            
            # Génère un nom médiéval fantastique aléatoire
            medieval_name = generate_medieval_name()
            
            character = Character(
                name=f"{selected_char.name} {medieval_name}",
                team_color=team_color,
                hp=selected_char.hp,
                min_damage=selected_char.min_damage,
                max_damage=selected_char.max_damage,
                critical_chance=selected_char.critical_chance,
                fumble_chance=selected_char.fumble_chance,
                speed=selected_char.speed
            )
            team.append(character)
            
            # Confirmation visuelle de la sélection
            clear_screen()
            display_selection_screen(characters, current_index, team_name, team_color, char_num, team_size, team)
            print(f"\n{COLORS['GREEN']}Personnage {selected_char.name} '{medieval_name}' ajouté à l'équipe {team_name}!{COLORS['RESET']}")
            time.sleep(0.8)  # Pause brève pour montrer la confirmation
    
    # Réinitialise les hooks du clavier
    keyboard.unhook_all()
    
    return team

def select_team_members_manual(team_name, team_color, available_characters, team_size):
    """
    Méthode alternative de sélection avec input() standard en cas de problèmes avec le clavier
    """
    print(f"\n{COLORS[team_color]}=== ÉQUIPE {team_name} (Choisissez {team_size} personnages) ==={COLORS['RESET']}")
    
    # Configure la touche Échap pour quitter
    setup_exit_key()
    
    team = []
    for i in range(team_size):
        clear_screen()
        width, _ = get_terminal_size()
        
        print(f"{COLORS['BOLD']}{'=' * width}{COLORS['RESET']}")
        print(f"{COLORS[team_color]}{f' SÉLECTION DES PERSONNAGES - ÉQUIPE {team_name} ({i+1}/{team_size}) '.center(width, '=')}{COLORS['RESET']}")
        print(f"{COLORS['BOLD']}{'=' * width}{COLORS['RESET']}\n")
        
        # Affiche les personnages déjà sélectionnés
        if i > 0:
            print(f"{COLORS[team_color]}Personnages déjà sélectionnés pour l'équipe {team_name}:{COLORS['RESET']}")
            for j, char in enumerate(team):
                print(f"  {j+1}. {char.name}")
            print()
        
        # Affiche la liste des personnages disponibles
        for j, character in enumerate(available_characters):
            print(f"{COLORS['BOLD']}[{j+1}]{COLORS['RESET']} {character.name}")
            print(f"    {CharacterRoster.get_character_description(j)}")
            print(f"    HP: {character.hp} | Dégâts: {character.min_damage}-{character.max_damage}")
            print(f"    Critique: {character.critical_chance}% | Fumble: {character.fumble_chance}% | Vitesse: {character.speed}\n")
        
        # Demande la sélection
        while True:
            try:
                choice = int(input(f"Choisissez un personnage (1-{len(available_characters)}): "))
                if 1 <= choice <= len(available_characters):
                    selected_char = available_characters[choice-1]
                    
                    # Génère un nom médiéval fantastique aléatoire
                    medieval_name = generate_medieval_name()
                    
                    character = Character(
                        name=f"{selected_char.name} {medieval_name}",
                        team_color=team_color,
                        hp=selected_char.hp,
                        min_damage=selected_char.min_damage,
                        max_damage=selected_char.max_damage,
                        critical_chance=selected_char.critical_chance,
                        fumble_chance=selected_char.fumble_chance,
                        speed=selected_char.speed
                    )
                    team.append(character)
                    print(f"{COLORS['GREEN']}Personnage {selected_char.name} '{medieval_name}' ajouté à l'équipe {team_name}!{COLORS['RESET']}")
                    time.sleep(0.8)
                    break
                else:
                    print(f"{COLORS['RED']}Choix invalide. Veuillez entrer un nombre entre 1 et {len(available_characters)}.{COLORS['RESET']}")
            except ValueError:
                print(f"{COLORS['RED']}Veuillez entrer un nombre valide.{COLORS['RESET']}")
    
    return team

def display_selection_screen(characters, current_index, team_name, team_color, char_num, team_size, team):
    """
    Fonction séparée pour afficher l'écran de sélection, pour faciliter le rafraîchissement
    """
    width, _ = get_terminal_size()
    
    # Affiche l'en-tête
    print(f"{COLORS['BOLD']}{'=' * width}{COLORS['RESET']}")
    header_text = f" SÉLECTION DES PERSONNAGES - ÉQUIPE {team_name} ({char_num+1}/{team_size}) "
    print(f"{COLORS[team_color]}{header_text.center(width, '=')}{COLORS['RESET']}")
    print(f"{COLORS['BOLD']}{'=' * width}{COLORS['RESET']}")
    
    # Instructions
    print(f"\n{COLORS['YELLOW']}Utilisez les flèches ↑/↓ pour naviguer et Entrée pour sélectionner{COLORS['RESET']}")
    print(f"{COLORS['YELLOW']}Appuyez sur Échap pour quitter l'application{COLORS['RESET']}\n")
    
    # Affiche la liste des personnages
    for i, character in enumerate(characters):
        # Met en évidence le personnage actuellement sélectionné
        if i == current_index:
            highlight = f"{COLORS['BOLD']}{COLORS[team_color]}➤ "
            end_highlight = f" ←{COLORS['RESET']}"
        else:
            highlight = "  "
            end_highlight = ""
        
        print(f"{highlight}[{i+1}] {character.name}{end_highlight}")
        
        # Affiche la description et les stats uniquement pour le personnage sélectionné
        if i == current_index:
            print(f"    {CharacterRoster.get_character_description(i)}")
            print(f"    HP: {character.hp} | Dégâts: {character.min_damage}-{character.max_damage}")
            print(f"    Critique: {character.critical_chance}% | Fumble: {character.fumble_chance}% | Vitesse: {character.speed}")
        print()
    
    # Liste des personnages déjà sélectionnés
    if char_num > 0:
        print(f"\n{COLORS[team_color]}Personnages déjà sélectionnés pour l'équipe {team_name}:{COLORS['RESET']}")
        for i, char in enumerate(team):
            print(f"  {i+1}. {char.name}")

def select_team_members_interactive(team_name, team_color, available_characters, team_size):
    """Version améliorée qui utilise la sélection interactive"""
    print(f"\n{COLORS[team_color]}=== ÉQUIPE {team_name} (Choisissez {team_size} personnages) ==={COLORS['RESET']}")
    print("\nVous allez maintenant sélectionner les personnages avec les flèches et Entrée.")
    print(f"{COLORS['YELLOW']}Appuyez sur Échap à tout moment pour quitter l'application{COLORS['RESET']}")
    input("Appuyez sur Entrée pour continuer...")
    
    return interactive_character_selection(available_characters, team_name, team_color, team_size)

def display_team_battle(team1, team2, speed_controller, round_num):
    """Affiche l'état actuel de la bataille entre deux équipes"""
    clear_screen()
    width, _ = get_terminal_size()
    half_width = width // 2 - 5
    separator = f"{COLORS['BOLD']}|{COLORS['RESET']}"
    
    # Réduction de la taille des barres de vie pour éviter le problème de retour à la ligne
    bar_width = half_width - 25  # Réduction de la largeur pour éviter le débordement
    
    # Affiche l'en-tête avec le numéro de round actuel
    print(f"{COLORS['BLUE']}{'ÉQUIPE BLEUE'.center(half_width)}{COLORS['RESET']}{separator}{COLORS['RED']}{'ÉQUIPE ROUGE'.center(half_width)}{COLORS['RESET']}")
    
    # Affiche le round actuel
    round_display = f"ROUND ACTUEL: {COLORS['BOLD']}{round_num}{COLORS['RESET']}"
    print(f"{COLORS['YELLOW']}{round_display.center(width)}{COLORS['RESET']}")
    
    # Affiche les contrôles
    controls = f"[◀] Ralentir | [P] Pause | [▶] Accélérer | [ESC] Quitter | Vitesse: {speed_controller.get_speed_name()}"
    print(f"{COLORS['YELLOW']}{controls.center(width)}{COLORS['RESET']}")
    print("-" * width)
    
    # Affiche les membres des équipes et leurs barres de vie
    max_members = max(len(team1), len(team2))
    
    for i in range(max_members):
        left_bar = team1[i].get_status_bar(bar_width) if i < len(team1) else " " * half_width
        right_bar = team2[i].get_status_bar(bar_width) if i < len(team2) else " " * half_width
        print(f"{left_bar}{' ' * 5}{separator}{' ' * 5}{right_bar}")
    
    print("-" * width)
    
    # Récupère les messages des deux équipes
    all_messages = []
    for char in team1:
        all_messages.extend(char.clear_messages())
    for char in team2:
        all_messages.extend(char.clear_messages())
    
    # Retourne les messages pour le logger
    return all_messages

def determine_turn_order(team1, team2, battle_logger):
    """
    Détermine l'ordre de jeu en fonction de la vitesse des personnages.
    En cas d'égalité, un jet d'initiative est fait.
    """
    # Récupère tous les personnages vivants
    all_living_characters = get_living_characters(team1) + get_living_characters(team2)
    
    # Lance un dé d'initiative pour chaque personnage
    for character in all_living_characters:
        initiative_roll = character.roll_initiative()
        battle_logger.add_log(f"{character.get_colored_name()} lance un dé d'initiative: {initiative_roll}")
    
    # Trie les personnages par vitesse (du plus rapide au plus lent)
    # En cas d'égalité, utilise le jet d'initiative
    sorted_characters = sorted(
        all_living_characters, 
        key=lambda x: (x.speed, x.initiative_roll),
        reverse=True
    )
    
    # Journalisation de l'ordre des tours
    battle_logger.add_log("Ordre des tours pour ce round:")
    for i, character in enumerate(sorted_characters):
        battle_logger.add_log(f"{i+1}. {character.get_colored_name()} (Vitesse: {character.speed}, Initiative: {character.initiative_roll})")
    
    return sorted_characters

def team_is_defeated(team):
    """Vérifie si tous les membres d'une équipe sont morts"""
    return all(character.is_dead for character in team)

def get_living_characters(team):
    """Retourne la liste des personnages encore en vie dans l'équipe"""
    return [char for char in team if not char.is_dead]

def main():
    # Initialisation du logger et du contrôleur de vitesse
    battle_logger = BattleLogger()
    speed_controller = BattleSpeedController()
    
    try:
        # Configure la touche Échap pour quitter l'application
        setup_exit_key()
        
        # Affichage du titre du jeu
        clear_screen()
        width, _ = get_terminal_size()
        title = "BATAILLE D'ÉQUIPES"
        
        print(f"{COLORS['BOLD']}{title.center(width)}{COLORS['RESET']}")
        print(f"{COLORS['BOLD']}{'=' * width}{COLORS['RESET']}")
        print("\nBienvenue dans le jeu de combat d'équipes!")
        print(f"{COLORS['YELLOW']}Appuyez sur Échap à tout moment pour quitter l'application{COLORS['RESET']}")
        
        # Ajoute un log d'entrée
        battle_logger.add_log("Démarrage du jeu")
        
        # Demande la taille de l'équipe Bleue
        while True:
            try:
                team1_size = int(input("\nCombien de personnages pour l'équipe BLEUE? (1-4): "))
                if 1 <= team1_size <= 4:
                    break
                else:
                    print(f"{COLORS['RED']}Veuillez entrer un nombre entre 1 et 4.{COLORS['RESET']}")
            except ValueError:
                print(f"{COLORS['RED']}Veuillez entrer un nombre valide.{COLORS['RESET']}")

        # Demande la taille de l'équipe Rouge
        while True:
            try:
                team2_size = int(input("\nCombien de personnages pour l'équipe ROUGE? (1-4): "))
                if 1 <= team2_size <= 4:
                    break
                else:
                    print(f"{COLORS['RED']}Veuillez entrer un nombre entre 1 et 4.{COLORS['RESET']}")
            except ValueError:
                print(f"{COLORS['RED']}Veuillez entrer un nombre valide.{COLORS['RESET']}")

        battle_logger.add_log(f"Taille équipe BLEUE: {team1_size} personnages")
        battle_logger.add_log(f"Taille équipe ROUGE: {team2_size} personnages")
        
        # Sélection des personnages
        available_characters = CharacterRoster.get_all_characters()
        
        # Sélection de l'équipe 1 (bleue) avec l'interface interactive
        team1 = select_team_members_interactive("BLEUE", "BLUE", available_characters, team1_size)
        
        # Log des personnages choisis pour l'équipe 1
        battle_logger.add_log("Équipe BLEUE composée de:")
        for char in team1:
            battle_logger.add_log(f"- {char.name}: {char.hp} HP, {char.min_damage}-{char.max_damage} DMG, {char.critical_chance}% Crit, {char.fumble_chance}% Fumble, {char.speed} Vitesse")
        
        # Sélection de l'équipe 2 (rouge) avec l'interface interactive
        team2 = select_team_members_interactive("ROUGE", "RED", available_characters, team2_size)
        
        # Log des personnages choisis pour l'équipe 2
        battle_logger.add_log("Équipe ROUGE composée de:")
        for char in team2:
            battle_logger.add_log(f"- {char.name}: {char.hp} HP, {char.min_damage}-{char.max_damage} DMG, {char.critical_chance}% Crit, {char.fumble_chance}% Fumble, {char.speed} Vitesse")
        
        # Équilibrage optionnel pour les équipes de tailles différentes
        if team1_size < team2_size:
            # Bonus pour l'équipe 1 qui est plus petite
            bonus_factor = round(team2_size / team1_size, 1)  # Facteur de bonus basé sur le ratio
            print(f"\n{COLORS['BLUE']}Bonus d'équilibrage pour l'équipe BLEUE (équipe plus petite):{COLORS['RESET']}")
            for character in team1:
                character.hp = int(character.hp * bonus_factor)
                character.max_hp = character.hp
                character.min_damage = int(character.min_damage * bonus_factor)
                character.max_damage = int(character.max_damage * bonus_factor)
                battle_logger.add_log(f"Bonus appliqué à {character.name}: stats x{bonus_factor}")
                print(f"- {character.name}: stats x{bonus_factor}")
            time.sleep(1.5)  # Pause pour que le joueur puisse lire

        elif team2_size < team1_size:
            # Bonus pour l'équipe 2 qui est plus petite
            bonus_factor = round(team1_size / team2_size, 1)
            print(f"\n{COLORS['RED']}Bonus d'équilibrage pour l'équipe ROUGE (équipe plus petite):{COLORS['RESET']}")
            for character in team2:
                character.hp = int(character.hp * bonus_factor)
                character.max_hp = character.hp
                character.min_damage = int(character.min_damage * bonus_factor)
                character.max_damage = int(character.max_damage * bonus_factor)
                battle_logger.add_log(f"Bonus appliqué à {character.name}: stats x{bonus_factor}")
                print(f"- {character.name}: stats x{bonus_factor}")
            time.sleep(1.5)  # Pause pour que le joueur puisse lire
        
        # Confirmation des sélections
        clear_screen()
        print(f"\n{COLORS['BOLD']}Récapitulatif des équipes:{COLORS['RESET']}")
        
        print(f"\n{COLORS['BLUE']}Équipe BLEUE:{COLORS['RESET']}")
        for char in team1:
            print(f"  - {char.get_stats_display()}")
        
        print(f"\n{COLORS['RED']}Équipe ROUGE:{COLORS['RESET']}")
        for char in team2:
            print(f"  - {char.get_stats_display()}")
        
        print("\nQue la bataille commence!")
        print(f"\n{COLORS['YELLOW']}CONTRÔLES:{COLORS['RESET']}")
        print("- Touche P: Pause/Reprendre")
        print("- Flèche droite: Accélérer")
        print("- Flèche gauche: Ralentir")
        print("- Touche Échap: Quitter l'application")
        input("\nAppuyez sur Entrée pour commencer le combat...")
        
        # Réinitialise les hooks du clavier pour le contrôleur de vitesse
        keyboard.unhook_all()
        speed_controller.setup_keyboard_listeners()
        
        battle_logger.add_log("Début du combat")
        
        # Démarrage du combat
        round_num = 1
        
        while not team_is_defeated(team1) and not team_is_defeated(team2):
            battle_logger.add_round_separator(round_num)
            battle_logger.add_log(f"Détermination de l'ordre d'initiative pour le round {round_num}")
            
            # Affiche l'état du combat avec le numéro de round
            messages = display_team_battle(team1, team2, speed_controller, round_num)
            for msg in messages:
                battle_logger.add_log(msg)
                
            print(f"\n{COLORS['BOLD']}--- ROUND {round_num} ---{COLORS['RESET']}")
            print(f"\n{COLORS['YELLOW']}Lancement des dés d'initiative...{COLORS['RESET']}")
            
            # Détermine l'ordre de jeu basé sur la vitesse
            turn_order = determine_turn_order(team1, team2, battle_logger)
            
            # Affiche l'ordre des tours
            print(f"\n{COLORS['BOLD']}Ordre des tours pour ce round:{COLORS['RESET']}")
            for i, character in enumerate(turn_order):
                speed_text = f"{COLORS['YELLOW']}Vitesse: {character.speed}, Initiative: {character.initiative_roll}{COLORS['RESET']}"
                print(f"{i+1}. {character.get_colored_name()} - {speed_text}")
            
            speed_controller.wait(1.0)
            
            # Exécute les attaques dans l'ordre déterminé
            for attacker in turn_order:
                if attacker.is_dead:
                    continue  # Vérifie que le personnage est toujours en vie
                
                # Identifie l'équipe ennemie
                enemy_team = team2 if attacker.team_color == "BLUE" else team1
                
                if not team_is_defeated(enemy_team):
                    # Sélectionne une cible aléatoire parmi les personnages encore en vie
                    living_enemies = get_living_characters(enemy_team)
                    if living_enemies:
                        target = random.choice(living_enemies)
                        attacker.attack(target)
                        
                        # Affiche l'état et attends
                        messages = display_team_battle(team1, team2, speed_controller, round_num)
                        for msg in messages:
                            battle_logger.add_log(msg)
                            print(msg)
                        
                        speed_controller.wait(0.3)
            
            round_num += 1
            speed_controller.wait(1.0)
        
        # Affiche le résultat final avec le dernier round
        final_messages = display_team_battle(team1, team2, speed_controller, round_num-1)
        for msg in final_messages:
            battle_logger.add_log(msg)
            print(msg)
        
        # Détermine l'équipe gagnante
        if team_is_defeated(team1):
            winner_team = "ROUGE"
            winner_color = "RED"
            living_count = len(get_living_characters(team2))
        else:
            winner_team = "BLEUE"
            winner_color = "BLUE"
            living_count = len(get_living_characters(team1))
        
        result_message = f"L'équipe {winner_team} a gagné en {round_num-1} rounds!"
        print(f"\n{COLORS['BOLD']}{COLORS[winner_color]}{result_message}{COLORS['RESET']}")
        print(f"Il reste {living_count} personnages en vie dans l'équipe victorieuse.")
        
        battle_logger.add_log(result_message)
        battle_logger.add_log(f"Personnages survivants: {living_count}")
        
        # Statistiques des survivants
        if not team_is_defeated(team1):
            print(f"\n{COLORS['BLUE']}Survivants de l'équipe BLEUE:{COLORS['RESET']}")
            for char in get_living_characters(team1):
                survivor_msg = f"{char.name}: {char.hp}/{char.max_hp} HP"
                print(f"  - {survivor_msg}")
                battle_logger.add_log(f"Survivant (BLEUE): {survivor_msg}")
        
        if not team_is_defeated(team2):
            print(f"\n{COLORS['RED']}Survivants de l'équipe ROUGE:{COLORS['RESET']}")
            for char in get_living_characters(team2):
                survivor_msg = f"{char.name}: {char.hp}/{char.max_hp} HP"
                print(f"  - {survivor_msg}")
                battle_logger.add_log(f"Survivant (ROUGE): {survivor_msg}")
        
        # Sauvegarde des logs
        log_file = battle_logger.save_to_file("BLEUE", "ROUGE", winner_team)

        print(f"\n{COLORS['GREEN']}Logs du combat sauvegardés dans: {log_file}{COLORS['RESET']}")
        
        # Option pour quitter
        print(f"\n{COLORS['YELLOW']}Appuyez sur Échap pour quitter ou sur Entrée pour terminer{COLORS['RESET']}")
        input()
        if keyboard.is_pressed('l'):
            print_logs(log_file)
        else:
            return
    
    except KeyboardInterrupt:
        # Gestion de l'interruption (Ctrl+C)
        print(f"\n\n{COLORS['YELLOW']}Combat interrompu par l'utilisateur{COLORS['RESET']}")
        
        # Sauvegarde des logs même en cas d'interruption
        battle_logger.add_log("Combat interrompu par l'utilisateur")
        log_file = battle_logger.save_to_file("BLEUE", "ROUGE", "INTERRUPTION")
        print(f"\n{COLORS['GREEN']}Logs du combat sauvegardés dans: {log_file}{COLORS['RESET']}")
        if keyboard.is_pressed('l'):
            print_logs(log_file)
        else:
            return
    finally:
        # Arrête la gestion du clavier
        keyboard.unhook_all()
if __name__ == "__main__":
    main()