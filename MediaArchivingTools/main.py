import datetime
import os


# 以修改时间为准

def main():
    filepath = '/Users/macbookpro/Desktop/09/0921/'
    filesnames = os.listdir(filepath)

    for name in filesnames:
        filename = filepath + name
        modifiedtime = os.path.getmtime(filename)
        formatted_time = datetime.datetime.fromtimestamp(modifiedtime)
        print(formatted_time)
        os.utime(filename, (modifiedtime, modifiedtime))


if __name__ == '__main__':
    main()
