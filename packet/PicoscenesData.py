import json
import numpy as np
import logging

from picoscenes import Picoscenes

from packet.PacketData import PacketData
from packet.PacketFormatEnum import PacketFormatEnum

class PicoscenesData:
    def __init__(self, data_path):
        self.logger = logging.getLogger(__name__)
        self.data_path = data_path
        self.logger.setLevel(logging.DEBUG)
        # self.datas = [PacketData(item) for item in Picoscenes(self.data_path).raw]

    def __len__(self):
        return len(self.datas)

    def loadData(self, datas: list) -> None:
        self.datas = [PacketData(item) for item in datas]
        self.logger.debug("self.data has {} item".format(len(self.datas)))

    def filterFormat(self, format: PacketFormatEnum) -> None:
        self.datas = [
            data for data in self.datas if data.RxSBasic.packetFormat == format.value
        ]
        self.logger.debug(
            "self.data only has {} format item, len={}".format(format, len(self.datas))
        )

    def filterBandwidth(self, bandwidth: int) -> None:
        # RxSBasic.CBW 跟 CSI.CBW 貌似不一樣 要查一下why?? 查過可能是router自動降低bandwidth
        self.datas = [data for data in self.datas if data.CSI.CBW == bandwidth]
        self.logger.debug(
            "self.data only has {} bandwidth item, len={}".format(
                bandwidth, len(self.datas)
            )
        )

    # try to use yield
    def splitData(self, sampleSize: int) -> np.array:
        # 假設在收集資料的時候就確保了 sampleRate 為穩定的且資料量都正確
        # 但還是要確定一下
        # 應該要分成 每n個一組 跟 每t 前幾秒內一組 有好多種分法
        self.logger.warning("make sure data's sample rate is correct, and split method")

        # 先寫成 每 n 個一組
        for i in range(0, len(self.datas), sampleSize):
            processed_chunk = self.datas[i : i + sampleSize]
            yield np.array(processed_chunk)

    def getSubcarrier(
        self, samples: np.array, carrierIndex: int, parameter: str
    ) -> np.array:
        if samples[0].CSI.numTones <= carrierIndex or carrierIndex < 0:
            raise ValueError(
                "carrierIndex out of range only in 0-{}".format(samples[0].CSI.numTones)
            )
        if not hasattr(samples[0].CSI, parameter):
            raise ValueError("parameter out of range")

        return np.array(
            [getattr(data.CSI, parameter)[carrierIndex] for data in samples]
        )

    # yeild sample as dataSize
    # def

    # 輸入的array應該會是已經經過sample rate分好後的資料
    # 所以應該直接用 lag = 1 來算也可以
    def autoCov(self, samples: np.array, lag: int) -> float:
        n = len(samples)
        mean = np.mean(samples)
        lis = (samples[: n - lag] - mean) * (samples[lag:] - mean)

        acvf = np.sum(lis) / n
        return acvf

    def calAvgMotionStatistic(self, sampleSize: int) -> float:
        if len(self.datas) == 0:
            raise ValueError("No data")
        sampleSubCarrier = self.datas[0].CSI.numTones

        result = []
        for samples in self.splitData(sampleSize):
            motion = 0.0
            for i in range(sampleSubCarrier):
                subcarrierSample = self.getSubcarrier(samples, i, "Mag")
                motion += self.autoCov(subcarrierSample, 1) / self.autoCov(
                    subcarrierSample, 0
                )
            result.append(motion / sampleSubCarrier)
        return result

    def getDatas(self, index: int):
        return self.datas[index]

    # 或許可以用這個來接收資料避免資料過大
    # @retry
    # def connectEdge(self, edge: str) -> None:

if __name__=="__main__":
    print("hello")