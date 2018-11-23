import random

class MontyHall:
    def __init__(self, n=3):
        self.prize_door = self.pick_door(n)
        self.select_door = self.pick_door(n)
    
    def pick_door(self, n):
        return random.randint(1, n)
    
    def user_win(self):
        if self.select_door == self.prize_door:
            return True
        else:
            return False


def play(n=3, size = 100):
    """ Play Monty Hall game 'size' times for n doors
    """
    win = 0
    loss = 0
    for i in range(0, size):
        m = MontyHall(n)
        if m.user_win():
            win += 1
        else:
            loss += 1
    total = win + loss
    return [win/total, loss/total]


if __name__== "__main__":
    # calculate average wins for n games
    n = 100
    num_door = 3
    avg_win = 0
    avg_loss = 0
    for i in range(0,n):
        cup = play(num_door, 100)
        avg_win += cup[0]
        avg_loss += cup[1]
    avg_win /= n
    avg_loss /= n
    print("User won: " + str(round(avg_win, 2)) + "\n")
    print("User loss: " + str(round(avg_loss, 2)))        