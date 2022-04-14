import pymongo #pymongo is driver to make connection between python and mongodb

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

db=myclient["selenium"]
mycol=db["mongo"]
mydict=[{"SNO":105,"SNAME":"SUREKHA","SCOURSE":"DATA SCIENCE","SADDRESS":"BANGALORE"},
       {"SNO":101,"SNAME":"TEJASWINI","SCOURCE":"PYTHON","SADDRESS":"HYDERABAD"},
       {"SNO":102,"SNAME":"SAI","SCOURE":"SALESFORCE","SADDRESS":"MUMBAI"},
       {"SNO":103,"SNAME":"PRAVEEN","SCOURSE":"MEDICAL CODING","SADDRESS":"CHENNAI"}]
x=mycol.insert_many(mydict)
print(x.inserted_ids)
