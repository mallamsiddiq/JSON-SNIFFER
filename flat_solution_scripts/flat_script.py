import json


type_names = {int:'INTEGER', float:'NUMBER',str:'STRING', dict:'OBJECT', list:'ARRAY', bool:'BOOLEAN'}

class Sniffer: 

    def __init__(self, data : dict = {}):

        self.data = data

    # to load data from json dir and overide the self.data with deserialized object
    def load(self, path : str ) -> dict:

        with open(path, "r") as read_data:
            self.data = json.load(read_data)['message']
        return self.data # in case you want the sniffed data returned

    # the main func to sniff through the deserialized json
    def sniff(self):

        ret_arr = []

        def dfs(node): # depth first search algorith that perform the main logic

            for ch_node in node: # go trough all children nodes
                new_dict = {"type": type_names[type(node[ch_node])], "tag": "", "description": ""}
                if new_dict['type'] == "OBJECT": # if child is object go through depths recursively
                    dfs(node[ch_node])

                elif new_dict['type'] == "ARRAY":
                    if node[ch_node] and type(node[ch_node][0]) == dict: # i first confirm list exixtence to avoid index out of range

                        # i pick 1st or just any objects in ARRAY
                        dfs(node[ch_node][0])

                    # otherwise, chage type from array to ENUM 
                    else:

                        new_dict['type'] = 'ENUM'

                new_dict["required"] = False

                ret_arr.append(new_dict)

        dfs(self.data)

        self.data = ret_arr

    def save(self, path):

        json_object = json.dumps(self.data, indent = 4)

        with open(path, "w") as outfile:
            outfile.write(json_object)

if __name__ == '__main__' :

    try_sniff = Sniffer()

    try_sniff.load("../../data/data_2.json")

    try_sniff.sniff()

    try_sniff.save("./example_output2_flat.json")

    try_sniff = Sniffer()

    try_sniff.load("../../data/data_1.json")

    try_sniff.sniff()

    try_sniff.save("./example_output1_flat.json")

