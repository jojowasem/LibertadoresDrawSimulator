import pandas as pd
import numpy as np

def draw():
    data = {
            'team': [
            'Flamengo (BRA)', 'River Plate (ARG)', 'Palmeiras (BRA)', 'Boca Juniors (ARG)',
            'Nacional (URU)', 'Athletico (BRA)', 'Independiente del Valle (ECU)', 'Olimpia (PAR)',
            "Libertad (PAR)", "Atlético Nacional (COL)", "Internacional (BRA)", "Barcelona (ECU)",
            "Racing (ARG)", "Corinthians (BRA)", "Colo Colo (CHI)", "Fluminense (BRA)",
            "Bolívar (BOL)", "The Strongest (BOL)", "Melgar (PER)", "Alianza Lima (PER)",
            "Argentinos Juniors (ARG)", "Metropolitanos (VEN)", "Aucas (ECU)", "Monagas (VEN)",
            "Liverpool (URU)", "Deportivo Pereira (COL)", "Ñublense (CHI)", "Patronato (ARG)",
            "Atlético-MG (BRA)", "Sporting Cristal (PER)", "Cerro Porteño (PAR)", "Independiente Medellín (COL)"
            ],
            'nation': [
            '(BRA)', '(ARG)', '(BRA)', '(ARG)',
            '(URU)', '(BRA)', '(ECU)', '(PAR)',
            "(PAR)", "(COL)", "(BRA)", "(ECU)",
            "(ARG)", "(BRA)", "(CHI)", "(BRA)",
            "(BOL)", "(BOL)", "(PER)", "(PER)",
            "(ARG)", "(VEN)", "(ECU)", "(VEN)",
            "(URU)", "(COL)", "(CHI)", "(ARG)",
            "(PL1)", "(PL2)", "(PL3)", "(PL4)"
            ],
            'seed': [
            1,1,1,1,1,1,1,1,
            2,2,2,2,2,2,2,2,
            3,3,3,3,3,3,3,3,
            4,4,4,4,4,4,4,4,
            ],
            'is_champion': [
            1,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,
            ]}

    df = pd.DataFrame(data)

    groups = pd.DataFrame(columns=['group_name', 'team_1', 'team_2', 'team_3', 'team_4'])

    seed_groups = {}
    for seed in range(1, 5):
        seed_groups[seed] = df[df['seed'] == seed].reset_index(drop=True)

    for seed in seed_groups:
        seed_groups[seed] = seed_groups[seed].sample(frac=1).reset_index(drop=True)

    group_names = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        
    # Initialize a set to keep track of teams that have already been assigned to a group
    used_teams = set()

    # Loop through each group and assign teams based on seed, nation, and availability
    for i, group_name in enumerate(group_names):
        used_nations = set()
        team_1, team_2, team_3, team_4 = None, None, None, None
        for seed in range(1, 5):
            pot = seed_groups[seed]
            if seed == 1:
                pot = pot.sort_values('is_champion', ascending=False)
                pot = pot.reset_index(drop=True)
            for j in range(len(pot)):
                if pot.at[j, 'nation'] not in used_nations and pot.at[j, 'team'] not in used_teams:
                    if seed == 1 and team_1 is None:
                        team_1 = pot.at[j, 'team']
                        used_nations.add(pot.at[j, 'nation'])
                        used_teams.add(team_1)
                        print(team_1)
                        break
                    elif seed == 2 and pot.at[j, 'team'] != team_1 and team_2 is None and pot.at[j, 'nation'] not in used_nations:
                        team_2 = pot.at[j, 'team']
                        used_nations.add(pot.at[j, 'nation'])
                        used_teams.add(team_2)
                        print(team_2)
                        break
                    elif seed == 3 and pot.at[j, 'team'] not in [team_1, team_2] and team_3 is None and pot.at[j, 'nation'] not in used_nations:
                        team_3 = pot.at[j, 'team']
                        used_nations.add(pot.at[j, 'nation'])
                        used_teams.add(team_3)
                        print(team_3)
                        break
                    elif seed == 4 and pot.at[j, 'team'] not in [team_1, team_2, team_3] and team_4 is None and pot.at[j, 'nation'] not in used_nations:
                        team_4 = pot.at[j, 'team']
                        used_nations.add(pot.at[j, 'nation'])
                        used_teams.add(team_4)
                        print(team_4)
                        break
            if team_1 is not None and team_2 is not None and team_3 is not None and team_4 is not None:
                break

        groups.loc[i] = [group_name, team_1, team_2, team_3, team_4]
    return groups

i = 0
libertadores = draw()

while libertadores.isnull().values.any():
    print(libertadores)
    libertadores = draw()
    print(i)
    i = i + 1

print(libertadores)
