import os

PRJDIR = '/Users/zhuzihui/Pycharm/toolkit'
DATADIR = os.path.join(PRJDIR, 'data')



if __name__ == "__main__":
    import os
    import toolkit_config as cfg
    tic = 'QAN.AX'
    pth = os.path.join(cfg.DATADIR, 'qan_stk_prc.csv')
    yf_prc_to_csv(tic, pth)