class PacketData:
    def __init__(self, data):
        self.StandardHeader = StandardHeader(data['StandardHeader'])
        self.RxSBasic = RxSBasic(data['RxSBasic'])
        self.RxExtraInfo = RxExtraInfo(data['RxExtraInfo'])
        self.CSI = CSI(data['CSI'])
        self.MVMExtra = MVMExtra(data['MVMExtra'])
        self.MPDUS = data['MPDUS']
    def __str__(self):
            return str(self.__dict__)

class StandardHeader:
    def __init__(self, data):
        self.ControlField = ControlField(data['ControlField'])
        self.Addr1 = data['Addr1']
        self.Addr2 = data['Addr2']
        self.Addr3 = data['Addr3']
        self.Fragment = data['Fragment']
        self.Sequence = data['Sequence']
    def __str__(self):
            return str(self.__dict__)

class ControlField:
    def __init__(self, data):
        self.Version = data['Version']
        self.Type = data['Type']
        self.SubType = data['SubType']
        self.ToDS = data['ToDS']
        self.FromDS = data['FromDS']
        self.MoreFrags = data['MoreFrags']
        self.Retry = data['Retry']
        self.PowerManagement = data['PowerManagement']
        self.More = data['More']
        self.Protected = data['Protected']
        self.Order = data['Order']
    def __str__(self):
            return str(self.__dict__)

class RxSBasic:
    def __init__(self, data):
        self.deviceType = data['deviceType']
        self.timestamp = data['timestamp']
        self.systemns = data['systemns']
        self.centerFreq = data['centerFreq']
        self.controlFreq = data['controlFreq']
        self.CBW = data['CBW']
        self.packetFormat = data['packetFormat']
        self.packetCBW = data['packetCBW']
        self.GI = data['GI']
        self.MCS = data['MCS']
        self.numSTS = data['numSTS']
        self.numESS = data['numESS']
        self.numRx = data['numRx']
        self.noiseFloor = data['noiseFloor']
        self.rssi = data['rssi']
        self.rssi1 = data['rssi1']
        self.rssi2 = data['rssi2']
        self.rssi3 = data['rssi3']
    def __str__(self):
            return str(self.__dict__)

class RxExtraInfo:
    def __init__(self, data):
        self.hasLength = data['hasLength']
        self.hasVersion = data['hasVersion']
        self.hasMacAddr_cur = data['hasMacAddr_cur']
        self.hasMacAddr_rom = data['hasMacAddr_rom']
        self.hasChansel = data['hasChansel']
        self.hasBMode = data['hasBMode']
        self.hasEVM = data['hasEVM']
        self.hasTxChainMask = data['hasTxChainMask']
        self.hasRxChainMask = data['hasRxChainMask']
        self.hasTxpower = data['hasTxpower']
        self.hasCF = data['hasCF']
        self.hasTxTSF = data['hasTxTSF']
        self.hasLastHwTxTSF = data['hasLastHwTxTSF']
        self.hasChannelFlags = data['hasChannelFlags']
        self.hasTxNess = data['hasTxNess']
        self.hasTuningPolicy = data['hasTuningPolicy']
        self.hasPLLRate = data['hasPLLRate']
        self.hasPLLClkSel = data['hasPLLClkSel']
        self.hasPLLRefDiv = data['hasPLLRefDiv']
        self.hasAGC = data['hasAGC']
        self.hasAntennaSelection = data['hasAntennaSelection']
        self.hasSamplingRate = data['hasSamplingRate']
        self.hasCFO = data['hasCFO']
        self.hasSFO = data['hasSFO']
        self.length = data['length']
        self.version = data['version']
        self.macaddr_cur = data['macaddr_cur']
        self.macaddr_rom = data['macaddr_rom']
        self.tx_chainmask = data['tx_chainmask']
        self.rx_chainmask = data['rx_chainmask']
    def __str__(self):
            return str(self.__dict__)

class CSI:
    def __init__(self, data):
        self.DeviceType = data['DeviceType']
        self.PacketFormat = data['PacketFormat']
        self.FirmwareVersion = data['FirmwareVersion']
        self.CBW = data['CBW']
        self.CarrierFreq = data['CarrierFreq']
        self.SamplingRate = data['SamplingRate']
        self.SubcarrierBandwidth = data['SubcarrierBandwidth']
        self.numTones = data['numTones']
        self.numTx = data['numTx']
        self.numRx = data['numRx']
        self.numESS = data['numESS']
        self.numCSI = data['numCSI']
        self.ant_sel = data['ant_sel']
        self.CSI = data['CSI']
        self.Mag = data['Mag']
        self.Phase = data['Phase']
        self.SubcarrierIndex = data['SubcarrierIndex']
    def __str__(self):
            return str(self.__dict__)
class MVMExtra:
    def __init__(self, data):
        self.value56 = data['value56']
        self.rateNflag = data['rateNflag']
        self.value96 = data['value96']
    def __str__(self):
            return str(self.__dict__)

# 使用示例
if __name__=="__main__":
    packet_data = PacketData(your_dict)
