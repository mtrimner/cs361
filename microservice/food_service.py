import random
import time

food_list = ["chicken", "snickers", "pizza"]

def listen():
    while True:
        with open("./food_service.txt", "r+") as file:
            txt = file.read()
            if "request" in txt:
                file.seek(0)
                file.truncate()
                food = random.choice(food_list)
                file.write(food)
        time.sleep(0.1)


def run():
    listen()
    # Call the listen function

if __name__=='__main__':
    run()