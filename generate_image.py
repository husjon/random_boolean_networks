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

    point_list_on = []
    point_list_off = []
    for i in range(ITERATIONS):
        for j, node in enumerate(rbn.nodes):
            if node.state == 1:
                point_list_on.append((i, j))
            else:
                point_list_off.append((i, j))

        rbn.iterate()

    draw.point(point_list_on, fill='yellow')
    draw.point(point_list_off, fill='black')
    img.save('rbn.png')


if __name__ == "__main__":
    main()
