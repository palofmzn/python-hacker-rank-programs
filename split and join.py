def split_and_join(line):
    line='-'.join(result)
    result=result.split(' ')
if __name__ == '__main__':
    line = raw_input()
    result = split_and_join(line)
    print(result)
