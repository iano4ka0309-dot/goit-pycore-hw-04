def get_cats_info(path):
    cat_list = []  
    try:
        
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()  
                if line:             
                    cat_id, name, age = line.split(',')
                    cat_list.append({
                        "id": cat_id, 
                        "name": name, 
                        "age": int(age)
                    })
        return cat_list
        
    except FileNotFoundError:
        print(f"помилка: Файл не знайдено {path}")
        return []
   


path_to_cats = r"C:\Users\PC\Desktop\cats.txt"


print(get_cats_info(path_to_cats))






