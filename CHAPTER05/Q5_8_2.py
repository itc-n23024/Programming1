d = [
    ["01", "0001", "Male", "Yamada", "Tarou", 25, "Tokyo"],
    ["01", "0002", "Male", "Satou", "Takeshi", 27, "Kanagawa"],
    ["01", "0003", "Female", "Tanaka", "Yuko", 25, "Saitama"],
    ["02", "0004", "Male", "Smith", "Mika", 22, "NewJersey"],
    ["02", "0005", "Male", "Turnur", "Tom", 27, "Kansas"],
    ["02", "0006", "Male", "Jackson", "David", 22, "Florida"],
]
print(d)
member_information = {}
for record in d:
    key = (record[0], record[1])
    info = record[2:]
    member_information[key] = info
print("number", "information", sep="\t")
for key, info in member_information.items():
    print(key, info)
