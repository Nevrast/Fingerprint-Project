import argparse

from fingerprint_creating import fing_creat

parser = argparse.ArgumentParser(description="This is a script which provides information about quality degradation level in chosen signal. User indicates the reference signal (first argument) and the measured signal (second argument).")

parser.add_argument("reference", help="- reference signal")
parser.add_argument("input", help="- input signal")
parser.add_argument("-o", "--output", help="- output file")
parser.add_argument("-d", "--debug", help="- debugging mode, this argument is called without any value", default=False, action='store_true')

args = parser.parse_args()

REFERENCE_PATH = args.reference
INPUT_PATH = args.input
if args.output:
    OUTPUT_PATH =args.output

if args.debug:
    print("Input file: ", INPUT_PATH)
    print("Reference file: ", REFERENCE_PATH)
    if args.output:
        print("Reference file: ", OUTPUT_PATH)

def diff_counting(ref, input):
    ref_fing = fing_creat(ref)
    input_fing = fing_creat(input)

#wywołanie funkcji
diff_counting(REFERENCE_PATH, INPUT_PATH)
