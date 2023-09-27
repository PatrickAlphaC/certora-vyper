from brownie import reverts


def test_initial_owner(vault, account):
    assert vault.owner() == account.address


def test_deposit(vault, account):
    amount_to_deposit = 1e18
    vault.deposit({"from": account, "value": amount_to_deposit})
    assert vault.balance() == vault.address_to_amount_deposited(account.address)
    assert vault.balance() == amount_to_deposit


def test_withdraw_large(vault, account):
    amount_to_deposit = 101e18
    vault.deposit({"from": account, "value": amount_to_deposit})
    vault.withdraw(amount_to_deposit, {"from": account})
    assert vault.balance() == 0


def test_withdraw_medium(vault, account):
    amount_to_deposit = 11e18
    vault.deposit({"from": account, "value": amount_to_deposit})
    vault.withdraw(amount_to_deposit, {"from": account})
    assert vault.balance() == 0


def test_withdraw_small(vault, account):
    amount_to_deposit = 2e18
    vault.deposit({"from": account, "value": amount_to_deposit})
    vault.withdraw(amount_to_deposit, {"from": account})
    assert vault.balance() == 0


def test_withdraw_tiny(vault, account):
    amount_to_deposit = 1e17
    vault.deposit({"from": account, "value": amount_to_deposit})
    vault.withdraw(amount_to_deposit, {"from": account})
    assert vault.balance() == 0


def test_withdraw_more_than_zero(vault, account):
    amount_to_withdraw = 1e18
    with reverts():
        vault.withdraw(amount_to_withdraw, {"from": account})


def test_cant_withdraw_too_much(vault, account):
    amount_to_deposit = 1e18
    vault.deposit({"from": account, "value": amount_to_deposit})
    amount_to_withdraw = 2e18
    with reverts():
        vault.withdraw(amount_to_withdraw, {"from": account})
