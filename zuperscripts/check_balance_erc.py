import requests

def get_erc_balance(wallet_address, rpc_endpoint):

    """
    Get the balance of the wallet address

    Attributes:
        wallet_address (str): Wallet address that we will check the balance for
        rpc_endpoint (str): Ethereum RPC endpoint

    Returns:
        balance_wei (int): The corresponding balance of the given address in Wei format
    """

    payload = {
        "jsonrpc": "2.0",
        "method": "eth_getBalance",
        "params": [wallet_address, "latest"],
        "id": 1
    }
    response = requests.post(rpc_endpoint, json=payload)
    balance_hex = response.json()['result']
    balance_wei = int(balance_hex, 16)

    return balance_wei

def check_erc_balance():

    """
    Check the balance of the wallet address

    Attributes:
        None

    Returns:
        None
    """

    balance_wei = get_erc_balance(wallet_address)
    balance_in_ether = balance_wei / 1e18
    
    print(f'Wallet Address: {wallet_address}')
    print(f'Balance: {balance_in_ether} ETH')
