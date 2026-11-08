# Task 2: Stock Portfolio Tracker

A simple console program that calculates the total value of a stock portfolio using manually defined prices.

## How to Run

```
python stock_tracker_simple.py
```

Requires Python 3. No extra packages needed.

## How to Use

1. The program lists the available stocks.
2. Enter a stock name (for example `AAPL`) and the number of shares.
3. Repeat for as many stocks as you like.
4. Type `done` when you are finished.
5. The program shows each holding and the total investment value.
6. Choose `y` when asked if you want to save the result to `portfolio.txt`.

## Stock Prices

Prices are hardcoded in a dictionary at the top of the script. You can edit them or add your own stocks.

| Stock | Price |
|-------|-------|
| AAPL  | 180   |
| TSLA  | 250   |
| GOOGL | 140   |
| MSFT  | 330   |

## Example

```
Stock name: AAPL
How many shares of AAPL? 10

Stock name: TSLA
How many shares of TSLA? 5

Stock name: done

--- Your portfolio ---
AAPL : 10 x 180 = 1800
TSLA : 5 x 250 = 1250
Total investment: 3050
```

## Features

- Rejects stocks that are not in the price list
- Rejects invalid quantities
- Adds to the quantity if you enter the same stock twice
- Optional saving of the results to a text file

## Concepts Used

- Dictionary (stock prices and holdings)
- Input / output
- Basic arithmetic (quantity x price, running total)
- File handling (optional save to `portfolio.txt`)

## Files

| File | Description |
|------|-------------|
| `stock_tracker_simple.py` | The tracker script |
| `portfolio.txt` | Created only if you choose to save |
