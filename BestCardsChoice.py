import requests
import pandas as pd
import CardLevel
import KnapsackSolution
import sys


def chooseBestCards(card_id=111,gold='false',edition=1,bcx=5):

    url = f"https://api2.splinterlands.com/market/for_sale_by_card?card_detail_id={card_id}&edition={edition}&gold={gold}"
    request = requests.get(url)    
    df = pd.DataFrame(request.json())
    df = df.drop(columns=['fee_percent','last_used_block','desc','type','last_transferred_block','last_transferred_date','last_used_date','last_used_player'])
    df['buy_price']= df['buy_price'].astype('float')

    cards_info = pd.DataFrame(requests.get('https://api.splinterlands.io/cards/get_details').json())
    card_info = cards_info[cards_info['id']==card_id]

    df[['lvl','bcx']]=df.apply(lambda x: CardLevel.getLevelAndBcx(xp = x.xp , edition = edition, rarity = card_info.rarity.item(),gold =x.gold,tier = card_info.tier.item()),axis=1).apply(pd.Series)    
    
    chosen = KnapsackSolution.minimumCost(df,bcx)
    print(chosen)

if __name__ == '__main__':
    card_id, gold, edition, bcx  = sys.argv[1], sys.argv[2], sys.argv[3],sys.argv[4]
    card_id = int(card_id)
    edition = int(edition)
    bcx = int(bcx)
    chooseBestCards(card_id, gold, edition, bcx)