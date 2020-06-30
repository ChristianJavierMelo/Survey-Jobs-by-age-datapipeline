import argparse
from p_acquisition import m_acquisition as acq
from p_wrangling import m_wrangling as wrang

def argument_parser():

    parser = argparse.ArgumentParser(description='specify input file')
    parser.add_argument("-p", "--path", type=str, help='specify .db database path', required=True)
    # parser.add_argument("-c", "--country", type=str, help='specify country involved', required=False)
    args = parser.parse_args()
    return args

def main(args):
    print('starting data analysis process...')
    all = acq.getall(args.path)
    print(wrang.wrangling(all))
    print('pipeline finished')

if __name__ == '__main__':
    arguments = argument_parser()
    main(arguments)