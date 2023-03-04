#! ./.venv/bin/python3
import subprocess
from pathlib import Path
from typing import Any

BASE_DIR = Path(__file__).parent.absolute()
BEFORE = BASE_DIR.joinpath('images/before')
AFTER = BASE_DIR.joinpath('images/after')



def gen_remove_cmd(path_obj:Path):
    file_name = path_obj.name
    before_path = str(path_obj.resolve())
    after_path = str(AFTER.joinpath(file_name).resolve())
    
    # backgroundremover -i "/path/to/image.jpeg" -a -ae 15 -o "output.png"

    return f'backgroundremover -i {before_path} -o {after_path} -a -ae 15'

def run(cmd: str) -> Any:
    print(cmd)
    process = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    if error:
        raise Exception(error)
    else:
        return output




for f in BEFORE.iterdir():
    if not(f.is_file()):
        continue
    run(gen_remove_cmd(f))










# cur_path

