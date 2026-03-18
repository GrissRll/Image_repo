#создай здесь свой индивидуальный проект!
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, accuracy_score



some_dict = {"Alumnus (Specialist)": 4,
             "Student (Specialist)": 2,
             "Student (Bachelor's)": 1,
             "Alumnus (Bachelor's)": 3,
             "Alumnus (Master's)": 6,
             "PhD": 7,
             "Student (Master's)": 5,
             "Undergraduate applicant": 0,
             "Candidate of Sciences": 8}


some_list = ["Alumnus (Specialist)",
            "Alumnus (Bachelor's)", 
            "Alumnus (Master's)",
            "Student (Master's)",
            ]
relatin_dict ={ 1 : "не женат/не замужем",
                2 : "есть друг/есть подруга",
                3 : "помолвлен/помолвлена",
                4 : "женат/замужем",
                5 : "всё сложно",
                6 : "в активном поиске",
                7 : "влюблён/влюблена",
                8 : "в гражданском браке",
                0 : "не указано"
}



def fix_relatio(data):
    if data in[0,7,3]:
        return 3
    if data in [5,6,8]:
        return 1
    return 2



def priority_studing(data):
    if data in [1,5]:
        return 2
    if data in [0, 7, 2]:
        return 1
    return 3
        
    

def fix_education_status(cell_data):
    return some_dict[cell_data]


def end_start(data):
    if data != 'False':
        return int(data)
    else:
        return 0

def time(ydm):
    if int(ydm.split('-')[1]) >= 6:
        return 2
    if int(ydm.split('-')[0]) == 2021:
        return 2
    return 1

def languages(lang):
    if len(lang.split(';')) >=2:
         return 1
    if len(lang.split(';')) == 1:
        return 0
    


def st_or_not(student):
    if student == 'unversity':
        return 1
    elif student == 'work':
        return 0
    return 1

def people_fix(row):
    if row["people_main"] in [0,6] :
        return 3
    if row["people_main"] in [1,2,5] :
        return 2
    return 1

def life_main(data):
    if data in [6,7]:
        return 3
    if data in [0,1,5]:
        return 2
    return 1


def ed_form(data):
    if data == "Full-time":
        return 1
    return 0

df = pd.read_csv('train.csv')
df['education_form'].fillna('Full-time', inplace = True)

df['has_mobile'] = df['has_mobile'].apply(int)
df['ed_form'] = df['education_form'].apply(ed_form)
df['followers_count'] = df['followers_count'].apply(int)
df['graduation'] = df['graduation'].apply(int)
df['relation'] = df['relation'].apply(int)
df['career_end'] = df['career_end'].apply(end_start)
df['career_start'] = df['career_start'].apply(end_start)
df['people_main'] = df['people_main'].apply(end_start)
df['life_main'] = df['life_main'].apply(end_start)
df['occupation_type'] = df['occupation_type'].apply(st_or_not)
df['last_seen'] = df['last_seen'].apply(time)
df['len langs'] = df['langs'].apply(languages)
df['relation_new'] = df['relation'].apply(fix_relatio)
df['activity'] = df.apply(people_fix, axis=1)
df['education_status'] = df['education_status'].apply(fix_education_status)

df['prioryty'] = df['education_status'].apply(priority_studing)
df['len_langs'] = df['langs'].apply(languages)
df['life_main'] = df['life_main'].apply(life_main)
df.drop(['occupation_name', 
        'city', 
        'bdate', 
        'langs', 
        'education_form',
        'has_photo', 
        'relation', 

        'graduation', 
        'followers_count',
        'career_start' ,
        'career_end',
        'people_main',
        "education_status" ,
        'last_seen',

        'has_mobile',
        'ed_form',
        'occupation_type'
        
       ], axis = 1, inplace = True)

