# display results in terminal
from lazada import scrap_lazada
from shopee import scrap_shopee
import pandas as pd

keyword = input("Please enter the keyword to search: ")

result = scrap_shopee(keyword,30)
try:
    result += scrap_lazada(keyword,30)
except IndexError:
    pass

if __name__ == "__main__":
    df = pd.DataFrame([t.__dict__ for t in result])
    print(df)
    
