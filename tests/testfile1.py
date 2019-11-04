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



class MyAddTestCase(unittest.TestCase):
    
    def setUp(self):
        self.person = Add(3,2)

    def test_add(self):
        value = self.person.add()
        self.assertGreater(value , 3) #it will pass because 3+2 is greater than 3

    def test_substract(self):
        value = self.person.substract()
        self.assertFalse(value, 1) #it will fail because 3-2 is 1

    def tearDown(self):
        del self.person



    