import argparse
from p_acquisition import m_acquisition as acq
from p_wrangling import m_wrangling as wrang
from p_analysis import m_analysis as anal

def argument_parser():

    parser = argparse.ArgumentParser(description='specify input file')
    parser.add_argument("-p", "--path", type=str, help='specify .db database path', required=True)
    parser.add_argument("-c", "--country", type=str, default='all', help='select a country involved on this list: ')
    args = parser.parse_args()
    return args

def main(args):
    print('starting data analysis process...')
    all = acq.getall(args.path)
    moreall = wrang.wrangling(all)
    print(anal.grouptable(moreall, args.country))
    print('pipeline finished')

if __name__ == '__main__':
    valid_countries = []
    arguments = argument_parser()
    main(arguments)