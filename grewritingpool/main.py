import sys
import grewritingpool.fetch

def main(args):
    if len(args) == 1:
        if args[0] in ("-h", "--help"):
            print("grewritingpool.py [all|issue|argument]")
            sys.exit()
        else:
            grewritingpool.fetch.download_pool(args[0])
    else:
        print("grewritingpool.py [all|issue|argument]")
        sys.exit(1)

if __name__ == "__main__":
    main(sys.argv[1:])