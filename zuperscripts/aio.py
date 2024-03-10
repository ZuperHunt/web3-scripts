import requests
import random
import time

def get_ethereum_balance(wallet_address, rpc_endpoint):
    payload = {
        "jsonrpc": "2.0",
        "method": "eth_getBalance",
        "params": [wallet_address, "latest"],
        "id": 1
    }
    response = requests.post(rpc_endpoint, json=payload)
    balance_hex = response.json()['result']
    balance_wei = int(balance_hex, 16)
    return balance_wei / 1e18

def check_ethereum_balance(wallet_address, rpc_endpoint):
    balance = get_ethereum_balance(wallet_address, rpc_endpoint)
    print(f'Wallet Address: {wallet_address}')
    print(f'Balance: {balance} ETH')

def get_near_balance(account_id, rpc_endpoint):
    payload = {
        "jsonrpc": "2.0",
        "method": "query",
        "params": {
            "request_type": "view_account",
            "finality": "final",
            "account_id": account_id
        },
        "id": "1"
    }
    response = requests.post(rpc_endpoint, json=payload)
    data = response.json()
    if 'result' in data:
        return data['result']['amount']
    else:
        return None

def check_near_balance(account_id, rpc_endpoint):
    balance = get_near_balance(account_id, rpc_endpoint)
    if balance is not None:
        print(f'Account ID: {account_id}')
        print(f'Balance: {balance} NEAR')
    else:
        print(f'Failed to retrieve balance for account: {account_id}')

def main():
    # Ethereum Configuration
    ethereum_rpc_endpoint = 'https://eth1.lava.build/lava-referer-630567c6-c700-4955-b1d0-f512e7364026/'
    ethereum_wallet_address = '0x0000004C4F555675F3043F83b653834359e671c3'
    ethereum_tx_counter = 0

    # NEAR Mainnet Configuration
    near_mainnet_rpc_endpoint = 'https://near.lava.build/lava-referer-630567c6-c700-4955-b1d0-f512e7364026/'
    near_mainnet_account_id = 'lavaman.near'
    near_mainnet_tx_counter = 0

    # NEAR Testnet Configuration
    near_testnet_rpc_endpoint = 'https://near-testnet.lava.build/lava-referer-630567c6-c700-4955-b1d0-f512e7364026/'
    near_testnet_account_id = 'lavaman.testnet'
    near_testnet_tx_counter = 0

    while True:
        # Ethereum
        ethereum_tx_counter += 1
        print(f"Ethereum Transaction no. {ethereum_tx_counter} \n")

        try:
            check_ethereum_balance(ethereum_wallet_address, ethereum_rpc_endpoint)
        except Exception as e:
            print("An error occurred:", e)

        # NEAR Mainnet
        near_mainnet_tx_counter += 1
        print(f"NEAR Mainnet Transaction no. {near_mainnet_tx_counter} \n")

        try:
            check_near_balance(near_mainnet_account_id, near_mainnet_rpc_endpoint)
        except Exception as e:
            print("An error occurred:", e)

        # NEAR Testnet
        near_testnet_tx_counter += 1
        print(f"NEAR Testnet Transaction no. {near_testnet_tx_counter}\n")

        try:
            check_near_balance(near_testnet_account_id, near_testnet_rpc_endpoint)
        except Exception as e:
            print("An error occurred:", e)

        # Generate a random delay between 60 and 90 seconds
        random_delay = random.randint(60, 90)
        print(f"Waiting for {random_delay} seconds...")
        print("=======================================================")


        # Wait for the random delay before looping again
        time.sleep(random_delay)

if __name__ == "__main__":
    main()
