import argparse
import sys
from nac_ise.import_matrix import Matrix

def main():
    parser = argparse.ArgumentParser()

    subparsers = parser.add_subparsers(dest='command', help='commands help')

    import_parser = subparsers.add_parser('import-matrix', help='Import matrix from an input file and export to an output file')
    import_parser.add_argument('--input', type=str, required=True, help="Input xlsx file")
    import_parser.add_argument('--output', type=str, required=True, help="Output file")
    import_parser.add_argument('--sgt-start-value', type=int, default=1000, help="SGT start value")

    args = parser.parse_args()

    if args.command == 'import-matrix':
        Matrix.import_matrix(args.input, args.output, args.sgt_start_value)
    else:
        # Code to run when export-matrix command is used
        pass

    if len(sys.argv)==1:
        parser.print_help(sys.stderr)
        sys.exit(1)

    args = parser.parse_args()
    if args.input:
        Matrix.import_matrix(args.input, args.output, args.sgt_start_value)

if __name__ == "__main__":
    main()
