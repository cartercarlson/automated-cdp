from py.cdp import CDP

cdp = CDP(price=208.05, eth_deposited=86.722, start_eth_on_hand=2.447)
withdrawal_1 = 5488
cdp.generate(withdrawal_1)
cdp.trade(side='BUY', usd=withdrawal_1, price=228)
cdp.deposit(eth=23.03)
cdp.summarize(price=400, save=True)


if __name__ == '__main__':
    main()
