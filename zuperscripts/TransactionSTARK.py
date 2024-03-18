import requests

class TransactionSTARK:
    def __init__(self, rpc_endpoint):

        """
        Transaction class to interact with Starknet Mainnet and Testnet Blockchain

        Attributes:
            rpc_endpoint (str): RPC endpoint

        Returns:
            None
        """

        self.rpc_endpoint = rpc_endpoint

    def get_block(self):

        """
        Get the latest block

        Arguments:
            None

        Returns:
            txs (int): Transactions in single block/latest
        """

        payload = {
            "jsonrpc": "2.0",
            "method": "starknet_getBlockTransactionCount",
            "params": ["latest"],
            "id": "1"
        }
        response = requests.post(self.rpc_endpoint, json=payload)
        txs = response.json()['result']
        
        return txs

    def check_txs(self):

        """
        Check the transactions of the latest block, wait for a random time

        Arguments:
            None

        Returns:
            None
        """

        try:
            txs = self.get_block()

            print(f'Latest block: {txs} txs')
        except Exception as e:
            print("An error occurred:", e)