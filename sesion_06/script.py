import argparse

parser = argparse.ArgumentParser(description='Repite palabras el número indicado de veces.')
parser.add_argument('word', metavar='<word>', type=str, nargs=1, help='la palabra a usar')
parser.add_argument('repetitions', metavar='<repetitions>', type=int, nargs=1, help='el número de repeticiones')

args = parser.parse_args()

word = args.word[0]
repetitions = args.repetitions[0]

for _ in range(repetitions):
    print(word)
