import unittest 
from maxsliding import maxSlidingWindow


class test_sliding(unittest.TestCase):
    def test_ans(self):
        self.assertEqual(maxSlidingWindow([1,3,-1,-3,5,3,6,7],3),[3, 3, 5, 5, 6, 7])
        self.assertEqual(maxSlidingWindow([1],1),[1])
        self.assertEqual(maxSlidingWindow([1,-1],1),[1,-1])
        self.assertEqual(maxSlidingWindow([9,11],2),[11])
        self.assertEqual(maxSlidingWindow([4,-2],2),[4])

if __name__ == '__main__':
    unittest.main()