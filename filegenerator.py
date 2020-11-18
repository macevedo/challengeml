import time, random, csv


with open('data/mlmetric.csv', 'a', newline='') as file:
    writer = csv.writer(file)
    for i in range(5):
        writer.writerow([str(time.time())[:10], str(random.randrange(10, 2000))])
        time.sleep(5)
