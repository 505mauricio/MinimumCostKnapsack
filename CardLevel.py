import math

def getLevelAndBcx(xp:int,edition:int,rarity:int,gold:bool,tier):

        xp_levels=[[20,60,160,360,760,1560,2560,4560,7560],
                   [100,300,700,1500,2500,4500,8500],
                   [250,750,1750,3750,7750],
                   [1000,3000,7000]]

        alpha_xp=[20,100,250,1000]

        gold_xp=[250,500,1000,2500]

        beta_xp= [15,75,175,750]

        beta_gold_xp=[200,400,800,2000]

        combine_rates=[[1,5,14,30,60,100,150,220,300,400],
                       [1,5,14,25,40,60,85,115],
                       [1,4,10,20,32,46],
                       [1,3,6,11]]

        gold_combine_rates=[[0,0,1,2,5,9,14,20,27,38],
                            [0,1,2,4,7,11,16,22],
                            [0,1,2,4,7,10],
                            [0,1,2,4]]                       


        if edition == 0:
                xp_ranges = xp_levels[rarity-1]
                for iteration,i in enumerate(xp_ranges):
                    if xp < i:
                        level = iteration+1
                        break            
                    level = iteration+2  
                if gold == False:
                    bcx = (xp/alpha_xp[rarity-1]+1)
                if gold == True:
                    bcx = (xp/gold_xp[rarity-1])

        if edition == 2:
                xp_ranges = xp_levels[rarity-1]
                for iteration,i in enumerate(xp_ranges):
                    if xp < i:
                        level = iteration+1
                        break 
                    level = iteration+2
                if gold == False:
                    bcx = (xp/beta_xp[rarity-1]+1)
                if gold == True:
                    bcx = (xp/beta_gold_xp[rarity-1]) 
                              
        if edition == 1 or (edition == 3 and math.isnan(tier)):
            xp_ranges = xp_levels[rarity-1]
            for iteration,i in enumerate(xp_ranges):
                if xp < i:
                    level = iteration+1
                    break 
                level = iteration+2
            if gold == False:
                bcx = (xp/beta_xp[rarity-1]+1)
            if gold == True:
                bcx = (xp/beta_gold_xp[rarity-1])

        if (edition == 3 and tier == 4) or edition == 4 or edition == 5:
            if gold == False:
                xp_ranges = combine_rates[rarity-1]
                for iteration,i in enumerate(xp_ranges):
                    if xp < i:
                        level = iteration
                        break 
                    level = iteration+1    
                bcx = xp                          
            if gold == True:
                xp_ranges = gold_combine_rates[rarity-1]
                for iteration,i in enumerate(xp_ranges):
                    if xp < i:
                        level = iteration
                        break
                    level = iteration+1
                bcx = xp

        if edition == 3 and tier == 7:
            if gold == False:
                xp_ranges = combine_rates[rarity-1]
                for iteration,i in enumerate(xp_ranges):
                    if xp < i:
                        level = iteration
                        break 
                    level = iteration+1       
                bcx = xp
            if gold == True:
                xp_ranges = gold_combine_rates[rarity-1]
                for iteration,i in enumerate(xp_ranges):
                    if xp < i:
                        level = iteration
                        break                     
                    level = iteration+1 
                bcx = xp                          
                
        return level,int(bcx)