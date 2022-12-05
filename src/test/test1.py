class ReadData:
    def __init__(self, data_path):
        self.data_path = data_path

    def __iter__(self):
        print('ReadData 의 iter 를 호출')
        with open(self.data_path, "r", encoding='utf-8') as f:
            for line in f:
                yield line


file_name = '../../data/test.dat'
r = ReadData(file_name)
i = iter(r)
print(next(i))
print(next(i))
print(next(i))
