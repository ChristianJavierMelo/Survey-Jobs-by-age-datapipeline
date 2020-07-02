import argparse
from p_acquisition import m_acquisition as acq
from p_wrangling import m_wrangling as wrang
from p_analysis import m_analysis as anal
from p_reporting import m_reporting as rep


def argument_parser():
    parser = argparse.ArgumentParser(description='specify input file')
    parser.add_argument("-p", "--path",
                        type=str,
                        help='specify the path of the file .db',
                        required=True)
    parser.add_argument("-c", "--country",
                        type=str,
                        default='all',
                        choices=valid_countries,
                        help='select a specific country showed on the list named valid_countries')

    args = parser.parse_args()
    return args


def main(args):
    print('starting the analysis procedure...')
    all = acq.getall(args.path)
    moreall = wrang.wrangling(all)
    #report = anal.grouptable(moreall, args.country)
    #print(rep.plot_returns(report))
    print(anal.grouptable(moreall, args.country))
    print('pipeline finished')


if __name__ == '__main__':
    valid_countries = ['Austria', 'Belgium', 'Bulgaria', 'Cyprus', 'Czechia', 'Germany',
                       'Denmark', 'Estonia', 'Spain', 'Finland', 'France',
                       'UnitedKingdom', 'Greece', 'Croatia', 'Hungary', 'Ireland',
                       'Italy', 'Lithuania', 'Luxembourg', 'Latvia', 'Malta',
                       'Netherlands', 'Poland', 'Portugal', 'Romania', 'Sweden',
                       'Slovenia', 'Slovakia', 'all']
    arguments = argument_parser()
    main(arguments)
