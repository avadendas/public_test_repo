import os 

thisDir = os.path.dirname(__file__)
thisDir = os.path.abspath(thisDir)

print("Hello from %s\n" %(thisDir))
