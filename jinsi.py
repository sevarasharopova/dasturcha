import time

b = input('''sonni tanlang:
1.
2.
''')

def jinsi():
        if b == '1':
           print("")
            for x in range(20):
                time.sleep(0.2)
                print("qiz bola")
        elif b == '2':
            for x in range(20):
                time.sleep(0.2)
                print("yigit bola")
        else:
            print("xato")


