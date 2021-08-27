import sys


equip_shop = {'Weapons': {'Dagger': [8, 4, 0],
                           'Shortsword': [10, 5, 0],
                           'Warhammer': [25, 6, 0],
                           'Longsword': [40, 7, 0],
                           'Greataxe': [74, 8, 0]},

               'Armor': {'Leather' : [13, 0, 1],
                          'Chainmail': [31, 0, 2],
                          'Splintmail': [53, 0, 3],
                          'Bandemail': [75, 0, 4],
                          'Platemail': [102, 0, 5]},

               'Rings': {'Damage_p1' : [25, 1, 0],
                          'Damage_p2' : [50, 2, 0],
                          'Damage_p3' : [100, 3, 0],
                          'Defense_p1': [20, 0, 1],
                          'Defense_p2' : [40, 0, 2],
                          'Defense_p3' : [80, 0, 3]}}


def get_stats(file):
    with open(file, 'r') as f:
        boss_stats = []
        for line in f:
            boss_stats.append(int(line.split(': ')[1].strip('\n')))
    return boss_stats


def go_shopping(boss_stats):
    cost_of_winning = []
    cost_of_losing = []
    weapon_opt = equip_shop['Weapons'].keys()
    equip_shop['Armor']['Empty'] = [0, 0, 0]
    equip_shop['Rings']['Empty1'] = [0, 0, 0]
    equip_shop['Rings']['Empty2'] = [0, 0, 0]
    armor_opt = equip_shop['Armor'].keys()
    ring_opt = equip_shop['Rings'].keys()

    for w in weapon_opt:
        for a in armor_opt:
            for r1 in ring_opt:
                for r2 in list(set(ring_opt) - set(r1)):
                    stats = []
                    for metric in [0, 1, 2]:
                        stats.append(equip_shop['Weapons'][w][metric] + equip_shop['Armor'][a][metric] + equip_shop['Rings'][r1][metric] + equip_shop['Rings'][r2][metric])

                    cost, loser = battle(boss_stats, stats)
                    if loser == 'Boss':
                        cost_of_winning.append(cost)
                    elif loser == 'Me':
                        cost_of_losing.append(cost)
    lowest_cost_to_win = min(cost_of_winning)
    highest_cost_to_lose = max(cost_of_losing)
    return lowest_cost_to_win, highest_cost_to_lose


def battle(boss_stats, my_stats):
    boss_d_deal = max((boss_stats[1] - my_stats[2]), 1)
    my_d_deal = max((my_stats[1] - boss_stats[2]), 1)
    boss_hp = boss_stats[0]
    my_hp = 100
    turn_num = 0
    while boss_hp > 0:
        turn_num += 1
        boss_hp -= my_d_deal
        if boss_hp <= 0:
            loser = 'Boss'
            break

        if my_hp > 0:
            my_hp -= boss_d_deal
        if my_hp <= 0:
            loser = 'Me'
            break
    return my_stats[0], loser



def main(input):
    boss_stats = get_stats(input)
    lowest_cost_to_win, highest_cost_to_lose = go_shopping(boss_stats)
    print(f'Lowest cost to win: {lowest_cost_to_win}')
    print(f'Highest cost to lose: {highest_cost_to_lose}')


if __name__ == "__main__":
    main(sys.argv[1])