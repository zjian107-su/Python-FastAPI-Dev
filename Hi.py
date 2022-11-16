import sys
print("Python version")
print (sys.version)
print("Version info.")
print (sys.version_info)

a = {
    "name": "Daniel",
    "age": "27"
}
for key, value in a.items():
    print(key, value)