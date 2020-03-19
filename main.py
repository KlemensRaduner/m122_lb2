import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-d", "--Directory", required=True,
                help="Directory where the files will be copied to")
ap.add_argument('-l', '--list', action='append',
                help='<Required> Set flag', required=True)


args = vars(ap.parse_args())


print(args)
