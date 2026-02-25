from pyscript import display, document

teams = {
    "7_Ruby": "Red Bulldogs",
    "7_Emerald": "Green Hornets",
    "7_Sapphire": "Blue Bears",
    "7_Diamond": "Yellow Tigers",
    "8_Ruby": "Red Bulldogs",
    "8_Emerald": "Green Hornets",
    "8_Sapphire": "Blue Bears",
    "8_Diamond": "Yellow Tigers",
    "9_Ruby": "Red Bulldogs",
    "9_Emerald": "Green Hornets",
    "9_Sapphire": "Blue Bears",
    "9_Diamond": "Yellow Tigers",
    "10_Ruby": "Red Bulldogs",
    "10_Emerald": "Green Hornets",
    "10_Sapphire": "Blue Bears",
    "10_Diamond": "Yellow Tigers",
}

players_list = [
    "Abayon",
    "Antes",
    "Apostol",
    "Banaag",
    "Barrientos",
    "Casal",
    "Coeli",
    "David",
    "De Mata",
    "Dela Cruz F",
    "Dela Cruz L",
    "Dellejero",
    "Fukuda",
    "Fukuda",
    "Gozum",
    "Ibay",
    "Lim",
    "Lozano",
    "Mamauag",
    "Navarro",
    "Precones",
    "Ramos",
    "Sidhu",
    "Villamayor",
    "Zaragoza"
]

def hide_all_sections():
    document.getElementById('signup_section').style.display = 'none'
    document.getElementById('teamchecker_section').style.display = 'none'
    document.getElementById('players_section').style.display = 'none'

def show_signup(e):
    hide_all_sections()
    document.getElementById('signup_section').style.display = 'block'

def show_teamchecker(e):
    hide_all_sections()
    document.getElementById('teamchecker_section').style.display = 'block'

def show_players(e):
    hide_all_sections()
    document.getElementById('players_section').style.display = 'block'

def signup_form(e):
    username = document.getElementById('username').value
    password = document.getElementById('password').value
    
    if username and password:
        document.getElementById('signup_output').innerHTML = 'Account created. You may now log in using your credentials.'
    else:
        document.getElementById('signup_output').innerHTML = 'Please fill in all fields'

def team_checker_form(e):
    grade = document.getElementById('grade').value
    section = document.getElementById('section').value
    
    if grade and section:
        team_key = f"{grade}_{section}"
        team_name = teams.get(team_key, "Unknown Team")
        document.getElementById('teamchecker_output').innerHTML = f'Congratulations! You are part of the {team_name}'
    else:
        document.getElementById('teamchecker_output').innerHTML = 'Please select your grade and section'

def show_players_list(e):
    document.getElementById('players_output').innerHTML = ''
    players_text = '<br>'.join([f'{i}) {player}' for i, player in enumerate(players_list, 1)])
    document.getElementById('players_output').innerHTML = players_text


