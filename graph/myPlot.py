import numpy as np
import logging
import matplotlib.pyplot as plt
import scipy.stats as stats


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
    
    # def CFRGraph(self,csi:np.array) -> None:
    #     plt.plot(csi)
    #     plt.xlabel("subCarrier")
    #     plt.ylabel(r"$\phi$")
    #     plt.title("Motion Statistic")
    #     plt.ylim(-0.2,1)
    #     plt.show()

    def QQPlot(self, data: np.array) -> None:
        # noise Q-Q plot
        
        stats.probplot(data, dist="norm", plot=plt)
        plt.title('Q-Q plot')
        plt.xlabel('Theoretical quantiles')
        plt.ylabel('Ordered Values')
        plt.grid(True)

        # OutputName = f"./result/QQPlot/static_sub{subIndex}.png"
        # plt.savefig(OutputName)
        plt.show()
    
    def plotCrossCorrelation(self,data:np.array)->None:
        plt.imshow(data, cmap='Blues', interpolation='nearest')
        plt.gca().invert_yaxis()
        plt.colorbar(label='Cross Correlation')
        plt.title('Cross Correlation Matrix')
        plt.xlabel('subCarrier Index')
        plt.ylabel('subCarrier Index')
        plt.show()


def main():
    pass


if __name__ == "__main__":
    main()
