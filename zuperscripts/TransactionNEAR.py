import requests
from zuperscripts.TransactionERC import TransactionERC

class TransactionNear(TransactionERC):
    def __init__(self, account_id, rpc_endpoint):

        """
        Transaction class to interact with NEAR Mainnet Blockchain

        Attributes:
            wallet_address (str): Account ID that we will check the balance for
            rpc_endpoint (str): RPC endpoint

        Returns:
            None
        """

        super().__init__(account_id, rpc_endpoint)

    def get_balance(self):

        """
        Get the balance of the account ID

        Arguments:
            None

        Returns:
            balance (int): The corresponding balance of the given address
        """

        payload = {
            "jsonrpc": "2.0",
            "method": "query",
            "params": {
                "request_type": "view_account",
                "finality": "final",
                "account_id": self.wallet_address
            },
            "id": "1"
        }
        response = requests.post(self.rpc_endpoint, json=payload)
        data = response.json()

        if 'result' in data:
            return data['result']['amount']
        else:
            return None

    def check_balance(self):

        """
        Check the balance of the account ID

        Arguments:
            None

        Returns:
            None
        """

        balance = self.get_balance()

        if balance is not None:
            print(f'Account ID: {self.wallet_address}')
            print(f'Balance: {balance} NEAR')
        else:
            print(f'Failed to retrieve balance for account: {self.account_id}')
