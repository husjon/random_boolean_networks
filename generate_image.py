import logging

from PIL import Image, ImageDraw

from random_boolean_network import RandomBooleanNetwork

logging.basicConfig(
    format='%(asctime)-15s %(levelname)-8s %(message)s',
    filename='rbn.log',
    level=logging.DEBUG
)

NODES = 600
NODE_NEIGHBOR_COUNT = 10
ITERATIONS = 800


def main():
    img = Image.new('RGB', (ITERATIONS, NODES), color='black')

    rbn = RandomBooleanNetwork(node_count=NODES,
                               neighbor_count=NODE_NEIGHBOR_COUNT)
    rbn.setup()

    draw = ImageDraw.Draw(img)

    for i in range(ITERATIONS):
        for j, node in enumerate(rbn.nodes):
            if node.state == 1:
                draw.point((i, j), fill='yellow')
            else:
                draw.point((i, j), fill='black')

        rbn.iterate()

    img.save('rbn.png')


if __name__ == "__main__":
    main()
