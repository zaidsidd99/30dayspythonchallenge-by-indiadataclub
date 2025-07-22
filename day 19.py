# import time
# import threading
# def caculating_square (numbers):
#     print ("calculate square numbers")
#     for n in numbers:
#         time.sleep(0.2)
#         print('square:',n*n)


# def caculating_cube (numbers):
#     print ("caulate cube of numbers")
#     for n in numbers:
#         time.sleep (0.2)
#         print ('cube:',n*n*n)


# arr= [2,3,7,9]

# t =time.time()
# t1=threading.Thread(target=caculating_square, args=(arr,))
# t2=threading.Thread(target=caculating_cube, args=(arr,))

# t1.start()
# t2.start()

# t1.join()
# t2.join()

# print ("done in :",time.time()-t)




# Download multiple files concurrently using threads ?

import threading
import time

# Simulated URLs (just names for demo)
files = ['file1.txt', 'file2.txt', 'file3.txt']

def fake_download(file_name):
    print(f"Starting download: {file_name}")
    time.sleep(2)  # simulate time delay for download
    with open(file_name, 'w') as f:
        f.write("This is a downloaded file: " + file_name)
    print(f"Downloaded: {file_name}")

threads = []

for file in files:
    thread = threading.Thread(target=fake_download, args=(file,))
    thread.start()
    threads.append(thread)

# Wait for all to finish
for thread in threads:
    thread.join()

print("All downloads simulated.")
