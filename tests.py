import unittest
from html_generator.generator import generator_task1, generator_task2


class TestGenerator(unittest.TestCase):

    def test_generator_task1(self):
        request = """
                [
                   {
                      "title": "Title #1",
                      "body": "Hello, World 1!"
                   },
                   {
                      "title": "Title #2",
                      "body": "Hello, World 2!"
                   }
                ]
                """
        response = '<h1>Title #1</h1><p>Hello, World 1!</p><h1>Title #2</h1><p>Hello, World 2!</p>'
        self.assertEqual(generator_task1(request), response)

    def test_generator_task2(self):
        request = """
                    [
                       {
                          "h3": "Title #1",
                          "div": "Hello, World 1!"
                       }
                    ]
                    """
        response = '<h3>Title #1</h3><div>Hello, World 1!</div>'
        self.assertEqual(generator_task2(request), response)


if __name__ == '__main__':
    unittest.main()
