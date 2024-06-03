from bord import Bord
from is_tourn import Tourn
from is_win import Is_win



if __name__ == '__main__':
    bord = Bord()
    tura = Tourn()
    test = Is_win()

    while True:


        x = bord.pozition()

        if bord.point_is_empty(x):
            bord.set_new_point(x, tura.turn)
            tura.new_turn()
        else:
            print('To miejsce jest juz zajete')
        bord.print_bord()
        if bord.is_win_test():
             break
