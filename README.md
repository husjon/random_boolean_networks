# Inspiration
[Random Boolean Networks - Computerphile](https://www.youtube.com/watch?v=mCML2B94rUg)


# System
## Setup
* Initialize [Truth Table](#truth-table) with an initial random state
* Instantiate `20` nodes with a random initial boolean state
  * For each node: Set up [Node connections](#node-connections)


## Node connections
Example:

    00 -> 09 04 11
    01 -> 04 04 07
    02 -> 08 18 12

A node can be connected to another time multiple times as seen above with `01 -> 04 04 07`



## Truth Table
Example:
| index | input | value |
|-------|-------|-------|
| 0     | 000   | 1     |
| 1     | 001   | 0     |
| 2     | 010   | 0     |
| 3     | 011   | 1     |
| 4     | 100   | 0     |
| 5     | 101   | 0     |
| 6     | 110   | 1     |
| 7     | 111   | 1     |


# Example images
![rbn.8372505475179784578.png]

![rbn.5726690637511444178.png]

![rbn.9017506907730236911.png]

[rbn.8372505475179784578.png]: https://github.com/husjon/random_boolean_networks/raw/master/images/rbn.8372505475179784578.png
[rbn.5726690637511444178.png]: https://github.com/husjon/random_boolean_networks/raw/master/images/rbn.5726690637511444178.png
[rbn.9017506907730236911.png]: https://github.com/husjon/random_boolean_networks/raw/master/images/rbn.9017506907730236911.png
