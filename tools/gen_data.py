import argparse
import os

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
        "--skip_if_exist",
        action="store_true",
        help="if enable, skip the case already generated",
    )
    arg_parser.add_argument(
        "--std_path", type=str, required=True, help="standard executor path"
    )
    args = arg_parser.parse_args()
    return args


def gen_one_case(case_id, args):
    print(f"Case #{case_id}:")
    input_suffix = args.input_suffix
    output_suffix = args.output_suffix
    skip_if_exist = args.skip_if_exist
    save_dir = args.save_dir
    std = args.std_path
    io = register_io(
        save_dir=save_dir,
        case_id=case_id,
        skip_if_exist=skip_if_exist,
        input_suffix=input_suffix,
        output_suffix=output_suffix,
    )
    if io is None:
        print(f"Case #{case_id} already exists, skip.")
        return
    try:
        gen = BaseGenoirator(2, std)
        n, k = gen.gen()
        print(n, k)
        io.input_writeln(n, k)
        gen = VectorGenoirator(1, std)
        data = gen.gen()
        for line in data:
            line = [-1 if _ < 0 else _ for _ in line]
            assert len(line) == n
            io.input_writeln(line)
        io.output_gen(std)
        io.close()
    except Exception as e:
        print(f"generate data failed {e}")
        if io.input_filename is not None:
            os.remove(io.input_filename)
        if io.output_filename is not None:
            os.remove(io.output_filename)


if __name__ == "__main__":
    args = parse_args()
    T = args.case_num
    case_id = 0 if args.index_start_with_zero else 1
    for i in range(T):
        gen_one_case(case_id, args)
        case_id += 1
