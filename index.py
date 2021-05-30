import argparse
import glob
import sys
import errno
from utils import translationService

# def str2bool(v):
#     if isinstance(v, bool):
#         return v
#     if v.lower() in ('yes', 'true', 't', 'y', '1'):
#         return True
#     elif v.lower() in ('no', 'false', 'f', 'n', '0'):
#         return False
#     else:
#         raise argparse.ArgumentTypeError('Boolean value expected.')

# parser = argparse.ArgumentParser(description="Dry run will not call APIs and directly export untranslated text to output")
# parser.add_argument('-d', type=str2bool, nargs='?', const=True, default=False, help='Do a dryrun without any API calls or translations')
# args = parser.parse_args()
# print(args.dryrun)

dryrunFlag = True


path = './input/*.txt'
files=glob.glob(path)
for name in files: # 'file' is a builtin type, 'name' is a less-ambiguous variable name.
    try:
        print(name)
        outputarr = name.split("/")
        outputarr[1] = 'output'
        outputpath = '/'.join(outputarr)
        with open(name) as f: # No need to specify 'r': this is the default.
            content = f.read()
            f.close()
            print(content)
            if (dryrunFlag):
                translation = content
            else:
                translation = translationService.translate_text('en', content)
            w=open(outputpath, 'w')
            w.write(translation)
            w.close()
    except IOError as exc:
        if exc.errno != errno.EISDIR: # Do not fail if a directory is found, just ignore it.
            raise # Propagate other kinds of IOError.
