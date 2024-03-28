import requests
from TransactionERC import TransactionERC
from starknet_py.net.full_node_client import FullNodeClient
from starknet_py.net.models.chains import StarknetChainId
from starknet_py.net.signer.stark_curve_signer import KeyPair
from starknet_py.net.account.account import Account

class TransactionSTARK(TransactionERC):
    def __init__(self, wallet_address, rpc_endpoint, network_type):

        """
        Transaction class to interact with Starknet Mainnet and Testnet Blockchain

        Attributes:
            wallet_address (str): Wallet address that we will check the balance for
            rpc_endpoint (str): RPC endpoint
            network_type (str): MAINNET, GOERLI, SEPOLIA or SEPOLIA_INTEGRATION

        Returns:
            None
        """

        super().__init__(wallet_address, rpc_endpoint)
        self.network_type = network_type

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

    def get_balance(self):

        """
        Get the balance of the wallet address

        Arguments:
            None

        Returns:
            balance_wei (int): The corresponding balance of the given address in Wei format
        """

        if self.network_type == "MAINNET":
            account = Account(
                address=self.wallet_address,
                client=FullNodeClient(node_url=self.rpc_endpoint),
                key_pair=KeyPair(12, 34),
                chain=StarknetChainId.MAINNET,
            )
        elif self.network_type == "SEPOLIA_INTEGRATION":
            account = Account(
                address=self.wallet_address,
                client=FullNodeClient(node_url=self.rpc_endpoint),
                key_pair=KeyPair(12, 34),
                chain=StarknetChainId.SEPOLIA_INTEGRATION,
            )

        balance_wei = account.get_balance_sync()

        return balance_wei

    def check_balance(self):

        """
        Check the balance of the wallet address and print the balance

        Arguments:
            None

        Returns:
            None
        """

        try:
            balance_wei = self.get_balance()
            balance_in_ether = balance_wei / 1e18

            print(f'Wallet Address: {self.wallet_address}')
            print(f'Balance: {balance_in_ether} ETH')
        except Exception as e:
            print("An error occurred:", e)

    def check_block(self):

        """
        Check the transactions of the latest block

        Arguments:
            None

        Returns:
            None
        """

        try:
            txs = self.get_block()

            print(f'Wallet Address: {self.wallet_address}')
            print(f'Latest block: {txs} txs')
        except Exception as e:
            print("An error occurred:", e)
