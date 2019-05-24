import argparse
from scipy.spatial import minkowski_distance
from fingerprint_creating import fing_creat

parser = argparse.ArgumentParser(description="This is a script which provides information about quality"
                                             " degradation level in chosen signal. User indicates the reference signal"
                                             " (first argument) and the measured signal (second argument).")

parser.add_argument("reference", help="- reference signal")
parser.add_argument("input", help="- input signal")
parser.add_argument("-o", "--output", help="- output file")
parser.add_argument("-d", "--debug", help="- debugging mode, this argument is called without any value", default=False,
                    action='store_true')

args = parser.parse_args()

REFERENCE_PATH = args.reference
INPUT_PATH = args.input
if args.output:
    OUTPUT_PATH = args.output

if args.debug:
    print("Input file: ", INPUT_PATH)
    print("Reference file: ", REFERENCE_PATH)
    if args.output:
        print("Reference file: ", OUTPUT_PATH)


def diff_counting(ref, input):
    ref_fing_l, input_fing_r = fing_creat(ref)
    input_fing_l, ref_fing_r = fing_creat(input)
    print(ref_fing_l.shape, input_fing_l.shape)
    print(ref_fing_r.shape, input_fing_r.shape)
    dst = minkowski_distance(ref_fing_l, input_fing_l)
    dst2 = minkowski_distance(ref_fing_r, input_fing_r)
    print(dst, dst2)


#wywołanie funkcji
diff_counting(REFERENCE_PATH, INPUT_PATH)
