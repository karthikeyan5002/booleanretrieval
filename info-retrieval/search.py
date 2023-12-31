import argparse
import timeit

from ir_system import IRSystem

docs = ["Ice-cream, Mango, Litchi",
        "Hockey, Cricket, Sport",
        "Ice-cream, Litchi, Mango, Chocolate",
        "Ice-cream, Milk-shake, Water",
        "Nice, Good, Cute"]

stop_words = ['is', 'a', 'for', 'the', 'of']


def parse_args():
    parser = argparse.ArgumentParser(
        description='Information Retrieval System Configuration')
    return parser.parse_args()


def main():
    args = parse_args()
    ir = IRSystem(docs, stop_words=stop_words)

    while True:
        query = input('Enter boolean query: ')

        start = timeit.default_timer()
        results = ir.process_query(query)
        stop = timeit.default_timer()
        if results is not None:
            print('Processing time: {:.5} secs'.format(stop - start))
            print('\nDoc IDS: ')
            print(results)
        print()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt as e:
        print('EXIT')
