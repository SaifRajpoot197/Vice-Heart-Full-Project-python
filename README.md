# 🏎️ VICE HEARTS

**VICE HEARTS** is a console-based action and car-collecting simulation game built in Python. Inspired by classic open-world games, players can complete missions to earn cash, buy luxury cars, manage their personal garage, sell vehicles, and save their progress to a local file.

## ✨ Features
* **Starting Balance:** Start your journey with **\$60,000** in cash.
* **Luxury Car Shop:** Browse and purchase four different cars:
  * **Porsche** (\$5,000)
  * **Audi** (\$20,000)
  * **BMW** (\$50,000)
  * **Lamborghini** (\$100,000)
* **Missions System:** Earn extra money by completing jobs:
  * *Pizza Delivery* (+\$1,000)
  * *Bank Robbery* (+\$7,000)
* **Garage & Selling:** Store your purchased vehicles in your garage and sell them anytime for **\$25,000** each.
* **Save Progress:** Save your current money and garage inventory directly to a `vice_save.txt` file.

## 🛠️ Technologies Used
* **Python 3** (Functions, Lists, Dictionaries, File Handling, and Loops)

## 🚀 How to Run the Game

1. **Clone the repository:**
   ```bash
   git clone https://github.com
   ```

2. **Navigate to the project folder:**
   ```bash
   cd YOUR-REPO-NAME
   ```

3. **Run the script:**
   ```bash
   python main.py
   ```
   *(Make sure to replace `main.py` with your actual Python file name).*

## 🎮 Gameplay Preview

```text
=== VICE HEARTS ===
Money: 60000 | Garage: []
1. Car Shop
2. Mission
3. Sell Car
4. Save Game
5. Exit
Choose: 1

--- CAR SHOP ---
1 . Porsche - \(5000 2 . Audi -\) 20000
3 . BMW - \(50000 4 . Lamborghini -\) 100000
Choose Car (1-4): 3
Bought BMW
```

## 🔮 Future Improvements
* Add a **Load Game** option to read saved progress from `vice_save.txt` on startup.
* Calculate car resale value dynamically based on each car's original price.
* Add risk/reward mechanics (like police chases) to the Bank Robbery mission.
* Add input validation (`try-except`) to prevent crashes on invalid inputs.
