import argparse
import re


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Calculate numbers of tandems and percentage of genome.")
    parser.add_argument("-i", "--input", help="Input gff file", required=True)
    parser.add_argument("--genome_size", "-s", help="Expected genome size", required=True)
    args = vars(parser.parse_args())

    gff_file = args["input"]
    genome_size = int(args["genome_size"])

    num_tr = 0
    len_all_tr = 0
    with open(gff_file, "r") as file:
        for num_tr, line in enumerate(file):
            num_tr += 1
            str_len = re.findall("length=\d+", line)
            num_len = re.findall("\d+", str_len[0])
            len_all_tr += int(num_len[0])
    perc_tr = (len_all_tr / genome_size) * 100
    print('N repeat tandems -', num_tr)
    print('repeats of genome -', "{:.2f}".format(perc_tr), "%")