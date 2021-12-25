# assert sum([1, 2, 3]) == 6 , "Should be 6"

# def sum(nums):
#     result = 0
#     for n in nums:
#         result += n
#     #return result
#     return 0

# sum_3 = sum([1,2,3])
# print(sum_3)

# assert sum([1,2,3]) == 6,"Should be 6"

# def test_sum():
#     assert sum([1, 2, 3]) == 6, "Should be 6"

# if __name__ == "__main__":
#     test_sum()
#     print("Everything passed")


# nose
# import unittest


# class TestSum(unittest.TestCase):

#     def test_sum(self):
#         self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")

#     def test_sum_tuple(self):
#         self.assertEqual(sum((1, 2, 2)), 5, "Should be 5")

# if __name__ == '__main__':
#     unittest.main()

#pytest
def test_sum():
    assert sum([1, 2, 3]) == 6, "Should be 6"

def test_sum_tuple():
    assert sum((1, 2, 2)) == 6, "Should be 6"