import pickle

infile = open("names_pickle_file_write.dat", "rb")

names = pickle.load(infile)

print(type(names))

print(names)

name = input("Add a name to the list: ")
names.append(name)

print(names)

infile.close()

outfile = open("names_pickle_file_write.dat", "wb")

pickle.dump(names, outfile)

outfile.close()
