# --------猜数字游戏-第四次修改--------
n = int(input("请输入要猜的次数："))
for i in range(n):
    num = input("猜猜我心里想的是哪个数字？")
    guess = int(num)
    if guess == 6:
        print("恭喜你猜对了，真厉害")
        break
    elif guess > 6:
        print("错了，错了，猜大了")
    elif guess < 6:
        print("错了，错了，猜小了")