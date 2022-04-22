# This is a sample Python script.
import logging

import pyshark
import netifaces
import pandas as pd
import matplotlib.pyplot as plt

logging.basicConfig(format='%(asctime)s [%(levelname)s] - %(message)s', level=logging.INFO)
number_of_packets = 0
tcp_encrypted = 0
tcp_readable = 0
udp_encrypted = 0
udp_readable = 0


def packet_decider(packet):
    global number_of_packets
    global udp_readable
    global udp_encrypted
    global tcp_readable
    global tcp_encrypted

    if "IP" in packet:
        if "UDP" in packet:
            if str(packet).count("Layer") > 3:
                udp_readable += 1
            else:
                udp_encrypted += 1
        elif "TCP" in packet:
            if 'tls' in dir(packet):
                if 'record_version' in dir(packet.tls):
                    if packet.tls.record_version == '0x00000303' or packet.tls.record_version == '0x00000302' \
                            or packet.tls.record_version == '0x00000301':
                        tcp_encrypted += 1
                        print("Size: " + str(packet.tcp.window_size))
                else:
                    tcp_readable += 1
            else:
                tcp_readable += 1
        elif "IPV6" in packet:
            if "UDP" in packet:
                # TBD: yes
                print("IPV6 UDP")
            elif "TCP" in packet:
                # TBD: yes
                print("IPV6 TCP")


def live_capturing():
    """
    Funkce sbira data z interface(nastaveno je maximalne 1000 packetu(packet_count))
    Mozna to bude chtit jine cislo interface, mne funguje 1. parametr

    :return: [string, int] Protokol a sifrovani, cislo
    """
    global number_of_packets
    reset_statistics()
    logging.info('Starting Live Capture')
    interfaces = netifaces.interfaces()
    logging.info(f'Getting data from interface {interfaces[1]}')
    capture = pyshark.LiveCapture(interface=str(interfaces[1]))
    file = open('packet.save', 'w')
    packet_data = []

    for packet in capture.sniff_continuously(packet_count=1000):
        file.write(str(packet) + '\n\n\n\n\n\n\n\n\n\n')
        packet_decider(packet)

    packet_data.append(["TCP Encrypted", tcp_encrypted])
    packet_data.append(["TCP", tcp_readable])
    packet_data.append(["UDP Encrypted", udp_encrypted])
    packet_data.append(["UDP", udp_readable])

    logging.info(f'Total number of packets packets: {number_of_packets}')
    logging.info(f"TCP Encrypted: {tcp_encrypted}")
    logging.info(f"TCP: {tcp_readable}")
    logging.info(f"UDP Encrypted: {udp_encrypted}")
    logging.info(f"UDP: {udp_readable}")

    number_of_packets = len(capture)
    return packet_data


def reset_statistics():
    """
    Bad practice to reset global counters
    :return:
    """
    global number_of_packets
    global udp_readable
    global udp_encrypted
    global tcp_readable
    global tcp_encrypted
    number_of_packets = 0
    tcp_encrypted = 0
    tcp_readable = 0
    udp_encrypted = 0
    udp_readable = 0

def main():
    logging.info('Starting script to show traffic')

    # Spusteni sbirani soukromych dat
    # Kliknutim na 'Run' souhlasite se vsim
    network_traffic_capture = live_capturing()

    # Vlozeni data do pandy (Ne kocky)
    data = pd.DataFrame(network_traffic_capture, columns=['Protocol', 'Number'])

    # Overovaci printy
    print(data)
    # print(data.info())

    # Naprosto uzasny graf, @FrontendPerson to pak se u tebe zmeni, jen docasne at vidim
    x = list(data.iloc[:, 0])
    y = list(data.iloc[:, 1])
    plt.bar(x, y)
    plt.title("Stats of packets")
    plt.xlabel("Protocol")
    plt.ylabel("Number of packets")
    plt.show()
    logging.info('Schluss fur Heute')


if __name__ == '__main__':
    main()
