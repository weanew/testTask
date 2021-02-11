# import asyncio
from html_generator.generator import main_generator
INPUT_FILE = 'input/source.json'
OUTPUT_FILE = 'output/index.html'


if __name__ == '__main__':
    request = ''
    with open(INPUT_FILE, 'r') as f:
        request = f.read()

    response = main_generator(request)

    with open(OUTPUT_FILE, 'w') as f:
        request = f.write(response)


    # uri = 'ws://localhost:8765'
    # asyncio.get_event_loop().run_until_complete(run_con(uri))