from itertools import permutations as permute


def get_cases():
    for p in permute(range(1, 10)):
        five_gon = p
        t_one = 10 + five_gon[4] + five_gon[5]
        t_two = five_gon[0] + five_gon[5] + five_gon[6]
        t_three = five_gon[1] + five_gon[6] + five_gon[7]
        t_four = five_gon[2] + five_gon[7] + five_gon[8]
        t_five = five_gon[3] + five_gon[8] + five_gon[4]
        if t_one == t_two == t_three == t_four == t_five:
            yield (10,) + p


def get_data(tuple):
    print("=========================")
    print(f"tuple = {tuple}")
    outer_nodes = [tuple[i] for i in range(5)]
    print(f"total = {tuple[0] + tuple[5] + tuple[6]}")
    print(f"outer nodes = {outer_nodes}")
    print(f"smallest outer node = {min(outer_nodes)}")


def main():
    for case in get_cases():
        get_data(case)
    print("=========================")
    print("\nUsing the above data, and pencil and paper, \nthe answer is obvious:")
    print("6531031914842725")
    print("This makes the final part of the algorithm unecessary")


if __name__ == "__main__":
    main()

