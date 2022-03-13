# This is a sample Python script.
import logging

import pyshark
import netifaces
import pandas as pd
import matplotlib.pyplot as plt

logging.basicConfig(format='%(asctime)s [%(levelname)s] - %(message)s', level=logging.INFO)
number_of_packets = 0


def live_capturing():
    """
    Funkce sbira data z interfacu(nastaveno je maximalne 1000 packetu(packet_count))
    Mozna to bude chtit jine cislo interfacu, mne funguje 1 parametr
    Tech moc IFu tam je, protoze Ctrl + C a Ctrl + V, struktura packetu a jak v tom vyhledavat je meh

    :return: [string, int] Protokol a sifrovani, cislo
    """
    global number_of_packets
    tls_encrypted = 0
    tls_readable = 0
    udp_encrypted = 0
    udp_readable = 0

    logging.info('Starting Live Capture')
    interfaces = netifaces.interfaces()
    logging.info(f'Getting data from interface {interfaces[1]}')
    capture = pyshark.LiveCapture(interface=str(interfaces[1]))
    # capture = pyshark.LiveCapture(interface=str(interfaces[1]), display_filter='ssl')
    file = open('packet.save', 'w')
    packet_data = []

    for packet in capture.sniff_continuously(packet_count=1000):
        file.write(str(packet) + '\n\n\n\n\n\n\n\n\n\n')
        if "IP" in packet:
            # something = capture[0]
            # print(f'Ja fakt netusim {something}')
            if "UDP" in packet:
                # TBD: Detection of encrypted packets
                # print(f'UDP: {packet.udp.payload}')
                udp_readable += 1
            elif "TCP" in packet:
                # TBD: Get better definition of TLS version and so
                print(dir(packet.transport_layer))
                # print(dir(packet.tls.record_version))
                # print(f'TCP: {packet.tls.record_version}')
                if 'tls' in dir(packet):
                    if 'record_version' in dir(packet.tls):
                        if packet.tls.record_version == '0x00000303':
                            tls_encrypted += 1
                    else:
                        tls_readable += 1
                else:
                    tls_readable += 1
            elif "IPV6" in packet:
                if "UDP" in packet:
                    # TBD: yes
                    print("IPV6 UDP")
                elif "TCP" in packet:
                    # TBD: yes
                    print("IPV6 TCP")

    packet_data.append(["TCP Encrypted", tls_encrypted])
    packet_data.append(["TCP", tls_readable])
    packet_data.append(["UDP Encrypted", udp_encrypted])
    packet_data.append(["UDP", udp_readable])

    logging.info(f'Total number of packets packets: {number_of_packets}')
    logging.info(f"TCP Encrypted, {tls_encrypted}")
    logging.info(f"TCP , {tls_readable}")
    logging.info(f"UDP Encrypted, {udp_encrypted}")
    logging.info(f"UDP , {udp_readable}")

    number_of_packets = len(capture)
    return packet_data


def main():
    logging.info('Le start')

    # Spusteni sbirani soukromych dat
    # Kliknutim na 'Run' souhlasite se vsim
    network_traffic_capture = live_capturing()

    # Vlozeni data do pandy (Ne kocky)
    data = pd.DataFrame(network_traffic_capture, columns=['Protocol', 'Number'])

    # Overovaci printy
    print(data)
    print(data.info())

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
