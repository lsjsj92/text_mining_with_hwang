import sys

with open('./test.txt', 'w', encoding='utf8') as f:
    f.write(sys.argv[0]+","+sys.argv[1])