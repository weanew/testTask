from html_generator.generator import generator_task1

if __name__ == '__main__':
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
    res = generator_task1(request)
    print(res)