import unittest
from html_generator.generator import main_generator


class TestGenerator(unittest.TestCase):

    def test_generator_task3(self):
        request = """
                    [
                       {
                          "h3": "Title #1",
                          "div": "Hello, World 1!"
                       },
                       {
                          "h3": "Title #2",
                          "div": "Hello, World 2!"
                       }
                    ]
                    """
        response = '<ul><li><h3>Title #1</h3><div>Hello, World 1!</div></li><li><h3>Title #2</h3>' \
                   '<div>Hello, World 2!</div></li></ul>'
        self.assertEqual(main_generator(request), response)

    def test_generator_task4(self):
        request = """
                    [
                       {
                          "span": "Title #1",
                          "content": [
                            {
                                "p": "Example 1",
                                "header": "header 1"    
                            }
                          ]
                       },
                       {"div": "div 1"}
                    ]
                    """
        response = '<ul><li><span>Title #1</span><content><ul><li><p>Example 1</p><header>header 1</header></li></ul>' \
                   '</content></li><li><div>div 1</div></li></ul>'
        self.assertEqual(main_generator(request), response)


if __name__ == '__main__':
    unittest.main()
