if __name__ == "__main__":
    import sys

    from dotslash import locate

    dotslash = locate()

    if sys.platform == "win32":
        import subprocess

        process = subprocess.run([dotslash, *sys.argv[1:]])
        sys.exit(process.returncode)
    else:
        import os

        os.execvp(dotslash, [dotslash, *sys.argv[1:]])
