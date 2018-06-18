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
	def testequalityFloat(self):
		a = v.Vect2D([0.2,.34])
		b = (1+1e-5)*a
		self.assertNotEqual(a,b)
		b = (1+1e-14)*a
		self.assertEqual(a,b)
	def testchangeNormwithR(self):
		a = v.Vect2D([1,2])
		b = v.Vect2D([1,2])
		a.r = 3
		self.assertEqual(3,a.norm())
		self.assertEqual(0,b^a)
	
	def testpolarCoord(self):
		a = v.Vect2D([1,0])
		self.assertEqual(a.r,1)
		self.assertEqual(a.phi,0)
		a.y=-1
		self.assertEqual(a.phi%360,315)
		a.phi = 90
		self.assertEqual(v.Vect2D([0,1]),a)
		a = v.Vect2D(25,0.0)
		self.assertEqual(a.phi,0)

unittest.main()