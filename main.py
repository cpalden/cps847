import unittest

class SimpleCall(unittest.TestCase):
	def setUp(self):
		print "Set up"
		
	def tearDown(self):
		print "Tear down"
		
	def test_main(self):
		#Code for the test_main
		self.assertEqual(3,3,'We are Equal')
		
if __name__ == '__main__':
	unittest.main()