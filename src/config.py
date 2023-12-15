import sys
from pathlib import Path
from build import RESOURCE_FOLDER

is_development: bool = False

if getattr(sys, 'frozen', False):
    is_development = False
else:
    is_development = True

resource_path: str = None
if is_development:
    resource_path = (Path(__file__).parent / "nsuda_client" / "resource").absolute().as_posix()
else:
    resource_path = (Path(__file__).parent / RESOURCE_FOLDER).absolute().as_posix()

window_width = 500
window_height = 400

input_field_width = 350
