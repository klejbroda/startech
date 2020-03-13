# import sqlite3
# from check_for_csv import CheckForCsv
from arp_analyzer import ArpAnalyzer
from arp_reader import ArpReader
from arp_poisoning_export import ArpPoisoningExport
from portscan_reader import PortScanReader
from port_scan_export import PortScanExport
from portscan_analyzer import PortScanAnalyzer
from synflood_reader import SynFloodReader
from syn_flood_export import SynFloodExport
from syn_flood_analyzer import SynFloodAnalyzer


def run_syn_analysis():
    synflood_file = SynFloodReader()
    rows = synflood_file.create_dataset()
    db = SynFloodExport()
    db.create_table()
    db.insert_data(rows)
    analysis = SynFloodAnalyzer()
    analysis.access_db()
    analysis.create_ip_list()
    return analysis.synflood_analyzer()


def run_arp_analysis():
    arp_file = ArpReader()
    rows = arp_file.create_dataset()
    db = ArpPoisoningExport()
    db.create_table()
    db.insert_data(rows)
    analysis = ArpAnalyzer()
    return analysis.arp_analyzer()


def run_port_analysis():
    portscan_file = PortScanReader()
    rows = portscan_file.create_dataset()
    db = PortScanExport()
    db.create_table()
    db.insert_data(rows)
    analysis = PortScanAnalyzer()
    return analysis.portscan_analyzer()