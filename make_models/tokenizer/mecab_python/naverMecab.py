import MeCab, csv, os
import glob, pandas as pd, numpy as np
m = MeCab.Tagger('-d /home/mecab/mecab-ko-dic-2.1.1-20180720')
root_dir = "./data"
category_, date_, content_ = [], [], []
month = ['6m', '7m', '8m', '9m']

def register_dic(month):
    files = glob.glob(root_dir+"/"+month+"/*.csv", recursive=True)
    for i in files:
        file_to_ids(i, month)


def file_to_ids(fname, month):
    name = fname.split(".csv")[0]
    name_array = name.split('/')
    f_name = name_array[3] #파일이름
    #tags for tokenizer
    tag_classes = ['NNG', 'NNP','VA', 'VV+EC', 'XSV+EP', 'XSV+EF', 'XSV+EC', 'VV+ETM', 'MAG', 'MAJ', 'NP', 'NNBC', 'IC', 'XR', 'VA+EC']
    #데이터 읽어오고.
    data = pd.read_csv(fname)
    #각각 분류
    title = data.iloc[:,0].values
    date = data.iloc[:, 1].values
    content = data.iloc[:, 2].values

    for cnt, value in enumerate(title):
        result = ''
        value = m.parseToNode(str(title[cnt]).strip() + str(content[cnt]).strip())
        while value:
            tag = value.feature.split(",")[0]
            word = value.feature.split(",")[3]
            if tag in tag_classes:
                if word == "*": value = value.next
                result += word.strip()+" "
            value = value.next
        content_.append(result)
        date_.append(date[cnt])
        #category
        if 'policy' in f_name : category_.append("0")
        if 'economy' in f_name : category_.append("1")
        if 'IT' in f_name : category_.append("2")
        if 'entertain' in f_name : category_.append("3")

def save(month, file_path, f_name):
    if not os.path.exists(file_path):
        os.mkdir(file_path)
    with open(file_path+"/"+f_name+'_after_prepro.csv', 'a', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        for cnt, i in enumerate(content_):
            date__ = date_[cnt]
            content__ = content_[cnt]
            category__ = category_[cnt]
            writer.writerow((date__, content__, category__))


for mon in month:
    register_dic(mon)
    save(mon, './data_after_preprocessing_data/'+mon, mon)
#save_files()
print('done`')
