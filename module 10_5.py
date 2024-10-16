import multiprocessing
import datetime


def read_info(name):
    all_data = []
    with open(name) as file:
        for line in file:
            all_data.append(line)


if __name__ == '__main__':
    filenames = [f'./file {number}.txt' for number in range(1, 5)]
    # start = datetime.datetime.now()
    # for name in filenames:
    #     read_info(name)
    # end = datetime.datetime.now()
    # print(end - start)
    start1 = datetime.datetime.now()
    with multiprocessing.Pool(processes=2) as pool:
        pool.map(read_info, filenames)
        end1 = datetime.datetime.now()
    print(end1 - start1)
