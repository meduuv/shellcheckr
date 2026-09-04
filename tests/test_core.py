import unittest
from shellcheckr.core import lint
class Tests(unittest.TestCase):
 def test_rule(self): self.assertTrue(lint('rm -rf $HOME'))
if __name__=='__main__': unittest.main()
