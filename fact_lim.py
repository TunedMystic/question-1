import sys
import operator
import unittest


def decremented_list(start, length):
  """
  Return a descending list of values starting
  at 'start', with a length of 'length'.
  
  For example:
  decremented_list(5, 2) -> [5, 4]
  decremented_list(8, 5) -> [8, 7, 6, 5, 4]
  decremented_list(3, 1) -> [3]
  """

  stop_value = start - length
  if stop_value < 0:
    stop_value = 0
  return range(start, stop_value, -1)

def fact_lim(n, lim):
  """
  Calculate the summation of the factorials of all
  numbers starting from n and ending at n - lim from 1 to n.
  """
  # Check if 'n' or 'lim' are less than 1.
  if n < 1 or lim < 1:
    raise Exception(
      "Incorrect value for n ({0}) or lim ({1})".format(n, lim)
    )
  # Check if 'lim' if greater than 'n'.
  if lim > n:
    raise Exception(
      "Value for lim ({0}) cannot be more than n ({1})".format(lim, n)
    )
  # For values from 1 to n, make a decremented
  # list (start at n, stop at n - lim).
  reduced_values = [decremented_list(x, lim) for x in range(1, n + 1)]
  # Get the product of each sublist in 'reduces_values'.
  reduced_values = [reduce(operator.mul, chunk) for chunk in reduced_values]
  # Return the sum of each value in 'reduced_values'.
  return sum(reduced_values)


class FunctionTester(unittest.TestCase):
  def test_exception_cases(self):
    self.assertRaises(Exception, fact_lim, -1, 2)
    self.assertRaises(Exception, fact_lim, 3, -1)
    self.assertRaises(Exception, fact_lim, 4, 7)
  
  def test_success_cases(self):
    self.assertEqual(fact_lim(1, 1), 1)
    self.assertEqual(fact_lim(2, 1), 3)
    self.assertEqual(fact_lim(2, 2), 3)
    self.assertEqual(fact_lim(3, 2), 9)
    self.assertEqual(fact_lim(5, 1), 15)
    self.assertEqual(fact_lim(5, 2), 41)
    self.assertEqual(fact_lim(5, 4), 153)


if __name__ == "__main__":
  if "test" in sys.argv[1:]:
    sys.argv.pop()
    unittest.main()
