def parse_card(card_str):
    # print(card_str)
    value, suit = card_str[:-1], card_str[-1]
    return value, suit

def parse_hand(hand_str):
    # print(hand_str)
    cards = hand_str.split()
    return [parse_card(card) for card in cards]

def is_high_card(hand):
    # print('is_high_card')
    values = [card[0] for card in hand]
    # print(values)
    # print(max(values))
    # print(max(values, key=poker_ranks_order.index))
    return max(values, key=poker_ranks_order.index)

def is_pair(hand):
    # print('is_pair')
    values = [card[0] for card in hand]
    unique_values = set(values)

    if len(unique_values) == 4:
        return max(unique_values, key=values.count)
    else:
        return None

def is_two_pairs(hand):
    # print('is_two_pairs')
    values = [card[0] for card in hand]
    # print(values)
    unique_values = set(values)
    # print(unique_values)

    if len(unique_values) == 3:
        # print(unique_values)
        pairs = sorted([val for val in unique_values if values.count(val) == 2], reverse=True)
        # print(pairs)
        return pairs if len(pairs) == 2 else None
    else:
        return None

def is_three_of_a_kind(hand):
    # print('is_three_of_a_kind')
    values = [card[0] for card in hand]
    unique_values = set(values)

    if len(unique_values) == 3:
        sorted_values = sorted(unique_values, key=lambda x: (values.count(x), x), reverse=True)
        # print(sorted_values)
        pairs = sorted([val for val in unique_values if values.count(val) == 3], reverse=True)
        # print(pairs)
        return pairs if len(pairs) == 1 else None
    else:
        return None

def is_full_house(hand):
    # print('is_full_house')
    values = [card[0] for card in hand]
    unique_values = set(values)

    if len(unique_values) == 2 and values.count(max(unique_values, key=values.count)) == 3:
        three_of_a_kind = max(unique_values, key=values.count)
        pair = min(unique_values, key=values.count)
        return three_of_a_kind, pair
    else:
        return None

def is_four_of_a_kind(hand):
    # print('is_four_of_a_kind')
    values = [card[0] for card in hand]
    unique_values = set(values)

    if len(unique_values) == 2 and values.count(max(unique_values, key=values.count)) == 4:
        return max(unique_values, key=values.count)
    else:
        return None

def is_straight(hand):
    # print('is_straight')
    values = [card[0] for card in hand]
    # print(values)
    sorted_values = sorted(values, key=lambda x: '23456789TJQKA'.index(x))
    # print(sorted_values)
    return all(sorted_values[i] == '23456789TJQKA'[i] for i in range(5))

def is_flush(hand):
    # print('is_flush')
    suits = [card[1] for card in hand]
    return len(set(suits)) == 1

def is_straight_flush(hand):
    # print('is_straight_flush')
    return is_straight(hand) and is_flush(hand)

def is_royal_flush(hand):
    # print('is_royal_flush')
    return is_straight_flush(hand) and all(card[0] in 'TJQKA' for card in hand)

# Define a custom order for poker ranks
poker_ranks_order = '23456789TJQKA'

def compare_each_cards(card1, card2):

    print(card1, card2)

    # Sort cards by poker power index
    sorted_cards1 = sorted(card1, key=lambda x: poker_ranks_order.index(x[0]), reverse=True)
    sorted_cards2 = sorted(card2, key=lambda x: poker_ranks_order.index(x[0]), reverse=True)

    print(sorted_cards1, sorted_cards2)
    # Compare cards in descending order
    for i in range(len(sorted_cards1)):
        if poker_ranks_order.index(sorted_cards1[i][0]) > poker_ranks_order.index(sorted_cards2[i][0]):
            return 1
        elif poker_ranks_order.index(sorted_cards2[i][0]) > poker_ranks_order.index(sorted_cards1[i][0]):
            return 2

    return 0  # Cards are equal


