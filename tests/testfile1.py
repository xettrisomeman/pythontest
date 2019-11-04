import unittest
from file1 import Add , Person




class MyTestPerson(unittest.TestCase):

    def setUp(self):
        self.person = Person()


    def test_create(self):
        new_person = self.person.name("John" , "Smith")
        self.assertEqual(new_person, "JohnSmith")

    def tearDown(self):
        del self.person


