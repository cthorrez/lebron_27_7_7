import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy.stats import norm
import os
from collections import Counter
from scipy.stats import multivariate_normal
from scipy.stats import mvn




matplotlib.rcParams.update({'font.size': 12})


def main():
    df = pd.read_csv(os.path.join('data','log.csv'), index_col=None)
    pts = df['pts']
    trb = df['trb']
    ass = df['ass']

    pts_mean = pts.mean()
    pts_sd = pts.std()
    trb_mean = trb.mean()
    trb_sd = trb.std()
    ass_mean = ass.mean()
    ass_sd = ass.std()

    print('points mean:', pts_mean, 'variance:', np.power(pts_sd,2), 'stdev:', pts_sd)
    print('rebounds mean:', trb_mean, 'variance:', np.power(trb_sd,2), 'stdev:', trb_sd)
    print('assists mean:', ass_mean, 'variance:', np.power(ass_sd,2), 'stdev:', ass_sd)


    pts_cnt = Counter(pts)
    pts_x = list(pts_cnt.keys())
    pts_y = [pts_cnt[x] for x in pts_x]
    pts_norm_x = np.arange(np.min(pts), np.max(pts), 0.001)

    trb_cnt = Counter(trb)
    trb_x = list(trb_cnt.keys())
    trb_y = [trb_cnt[x] for x in trb_x]
    trb_norm_x = np.arange(np.min(trb), np.max(trb), 0.001)

    ass_cnt = Counter(ass)
    ass_x = list(ass_cnt.keys())
    ass_y = [ass_cnt[x] for x in ass_x]
    ass_norm_x = np.arange(np.min(ass), np.max(ass), 0.001)

    plt.figure(1)
    plt.xlabel('number of points')
    plt.ylabel('number of games')
    plt.scatter(pts_x,pts_y)
    plt.xticks([5*x for x in range(14)])
    plt.plot(pts_norm_x, 1143*norm.pdf(pts_norm_x,pts_mean,pts_sd))
    plt.savefig(os.path.join('figures', 'points.jpg'))

    plt.figure(2)
    plt.xlabel('number of rebounds')
    plt.ylabel('number of games')
    plt.scatter(trb_x,trb_y)
    plt.xticks([x for x in range(22)])
    plt.plot(trb_norm_x, 1143*norm.pdf(trb_norm_x,trb_mean,trb_sd))
    plt.savefig(os.path.join('figures', 'rebounds.jpg'))

    plt.figure(3)
    plt.xlabel('number of assists')
    plt.ylabel('number of games')
    plt.scatter(ass_x,ass_y)
    plt.xticks([x for x in range(22)])
    plt.plot(ass_norm_x, 1143*norm.pdf(ass_norm_x,ass_mean,ass_sd))
    plt.savefig(os.path.join('figures', 'assists.jpg'))


    #multivariate gaussian stuff
    data = np.array(df.iloc[:,1:4])
    mu = np.mean(data, axis=0)
    sigma = np.cov(data, rowvar=0)

    print(sigma)


    fx = multivariate_normal.pdf([27,7,7], mu, sigma)
    print(fx)

    low = np.array([26.5,6.5,6.5])
    high = np.array([27.5,7.5,7.5])

    p,_ = mvn.mvnun(low,high,mu,sigma)
    print(p)







if __name__ == '__main__':
    if not os.path.exists('figures'):
        os.mkdir('figures')
    main()