def determine_winner(hand1, hand2):
    # print(hand1)
    # print(hand2)
    for hand_checker in [is_royal_flush, is_straight_flush, is_four_of_a_kind, is_full_house, is_flush, is_straight, is_three_of_a_kind, is_two_pairs, is_pair, is_high_card]:
    # for hand_checker in [is_royal_flush]:
        # print(hand_checker)
        result1 = hand_checker(hand1)
        result2 = hand_checker(hand2)
        # print(result1)
        # print(result2)

        if result1 is not None and result2 is None:
            return 1
        elif result2 is not None and result1 is None:
            return 2
        elif result1 is not None and result2 is not None:
            if hand_checker == is_high_card:
                result_compare = compare_each_cards(hand1, hand2)
                print(result1, result2, result_compare)
                return result_compare

            elif result1 > result2:
                return 1
            elif result2 > result1:
                return 2

    return 0  # It's a tie if no winner is determined

def save_to_file(hand1, hand2, result):
    filename = f"{result.lower()}.txt"
    # print(hand1)
    # hand1.append(hand2)
    # print(hand1)
    # print('type', type(hand2[0]))
    hands = hand1 + hand2
    print(hands)
    hands_str = ""
    for hand in hands:
        print(hand)
        print(hand[0] + hand[1])
        hands_str += hand[0] + hand[1] + " "
    print(hands_str)

    with open('results/'+filename, "a") as file:
        file.write(f"{hands_str}\n")
        # file.write(f"{' '.join(hand1_str)} | {' '.join(hand2_str)} | Winner: {result}\n")

def main():
    player1_wins = 0
    player2_wins = 0

    # with open("poker-hands-short.txt", "r") as file:
    # with open("poker-hands-long.txt", "r") as file:
    # with open("poker-hands-tie.txt", "r") as file:
    with open("poker-hands.txt", "r") as file:
    # with open("results/high card.txt", "r") as file:
    # with open("results/tie.txt", "r") as file:
        hand_number = 1
        count_tie = 0
        for line in file:
            line = line.strip()
            if not line:
                break  # End of file reached
            print(line[:15],"   ", line[15:])

            cards = parse_hand(line)
            # print(cards)
            player1_hand = cards[:5]
            player2_hand = cards[5:]
            # print(player1_hand)
            # print(player2_hand)

            winner = determine_winner(player1_hand, player2_hand)

            print(f"Hand {hand_number}:", end=" ")
            if winner == 1:
                player1_wins += 1
                print(f"Player 1 wins with {hand_description(player1_hand)}")
                # save_to_file(player1_hand, player2_hand, hand_description(player1_hand))
            elif winner == 2:
                player2_wins += 1
                print(f"Player 2 wins with {hand_description(player2_hand)}")
                # save_to_file(player1_hand, player2_hand, hand_description(player1_hand))
            else:
                count_tie += 1
                print("It's a tie!")
                # save_to_file(player1_hand, player2_hand, 'tie')

            hand_number += 1

            # if hand_description(player1_hand) == 'One Pair' or hand_description(player2_hand) == 'One Pair' :
            #     pass
            # else:
            #     input()

    print(f"\nPlayer 1 total wins: {player1_wins} hands")
    print(f"Player 2 total wins: {player2_wins} hands")
    print('tie', count_tie)

def hand_description(hand):
    if is_royal_flush(hand):
        # print('win with royal_flush')
        return "Royal Flush"
    elif is_straight_flush(hand):
        # print('win with straight_flush')
        return "Straight Flush"
    elif is_four_of_a_kind(hand):
        # print('win with four_of_a_kind')
        return "Four of a Kind"
    elif is_full_house(hand):
        # print('win with full_house')
        return "Full House"
    elif is_flush(hand):
        # print('win with flush')
        return "Flush"
    elif is_straight(hand):
        # print('win with straight')
        return "Straight"
    elif is_three_of_a_kind(hand):
        # print('win with three_of_a_kind')
        return "Three of a Kind"
    elif is_two_pairs(hand):
        # print('win with two_pairs')
        return "Two Pairs"
    elif is_pair(hand):
        # print('win with pair')
        return "One Pair"
    else:
        return "High Card"

if __name__ == "__main__":
    main()
