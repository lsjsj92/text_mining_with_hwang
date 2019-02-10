import sys
import MeCab, os
m = MeCab.Tagger('-d ./hwang_main/mecab-ko-dic-2.1.1-20180720')
input_value = sys.argv[1]
print(input_value)
tag_classes = ['NNG', 'NNP','VA', 'VV+EC', 'XSV+EP', 'XSV+EF', 'XSV+EC', 'VV+ETM', 'MAG', 'MAJ', 'NP', 'NNBC', 'IC', 'XR', 'VA+EC']
result = ''
value = m.parseToNode(input_value)
print(value)
while value:
    tag = value.feature.split(",")[0]
    word = value.feature.split(",")[3]
    if tag in tag_classes:
        if word == "*": value = value.next
        result += word.strip()+" "
        #print(word.strip(), type(word.strip()), tag)
    value = value.next


with open('./hwang_main/subprocess/test.txt', 'w', encoding='utf8') as f:
    f.write(result)
