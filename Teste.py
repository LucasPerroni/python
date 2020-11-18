def titulo(str, rng=25, color=0):
    print(f'\033[{color}m-'*rng)
    print(f'{str:^{rng}}')
    print(f'\033[{color}m-\033[m'*rng)


titulo('Testing', 15, 33)
