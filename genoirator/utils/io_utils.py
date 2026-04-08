import os

from cyaron import IO


def register_io(save_dir, case_id, **kwargs) -> IO:
    input_file = os.path.join(save_dir, f"{case_id}.in")
    output_file = os.path.join(save_dir, f"{case_id}.out")
    io = IO(input_file, output_file, case_id, **kwargs)
    return io
