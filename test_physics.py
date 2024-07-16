import unittest
from physics import *

class testPhysics(unittest.TestCase):
    def testBuoyancy(self):
        self.assertAlmostEqual(calculate_buoyancy(1, 1), 9.81)
        self.assertAlmostEqual(calculate_buoyancy(100, 1), 981)
        self.assertAlmostEqual(calculate_buoyancy(10, 996), 97707.6)

    def testFloat(self):
        self.assertEqual(will_it_float(1000, 10), True)
        self.assertEqual(will_it_float(1, 1000), False)
        self.assertEqual(will_it_float(-1, 1000), None)

    def testPressure(self):
        self.assertEqual(calculate_pressure(0), 101325)
        self.assertAlmostEqual(calculate_pressure(10), 199425)
        self.assertAlmostEqual(calculate_pressure(-10), 199425)

    def testAcceleration(self):
        self.assertEqual(calculate_acceleration(10, 1), 10)
        self.assertEqual(calculate_acceleration(0, 10), None)
        self.assertEqual(calculate_acceleration(-10, 10), -1)
        self.assertEqual(calculate_acceleration(-10, -10), None)

    def testAngularAcceleration(self):
        self.assertAlmostEqual(calculate_angular_acceleration(10, 0.33), 30.30)
        self.assertEqual(calculate_angular_acceleration(10, 0), None)
        self.assertEqual(calculate_angular_acceleration(0, 0.33), None)
        self.assertAlmostEqual(calculate_angular_acceleration(-10, 0.33), -30.30)

    def testTorque(self):
        
