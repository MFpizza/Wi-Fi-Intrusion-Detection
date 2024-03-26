from enum import Enum


class PacketFormatEnum(Enum):
    PacketFormat_NonHT = 0
    PacketFormat_HT = 1
    PacketFormat_VHT = 2
    PacketFormat_HESU = 3
    PacketFormat_HEMU = 4
    PacketFormat_Unknown = 5


if __name__ == "__main__":
    print(PacketFormatEnum.PacketFormat_NonHT)
    print(PacketFormatEnum.PacketFormat_HT)
    print(PacketFormatEnum.PacketFormat_VHT)
    print(PacketFormatEnum.PacketFormat_HESU)
    print(PacketFormatEnum.PacketFormat_HEMU)
    print(PacketFormatEnum.PacketFormat_Unknown)
