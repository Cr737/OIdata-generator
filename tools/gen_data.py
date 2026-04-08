import argparse

from genoirator.base_genoirator import BaseGenoirator, VectorGenoirator
from genoirator.utils.io_utils import register_io


def parse_args():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument(
        "--save_dir",
        type=str,
        default="/tmp/test_io",
        help="dir to store data, default set to /tmp/test_io",
    )
    arg_parser.add_argument(
        "--case_num", type=int, default=1, help="number of test cases, default set to 1"
    )
    arg_parser.add_argument(
        "--index_start_with_zero",
        action="store_true",
        help="if enable, test_case id starts with 0",
    )
    arg_parser.add_argument(
        "--input_suffix",
        type=str,
        default=".in",
        help="suffix of input file, default set to .in",
    )
    arg_parser.add_argument(
        "--output_suffix",
        type=str,
        default=".out",
        help="suffix of output file, default set to .out",
    )
    arg_parser.add_argument(
        "--std_path", type=str, required=True, help="standard executor path"
    )
    args = arg_parser.parse_args()
    return args


def gen_one_case(case_id, args):
    input_suffix = args.input_suffix
    output_suffix = args.output_suffix
    save_dir = args.save_dir
    std = args.std_path
    io = register_io(
        save_dir=save_dir,
        case_id=case_id,
        input_suffix=input_suffix,
        output_suffix=output_suffix,
    )
    gen = BaseGenoirator(1, "/tmp/a.out")
    data = gen.gen()
    print(data)
    io.input_writeln(data)
    io.output_gen(std)
    io.close()


if __name__ == "__main__":
    args = parse_args()
    T = args.case_num
    case_id = 0 if args.index_start_with_zero else 1
    for i in range(T):
        gen_one_case(case_id, args)
        case_id += 1
