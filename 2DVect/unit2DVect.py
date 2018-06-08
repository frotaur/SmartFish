import unittest
import Vect2D as v

class testVect(unittest.TestCase):
	def testStr(self):
		a = v.Vect2D((1,2))
		self.assertEqual("(1,2)",str(a))

	def testAddandEqual(self):
		a = v.Vect2D((1,2))
		b = v.Vect2D((2,6))

		self.assertEqual(v.Vect2D((3,8)),a+b)
	def testDot(self):
		a = v.Vect2D((1,2))
		b = v.Vect2D((2,6))
		self.assertEqual(14,a*b)
	def testCross(self):
		a = v.Vect2D((1,2))
		b = v.Vect2D((2,6))
		self.assertEqual(2,a^b)
		self.assertEqual(-2,b^a)
	def testScalMult(self):
		a = v.Vect2D([1,2])
		self.assertEqual(v.Vect2D([4,8]),4*a)
		self.assertEqual(v.Vect2D([0.5,1]),a*0.5)
	def equalityFloat(self):
		a = v.vect2D([0.2,.34])
		b = (1+1e-5)*a
		self.assertNotEqual(a,b)
		b = (1+1e-14)*a
		self.assertEqual(a,b)
	def changeNormwithR(self):
		a = v.Vect2D([1,2])
		b = v.Vect2D([1,2])
		a.r = 3
		self.assertEqual(3,a.norm())
		self.assertEqual(0,b^a)
unittest.main()