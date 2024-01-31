import argparse

def get_signed_rpm_signature(rpm):
    print("Getting the signature of the RPM package")
    if not os.path.exists(args.rpm):
        print(f"RPM package {args.rpm} does not exist")
        return 1


def upload_rpm_signature(rpm, rekor, key):
    rpm_signature = get_signed_rpm_signature(rpm):
    if rpm_signature == None:
        return 1

    print("Uploading the signature of the RPM package")
    return 0

def verify_rpm_signature(rpm, rekor, key):
    print("Verifying the signature of the RPM package")
    return 0

def parse_args(argv):
    parser = argparse.ArgumentParser(description="A tool for uploading and verifying RPM package signatures using Sigstore")
    parser.add_argument("command", help="The command to execute", choices=["upload", "verify"])
    parser.add_argument("-r", "--rpm", help="Path to the RPM package", required=True)
    parser.add_argument("-s", "--rekor", help="The Rekor server to use", default="https://rekor.sigstore.dev")
    parser.add_argument("-k", "--key", help="Path to the key that matches the RPM signature", required=True)
    return parser.parse_args(argv[1:])

def main(argv):
    parse_args(argv)
    if args.command == "upload":
        return upload_rpm_signature(args.rpm, args.rekor, args.key)
    elif args.command == "verify":
        return verify_rpm_signature(args.rpm, args.rekor, args.key)
    else:
        print(f"Unknown command {args.command}")
    return 0

if __name__ == "__main__":
    import sys
    sys.exit(main(sys.argv))
