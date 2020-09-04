import subprocess


def convert(inputFileName, outputFileName):
    result = subprocess.run(
        ['ddjvu', '-quality=60', '-format=pdf', inputFileName, outputFileName, ])
    return result.args[-1]
