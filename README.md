# dOc [please, Read ME]

### A MODULE THAT SNIFFS SCHEMA OF A JSON FILE AND OUTPUT ACCORDINGLY

### Overview

The case is to read  a nested JSON file and write generic algorithm that:

- Sniffs the schema of the JSON file 
- Dumps the output in (./schema/)

more info inside PROBLEM.md


### The files and folders

The ./data/ contains the test data to be sniffed, in it i created a folder /test_outputs/ that houses the data i use for test cases.

The ./schema/ is the folder that expects my outputs from data_1, data_2 as schema_1.json and schema_2.json respectively. Inside with i saved my sniffed .json outputs as required

the ./main_scripts/ contains the main.py and test.py files for the logic and also the unit testing functionalities

while flat_solution_scripts contains the flat_script.py which I created  to compensate for the ambiguity on what to do with the nested objects, alongside its simulated outputs example_output1_flat.json, example_output1_flat.json mapping data_1.json and data_2.json. Returning flatter json outputs [not nested]. More on this later. 


### Implementation

I have solved this problem using a depth first search algorithm with a backtracking approach. I consider each object to be a node of a tree since the objects don't have an interwoven relationship with each other i.e a child can't be a parent to any of its ancestors [hierarchical order] and a child don’t have multiple parents. Hence I feel safe to model the problem as a tree.

I have also considered several data types [bool -> BOOLEAN, float -> NUMBER, and objects -> OBJECT].

in a case when the type is an object or an array of objects: i add an additional padding "nested-properties' ' and "items' ' respectively to recursively continue attaching the children objects schema. And return a backtrack node.

### NOTE

As the documentation doesn't give a clarifying directive as what to do with nested objects, alongside my prefered solution earlier explained i hereby also consider another solution which is also recursive but not backtracking, by going down the nodes i just append each objects to a list of objects and later return it as .json which results in a flat json object of a single top layer. Kindly check the flat_solution_scripts folder for the script and its associated sample output for each of data_1 and data_2.json. I didn't write test case for this module as i only introduced it to clear the ambiguities, kindly reach out to me in case of any required addition or changes

## RUNNING

The script that performs the main logic is the ./main_scripts/main.py file contained as a class : Sniffer that takes in nothing by default but you can instantiate with a dict object if a deserialized json object is available. in this class is a method load(path) that takes in a path to json to read then deserializes and updates it to Sniffer.data. Also, I created a sniff() method that does the main sniffing logic and updates the Sniffer.data variable without wasting memory extraspace.

so with python installed on your machine, right inside the ./main_scripts/ directory; you can run :

		python -m unittest test

for the unittest module. I have created a few test cases to test for the functionalities of my module.

### via Console

So right in this ./main_scripts/ directory you can make a call to the module Objects: Sniffer and play around with its methods as a typical example that follows:

	>>> from main import Sniffer
	>>> snf = Sniffer()
	>>> snf.data	#	check the predefined value as empty object
	{}   

	# load a .json file and deserialize then save to self.data
	>>> snf.load("../data/data_2.json")  # 
	{'user': {'id': 'ABCDEFGHIJKLMNOP', 'nickname': 'ABCD', 'title': 'ABCDEFGHIJKLMNOPQRSTUVWXYZABC', 
	'accountType': 'ABCDEFGHIJKLMNOPQRSTUVWX', 'countryCode': 'ABCDEFGHIJKLMNOPQRSTUVWX', 'orientation': 'ABCDEFGHIJKLMNOPQRSTU'}, 
	'time': 890, 'acl': [], 'publicFeed': False, 'internationalCountries': ['ABCDEFGHIJKLMNOPQRSTUVWXYZA', 
	'ABCDEFGHIJKLMNOPQ', 'ABCDEFGHIJKLMNOPQRSTUVW', 'ABCDEFGHIJKLMNOPQRSTUVWXY', 'ABCDEFGHIJK', 
	'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'ABCDEFGHIJKLMNOPQR', 'ABCDEFG', 'ABCDEFGHIJKLM'], 'topTraderFeed': True}

	#	sniff the data and return to self.data object
	>>>	snf.sniff()

	# 	casually view the updated sniffed data
	>>> snf.data
	{'user': {'type': 'OBJECT', 'tag': '', 'description': '', 'nested-properties': {'id': {'type': 'STRING', 'tag': '', 
	'description': '', 'required': False}, 'nickname': {'type': 'STRING', 'tag': '', 'description': '', 'required': False}, 
	'title': {'type': 'STRING', 'tag': '', 'description': '', 'required': False}, 'accountType': {'type': 'STRING', 
	'tag': '', 'description': '', 'required': False}, 'countryCode': {'type': 'STRING', 'tag': '', 'description': '', 
	'required': False}, 'orientation': {'type': 'STRING', 'tag': '', 'description': '', 'required': False}}, 'required': False}, 
	'time': {'type': 'INTEGER', 'tag': '', 'description': '', 'required': False}, 'acl': {'type': 'ENUM', 'tag': '', 
	'description': '', 'required': False}, 'publicFeed': {'type': 'BOOLEAN', 'tag': '', 'description': '', 
	'required': False}, 'internationalCountries': {'type': 'ENUM', 'tag': '', 'description': '', 'required': False}, 
	'topTraderFeed': {'type': 'BOOLEAN', 'tag': '', 'description': '', 'required': False}}
	>>>

	#	save/ write the sniffed schema to the provided valid path as a .json object
	>>> snf.save("./console.json")

I have written more unit test to further cover more edge cases


thanks 

SODIQ


further complaints to @mallamsiddiq@gmail.com




