import sys

def main(argv):
    if ( len(argv) != 4 ):
        print ("Usage: python config.py --command=<command> --script=<vpnc-script> --address=<vpn-adress> --out=<outfile>")
        return 1

    command = ""
    script = ""
    address = ""
    out = ""
    for arg in argv:
        if ( arg.find("--command=") != -1 ):
           command = arg.split("--command=")[1]
        elif ( arg.find( "--script=" ) != -1 ):
            script = arg.split("--script=")[1]
        elif ( arg.find("--address=") != -1 ):
            address = arg.split("--address=")[1]
        elif ( arg.find("--out=") != -1 ):
            out = arg.split("--out=")[1]

    # Consistency check
    if ( command == "" ):
        print ("No command specified...")
        return 1
    elif ( script == "" ):
        print ("No script specified...")
        return 1
    elif ( address == "" ):
        print ("No address specified...")
        return 1
    elif ( out == "" ):
        print ("No outfile specified...")
        return 1

    os = open( out, "w" )
    os.write("# Generated with: python --command=%s --script=%s --address=%s --out=%s\n"%(command, script, address, out))
    os.write("%s --script=%s %s\n"%(command, script, address))
    os.close()
    print ("Created command file %s"%(out))
    
    # Add to the gitignore file
    ignore = open( ".gitignore", "a" )
    ignore.write("%s\n"%(out)) 
    ignore.close()

if __name__ == "__main__":
    main(sys.argv[1:])
