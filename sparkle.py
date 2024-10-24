def sparkl(back = purple, rg = joker, delay = 0.7, spark = 4):
    for i in range(spark):
        what = random.randint(0,29)
        who = random.randint(0,29)
        why = random.randint(0,29)
        np.fill(back)
        np[what] = rg
        np[who] = rg
        np[why] = rg
        np.show()
        time.sleep(delay)
