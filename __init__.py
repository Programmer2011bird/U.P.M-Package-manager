import installDir
import argparse



parser: argparse.ArgumentParser = argparse.ArgumentParser()

parser.add_argument("--install", help="installs the specified package", type=str)
parser.add_argument("--decompress", help="decompresses the whl or tgz file", type=str)
parser.add_argument("--js", help="Used with --install, downloads a javascript package", action="store_true")
parser.add_argument("--py", help="Used with --install, downloads a python package", action="store_true")
args = parser.parse_args()

if (args.install and not args.js) or (args.install and args.py):
    parser.error("--py or --js is needed when using --install")

if (args.decompress and not args.js) or (args.decompress and args.py):
    parser.error("--py or --js is needed when using --decompress")

if args.install:
    packageName: str = str(args.install)
    
    if args.py:
        installDir.install_PIP(packageName)
    
    if args.js:
        installDir.install_NPM(packageName)

if args.decompress:
    packageName: str = str(args.decompress)
    
    if args.py:
        installDir.decompress_PIP_packages(packageName)
    
    if args.js:
        installDir.decompress_NPM_packages(packageName)
