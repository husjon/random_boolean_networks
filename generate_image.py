import logging

from PIL import Image, ImageDraw, ImageFont

from random_boolean_networks import RandomBooleanNetwork

logging.basicConfig(format='%(asctime)-15s %(levelname)-8s %(message)s',
                    filename='rbn.log',
                    level=logging.INFO)

NODES = 20
NODE_NEIGHBOR_COUNT = 3
ITERATIONS = 50

SCALING = 5
FONT_SIZE = 10


def main():
    img = Image.new('RGB', (ITERATIONS * SCALING, NODES * SCALING + 20),
                    color='black')

    rbn = RandomBooleanNetwork(node_count=NODES,
                               neighbor_count=NODE_NEIGHBOR_COUNT,
                               seed=None)
    rbn.setup()

    draw = ImageDraw.Draw(img)

    for i in range(ITERATIONS):
        for j, node in enumerate(rbn.nodes):
            if node.state == 1:
                rect = (
                    i * SCALING,            # x1
                    j * SCALING,            # y1
                    i * SCALING + SCALING,  # x2
                    j * SCALING + SCALING   # y2
                )
                draw.rectangle(rect, fill='red', outline='red' if SCALING == 1 else 'black')

        rbn.iterate()

    fnt = ImageFont.FreeTypeFont(font='fonts/Roboto/Roboto-Regular.ttf',
                                 size=FONT_SIZE)
    draw.text(xy=(1, NODES * SCALING - 1),
              text=f'S: {rbn.seed}',
              fill='red',
              font=fnt)
    draw.text(xy=(1, NODES * SCALING + FONT_SIZE - 1),
              text=f'I: {ITERATIONS} - N: {rbn.node_count} - P: {rbn.neighbor_count}',
              fill='red',
              font=fnt,
              align='right')
    img.save('rbn.png')

if __name__ == "__main__":
    main()
