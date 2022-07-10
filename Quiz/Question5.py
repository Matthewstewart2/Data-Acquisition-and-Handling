import numpy as np
import matplotlib.pyplot as plt


def main():
    # set input mean, mu, and standard deviation, sigma
    mu = 6
    sigma = 2
    variance = sigma**2

    # 10000 gaussian/normal distributed samples using input parameters above
    samples = np.random.normal(mu, sigma, 10000)
    # histogram with 50 bins
    hist = plt.hist(samples, bins=50)

    plt.xlabel('x')
    plt.ylabel('Frequency')
    plt.show()

    # chosen input values
    print(f'Input mean = {mu}, Input variance = {variance}')
    # estimated mean and variance of random samples to compare
    print(f'Estimated mean = {samples.mean()}, Estimated variance = {samples.var()}')


main()
