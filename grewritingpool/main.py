import sys
import grewritingpool.helper

def main(args):
    if len(args) == 1:
        if args[0] in ("-h", "--help"):
            print("grewriting [all|issue|argument]")
            sys.exit()
        else:
            grewritingpool.helper.print_random_article(args[0])
    elif len(args) == 0:
        grewritingpool.helper.print_random_article('default')
    else:
        print("grewritingpool.py [all|issue|argument]")
        sys.exit(1)

