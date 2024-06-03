
class Bord:
    def __init__(self):
        self._char = [' '] *9

    def set_new_point(self, index, point):
        self._char[index] = point

    def print_bord(self):
        print(f"""
          {self._char[0]}|{self._char[1]}|{self._char[2]}
        ---------
          {self._char[3]}|{self._char[4]}|{self._char[5]}
        ---------
          {self._char[6]}|{self._char[7]}|{self._char[8]}
        """)

    def point_is_empty(self, index):
        point = False
        if self._char[index] == ' ':
            point = True
        return point


    def is_win_test(self):
        if self._char[0] == self._char[1] == self._char[2] and self._char[2] != " ":
            print(f"Wygrywa gracz {self._char[0]}")
            return True
        if self._char[3] == self._char[4] == self._char[5] and self._char[5] != " ":
            print(f"Wygrywa gracz {self._char[4]}")
            return True
        if self._char[6] == self._char[7] == self._char[8] and self._char[7] != " ":
            print(f"Wygrywa gracz {self._char[7]}")
            return True

        if self._char[0] == self._char[3] == self._char[6] and self._char[6] != " ":
            print(f"Wygrywa gracz {self._char[3]}")
            return True
        if self._char[1] == self._char[4] == self._char[7] and self._char[7] != " ":
            print(f"Wygrywa gracz {self._char[4]}")
            return True
        if self._char[2] == self._char[5] == self._char[8] and self._char[2] != " ":
            print(f"Wygrywa gracz {self._char[5]}")
            return True

        if self._char[0] == self._char[4] == self._char[8] and self._char[8] != " ":
            print(f"Wygrywa gracz {self._char[4]}")
            return True
        if self._char[6] == self._char[4] == self._char[2] and self._char[2] != " ":
            print(f"Wygrywa gracz {self._char[4]}")
            return True

        c= 0
        for i in range(len(self._char)):
            if self._char[i] == " ":
                c+=1

        if c == 0:
            print("Remis")
            return True



    @staticmethod
    def pozition():
        while True:
            try:
                x = int(input("Podaj pozycje: "))
            except:
                print("Podano bledna wwartosc")
            else:
                if x <=8 and x>=0:
                    return x
                else:
                    print("Podano bledna pozycje")






if __name__ == '__main__':
    mapa = Bord()
    mapa.print_bord()
    mapa.set_new_point(1, 'T')
    mapa.print_bord()
