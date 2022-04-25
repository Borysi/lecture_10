import os
import csv


def read_data(file_name):
    """
    Reads csv file and returns numeric data.

    :param file_name: (str), name of CSV file
    :return: (dict), dictionary with numeric data, keys - csv column names, values - numbers in each column
    """
    cwd_path = os.getcwd()
    file_path = os.path.join(cwd_path, file_name)
    dictionary_numbers = dict()
    with open(file_path, mode = "r") as csv_file:
        reader = csv.DictReader(csv_file)

        for row in reader:
            for key, value in row.items():
                if key not in dictionary_numbers:
                    dictionary_numbers[key] = []
                dictionary_numbers[key].append(int(value))

    return dictionary_numbers


def selection_sort(sequence, direction):

   pocet_indexu = len(sequence)

   for index in range(pocet_indexu):
       minimum = index

       for index_2 in range(minimum + 1, pocet_indexu):
           if direction == 0:
               if sequence[index_2] < sequence[minimum]:
                   minimum = index_2
           if direction == 1:
               if sequence[index_2] > sequence[minimum]:
                   minimum = index_2

       sequence[index], sequence[minimum] = sequence[minimum], sequence[index]

   return sequence

def main():
    print(selection_sort(read_data("numbers.csv")["series_1"], 0))

if __name__ == '__main__':
    main()
