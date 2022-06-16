# Learning points: I am unable to fully recreate the 50/50 in the 4 star and simplifying parts into functions (I tried and failed).
# I might have time to resolve those issues however I should not be spending too much time on one project and instead spend that time on other projects.

import random
import BannerList  # List of obtainable items/characters (Banner was Ayato during the making of this project)

FiftyFiftyGuaranteed = 0
FiftyFifty = 0

i = 0  # Represents 5 star pity count
k = 0  # represents 4 star pity count

while i <= 90:
    playerPull = input("1 Pull or 10 Pulls? (Type 1 or 10) ")

    if playerPull == "1":  # Allowing the player to roll once.
        i = i + 1
        k = k + 1
        while i <= 75:  # this is when 5 star pity is less than 75 which

            x = random.randint(0, 999)  # 5Star = 0.6%; 4Star = 5.1%; 3Star = 94.4%. x determines the chances you get.

            if x <= 5:  # Range (Chance) of 5 star
                FiftyFifty = random.randint(0, 1)  # This is the 50/50 system when a 5 Star character is successfully pulled, FiftyFiftyGuaranteed decides whether you get the limited character or not.
                if FiftyFiftyGuaranteed == 1:  # If you lost a 50/50 previously, you will be guaranteed to get the limited Character.
                    print("*****", "Limited Character!", i, k)
                    FiftyFiftyGuaranteed = 0  # This is when you lost the 50/50. A random standard 5Star is then chosen based on BannerList. Your next 5 star is a guaranteed limited character.
                elif FiftyFifty == 0:  # This means
                    print("*****", BannerList.FiveStarsStandard[random.randint(0, 4)], i, k)
                    FiftyFiftyGuaranteed = 1
                else:  # When FiftyFifty == 1:, this means you won the 50/50 chance of getting a limited character.
                    print("*****", "Limited Character!", i, k)
                i = 0  # Five star and four star pity are reset once a five star is rolled
                k = 0
                break

            if 6 <= x <= 56:  # Range (chance) of 4 star
                if 0 < k < 10:
                    print("****", BannerList.FourStars[random.randint(0, 37)], i, k)
                    k = 0
                    break
            if k == 10:  # Guaranteed 4 star for every 10 pulls
                print("****", BannerList.FourStars[random.randint(0, 37)], i, k)
                k = 0
                break

            if x >= 57:  # Range (chance) of 3 star
                print("***", BannerList.ThreeStars[random.randint(0, 12)], i, k)
                break

        while 76 <= i <= 90:  # when 75 pity is reached, soft pity occurs. Chances of 5 star increases while chances of 3 star decreases.
            x = random.randint(0, 999)
            if i == 90:  # WHen pity is 90, a guaranteed 5 star is pulled.
                FiftyFifty = random.randint(0, 1)  # This section of code is copied from previous lines.
                if FiftyFiftyGuaranteed == 1:
                    print("*****", "Limited Character!", i, k)
                    FiftyFiftyGuaranteed = 0
                elif FiftyFifty == 0:
                    print("*****", BannerList.FiveStarsStandard[random.randint(0, 4)], i, k)
                    FiftyFiftyGuaranteed = 1
                else:
                    print("*****", "Limited Character!", i, k)
                i = 0
                k = 0
                break
            if x <= 36:  # Same lines of code buy with bigger chance of getting 5 stars.
                FiftyFifty = random.randint(0, 1)  # 50/50
                if FiftyFiftyGuaranteed == 1:
                    print("*****", "Limited Character!", i, k)
                    FiftyFiftyGuaranteed = 0
                elif FiftyFifty == 0:
                    print("*****", BannerList.FiveStarsStandard[random.randint(0, 4)], i, k)
                    FiftyFiftyGuaranteed = 1
                else:
                    print("*****", "Limited Character!", i, k)
                break

            if 36 <= x <= 87:  # Same thing as in no pity for 4 star and 3 star.
                if 0 < k < 10:
                        print("****", BannerList.FourStars[random.randint(0, 37)], i, k)
                        k = 0
                        break
            if k == 10:
                print("****", BannerList.FourStars[random.randint(0, 37)], i, k)
                k = 0
                break

            if x >= 88:
                print("***", BannerList.ThreeStars[random.randint(0, 12)], i, k)
                break

    if playerPull == "10":  # Same code for 1 pull but this time its programmed to pull 10 times.
        for j in range(1, 11):
            i = i + 1
            k = k + 1
            while i <= 75:  # no pity
                x = random.randint(0, 999)
                if x <= 5:
                    FiftyFifty = random.randint(0, 1)  # 50/50
                    if FiftyFiftyGuaranteed == 1:
                        print("*****", "Limited Character!", i, k)
                        FiftyFiftyGuaranteed = 0
                    elif FiftyFifty == 0:
                        print("*****", BannerList.FiveStarsStandard[random.randint(0, 4)], i, k)
                        FiftyFiftyGuaranteed = 1
                    else:
                        print("*****", "Limited Character!", i, k)
                    i = 0
                    k = 0
                    break

                if 6 <= x <= 56:
                    if 0 < k < 10:
                        print("****", BannerList.FourStars[random.randint(0, 37)], i, k)
                        k = 0
                        break
                if k == 10:
                    print("****", BannerList.FourStars[random.randint(0, 37)], i, k)
                    k = 0
                    break

                if x >= 57:
                    print("***", BannerList.ThreeStars[random.randint(0, 12)], i, k)
                    break

            while 76 <= i <= 90:  # soft pity
                x = random.randint(0, 999)
                if i == 90:  # hard pity
                    FiftyFifty = random.randint(0, 1)  # 50/50
                    if FiftyFiftyGuaranteed == 1:
                        print("*****", "Limited Character!", i, k)
                        FiftyFiftyGuaranteed = 0
                    elif FiftyFifty == 0:
                        print("*****", BannerList.FiveStarsStandard[random.randint(0, 4)], i, k)
                        FiftyFiftyGuaranteed = 1
                    else:
                        print("*****", "Limited Character!", i, k)
                    i = 0
                    k = 0
                    break
                if x <= 36:
                    FiftyFifty = random.randint(0, 1)  # 50/50
                    if FiftyFiftyGuaranteed == 1:
                        print("*****", "Limited Character!", i, k)
                        FiftyFiftyGuaranteed = 0
                    elif FiftyFifty == 0:
                        print("*****", BannerList.FiveStarsStandard[random.randint(0, 4)], i, k)
                        FiftyFiftyGuaranteed = 1
                    else:
                        print("*****", "Limited Character!", i, k)
                    i = 0
                    k = 0
                    break

                if 36 <= x <= 87:
                    if 0 < k < 10:
                        print("****", BannerList.FourStars[random.randint(0, 37)], i, k)
                        k = 0
                        break
                if k == 10:
                    print("****", BannerList.FourStars[random.randint(0, 37)], i, k)
                    k = 0
                    break

                if x >= 88:
                    print("***", BannerList.ThreeStars[random.randint(0, 12)], i, k)
                    break
