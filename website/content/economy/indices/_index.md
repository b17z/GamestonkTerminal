```
usage: indices [--export {csv,json,xlsx}] [-h]
```

US indices. [Source: Wall St. Journal]

```
optional arguments:
  -h, --help            show this help message (default: False)
  --export {csv,json,xlsx}
                        Export raw data into csv, json, xlsx (default: )
```

Example:
```
2022 Feb 15, 05:06 (✨) /economy/ $ indices
                      US Indices
┌───────────────────────┬──────────┬─────────┬───────┐
│                       │ Price    │ Chg     │ %Chg  │
├───────────────────────┼──────────┼─────────┼───────┤
│ DJIA                  │ 34566.17 │ -171.89 │ -0.49 │
├───────────────────────┼──────────┼─────────┼───────┤
│ Nasdaq Composite      │ 13790.92 │ -0.24   │ 0.00  │
├───────────────────────┼──────────┼─────────┼───────┤
│ S&P 500               │ 4401.67  │ -16.97  │ -0.38 │
├───────────────────────┼──────────┼─────────┼───────┤
│ DJ Total Stock Market │ 44670.32 │ -181.98 │ -0.41 │
├───────────────────────┼──────────┼─────────┼───────┤
│ Russell 2000          │ 2020.79  │ -9.36   │ -0.46 │
├───────────────────────┼──────────┼─────────┼───────┤
│ NYSE Composite        │ 16531.31 │ -133.68 │ -0.80 │
├───────────────────────┼──────────┼─────────┼───────┤
│ Barron's 400          │ 1008.20  │ -5.07   │ -0.50 │
├───────────────────────┼──────────┼─────────┼───────┤
│ CBOE Volatility       │ 26.49    │ -1.84   │ -6.49 │
├───────────────────────┼──────────┼─────────┼───────┤
│ DJIA Futures          │ 34766    │ 295     │ 0.86  │
├───────────────────────┼──────────┼─────────┼───────┤
│ S&P 500 Futures       │ 4446.00  │ 52.00   │ 1.18  │
└───────────────────────┴──────────┴─────────┴───────┘
```
