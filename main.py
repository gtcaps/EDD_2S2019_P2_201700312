import csv
import json
import hashlib
from datetime import datetime

def get_data_csv(name):
    try:
        with open('./blocks/{}asd.csv'.format(name)) as csv_file:
            csv_reader = csv.reader(csv_file)
            data = {
                "class": None,
                "data": None
            }

            for row in csv_reader:
                if len(row) > 0:
                    if row[0] == 'class':
                        data["class"] = row[1]
                    elif row[0] == 'data':
                        data["data"] = json.loads(row[1])
        csv_file.close()

        return data
    except:
        print("[Error] No se encontro el archivo solicitado, verique que se encuentre dentro de la carpeta blocks y sea extension .csv")
        return {
            "class": None,
            "data": None
         }
                

def hash_256(index, timestamp, class_name, data, previous_hash):
    string = '{}{}{}{}{}'.format(str(index),str(timestamp),str(class_name), data.replace(" ",""),str(previous_hash))
    hash = hashlib.sha256(string.encode())
    return str(hash.hexdigest())

def data_to_json(file_name):
    data = get_data_csv(file_name)
    block = {
		"INDEX": 0,
		"TIMESTAMP": "{}".format(datetime.now().strftime('%d-%m-%Y-::%H:%M:%S')),
		"CLASS": "{}".format(data["class"]),
		"DATA": data["data"],
		"PREVIOUSHASH": "0000",
		"HASH": None
	}
    block["HASH"] = hash_256(block["INDEX"], block["TIMESTAMP"], block["CLASS"], json.dumps(block["DATA"]), block["PREVIOUSHASH"])
    block = json.dumps(block)

    return block


def verify_json_string(json_string):
    try:
        block = json.loads(json_string)
        data_block = block["DATA"]

        if type(data_block) is not dict:
            data_block = json.loads(data_block)
        
        verify_hash = hash_256(block["INDEX"], block["TIMESTAMP"], block["CLASS"], json.dumps(data_block), block["PREVIOUSHASH"])

        print("Verified Hash: {}".format(verify_hash))
        print("Block Hash: {}".format(block["HASH"]))

        if verify_hash == block["HASH"]:
            return True
        else:
            return False
            
    except:
        print('[Error] No se puede verificar la cadena')
        return False



cadena = data_to_json('file')
print(verify_json_string(cadena))


print("---------------------------")

with open('answer.json') as file:
    data = file.read()
file.close()

print(verify_json_string(data))