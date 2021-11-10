import matplotlib.pyplot as plt
import random

# bankroll = float('inf')
# bankroll = 300000
bankroll = 200
# bankroll = 20
bet = 1
number_of_round = 0
bankroll_history = []

while bankroll > 0:
    number_of_round = number_of_round + 1
    print('Bet number {0}... {1}$ are placed on the bet.'.format(number_of_round, bet))
    round_result = random.randrange(0, 37)
    if round_result != 0 and round_result % 2 == 0:
        bankroll = bankroll + bet
        bet = 1
        print('Won! Current bankroll {0}'.format(bankroll))
    else:
        bankroll = bankroll - bet
        print('Lose! Current bankroll {0}'.format(bankroll))
        if bet * 2 <= bankroll:
            bet = bet * 2
        else:
            print('There is no possibility to double the bet, you have to try again...')
            bet = 1
    bankroll_history.append(bankroll)

plt.plot(range(len(bankroll_history)), bankroll_history)
plt.ylabel('Money')
plt.xlabel('Round Number')
plt.show()

print(bankroll_history)