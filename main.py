# This is a sample Python script.
import logging

import pyshark
import netifaces
import pandas as pd
import matplotlib.pyplot as plt

logging.basicConfig(format='%(asctime)s [%(levelname)s] - %(message)s', level=logging.INFO)

# Set of global variables
number_of_packets = 0
tcp_encrypted = 0
tcp_readable = 0
udp_encrypted = 0
udp_readable = 0
encrypted_traffic = 0
running = True
source_ip = {}
destination_ip = {}


def packet_decider(packet):
    """
    Funkce pro rozhodnuti zda je packet sifrovany nebo ne

    :param packet:
    """
    global number_of_packets
    global udp_readable
    global udp_encrypted
    global tcp_readable
    global tcp_encrypted
    global encrypted_traffic
    global source_ip
    global destination_ip

    if "IP" in packet:
        source_ip[packet.ip.src] = source_ip.get(packet.ip.src, 0) + 1
        destination_ip[packet.ip.dst] = destination_ip.get(packet.ip.dst, 0) + 1
        if "UDP" in packet:
            if "QUIC" in packet:
                udp_encrypted += 1
                encrypted_traffic += int(packet.udp.length)
            elif str(packet).count("Layer") > 3:
                udp_readable += 1
            else:
                udp_encrypted += 1
                encrypted_traffic += int(packet.udp.length)
        elif "TCP" in packet:
            if 'tls' in dir(packet):
                if 'record_version' in dir(packet.tls):
                    if packet.tls.record_version == '0x00000303' or packet.tls.record_version == '0x00000302' \
                            or packet.tls.record_version == '0x00000301':
                        tcp_encrypted += 1
                        encrypted_traffic += int(packet.tcp.window_size)
                else:
                    tcp_readable += 1
            else:
                tcp_readable += 1
    number_of_packets += 1


def get_number_of_packets():
    return number_of_packets


def live_capturing(pocet_paketu):
    """
    Funkce sbira data z interface(nastaveno je maximalne 1000 packetu(packet_count))
    Mozna to bude chtit jine cislo interface, mne funguje 1. parametr
    """
    reset_statistics()
    logging.info('Starting Live Capture')
    interfaces = netifaces.interfaces()
    logging.info(f'Getting data from interface {interfaces[1]}')
    capture = pyshark.LiveCapture(interface=str(interfaces[1]))
    file = open('packet.save', 'w')

    if pocet_paketu == 0:
        for packet in capture.sniff_continuously():
            file.write(str(packet) + '\n')
            packet_decider(packet)
            if not running:
                logging.info("Stopping it")
                break
    else:
        for packet in capture.sniff_continuously(pocet_paketu):
            file.write(str(packet) + '\n')
            packet_decider(packet)
            if not running:
                logging.info("Stopping it")
                break


def create_graph():
    network_traffic_capture = [["TCP Encrypted", tcp_encrypted], ["TCP", tcp_readable],
                               ["UDP Encrypted", udp_encrypted], ["UDP", udp_readable]]
    # Vlozeni data do pandy (Ne kocky)

    data = pd.DataFrame(network_traffic_capture, columns=['Protocol', 'Packets'])

    # Naprosto uzasny graf, @FrontendPerson to pak se u tebe zmeni, jen docasne at vidim
    x = list(data.iloc[:, 0])
    y = list(data.iloc[:, 1])
    plt.bar(x, y)
    plt.title("Stats of packets")
    plt.xlabel("Protocol")
    plt.ylabel("Number of packets")
    plt.show()
    logging.info('Schluss fur Heute')


def get_encrypted_traffic_percentage():
    return round(100 * (udp_encrypted + tcp_encrypted) / number_of_packets, 2)


def get_encrypted_traffic():
    return encrypted_traffic


def get_total_packets():
    return number_of_packets


def set_running(status):
    global running
    running = status


def print_stats_into_logs():
    logging.info(f'Total number of packets packets: {number_of_packets}')
    logging.info(f"TCP encrypted: {tcp_encrypted}")
    logging.info(f"TCP readable: {tcp_readable}")
    logging.info(f"UDP encrypted: {udp_encrypted}")
    logging.info(f"UDP readable: {udp_readable}")
    logging.info(f"Source IPs: {source_ip}")
    logging.info(f"Destination IPs: {destination_ip}")


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
    global encrypted_traffic
    global source_ip
    global destination_ip
    number_of_packets = 0
    tcp_encrypted = 0
    tcp_readable = 0
    udp_encrypted = 0
    udp_readable = 0
    encrypted_traffic = 0
    source_ip = {}
    destination_ip = {}


def main():
    logging.info('Starting script to show traffic')
    # Spusteni sbirani soukromych dat
    # Kliknutim na 'Run' souhlasite se vsim
    live_capturing()
    create_graph()


if __name__ == '__main__':
    main()
