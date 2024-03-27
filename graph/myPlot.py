import numpy as np
import logging
import matplotlib.pyplot as plt


class myPlot:
    def __init__(self) -> None:
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)
        plt.figure()

    def motionGraphByBatch(self, result: np.array) -> None:
        plt.plot(result)
        plt.xlabel("batch")
        plt.ylabel(r"$\phi$")
        plt.title("Motion Statistic")
        plt.ylim(-0.2,1)
        plt.show()


def main():
    pass


if __name__ == "__main__":
    main()
