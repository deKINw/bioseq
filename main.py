from seqbio.calculation.SeqCal import *
from seqbio.pattern.SeqPattern import *
from seqbio.seqMan.dnaconvert import *
# print("in Main.py")

def argparserLocal():
    from argparse import ArgumentParser
    '''Argument parser for the commands'''
    parser = ArgumentParser(prog='myseq', description='Work with sequence')

    subparsers = parser.add_subparsers(
        title='commands', description='Please choose command below:',
        dest='command'
    )
    subparsers.required = True

    cgc_command = subparsers.add_parser('gcContent', help='Calculate GC content')
    cgc_command.add_argument("-s", "--seq", type=str, default=None, dest='seq',
                             help="Provide sequence")

    count_command = subparsers.add_parser('countBases', help='Count number of each base')
    count_command.add_argument("-s", "--seq", type=str, default=None, dest='seq',
                             help="Provide sequence")
    count_command.add_argument("-r","--revcomp", default=None, action='store_true',
                                help="Convet DNA to reverse-complementary")
    
    scan_command = subparsers.add_parser('enzTargetsScan', help='Find restriction enzyme')
    scan_command.add_argument("-s", "--seq", type=str, default=None, dest='seq',
                             help="Provide sequence")
    scan_command.add_argument("-e", "--ENZ", type=str, dest='enz',
                             help="Provide sequence")
    scan_command.add_argument("-r","--revcomp", default=None, action='store_true',
                                help="Convet DNA to reverse-complementary")

    transcrip_command = subparsers.add_parser('transcription', help='Convert DNA->RNA')
    transcrip_command.add_argument("-s", "--seq", type=str, default=None, dest='seq',
                             help="Provide sequence")
    transcrip_command.add_argument("-r","--revcomp", default=None, action='store_true',
                                help="Convet DNA to reverse-complementary")

    translation_command = subparsers.add_parser('translation', help='Convert DNA->Protein')
    translation_command.add_argument("-s", "--seq", type=str, default=None, dest='seq',
                             help="Provide sequence")
    translation_command.add_argument("-r","--revcomp", default=None, action='store_true',
                                help="Convet DNA to reverse-complementary")




    parser.print_help()
    return parser

def test():
    # Input
    parser = argparserLocal()
    args = parser.parse_args(["cpgScan","-s","AAATTTCCCGGGCGGGGG"])
    print(args)
    print(cpgSearch(args.seq))
    
def main():
    parser = argparserLocal()
    args = parser.parse_args()

    print(args)

    if args.command == 'gcContent':
        if args.seq == None:
            exit(parser.parse_args(['gcContent','-h']))
        seq = args.seq.upper()
        print("Input",args.seq,"\nGC content =", gcContent(seq) )

    elif args.command == 'countBases':
        if args.seq == None:
            exit(parser.parse_args(['countBases','-h']))
        seq = args.seq.upper()
        if args.revcomp == True :
            rev = reverseComplementSeq(seq)
            print("Input",args.seq,"\ncountBases =", countBasesDict(rev) )
        else:
            print("Input",args.seq,"\ncountBases =", countBasesDict(seq) )

    elif args.command == 'transcription':
        if args.seq == None:
            exit(parser.parse_args(['transcription','-h']))
        seq = args.seq.upper()
        if args.revcomp == True :
            rev = reverseComplementSeq(seq)
            print("Input",args.seq,"\ntranscriptions =", dna2rna(rev) )
        else:
            print("Input",args.seq,"\ntranscriptions =", dna2rna(seq) )


    elif args.command == 'translation':
        if args.seq == None:
            exit(parser.parse_args(['translation','-h']))
        seq = args.seq.upper()
        if args.revcomp == True :
            rev = reverseComplementSeq(seq)
            print("Input",args.seq,"\ntranscriptions =", dna2protein(rev) )
        else:
            print("Input",args.seq,"\ntranscriptions =", dna2protein(seq) )


    elif args.command == 'enzTargetsScan':
        if args.seq == None:
            exit(parser.parse_args(['enzTargetsScan','-h']))
        seq = args.seq.upper()
        enz = args.enz
        if args.revcomp == True :
            rev = reverseComplementSeq(seq)
            print("Input",args.seq,"\nenzTargetsScan =", enzTargetsScan(rev, enz) )
        else:
            print("Input",args.seq,"\nenzTargetsScan =", enzTargetsScan(seq, enz) )
        
     

# print(__name__)
if __name__ == "__main__":
    #test()
    main()



