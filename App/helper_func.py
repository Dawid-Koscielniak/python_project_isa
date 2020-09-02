# Do przypisania 0 lub 2 pkt. 2 pkt w przypadku wieku poniżej 30 lub powyżej 50 lat. 
score_list = []
def q1 ():
    score_client = 0
    while True:
        try:
            t = input("Wprowadź wiek klienta w latach: ")
            years = int(t)            
            if years in range (0,110):
                if years <30 or years >60:
                    score_client +=2
                break
            else:
                print("Podaj prawidłową wartość")

        except ValueError:
            print("Podaj prawidłową wartość")
            
    score_list.append(score_client)

# Do przypisania 0 lub 1 pkt. 1 pkt w przypadku singla
def q2():
    score_client2 = 0
    while True:

        t1 = input("Wprowadź stan cywilny klienta: singiel, małżonek, wdowiec, w separacji: ")
        list = ("singiel", "małżonek", "wdowiec", "w separacji")

        if t1 in list:

            if t1 == "singiel":
                score_client2 +=1

            break

        else:
            print("Podaj prawidłowy stan cywilny")
            
    score_list.append(score_client2)

# Do przypisania 0 lub 2 pkt. 2 pkt w przypadku wykształcenia podstawowego 
def q3():
    score_client3 = 0
    while True:

        t2 = input("Wprowadź poziom wykształcenia klienta: podstawowe, średnie, wyższe, niepełne wyższe: ")
        list = ("podstawowe", "średnie", "wyższe", "niepełne wyższe")

        if t2 in list:

            if t2 == "podstawowe":
                score_client3 +=2

            break

        else:
            print("Podaj prawidłowy poziom wykształcena ")

    score_list.append(score_client3)

# Do przypisania 0 lub 2 pkt. 2 pkt w przypadku 3 członków rodziny.
def q4 ():
    score_client4 = 0
    while True:
        try:
            t3 = input("Podaj ilość członków rodziny klienta: 0,1,2,3,..5 - w przypadku 5 lub więcej: ")
            f_size = int(t3)

            if f_size in range (0,10):

                if f_size == 3:
                    score_client4 +=2 

                break

            else:
                print("Podaj prawidłową wartość.")

        except ValueError:
            print("Podaj prawidłową wartość")
            
    score_list.append(score_client4)

# Do przypisania 0 lub 1 pkt. 1 pkt w przypadku dochodu poniżej 150 tys. 
def q5 ():
    score_client5 = 0
    while True:
        try:
            t4 = input("Podaj dochód klienta w liczbach całkowitych: ")
            income = int(t4)

            if income in range (0, 10000000000):

                if income <= 150000:
                    score_client5 +=1

                break

            else:
                print("Podaj prawidłową wartość.")

        except ValueError:
            print("Podaj prawidłową wartość")

    score_list.append(score_client5)

# Do przypisania 3 lub 3 pkt. 3 pkt w przypadku emeryta, 2 pkt. w przypadku działalności.  
def q6 ():
    score_client6 = 0
    while True:

        t5 = input("Podaj rodzaj dochodu klienta: UOP, działalność, emeryt, student, inne ")
        list = ("UOP", "działalność", "emeryt", "student", "inne")

        if t5 in list:

            if t5 in list:
                if t5 == "emeryt":
                    score_client6 +=3
                elif t5 == "działalność":

                    score_client6 +=2
            break

        else:
            print("Podaj prawidłowy rodzaj dochodu.")

    score_list.append(score_client6)
    