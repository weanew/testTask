import unittest
from html_generator.generator import generator_task1


class TestGenerator(unittest.TestCase):

    def test_generator_task1(self):
        request = """
                [
                   {
                      "title":"Title #1",
                      "body":"Hello, World 1!"
                   },
                   {
                      "title":"Title #2",
                      "body":"Hello, World 2!"
                   }
                ]
                """
        response = '<h1>Title #1</h1><p>Hello, World 1!</p><h1>Title #2</h1><p>Hello, World 2!</p>'
        self.assertEqual(generator_task1(request), response)


if __name__ == '__main__':
    unittest.main()
