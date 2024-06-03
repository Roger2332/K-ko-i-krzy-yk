from  bord import Bord


class Is_win:
    def __init__(self):
        self.__bord = Bord()
        self.__test_bord = self.__bord._char

    def is_win_test(self) -> bool:
        if self.__test_bord[0] == self.__test_bord[1] == self.__test_bord[2] and self.__test_bord[2] != " ":
            print(f"Wygrywa gracz {self.__test_bord[0]}")
            return True
        if self.__test_bord[3] == self.__test_bord[4] == self.__test_bord[5]and self.__test_bord[5] != " ":
            print(f"Wygrywa gracz {self.__test_bord[4]}")
            return True
        if self.__test_bord[6] == self.__test_bord[7] == self.__test_bord[8]and self.__test_bord[7] != " ":
            print(f"Wygrywa gracz {self.__test_bord[7]}")
            return True

        if self.__test_bord[0] == self.__test_bord[3] == self.__test_bord[6]and self.__test_bord[6] != " ":
            print(f"Wygrywa gracz {self.__test_bord[3]}")
            return True
        if self.__test_bord[1] == self.__test_bord[4] == self.__test_bord[7]and self.__test_bord[7] != " ":
            print(f"Wygrywa gracz {self.__test_bord[4]}")
            return True
        if self.__test_bord[2] == self.__test_bord[5] == self.__test_bord[8]and self.__test_bord[2] != " ":
            print(f"Wygrywa gracz {self.__test_bord[5]}")
            return True

        if self.__test_bord[0] == self.__test_bord[4] == self.__test_bord[8] and self.__test_bord[8] != " ":
            print(f"Wygrywa gracz {self.__test_bord[4]}")
            return True
        if self.__test_bord[6] == self.__test_bord[4] == self.__test_bord[2] and self.__test_bord[2] != " ":
            print(f"Wygrywa gracz {self.__test_bord[4]}")
            return True

        else:
            return False


    def test_print(self):
        print(self.__test_bord)

