import time

while True:
    userinput = input("Press enter to request a food.")
    with open("./food_service.txt", "r+") as file:
        file.seek(0)
        file.truncate()
        file.write("request")
        file.flush()
        time.sleep(1)
        file.seek(0)
        food = file.read()
    print(food)