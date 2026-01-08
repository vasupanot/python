#Hello

data={
"Name":"Vasudev",
"Surname":"Panot",
"City" :"Bhavnagar",
"Dob":"23-09-2005",
"Taluka":"Talaja",
"Fav City":"kutch",
"Fav Book":"Geeta",
"Fav Fruit":"Apple",
"Fav Place":"Mahadev temple",
"State:":"Gujarat",
"Country":"india",
"College":"SSCCS",
"Cource":"BCA",
"Semester":6,
"Language":"Gujarati",
"IsMarried":False,
"Gender":"Male",
"Height":6.2,
"Weight":72,
"Age":20,
}

#Print Dictionary
print(data)
print(data["Name"],data["Gender"],data["Age"],data["Dob"])

#add pincode
data["Pincode"]=364120
print(data)

#destinations
data["FavDestinations"]=["Bortalav","Kutch","Dwarka","Salangpur","Malnath temple"]

print("favorite Destinations :",data["FavDestinations"])