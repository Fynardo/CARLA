def compute_total_cases(success_dice, diff_dice):
    return success_dice.size * diff_dice.size

def _compute_gt_cases(success_dice, diff_dice):
    return sum([max(min(i-diff_dice.lower, diff_dice.size), 0) for i in range(success_dice.lower, success_dice.upper+1)])

def _compute_ge_cases(success_dice, diff_dice):
    return sum([max(min(i - diff_dice.lower + 1, diff_dice.size), 0) for i in range(success_dice.lower, success_dice.upper+1)])

def compute_fav_cases(success_dice, diff_dice, case='>'):
    if case == '>':
        return _compute_gt_cases(success_dice, diff_dice)
    else:
        return _compute_ge_cases(success_dice, diff_dice)

def compute_probs(success_dice, diff_dice, case='>'):
    """ LaPlace
    """
    fav_cases = compute_fav_cases(success_dice, diff_dice, case)
    total_cases = compute_total_cases(success_dice, diff_dice)
    return round(fav_cases / total_cases, 2) 
