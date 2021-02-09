import unittest
from html_generator.generator import *


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
        self.assertEqual(generator_task3(request), response)

    def test_generator_task4(self):
        request = """
                    [
                       {
                          "span": "Title #1",
                          "content": [
                            {
                                "p": "example 1",
                                "header": "header 1"    
                            }
                          ]
                       },
                       {"div": "div 1"}
                    ]
                    """
        response = '<ul><li><span>Title #1</span><content><ul><li><p>Example 1</p><header>header 1</header></li></ul>' \
                   '</content></li><li><div>div 1</div></li></ul>'
        self.assertEqual(generator_task4(request), response)

    def test_generator_task5(self):
        request = """
                    {
                       "p.my-class#my-id":"hello",
                       "p.my-class1.my-class2":"example<a>asd</a>"
                    }
                    """
        response = '<p class="my-class" id="my-id">hello</p><p class="my-class1 my-class2">example&lt;a&gt;asd&lt;' \
                   '/a&gt;</p>'
        self.assertEqual(generator_task5(request), response)


if __name__ == '__main__':
    unittest.main()
