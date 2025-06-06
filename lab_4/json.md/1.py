import json

with open("sample-data.json", "r") as file:
    data = json.load(file)

print("Interface status")
print("=" * 80)
print("DN", " " * 40, "Description ", "speed", " " * 10, "MTU")
print("-" * 42, "-" * 13, "-" * 13, "\t", "-" * 5)
for imdata in data["imdata"]:
    for i in imdata:
        for j in imdata[i]: 
            print(imdata[i][j]["dn"],"\t", "\t"  , imdata[i][j]["speed"] ,"\t" , imdata[i][j]["mtu"])