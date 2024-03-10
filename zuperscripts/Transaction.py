import requests

class Transaction:
    def __init__(self, wallet_address, rpc_endpoint):
        self.wallet_address = wallet_address
        self.rpc_endpoint = rpc_endpoint

    def get_balance(self):
        """
        Get the balance of the wallet address

        Attributes:
            wallet_address (str): Wallet address that we will check the balance for
            rpc_endpoint (str): RPC endpoint

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

        Attributes:
            None

        Returns:
            None
        """

        balance_wei = self.get_erc_balance()
        balance_in_ether = balance_wei / 1e18

        print(f'Wallet Address: {self.wallet_address}')
        print(f'Balance: {balance_in_ether} ETH')
