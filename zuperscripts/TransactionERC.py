import requests
import random
import time

class TransactionERC:
    def __init__(self, wallet_address, rpc_endpoint):

        """
        Transaction class to interact with Ethereum Blockchain

        Attributes:
            wallet_address (str): Wallet address that we will check the balance for
            rpc_endpoint (str): RPC endpoint

        Returns:
            None
        """

        self.wallet_address = wallet_address
        self.rpc_endpoint = rpc_endpoint
        self.tx_counter = 0

    def get_balance(self):

        """
        Get the balance of the wallet address

        Arguments:
            None

        Returns:
            balance_wei (int): The corresponding balance of the given address in Wei format
        """

        payload = {
            "jsonrpc": "2.0",
            "method": "eth_getBalance",
            "params": [self.wallet_address, "latest"],
            "id": 1
        }
        response = requests.post(self.rpc_endpoint, json=payload)
        balance_hex = response.json()['result']
        balance_wei = int(balance_hex, 16)

        return balance_wei

    def check_balance(self):

        """
        Check the balance of the wallet address

        Arguments:
            None

        Returns:
            None
        """

        self.tx_counter += 1
        print(f"Ethereum Transaction no. {self.tx_counter} \n")

        try:
            balance_wei = self.get_balance()
            balance_in_ether = balance_wei / 1e18

            print(f'Wallet Address: {self.wallet_address}')
            print(f'Balance: {balance_in_ether} ETH')
        except Exception as e:
            print("An error occurred:", e)

        random_delay = random.randint(60, 90)
        print(f"Waiting for {random_delay} seconds...")
        print("=======================================================")

        time.sleep(random_delay)
