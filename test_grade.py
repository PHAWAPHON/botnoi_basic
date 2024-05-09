import pandas as pd 

#สร้างฟังก์ชันสําหรับคํานวณเกรด
def calculate_grade(score):
    if score >= 80:
        return 'A'
    elif score >= 70:
        return 'B'
    elif score >= 60:
        return 'C'
    elif score >= 50:
        return 'D'
    else:
        return 'F'

def main():

    #อ่านไฟล์excel มาเก็บในตัวแปร df
    df = pd.read_excel('grades_with_grades.xlsx')
    
    #df.dtypes

    #แปลง datatype ของคะแนนให้เป็นตัวเลข
    df['คะแนน'] = pd.to_numeric(df['คะแนน'], errors='coerce')
    
    #แปลงคะแนนในคอลัมน์เป็นเกรด
    df['เกรด'] = df['คะแนน'].apply(calculate_grade)

   #df['เกรด'] = pd.Categorical(df['เกรด'], categories=['A', 'B', 'C', 'D', 'F'], ordered=True)

    #เรียงลําดับตามเกรด
    df = df.sort_values(['เกรด', 'คะแนน'], ascending=[True, False])
    
    #overwrite 
    df.to_excel('grades_with_grades.xlsx', index=False)


if __name__ == '__main__':
    main()
