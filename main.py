from Cov import Cov
from longestPeriod import longestPeriod as lp

def main():
    coverages = [Cov(1, 20), Cov(21, 30), Cov(15, 25), Cov(28, 40), Cov(50, 60), Cov(61, 200)]
    time = lp(coverages)
    print(time)


if __name__ == "__main__":
    # execute only if run as a script
    main()