import random


def main():
    print("欢迎来到猜数字游戏！")
    print("我已经想好了一个 1 到 100 之间的数字，你来猜。")
    target = random.randint(1, 100)
    attempts = 0

    while True:
        attempts += 1
        try:
            guess = int(input("请输入你的猜测："))
        except ValueError:
            print("请输入一个有效的整数。")
            continue

        if guess < target:
            print("太小了，再试一次。")
        elif guess > target:
            print("太大了，再试一次。")
        else:
            print(f"恭喜你！猜对了，答案是 {target}。")
            print(f"你一共猜了 {attempts} 次。")
            break


if __name__ == "__main__":
    main()
