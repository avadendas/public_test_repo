import os 

thisDir = os.path.dirname(__file__)
thisDir = os.path.abspath(thisDir)

print("I am a file in %s\n" %(thisDir))
