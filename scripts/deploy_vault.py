from brownie import EthVault, network

from scripts.helper_functions import get_account


def deploy_vault() -> EthVault:
    account = get_account()
    print(f"On network {network.show_active()}")
    vault = EthVault.deploy(
        {"from": account},
    )
    return vault


def main():
    deploy_vault()
