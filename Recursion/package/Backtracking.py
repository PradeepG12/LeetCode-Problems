
def generate_binary_strings(n, path):
    if n == len(path):
        print(path)
        return
    
    generate_binary_strings(n, path + "0")
    
    generate_binary_strings(n, path + "1")
