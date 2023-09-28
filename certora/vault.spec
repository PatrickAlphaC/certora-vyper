rule moreWithdrawLessFee {
    env e;
    uint256 amount1;
    uint256 amount2;
    require 0 < amount1;
    require amount1 < amount2;
    require amount2 < getAddressToAmountDeposited(e);
    assert withdraw(e, amount1) < withdraw(e, amount2), "More withdraw should incur less fee.";
}
