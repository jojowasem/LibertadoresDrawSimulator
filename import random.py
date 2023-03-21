import random
import pandas as pd

def pot_1_dict(x):
    return {
        2:'River Plate (ARG)',
        3:'Palmeiras (BRA)',
        4:'Boca Juniors (ARG)',
        5:'Nacional (URU)',
        6:'Athletico (BRA)',
        7:'Independiente del Valle (ECU)',
        8:'Olimpia (PAR)'
    }[x]

def pot_2_dict(x):
    return {
        1: "Libertad (PAR)",
        2: "Atlético Nacional (COL)",
        3: "Internacional (BRA)",
        4: "Barcelona (ECU)",
        5: "Racing (ARG)",
        6: "Corinthians (BRA)",
        7: "Colo Colo (CHI)",
        8: "Fluminense (BRA)"
    }[x]

def pot_3_dict(x):
    return {
        1: "Bolívar (BOL)",
        2: "The Strongest (BOL)",
        3: "Melgar (PER)",
        4: "Alianza Lima (PER)",
        5: "Argentinos Juniors (ARG)",
        6: "Metropolitanos (VEN)",
        7: "Aucas (ECU)",
        8: "Monagas (VEN)"
    }[x]

def pot_4_dict(x):
    return {
        1: "Liverpool (URU)",
        2: "Deportivo Pereira (COL)",
        3: "Ñublense (CHI)",
        4: "Patronato (ARG)",
        5: "Atlético-MG (BRA)",
        6: "Sporting Cristal (PER)",
        7: "Cerro Porteño (PAR)",
        8: "Independiente Medellín (COL)"
    }[x]

def groups_dict(x):
    return {
        1: "A",
        2: "B",
        3: "C",
        4: "D",
        5: "E",
        6: "F",
        7: "G",
        8: "H"
    }[x]

group_a = ["Flamengo (BRA)"]
group_b = []
group_c = []
group_d = []
group_e = []
group_f = []
group_g = []
group_h = []
groups = [['Flamengo (BRA)', 'A']]

def append_team_to_group(i, pot_dict, team):
    if i == 1:
        group_a.append(pot_dict(team))
    elif i == 2:
        group_b.append(pot_dict(team))
    elif i == 3:
        group_c.append(pot_dict(team))
    elif i == 4:
        group_d.append(pot_dict(team))
    elif i == 5:
        group_e.append(pot_dict(team))
    elif i == 6:
        group_f.append(pot_dict(team))
    elif i == 7:
        group_g.append(pot_dict(team))
    elif i == 8:
        group_h.append(pot_dict(team))

def check_group_size(group, len):
    if group == 1:
        group_a.append(pot_dict(team))
    elif i == 2:
        group_b.append(pot_dict(team))
    elif i == 3:
        group_c.append(pot_dict(team))
    elif i == 4:
        group_d.append(pot_dict(team))
    elif i == 5:
        group_e.append(pot_dict(team))
    elif i == 6:
        group_f.append(pot_dict(team))
    elif i == 7:
        group_g.append(pot_dict(team))
    elif i == 8:
        group_h.append(pot_dict(team))

pot_1 = [2,3,4,5,6,7,8]
pot_2_groups = [i for i in range(1,9)]
pot_2_teams = [i for i in range(1,9)]

# Pot 1 draw
# set dict
pot_dict = pot_1_dict

for i in range(2,9):
    team = random.choice(pot_1)
    seeded = [pot_1_dict(team), groups_dict(i)]
    pot_1.remove(team)
    groups.append(seeded)
    append_team_to_group(i, pot_dict, team)

# Pot B draw
# set dict
pot_dict = pot_2_dict
group_mod = 0

while len(pot_2_teams) > 0:
    for i in pot_2_groups:
        group = pot_2_groups[0]
        temp = 0
        team = random.choice(pot_2_teams)
        # teams of the same country can't be in the same groups, except if they come from the previous stages
        print(pot_2_dict(team),"&", groups[group - 1][0])
        while (pot_2_dict(team)[-4:-1] == groups[group + temp - 1][0][-4:-1]):
            temp = temp + 1
            print(temp)
            print(i)
        if temp > 0:
            group = group + temp
        seeded = [pot_2_dict(team), groups_dict(group)]
        print(seeded)
        append_team_to_group(group, pot_dict, team)
        pot_2_teams.remove(team)
        pot_2_groups.remove(group)
        groups.append(seeded)    

print(groups)

# não está voltando a contagem