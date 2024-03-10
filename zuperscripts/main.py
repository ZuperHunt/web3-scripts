import threading
import random
import time
from TransactionERC import TransactionERC
from TransactionNEAR import TransactionNear

def erc_threading(wallet_address, rpc_endpoint):

    """
    Function to Define Ethereum Transaction Thread Doing

    Arguments:
        wallet_address (str): Wallet address that we will check the balance for
        rpc_endpoint (str): RPC endpoint

    Returns:
        None
    """

    erc_tx_counter = 0

    while True:
        erc_tx_counter += 1
        print(f"Ethereum Transaction no. {erc_tx_counter} \n")

        TransactionERC(wallet_address, rpc_endpoint).check_balance()

        random_delay = random.randint(60, 90)
        print(f"Waiting for {random_delay} seconds...")
        print("=======================================================")

        time.sleep(random_delay)

def near_mainnet_threading(account_id, rpc_endpoint):

    """
    Function to Define NEAR Mainnet Transaction Thread Doing

    Arguments:
        account_id (str): Account ID that we will check the balance for
        rpc_endpoint (str): RPC endpoint

    Returns:
        None
    """

    near_mainnet_tx_counter = 0

    while True:
        near_mainnet_tx_counter += 1
        print(f"NEAR Mainnet Transaction no. {near_mainnet_tx_counter} \n")

        TransactionNear(account_id, rpc_endpoint).check_balance()

        random_delay = random.randint(60, 90)
        print(f"Waiting for {random_delay} seconds...")
        print("=======================================================")

        time.sleep(random_delay)

def near_testnet_threading(account_id, rpc_endpoint):

    """
    Function to Define NEAR Testnet Transaction Thread Doing

    Arguments:
        account_id (str): Account ID that we will check the balance for
        rpc_endpoint (str): RPC endpoint

    Returns:
        None
    """

    near_testnet_tx_counter = 0

    while True:
        near_testnet_tx_counter += 1
        print(f"NEAR Testnet Transaction no. {near_testnet_tx_counter} \n")

        TransactionNear(account_id, rpc_endpoint).check_balance()

        random_delay = random.randint(60, 90)
        print(f"Waiting for {random_delay} seconds...")
        print("=======================================================")

        time.sleep(random_delay)

def main():
    # Ethereum Configuration
    ethereum_rpc_endpoint = 'https://eth1.lava.build/lava-referer-630567c6-c700-4955-b1d0-f512e7364026/'
    ethereum_wallet_address = '0x0000004C4F555675F3043F83b653834359e671c3'

    # NEAR Mainnet Configuration
    near_mainnet_rpc_endpoint = 'https://near.lava.build/lava-referer-630567c6-c700-4955-b1d0-f512e7364026/'
    near_mainnet_account_id = 'lavaman.near'

    # NEAR Testnet Configuration
    near_testnet_rpc_endpoint = 'https://near-testnet.lava.build/lava-referer-630567c6-c700-4955-b1d0-f512e7364026/'
    near_testnet_account_id = 'lavaman.testnet'

    # Building Threads
    erc_thread = threading.Thread(target=erc_threading, args=(ethereum_wallet_address, ethereum_rpc_endpoint))
    near_mainnet_thread = threading.Thread(target=near_mainnet_threading, args=(near_mainnet_account_id, near_mainnet_rpc_endpoint))
    near_testnet_thread = threading.Thread(target=near_testnet_threading, args=(near_testnet_account_id, near_testnet_rpc_endpoint))

    # Starting Threads
    erc_thread.start()
    time.sleep(2)
    near_mainnet_thread.start()
    time.sleep(2)
    near_testnet_thread.start()

if __name__ == "__main__":
    main()
