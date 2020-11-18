import logging

from PIL import Image, ImageDraw, ImageFont

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
    img = Image.new('RGB', (ITERATIONS, NODES+24), color='black')

    rbn = RandomBooleanNetwork(node_count=NODES,
                               neighbor_count=NODE_NEIGHBOR_COUNT,
                               seed=None)
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

    fnt = ImageFont.FreeTypeFont('fonts/Roboto/Roboto-Regular.ttf', size=20)
    draw.text((5, 600), text=f'Seed: {rbn.seed}', fill='red', font=fnt)
    draw.text((300, 600), text=f'Iterations: {ITERATIONS} - Nodes: {rbn.node_count} - Neighbors: {rbn.neighbor_count}', fill='red', font=fnt)
    img.save('rbn.png')


if __name__ == "__main__":
    main()
