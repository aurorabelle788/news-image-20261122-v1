import os
import shutil

# Copy the pre-built entry image to the grader's output directory.
# Standard library only: the grader installs nothing before it runs.
out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
src = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
dst = os.path.join(out_dir, "entry.png")
shutil.copyfile(src, dst)
