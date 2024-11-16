### Decentralized Honeypot System Using Blockchain

#### Introduction
This decentralized honeypot system utilizes blockchain technology to record intrusion attempts across a network of honeypots. By leveraging a blockchain-based ledger, all recorded intrusion data is immutable, ensuring tamper-proof evidence for forensic analysis.

#### Features
- **Intrusion Detection and Recording**: Detect simulated intrusions and log them locally as well as on a blockchain.
- **Immutable Evidence**: Blockchain ledger stores the details of intrusion attempts, ensuring that records are immutable and cannot be tampered with.
- **Decentralized Ledger**: Uses Ethereum blockchain to store intrusion details securely.

#### Usage Instructions
1. **Setup Dependencies**: Install necessary packages using `pip`.
    ```sh
    pip install web3 solcx
    ```
2. **Install Ganache**: Use Ganache to run a local Ethereum blockchain for testing purposes.
3. **Compile and Deploy Smart Contract**: The script compiles and deploys the smart contract automatically when it is first run.
4. **Run the Honeypot System**: Execute the script to start recording intrusions.
    ```sh
    python decentralized_honeypot.py
    ```

#### Prerequisites
- **Python 3.6 or above**: Ensure you have Python installed in your system.
- **Ganache**: Install Ganache for a local blockchain environment.
- **Solidity Compiler (solcx)**: Used to compile the Solidity smart contract.

#### How It Works
1. **Smart Contract Deployment**: The Solidity smart contract, `HoneypotRecord`, is compiled and deployed to a local Ethereum blockchain.
2. **Intrusion Simulation**: The script simulates intrusions by selecting a random IP address from a predefined list.
3. **Record Intrusion**: Each detected intrusion is recorded both in a local SQLite database and on the Ethereum blockchain via the smart contract.

#### Implementation Steps
1. **Clone Repository**: Clone this repository from GitHub.
2. **Install Dependencies**: Use the command `pip install -r requirements.txt` to install dependencies.
3. **Configure Blockchain**: Run Ganache and ensure it's listening on `http://127.0.0.1:8545`.
4. **Run the Tool**: Run the server using `python decentralized_honeypot.py` to start detecting and recording intrusions.

#### Contributing
If you find bugs or have suggestions for improvements, feel free to contribute by opening an issue or making a pull request.

#### License
This project is open-source and licensed under the MIT License.

#### Disclaimer
This project is intended for educational purposes only. Users are responsible for ensuring they comply with applicable laws and regulations before using or modifying the honeypot system.
