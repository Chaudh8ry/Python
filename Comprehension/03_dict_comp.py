tea_price_inr = {
    "Masala Chai": 90,
    "Gree Tea": 120,
    "Iced Tea": 100
}

tea_price_usd = {tea:price/90 for tea,price in tea_price_inr.items()}
print(tea_price_usd)