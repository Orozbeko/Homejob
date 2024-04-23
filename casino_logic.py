def calculate_win_loss(bet, winning_slot):
    if bet == winning_slot:
        return bet * 2
    else:
        return -bet