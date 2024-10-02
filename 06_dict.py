# key:value
library={
    "Шевченко":["Катерина","Кобзар","Заповіт"],
    "Франко":["Каменярі","Фарбований лис"]
}

print(library["Шевченко"][1])
print(list(library.keys()))
print("*"*30)
for author in library.keys():
    print("author=",author)
    # print(library[author])
    count=1
    for book in library[author]:
        print(f"\t{count}.{book}")
        count+=1

print("*"*30)
for books in library.values(): 
    print("books:",books)

print(list(library.items()))
library["Леся Українка"]=["Лісова пісня","Contra Spem..."]
# library["Леся Українка"]="Лісова пісня"

print("*"*30)
for author, books in library.items(): #(key, value)
    print(f"Author {author} wroten:")
    count=1
    for book in books:
        print(f"\t{count}. {book}")
        count+=1

groups=["I-21", "CT-21"]
count_students=[22,20]
print(list(zip(groups,count_students)))
print(tuple(zip(groups,count_students)))
print(dict(zip(groups,count_students)))
print(dict([(x, x*x) for x in range(1,21)]))

print("*"*30)
# key_lib=iter(library)
# print(next(key_lib))
# print(next(key_lib))
# print(next(key_lib))
# print(next(key_lib))

# groups=library.fromkeys()
library.setdefault("Stus","[]")
print(library["Stus"])
