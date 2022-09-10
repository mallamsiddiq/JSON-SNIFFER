import unittest
import json

from main import Sniffer


class SnifferTest(unittest.TestCase):

	@classmethod
	def setUpClass(cls):
		# i preload this to reduce cpu call in the tests
		with open("../data/data_2.json", "r") as read_data:
			cls.test_data_2 = json.load(read_data)

	# utility func to be used in a test to make the code more readable
	def sniffUtility(self): 

		sniffer1 = Sniffer()
		sniffer1.load("../data/data_1.json")

		sniffer2 = Sniffer(self.test_data_2["message"])

		# this three is returned to be used in sniffing test
		return sniffer1, sniffer2

	# test Sniffer class instantiation
	def test_snif_instance(self): 
		snf = Sniffer()
		snf2 = Sniffer({"key" : "val"})
		self.assertEqual(snf.data, {}) # empty dict as no data provided at creation
		self.assertEqual(snf2.data, {"key" : "val"}) # A dict was provided at creation and is test against

	# test json data reading to Sniffer.data
	def test_loading(self):

		snf = Sniffer()

		retload = snf.load("../data/data_2.json")

		self.assertEqual(snf.data, self.test_data_2["message"]) # compare updated data with presaved
		self.assertEqual(retload, self.test_data_2["message"]) 	# compare what's returned with presaved

	# test the main sniffing logic 
	def test_sniffing(self):

		sniffer1, sniffer2 = self.sniffUtility()

		sniffer1.sniff()
		sniffer2.sniff()

		# comparing sniffed data with excpected output for different input/output cases
		with open("../data/test_outputs/example_output1.json", "r") as read_data:

			testdata1 = json.load(read_data)
			self.assertEqual(testdata1, sniffer1.data)

		with open("../data/test_outputs/example_output2.json", "r") as read_data:

			testdata2 = json.load(read_data)
			self.assertEqual(testdata2, sniffer2.data)

	# test for json saving method
	def test_output_save(self):

		snf = Sniffer(self.test_data_2)
		snf.save("../data/test_outputs/save_output.json")

		with open("../data/test_outputs/save_output.json", "r") as read_data:

			testdata = json.load(read_data)
		# test if whatever is in self.data is well saved to provided directory at save() call

		self.assertEqual(self.test_data_2, testdata)

if __name__ == '__main__' :
	unittest.main()

