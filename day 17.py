class SafeFile:
    def __init__(self, name, mode):
        self.name = name
        self.mode = mode

    def __enter__(self):
        self.file = open(self.name, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()

# Run this part
if __name__ == "__main__":
    with SafeFile("myfile.txt", "w") as f:
        f.write("This is safe file handling.")
    print("File written successfully!")

