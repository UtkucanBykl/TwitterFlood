import unittest

from base import TweetFlood


class Testing(unittest.TestCase):

    def setUp(self):
        self.obj = TweetFlood("This is a flood", split_length=5)

    def test_missing_token(self):
        auth = self.obj.getAuth()
        self.assertEqual(auth, None)

    def test_auth_raise(self):
        self.assertRaises(BaseException, self.obj.setAuth("1", "1", "1", "1"))

    def test_tweet_array(self):
        self.assertListEqual(self.obj.tweet_array(), ["This", "is a", "flood"])




if __name__ == '__main__':
    unittest.main()