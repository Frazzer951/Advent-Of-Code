from dataclasses import dataclass
from dataclasses import field
from typing import Any
from typing import List

from adventofcode.util.helpers import solution_timer
from adventofcode.util.input_helpers import get_input_for_day

hex_dict = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111",
}


@dataclass
class Packet:
    version: int
    type_id: int
    data: str
    value: int = -1
    subPackets: List[Any] = field(default_factory=list)

    def get_version_sum(self):
        version_sum = self.version
        for packet in self.subPackets:
            version_sum += packet.get_version_sum()
        return version_sum


def hex_to_bin(hex_str: str) -> str:
    return "".join([hex_dict[x] for x in hex_str])


def parse_bin(bin_str: str):
    version = bin_str[:3]
    version = int(version, 2)
    type_id = bin_str[3:6]
    type_id = int(type_id, 2)
    bin_str = bin_str[6:]
    if type_id == 4:
        value = ""
        while True:
            chunk = bin_str[:5]
            if chunk[0] == "0":
                value += chunk[1:]
                bin_str = bin_str[5:]
                break
            else:
                value += chunk[1:]
                bin_str = bin_str[5:]
        value = int(value, 2)
        return Packet(version, type_id, bin_str, value=value)
    else:
        length_id = bool(int(bin_str[0]))
        if length_id:
            num_packets = bin_str[1:12]
            num_packets = int(num_packets, 2)
            bin_str = bin_str[12:]
            sub_packets = []
            for _ in range(num_packets):
                sub_packet = parse_bin(bin_str)
                sub_packets.append(sub_packet)
                bin_str = sub_packet.data
        else:
            bit_length = bin_str[1:16]
            bit_length = int(bit_length, 2)
            bin_str = bin_str[16:]
            sub_packets = []
            sub_bin_str = bin_str[:bit_length]
            bin_str = bin_str[bit_length:]
            while len(sub_bin_str) > 0:
                sub_packet = parse_bin(sub_bin_str)
                sub_packets.append(sub_packet)
                sub_bin_str = sub_packet.data

        value = 0
        if type_id == 0:
            # sum
            for packet in sub_packets:
                value += packet.value
        if type_id == 1:
            # product
            value = 1
            for packet in sub_packets:
                value *= packet.value
        if type_id == 2:
            # minimum
            value = sub_packets[0].value
            for packet in sub_packets:
                value = min(value, packet.value)
        if type_id == 3:
            # maximum
            value = sub_packets[0].value
            for packet in sub_packets:
                value = max(value, packet.value)
        if type_id == 5:
            # greater_than
            value = 1 if sub_packets[0].value > sub_packets[1].value else 0
        if type_id == 6:
            # less_than
            value = 1 if sub_packets[0].value < sub_packets[1].value else 0
        if type_id == 7:
            # equal
            value = 1 if sub_packets[0].value == sub_packets[1].value else 0

        return Packet(version, type_id, bin_str, value=value, subPackets=sub_packets)


@solution_timer(2021, 16, 1)
def part_one(input_data: List[str]):
    bin_str = hex_to_bin(input_data[0])
    p = parse_bin(bin_str)
    return p.get_version_sum()


@solution_timer(2021, 16, 2)
def part_two(input_data: List[str]):
    bin_str = hex_to_bin(input_data[0])
    p = parse_bin(bin_str)
    return p.value


if __name__ == "__main__":
    data = get_input_for_day(2021, 16)
    part_one(data)
    part_two(data)
