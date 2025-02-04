# XEParser - Python currency Exchange Rate Parser 📉💱
XEParser is a simple Python script that allows you to easily retrieve historical currency exchange rates from XE.com for any given day. 🌍💸

## Features ✨
- Fetch historical exchange rates for any date 📅
- Support for multiple currencies 💵💶
- Simple, intuitive script to access exchange rate data 🔧

## How to Use 🛠️

### 1. Clone the Repository 🧑‍💻
To get started, clone this repository to your local machine:

```bash
git clone https://github.com/Caportabow/XEParser.git
```

### 2. Install Required Dependencies 📦
Navigate into the project directory and install the required dependencies:

```bash
cd XEParser
pip install -r requirements.txt
```

### 3. Example Usage 🚀
Once you have the repository cloned, you can use the `XEParser` script as follows:

```python
from XEParser import XEParser

# Specify the base currency and date
base_currency = 'USD'
date = "2024-08-05"

# Create a parser object
parser = XEParser(base_currency, date)

# Parse and print the exchange rates
rates = parser.parse()
print(f'Exchange USD->EUR: {rates.EUR}')
print(f'All rates for this day: {rates.json}')
```

### Example Output:
```
Exchange USD->EUR: 0.92
All rates for this day: {"EUR": 0.92, "GBP": 0.75, "JPY": 110.55, ...}
```

## Parameters 📏
- `base_currency`: The base currency for exchange rates (e.g., `'USD'`, `'EUR'`, etc.)
- `date`: The date for which you want to get the exchange rates. The format should be `YYYY-MM-DD` (e.g., `'2025-01-01'`).

## How It Works 🔍
1. You specify the base currency and the date you're interested in.
2. The script fetches historical exchange rate data from XE.com.
3. You can access the exchange rate for any currency directly from the parsed data.

## Support 🤝
If you have any questions or need help, feel free to open an issue or contact the maintainer.

Happy coding! 🚀
