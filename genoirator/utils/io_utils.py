import os
from typing import Optional

from cyaron import IO


def register_io(save_dir, case_id, skip_if_exist, **kwargs) -> Optional[IO]:
    input_file = os.path.join(save_dir, f"{case_id}.in")
    output_file = os.path.join(save_dir, f"{case_id}.out")
    if os.path.exists(input_file):
        return None
    io = IO(input_file, output_file, case_id, **kwargs)
    return io
