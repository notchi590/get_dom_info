#! /usr/bin/python3

from oom import *
from oom.oomlib import *
import json
import os

Temperature = 0
Vcc = 1
Tx1_bias = 2
Tx1_power = 3
Rx1_power = 4
Tx2_bias = 5
Tx2_power = 6
Rx2_power = 7
Tx3_bias = 8
Tx3_power = 9
Rx3_power = 10
Tx4_bias = 11
Tx4_power = 12
Rx4_power = 13
Tx5_bias = 14
Tx5_power = 15
Rx5_power = 16
Tx6_bias = 17
Tx6_power = 18
Rx6_power = 19
Tx7_bias = 20
Tx7_power = 21
Rx7_power = 22
Tx8_bias = 23
Tx8_power = 24
Rx8_power = 25
Temp_high_alarm = 26
Temp_low_alarm = 27
Temp_high_warn = 28
Temp_low_warn = 29
Vcc_high_alarm = 30
Vcc_low_alarm = 31
Vcc_high_warn = 32
Vcc_low_warn = 33
Tx_bias_high_alarm = 34
Tx_bias_low_alarm = 35
Tx_bias_high_warn = 36
Tx_bias_low_warn = 37
Tx_power_high_alarm = 38
Tx_power_low_alarm = 39
Tx_power_high_warn = 40
Tx_power_low_warn = 41
Rx_power_high_alarm = 42
Rx_power_low_alarm = 43
Rx_power_high_warn = 44
Rx_power_low_warn = 45

dom_info = {"dom_info": []}

def remove_dom_info_json():
    exists = os.path.isfile("/run/dom_info.json")
    if exists:
        os.remove("/run/dom_info.json")

def write_dom_info_json():
    with open("/run/dom_info.json", 'w') as fp:
        json.dump(dom_info, fp, indent=4, sort_keys=True)

