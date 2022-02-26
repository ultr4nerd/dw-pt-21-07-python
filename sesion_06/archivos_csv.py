import csv

# Usando listas
with open("data.csv", "w") as my_csv:
    writer = csv.writer(my_csv)
    writer.writerow(["Creep", "Radiohead", "Pablo Honey"])
    writer.writerow(["Karma Police", "Radiohead", "OK Computer"])

with open("data.csv") as my_csv:
    reader = csv.reader(my_csv)
    for line in reader:
        print(line)


# Usando diccionarios para tener más contexto de los datos
with open("data.csv", "w") as my_csv:
    writer = csv.DictWriter(my_csv, fieldnames=["title", "artist", "album"])
    writer.writeheader()
    writer.writerow({
        "title": "Creep",
        "artist": "Radiohead",
        "album": "Pablo Honey"
    })
    writer.writerow({
        "artist": "Radiohead",
        "album": "OK Computer",
        "title": "Karma Police",
    })

with open("data.csv") as my_csv:
    reader = csv.DictReader(my_csv)
    for line in reader:
        print(line)
