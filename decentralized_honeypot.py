from web3 import Web3
import hashlib
import json
import datetime
import sqlite3
import random

# Setup Web3 connection (local Ganache or private Ethereum network)
web3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))

# Blockchain smart contract code (Solidity)
contract_source_code = '''
pragma solidity ^0.8.0;

contract HoneypotRecord {
    struct Intrusion {
        uint id;
        string ip;
        string timestamp;
        string signature;
    }

    mapping(uint => Intrusion) public intrusions;
    uint public intrusionCount;

    function recordIntrusion(string memory ip, string memory timestamp, string memory signature) public {
        intrusions[intrusionCount] = Intrusion(intrusionCount, ip, timestamp, signature);
        intrusionCount++;
    }
}
'''

# Compile and deploy contract (using local Web3 connection)
# NOTE: This requires a Solidity compiler (solcx) to compile the contract
import solcx
solcx.install_solc("0.8.0")
compiled_sol = solcx.compile_source(contract_source_code)
contract_interface = compiled_sol['<stdin>:HoneypotRecord']

# Deploy contract
web3.eth.default_account = web3.eth.accounts[0]
HoneypotRecord = web3.eth.contract(abi=contract_interface['abi'], bytecode=contract_interface['bin'])
tx_hash = HoneypotRecord.constructor().transact()
tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
contract_address = tx_receipt.contractAddress
honeypot_contract = web3.eth.contract(address=contract_address, abi=contract_interface['abi'])

# Database setup to store local logs
db_file = 'honeypot_data.db'

def setup_database():
    conn = sqlite3.connect(db_file)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS intrusions (id INTEGER PRIMARY KEY, ip TEXT, timestamp TEXT, signature TEXT)''')
    conn.commit()
    conn.close()

# Function to generate a hash (simulating intrusion signature)
def generate_signature(data):
    return hashlib.sha256(data.encode()).hexdigest()

# Record intrusion details locally and on blockchain
def record_intrusion(ip):
    timestamp = datetime.datetime.now().isoformat()
    signature = generate_signature(ip + timestamp)

    # Record intrusion locally in the database
    conn = sqlite3.connect(db_file)
    c = conn.cursor()
    c.execute("INSERT INTO intrusions (ip, timestamp, signature) VALUES (?, ?, ?)", (ip, timestamp, signature))
    conn.commit()
    conn.close()

    # Record intrusion on the blockchain
    tx_hash = honeypot_contract.functions.recordIntrusion(ip, timestamp, signature).transact()
    web3.eth.wait_for_transaction_receipt(tx_hash)
    print(f"Intrusion from IP {ip} recorded on blockchain with signature {signature}")

# Simulate honeypot detection and recording
def simulate_honeypot_activity():
    honeypot_ips = ["192.168.1.100", "192.168.1.101", "192.168.1.102"]
    random_ip = random.choice(honeypot_ips)
    print(f"Simulated intrusion detected from IP: {random_ip}")
    record_intrusion(random_ip)

if __name__ == "__main__":
    setup_database()
    print("Decentralized Honeypot System is running...")
    while True:
        # Simulate honeypot activity
        simulate_honeypot_activity()
        input("Press Enter to simulate the next intrusion...")