def get_dom_info_list(portList):
    for port in oom_get_portlist():
        modtype = type_to_str(get_port_type(port))
        port_name = port.port_name
        port_num = 0
        if port_name.find('port') != -1:
            port_num = int(port_name.strip('port'))
        elif port_name.find('QSFP') != -1:
            port_num = int(port_name.strip('QSFP'))
        elif port_name.find('SFP') != -1:
            port_num = int(port_name.strip('SFP'))
        else:
            port_num = int(port_name)

        if port_num not in portList:
            continue
        print(port_num)
        print(modtype)
        if modtype == 'SFP' or modtype == 'DWDM_SFP':
            temp = round(oom_get_keyvalue(port, 'TEMPERATURE'), 3)
            vcc = round(oom_get_keyvalue(port, 'VCC'), 3)
            tx_bias = round(oom_get_keyvalue(port, 'TX_BIAS'), 3)
            tx_power = round(oom_get_keyvalue(port, 'TX_POWER_DBM'), 3)
            rx_power = round(oom_get_keyvalue(port, 'RX_POWER_DBM'), 3)
            temp_high_alarm = round(oom_get_keyvalue(port, 'TEMP_HIGH_ALARM'), 3)
            temp_low_alarm = round(oom_get_keyvalue(port, 'TEMP_LOW_ALARM'), 3)
            temp_high_warn = round(oom_get_keyvalue(port, 'TEMP_HIGH_WARN'), 3)
            temp_low_warn = round(oom_get_keyvalue(port, 'TEMP_LOW_WARN'), 3)
            vcc_high_alarm = round(oom_get_keyvalue(port, 'VOLTAGE_HIGH_ALARM'), 3)
            vcc_low_alarm = round(oom_get_keyvalue(port, 'VOLTAGE_LOW_ALARM'), 3)
            vcc_high_warn = round(oom_get_keyvalue(port, 'VOLTAGE_HIGH_WARN'), 3)
            vcc_low_warn = round(oom_get_keyvalue(port, 'VOLTAGE_LOW_WARN'), 3)
            tx_bias_high_alarm = round(oom_get_keyvalue(port, 'BIAS_HIGH_ALARM'), 3)
            tx_bias_low_alarm = round(oom_get_keyvalue(port, 'BIAS_LOW_ALARM'), 3)
            tx_bias_high_warn = round(oom_get_keyvalue(port, 'BIAS_HIGH_WARN'), 3)
            tx_bias_low_warn = round(oom_get_keyvalue(port, 'BIAS_LOW_WARN'), 3)
            tx_power_high_alarm = round(oom_get_keyvalue(port, 'TX_POWER_HIGH_ALARM'), 3)
            tx_power_low_alarm = round(oom_get_keyvalue(port, 'TX_POWER_LOW_ALARM'), 3)
            tx_power_high_warn = round(oom_get_keyvalue(port, 'TX_POWER_HIGH_WARN'), 3)
            tx_power_low_warn = round(oom_get_keyvalue(port, 'TX_POWER_LOW_WARN'), 3)
            rx_power_high_alarm = round(oom_get_keyvalue(port, 'RX_POWER_HIGH_ALARM'), 3)
            rx_power_low_alarm = round(oom_get_keyvalue(port, 'RX_POWER_LOW_ALARM'), 3)
            rx_power_high_warn = round(oom_get_keyvalue(port, 'RX_POWER_HIGH_WARN'), 3)
            rx_power_low_warn = round(oom_get_keyvalue(port, 'RX_POWER_LOW_WARN'), 3)
            port_dom_info = []
            dom_key_val = {}
            dom_key_val["val"]= temp
            dom_key_val["keyId"] = Temperature
            port_dom_info.append(dom_key_val)
            dom_key_val = {}
            dom_key_val["val"]= vcc
            dom_key_val["keyId"] = Vcc
            port_dom_info.append(dom_key_val)

            dom_key_val = {}
            dom_key_val["val"]= tx_bias
            dom_key_val["keyId"] = Tx1_bias
            port_dom_info.append(dom_key_val)

            dom_key_val = {}
            dom_key_val["val"]= tx_power
            dom_key_val["keyId"] = Tx1_power
            port_dom_info.append(dom_key_val)

            dom_key_val = {}
            dom_key_val["val"]= rx_power
            dom_key_val["keyId"] = Rx1_power
            port_dom_info.append(dom_key_val)

            dom_key_val = {}
            dom_key_val["val"]= temp_high_alarm
            dom_key_val["keyId"] = Temp_high_alarm
            port_dom_info.append(dom_key_val)
            dom_key_val = {}
            dom_key_val["val"]= temp_low_alarm
            dom_key_val["keyId"] = Temp_low_alarm
            port_dom_info.append(dom_key_val)
            dom_key_val = {}
            dom_key_val["val"]= temp_high_warn
            dom_key_val["keyId"] = Temp_high_warn
            port_dom_info.append(dom_key_val)
            dom_key_val = {}
            dom_key_val["val"]= temp_low_warn
            dom_key_val["keyId"] = Temp_low_warn
            port_dom_info.append(dom_key_val)

            dom_key_val = {}
            dom_key_val["val"]= vcc_high_alarm
            dom_key_val["keyId"] = Vcc_high_alarm
            port_dom_info.append(dom_key_val)
            dom_key_val = {}
            dom_key_val["val"]= vcc_low_alarm
            dom_key_val["keyId"] = Vcc_low_alarm
            port_dom_info.append(dom_key_val)
            dom_key_val = {}
            dom_key_val["val"]= vcc_high_warn
            dom_key_val["keyId"] = Vcc_high_warn
            port_dom_info.append(dom_key_val)
            dom_key_val = {}
            dom_key_val["val"]= vcc_low_warn
            dom_key_val["keyId"] = Vcc_low_warn
            port_dom_info.append(dom_key_val)

            dom_key_val = {}
            dom_key_val["val"]= tx_bias_high_alarm
            dom_key_val["keyId"] = Tx_bias_high_alarm
            port_dom_info.append(dom_key_val)
            dom_key_val = {}
            dom_key_val["val"]= tx_bias_low_alarm
            dom_key_val["keyId"] = Tx_bias_low_alarm
            port_dom_info.append(dom_key_val)
            dom_key_val = {}
            dom_key_val["val"]= tx_bias_high_warn
            dom_key_val["keyId"] = Tx_bias_high_warn
            port_dom_info.append(dom_key_val)
            dom_key_val = {}
            dom_key_val["val"]= tx_bias_low_warn
            dom_key_val["keyId"] = Tx_bias_low_warn
            port_dom_info.append(dom_key_val)

            dom_key_val = {}
            dom_key_val["val"]= tx_power_high_alarm
            dom_key_val["keyId"] = Tx_power_high_alarm
            port_dom_info.append(dom_key_val)
            dom_key_val = {}
            dom_key_val["val"]= tx_power_low_alarm
            dom_key_val["keyId"] = Tx_power_low_alarm
            port_dom_info.append(dom_key_val)
            dom_key_val = {}
            dom_key_val["val"]= tx_power_high_warn
            dom_key_val["keyId"] = Tx_power_high_warn
            port_dom_info.append(dom_key_val)
            dom_key_val = {}
            dom_key_val["val"]= tx_power_low_warn
            dom_key_val["keyId"] = Tx_power_low_warn
            port_dom_info.append(dom_key_val)

            dom_key_val = {}
            dom_key_val["val"]= rx_power_high_alarm
            dom_key_val["keyId"] = Rx_power_high_alarm
            port_dom_info.append(dom_key_val)
            dom_key_val = {}
            dom_key_val["val"]= rx_power_low_alarm
            dom_key_val["keyId"] = Rx_power_low_alarm
            port_dom_info.append(dom_key_val)
            dom_key_val = {}
            dom_key_val["val"]= rx_power_high_warn
            dom_key_val["keyId"] = Rx_power_high_warn
            port_dom_info.append(dom_key_val)
            dom_key_val = {}
            dom_key_val["val"]= rx_power_low_warn
            dom_key_val["keyId"] = Rx_power_low_warn
            port_dom_info.append(dom_key_val)

            dom_info_port = {}
            dom_info_port["port"] = port_num
            dom_info_port["port_dom_info"] = port_dom_info
            dom_info["dom_info"].append(dom_info_port)

        elif modtype == 'QSFP_PLUS' or modtype == 'QSFP28':
            temp = round(oom_get_keyvalue(port, 'TEMPERATURE'), 3)
            vcc = round(oom_get_keyvalue(port, 'SUPPLY_VOLTAGE'), 3)
            tx1_bias = round(oom_get_keyvalue(port, 'TX1_BIAS'), 3)
            tx2_bias = round(oom_get_keyvalue(port, 'TX2_BIAS'), 3)
            tx3_bias = round(oom_get_keyvalue(port, 'TX3_BIAS'), 3)
            tx4_bias = round(oom_get_keyvalue(port, 'TX4_BIAS'), 3)
            tx1_power = round(oom_get_keyvalue(port, 'TX1_POWER_DBM'), 3)
            tx2_power = round(oom_get_keyvalue(port, 'TX2_POWER_DBM'), 3)
            tx3_power = round(oom_get_keyvalue(port, 'TX3_POWER_DBM'), 3)
            tx4_power = round(oom_get_keyvalue(port, 'TX4_POWER_DBM'), 3)
            rx1_power = round(oom_get_keyvalue(port, 'RX1_POWER_DBM'), 3)
            rx2_power = round(oom_get_keyvalue(port, 'RX2_POWER_DBM'), 3)
            rx3_power = round(oom_get_keyvalue(port, 'RX3_POWER_DBM'), 3)
            rx4_power = round(oom_get_keyvalue(port, 'RX4_POWER_DBM'), 3)
            temp_high_alarm = round(oom_get_keyvalue(port, 'TEMP_HIGH_ALARM'), 3)
            temp_low_alarm = round(oom_get_keyvalue(port, 'TEMP_LOW_ALARM'), 3)
            temp_high_warn = round(oom_get_keyvalue(port, 'TEMP_HIGH_WARN'), 3)
            temp_low_warn = round(oom_get_keyvalue(port, 'TEMP_LOW_WARN'), 3)
            vcc_high_alarm = round(oom_get_keyvalue(port, 'VOLTAGE_HIGH_ALARM'), 3)
            vcc_low_alarm = round(oom_get_keyvalue(port, 'VOLTAGE_LOW_ALARM'), 3)
            vcc_high_warn = round(oom_get_keyvalue(port, 'VOLTAGE_HIGH_WARN'), 3)
            vcc_low_warn = round(oom_get_keyvalue(port, 'VOLTAGE_LOW_WARN'), 3)
            tx_bias_high_alarm = round(oom_get_keyvalue(port, 'BIAS_HIGH_ALARM'), 3)
            tx_bias_low_alarm = round(oom_get_keyvalue(port, 'BIAS_LOW_ALARM'), 3)
            tx_bias_high_warn = round(oom_get_keyvalue(port, 'BIAS_HIGH_WARN'), 3)
            tx_bias_low_warn = round(oom_get_keyvalue(port, 'BIAS_LOW_WARN'), 3)
            tx_power_high_alarm = round(oom_get_keyvalue(port, 'TX_POWER_HIGH_ALARM'), 3)
            tx_power_low_alarm = round(oom_get_keyvalue(port, 'TX_POWER_LOW_ALARM'), 3)
            tx_power_high_warn = round(oom_get_keyvalue(port, 'TX_POWER_HIGH_WARN'), 3)
            tx_power_low_warn = round(oom_get_keyvalue(port, 'TX_POWER_LOW_WARN'), 3)
            rx_power_high_alarm = round(oom_get_keyvalue(port, 'RX_POWER_HIGH_ALARM'), 3)
            rx_power_low_alarm = round(oom_get_keyvalue(port, 'RX_POWER_LOW_ALARM'), 3)
            rx_power_high_warn = round(oom_get_keyvalue(port, 'RX_POWER_HIGH_WARN'), 3)
            rx_power_low_warn = round(oom_get_keyvalue(port, 'RX_POWER_LOW_WARN'), 3)
            port_dom_info = []
            dom_key_val = {}
            dom_key_val["val"]= temp
            dom_key_val["keyId"] = Temperature
            port_dom_info.append(dom_key_val)
            dom_key_val = {}
            dom_key_val["val"]= vcc
            dom_key_val["keyId"] = Vcc
            port_dom_info.append(dom_key_val)

            dom_key_val = {}
            dom_key_val["val"]= tx1_bias
            dom_key_val["keyId"] = Tx1_bias
            port_dom_info.append(dom_key_val)
            dom_key_val = {}
            dom_key_val["val"]= tx2_bias
            dom_key_val["keyId"] = Tx2_bias
            port_dom_info.append(dom_key_val)
            dom_key_val = {}
            dom_key_val["val"]= tx3_bias
            dom_key_val["keyId"] = Tx3_bias
            port_dom_info.append(dom_key_val)
            dom_key_val = {}
            dom_key_val["val"]= tx4_bias
            dom_key_val["keyId"] = Tx4_bias
            port_dom_info.append(dom_key_val)

            dom_key_val = {}
            dom_key_val["val"]= tx1_power
            dom_key_val["keyId"] = Tx1_power
            port_dom_info.append(dom_key_val)
            dom_key_val = {}
            dom_key_val["val"]= tx2_power
            dom_key_val["keyId"] = Tx2_power
            port_dom_info.append(dom_key_val)
            dom_key_val = {}
            dom_key_val["val"]= tx3_power
            dom_key_val["keyId"] = Tx3_power
            port_dom_info.append(dom_key_val)
            dom_key_val = {}
            dom_key_val["val"]= tx4_power
            dom_key_val["keyId"] = Tx4_power
            port_dom_info.append(dom_key_val)

            dom_key_val = {}
            dom_key_val["val"]= rx1_power
            dom_key_val["keyId"] = Rx1_power
            port_dom_info.append(dom_key_val)
            dom_key_val = {}
            dom_key_val["val"]= rx2_power
            dom_key_val["keyId"] = Rx2_power
            port_dom_info.append(dom_key_val)
            dom_key_val = {}
            dom_key_val["val"]= rx3_power
            dom_key_val["keyId"] = Rx3_power
            port_dom_info.append(dom_key_val)
            dom_key_val = {}
            dom_key_val["val"]= rx4_power
            dom_key_val["keyId"] = Rx4_power
            port_dom_info.append(dom_key_val)

            dom_key_val = {}
            dom_key_val["val"]= temp_high_alarm
            dom_key_val["keyId"] = Temp_high_alarm
            port_dom_info.append(dom_key_val)
            dom_key_val = {}
            dom_key_val["val"]= temp_low_alarm
            dom_key_val["keyId"] = Temp_low_alarm
            port_dom_info.append(dom_key_val)
            dom_key_val = {}
            dom_key_val["val"]= temp_high_warn
            dom_key_val["keyId"] = Temp_high_warn
            port_dom_info.append(dom_key_val)
            dom_key_val = {}
            dom_key_val["val"]= temp_low_warn
            dom_key_val["keyId"] = Temp_low_warn
            port_dom_info.append(dom_key_val)

            dom_key_val = {}
            dom_key_val["val"]= vcc_high_alarm
            dom_key_val["keyId"] = Vcc_high_alarm
            port_dom_info.append(dom_key_val)
            dom_key_val = {}
            dom_key_val["val"]= vcc_low_alarm
            dom_key_val["keyId"] = Vcc_low_alarm
            port_dom_info.append(dom_key_val)
            dom_key_val = {}
            dom_key_val["val"]= vcc_high_warn
            dom_key_val["keyId"] = Vcc_high_warn
            port_dom_info.append(dom_key_val)
            dom_key_val = {}
            dom_key_val["val"]= vcc_low_warn
            dom_key_val["keyId"] = Vcc_low_warn
            port_dom_info.append(dom_key_val)

            dom_key_val = {}
            dom_key_val["val"]= tx_bias_high_alarm
            dom_key_val["keyId"] = Tx_bias_high_alarm
            port_dom_info.append(dom_key_val)
            dom_key_val = {}
            dom_key_val["val"]= tx_bias_low_alarm
            dom_key_val["keyId"] = Tx_bias_low_alarm
            port_dom_info.append(dom_key_val)
            dom_key_val = {}
            dom_key_val["val"]= tx_bias_high_warn
            dom_key_val["keyId"] = Tx_bias_high_warn
            port_dom_info.append(dom_key_val)
            dom_key_val = {}
            dom_key_val["val"]= tx_bias_low_warn
            dom_key_val["keyId"] = Tx_bias_low_warn
            port_dom_info.append(dom_key_val)

            dom_key_val = {}
            dom_key_val["val"]= tx_power_high_alarm
            dom_key_val["keyId"] = Tx_power_high_alarm
            port_dom_info.append(dom_key_val)
            dom_key_val = {}
            dom_key_val["val"]= tx_power_low_alarm
            dom_key_val["keyId"] = Tx_power_low_alarm
            port_dom_info.append(dom_key_val)
            dom_key_val = {}
            dom_key_val["val"]= tx_power_high_warn
            dom_key_val["keyId"] = Tx_power_high_warn
            port_dom_info.append(dom_key_val)
            dom_key_val = {}
            dom_key_val["val"]= tx_power_low_warn
            dom_key_val["keyId"] = Tx_power_low_warn
            port_dom_info.append(dom_key_val)

            dom_key_val = {}
            dom_key_val["val"]= rx_power_high_alarm
            dom_key_val["keyId"] = Rx_power_high_alarm
            port_dom_info.append(dom_key_val)
            dom_key_val = {}
            dom_key_val["val"]= rx_power_low_alarm
            dom_key_val["keyId"] = Rx_power_low_alarm
            port_dom_info.append(dom_key_val)
            dom_key_val = {}
            dom_key_val["val"]= rx_power_high_warn
            dom_key_val["keyId"] = Rx_power_high_warn
            port_dom_info.append(dom_key_val)
            dom_key_val = {}
            dom_key_val["val"]= rx_power_low_warn
            dom_key_val["keyId"] = Rx_power_low_warn
            port_dom_info.append(dom_key_val)

            dom_info_port = {}
            dom_info_port["port"] = port_num
            dom_info_port["port_dom_info"] = port_dom_info
            dom_info["dom_info"].append(dom_info_port)


        elif modtype == 'QSFP_DD' or modtype == 'OSFP' or modtype == 'QSFPwCMIS':
            temp = round(oom_get_keyvalue(port, 'TEMPERATURE'), 3)
            vcc = round(oom_get_keyvalue(port, 'SUPPLY_VOLTAGE'), 3)
            tx1_bias = round(oom_get_keyvalue(port, 'TX1_BIAS'), 3)
            tx2_bias = round(oom_get_keyvalue(port, 'TX2_BIAS'), 3)
            tx3_bias = round(oom_get_keyvalue(port, 'TX3_BIAS'), 3)
            tx4_bias = round(oom_get_keyvalue(port, 'TX4_BIAS'), 3)
            tx5_bias = round(oom_get_keyvalue(port, 'TX5_BIAS'), 3)
            tx6_bias = round(oom_get_keyvalue(port, 'TX6_BIAS'), 3)
            tx7_bias = round(oom_get_keyvalue(port, 'TX7_BIAS'), 3)
            tx8_bias = round(oom_get_keyvalue(port, 'TX8_BIAS'), 3)
            tx1_power = round(oom_get_keyvalue(port, 'TX1_POWER_DBM'), 3)
            tx2_power = round(oom_get_keyvalue(port, 'TX2_POWER_DBM'), 3)
            tx3_power = round(oom_get_keyvalue(port, 'TX3_POWER_DBM'), 3)
            tx4_power = round(oom_get_keyvalue(port, 'TX4_POWER_DBM'), 3)
            tx5_power = round(oom_get_keyvalue(port, 'TX5_POWER_DBM'), 3)
            tx6_power = round(oom_get_keyvalue(port, 'TX6_POWER_DBM'), 3)
            tx7_power = round(oom_get_keyvalue(port, 'TX7_POWER_DBM'), 3)
            tx8_power = round(oom_get_keyvalue(port, 'TX8_POWER_DBM'), 3)
            rx1_power = round(oom_get_keyvalue(port, 'RX1_POWER_DBM'), 3)
            rx2_power = round(oom_get_keyvalue(port, 'RX2_POWER_DBM'), 3)
            rx3_power = round(oom_get_keyvalue(port, 'RX3_POWER_DBM'), 3)
            rx4_power = round(oom_get_keyvalue(port, 'RX4_POWER_DBM'), 3)
            rx5_power = round(oom_get_keyvalue(port, 'RX5_POWER_DBM'), 3)
            rx6_power = round(oom_get_keyvalue(port, 'RX6_POWER_DBM'), 3)
            rx7_power = round(oom_get_keyvalue(port, 'RX7_POWER_DBM'), 3)
            rx8_power = round(oom_get_keyvalue(port, 'RX8_POWER_DBM'), 3)
            temp_high_alarm = round(oom_get_keyvalue(port, 'TEMP_HIGH_ALARM'), 3)
            temp_low_alarm = round(oom_get_keyvalue(port, 'TEMP_LOW_ALARM'), 3)
            temp_high_warn = round(oom_get_keyvalue(port, 'TEMP_HIGH_WARN'), 3)
            temp_low_warn = round(oom_get_keyvalue(port, 'TEMP_LOW_WARN'), 3)
            vcc_high_alarm = round(oom_get_keyvalue(port, 'VOLTAGE_HIGH_ALARM'), 3)
            vcc_low_alarm = round(oom_get_keyvalue(port, 'VOLTAGE_LOW_ALARM'), 3)
            vcc_high_warn = round(oom_get_keyvalue(port, 'VOLTAGE_HIGH_WARN'), 3)
            vcc_low_warn = round(oom_get_keyvalue(port, 'VOLTAGE_LOW_WARN'), 3)
            tx_bias_high_alarm = round(oom_get_keyvalue(port, 'BIAS_HIGH_ALARM'), 3)
            tx_bias_low_alarm = round(oom_get_keyvalue(port, 'BIAS_LOW_ALARM'), 3)
            tx_bias_high_warn = round(oom_get_keyvalue(port, 'BIAS_HIGH_WARN'), 3)
            tx_bias_low_warn = round(oom_get_keyvalue(port, 'BIAS_LOW_WARN'), 3)
            tx_power_high_alarm = round(oom_get_keyvalue(port, 'TX_POWER_HIGH_ALARM'), 3)
            tx_power_low_alarm = round(oom_get_keyvalue(port, 'TX_POWER_LOW_ALARM'), 3)
            tx_power_high_warn = round(oom_get_keyvalue(port, 'TX_POWER_HIGH_WARN'), 3)
            tx_power_low_warn = round(oom_get_keyvalue(port, 'TX_POWER_LOW_WARN'), 3)
            rx_power_high_alarm = round(oom_get_keyvalue(port, 'RX_POWER_HIGH_ALARM'), 3)
            rx_power_low_alarm = round(oom_get_keyvalue(port, 'RX_POWER_LOW_ALARM'), 3)
            rx_power_high_warn = round(oom_get_keyvalue(port, 'RX_POWER_HIGH_WARN'), 3)
            rx_power_low_warn = round(oom_get_keyvalue(port, 'RX_POWER_LOW_WARN'), 3)
            port_dom_info = []
            dom_key_val = {}
            dom_key_val["val"]= temp
            dom_key_val["keyId"] = Temperature
            port_dom_info.append(dom_key_val)
            dom_key_val = {}
            dom_key_val["val"]= vcc
            dom_key_val["keyId"] = Vcc
            port_dom_info.append(dom_key_val)

            dom_key_val = {}
            dom_key_val["val"]= tx1_bias
            dom_key_val["keyId"] = Tx1_bias
            port_dom_info.append(dom_key_val)
            dom_key_val = {}
            dom_key_val["val"]= tx2_bias
            dom_key_val["keyId"] = Tx2_bias
            port_dom_info.append(dom_key_val)
            dom_key_val = {}
            dom_key_val["val"]= tx3_bias
            dom_key_val["keyId"] = Tx3_bias
            port_dom_info.append(dom_key_val)
            dom_key_val = {}
            dom_key_val["val"]= tx4_bias
            dom_key_val["keyId"] = Tx4_bias
            port_dom_info.append(dom_key_val)
            dom_key_val = {}
            dom_key_val["val"]= tx5_bias
            dom_key_val["keyId"] = Tx5_bias
            port_dom_info.append(dom_key_val)
            dom_key_val = {}
            dom_key_val["val"]= tx6_bias
            dom_key_val["keyId"] = Tx6_bias
            port_dom_info.append(dom_key_val)
            dom_key_val = {}
            dom_key_val["val"]= tx7_bias
            dom_key_val["keyId"] = Tx7_bias
            port_dom_info.append(dom_key_val)
            dom_key_val = {}
            dom_key_val["val"]= tx8_bias
            dom_key_val["keyId"] = Tx8_bias
            port_dom_info.append(dom_key_val)

            dom_key_val = {}
            dom_key_val["val"]= tx1_power
            dom_key_val["keyId"] = Tx1_power
            port_dom_info.append(dom_key_val)
            dom_key_val = {}
            dom_key_val["val"]= tx2_power
            dom_key_val["keyId"] = Tx2_power
            port_dom_info.append(dom_key_val)
            dom_key_val = {}
            dom_key_val["val"]= tx3_power
            dom_key_val["keyId"] = Tx3_power
            port_dom_info.append(dom_key_val)
            dom_key_val = {}
            dom_key_val["val"]= tx4_power
            dom_key_val["keyId"] = Tx4_power
            port_dom_info.append(dom_key_val)
            dom_key_val = {}
            dom_key_val["val"]= tx5_power
            dom_key_val["keyId"] = Tx5_power
            port_dom_info.append(dom_key_val)
            dom_key_val = {}
            dom_key_val["val"]= tx6_power
            dom_key_val["keyId"] = Tx6_power
            port_dom_info.append(dom_key_val)
            dom_key_val = {}
            dom_key_val["val"]= tx7_power
            dom_key_val["keyId"] = Tx7_power
            port_dom_info.append(dom_key_val)
            dom_key_val = {}
            dom_key_val["val"]= tx8_power
            dom_key_val["keyId"] = Tx8_power
            port_dom_info.append(dom_key_val)

            dom_key_val = {}
            dom_key_val["val"]= rx1_power
            dom_key_val["keyId"] = Rx1_power
            port_dom_info.append(dom_key_val)
            dom_key_val = {}
            dom_key_val["val"]= rx2_power
            dom_key_val["keyId"] = Rx2_power
            port_dom_info.append(dom_key_val)
            dom_key_val = {}
            dom_key_val["val"]= rx3_power
            dom_key_val["keyId"] = Rx3_power
            port_dom_info.append(dom_key_val)
            dom_key_val = {}
            dom_key_val["val"]= rx4_power
            dom_key_val["keyId"] = Rx4_power
            port_dom_info.append(dom_key_val)
            dom_key_val = {}
            dom_key_val["val"]= rx5_power
            dom_key_val["keyId"] = Rx5_power
            port_dom_info.append(dom_key_val)
            dom_key_val = {}
            dom_key_val["val"]= rx6_power
            dom_key_val["keyId"] = Rx6_power
            port_dom_info.append(dom_key_val)
            dom_key_val = {}
            dom_key_val["val"]= rx7_power
            dom_key_val["keyId"] = Rx7_power
            port_dom_info.append(dom_key_val)
            dom_key_val = {}
            dom_key_val["val"]= rx8_power
            dom_key_val["keyId"] = Rx8_power
            port_dom_info.append(dom_key_val)

            dom_key_val = {}
            dom_key_val["val"]= temp_high_alarm
            dom_key_val["keyId"] = Temp_high_alarm
            port_dom_info.append(dom_key_val)
            dom_key_val = {}
            dom_key_val["val"]= temp_low_alarm
            dom_key_val["keyId"] = Temp_low_alarm
            port_dom_info.append(dom_key_val)
            dom_key_val = {}
            dom_key_val["val"]= temp_high_warn
            dom_key_val["keyId"] = Temp_high_warn
            port_dom_info.append(dom_key_val)
            dom_key_val = {}
            dom_key_val["val"]= temp_low_warn
            dom_key_val["keyId"] = Temp_low_warn
            port_dom_info.append(dom_key_val)

            dom_key_val = {}
            dom_key_val["val"]= vcc_high_alarm
            dom_key_val["keyId"] = Vcc_high_alarm
            port_dom_info.append(dom_key_val)
            dom_key_val = {}
            dom_key_val["val"]= vcc_low_alarm
            dom_key_val["keyId"] = Vcc_low_alarm
            port_dom_info.append(dom_key_val)
            dom_key_val = {}
            dom_key_val["val"]= vcc_high_warn
            dom_key_val["keyId"] = Vcc_high_warn
            port_dom_info.append(dom_key_val)
            dom_key_val = {}
            dom_key_val["val"]= vcc_low_warn
            dom_key_val["keyId"] = Vcc_low_warn
            port_dom_info.append(dom_key_val)

            dom_key_val = {}
            dom_key_val["val"]= tx_bias_high_alarm
            dom_key_val["keyId"] = Tx_bias_high_alarm
            port_dom_info.append(dom_key_val)
            dom_key_val = {}
            dom_key_val["val"]= tx_bias_low_alarm
            dom_key_val["keyId"] = Tx_bias_low_alarm
            port_dom_info.append(dom_key_val)
            dom_key_val = {}
            dom_key_val["val"]= tx_bias_high_warn
            dom_key_val["keyId"] = Tx_bias_high_warn
            port_dom_info.append(dom_key_val)
            dom_key_val = {}
            dom_key_val["val"]= tx_bias_low_warn
            dom_key_val["keyId"] = Tx_bias_low_warn
            port_dom_info.append(dom_key_val)

            dom_key_val = {}
            dom_key_val["val"]= tx_power_high_alarm
            dom_key_val["keyId"] = Tx_power_high_alarm
            port_dom_info.append(dom_key_val)
            dom_key_val = {}
            dom_key_val["val"]= tx_power_low_alarm
            dom_key_val["keyId"] = Tx_power_low_alarm
            port_dom_info.append(dom_key_val)
            dom_key_val = {}
            dom_key_val["val"]= tx_power_high_warn
            dom_key_val["keyId"] = Tx_power_high_warn
            port_dom_info.append(dom_key_val)
            dom_key_val = {}
            dom_key_val["val"]= tx_power_low_warn
            dom_key_val["keyId"] = Tx_power_low_warn
            port_dom_info.append(dom_key_val)

            dom_key_val = {}
            dom_key_val["val"]= rx_power_high_alarm
            dom_key_val["keyId"] = Rx_power_high_alarm
            port_dom_info.append(dom_key_val)
            dom_key_val = {}
            dom_key_val["val"]= rx_power_low_alarm
            dom_key_val["keyId"] = Rx_power_low_alarm
            port_dom_info.append(dom_key_val)
            dom_key_val = {}
            dom_key_val["val"]= rx_power_high_warn
            dom_key_val["keyId"] = Rx_power_high_warn
            port_dom_info.append(dom_key_val)
            dom_key_val = {}
            dom_key_val["val"]= rx_power_low_warn
            dom_key_val["keyId"] = Rx_power_low_warn
            port_dom_info.append(dom_key_val)

            dom_info_port = {}
            dom_info_port["port"] = port_num
            dom_info_port["port_dom_info"] = port_dom_info
            dom_info["dom_info"].append(dom_info_port)

if __name__ == "__main__":
    ports = []
    n = len(sys.argv)
    if n > 1:
        for port in sys.argv[1:]:
            ports.append(int(port))
    remove_dom_info_json()
    if len(ports) != 0:
        get_dom_info_list(ports)
    write_dom_info_json()
