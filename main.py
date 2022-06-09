# This is a sample Python script.
import csv
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.



def csv_reding(file_name):
    with open(file_name) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        line_count = 0
        dijkstra_counter = 0.0
        bellman_ford_counter = 0.0
        prim_counter = 0.0
        kruskal_counter = 0.0
        i = 0
        for row in csv_reader:
            if line_count != 0:
                i = 1 + i
                dijkstra_counter += float(row[0])
                bellman_ford_counter += float(row[1])
                prim_counter += float(row[2])
                kruskal_counter += float(row[3])
            line_count += 1

    print('dijkstra_counter: ', dijkstra_counter/100)
    print('bellman_ford_counter', bellman_ford_counter/100)
    print('prim_counter', prim_counter/100)
    print('kruskal_counter', kruskal_counter/100)

directory_path = 'C:\\Users\\Michal\\Desktop\\Phyton\\Jakies projekty\\pythonProject\\'

directory_25 = '25_wierzcholkow\\'
directory_50 = '50_wierzcholkow\\'
directory_100 = '100_wierzcholkow\\'
directory_200 = '200_wierzcholkow\\'
directory_250 = '250_wierzcholkow\\'

directory_array = [directory_25, directory_50, directory_100, directory_200, directory_250]

list_path = 'lista\\'
list_file_25 = 'list25.txt'
list_file_55 = 'list55.txt'
list_file_75 = 'list75.txt'
list_file_99 = 'list99.txt'

list_array = [list_file_25, list_file_55, list_file_75, list_file_99]

matrix_path = 'macierz\\'
matrix_file_25 = 'mat25.txt'
matrix_file_55 = 'mat55.txt'
matrix_file_75 = 'mat75.txt'
matrix_file_99 = 'mat99.txt'

matrix_array = [matrix_file_25, matrix_file_55, matrix_file_75, matrix_file_99]

print('\n\n\nLISTY\n\n\n')
for directories in directory_array:
    # listy
    for list_file in list_array:
        final_path = ''
        final_path = directory_path + directories + list_path + list_file
        print(final_path)
        csv_reding(final_path)

print('\n\n\nMACIERZ\n\n\n')
for directories in directory_array:
    # macierze
    for matrix_file in matrix_array:
        final_path = ''
        final_path = directory_path + directories + matrix_path + matrix_file
        print(final_path)
        csv_reding(final_path)




