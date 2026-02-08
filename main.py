import time
import os

os.system("cls") #clear the console


init_print = '''Welcome to AI RTL Debugger!
This tool is designed to assist you in debugging your RTL code using AI.
Please note that this tool is in its early stages of development, and may not be fully functional yet.
This tool uses Google Gemini LLM to analyze the transcript of your ModelSim simulation and provide insights and suggestions for debugging.
and hence, the output may not be accurate. I hope, that you are a developed, who is using it.
As you are a developer, please make sure that the file path to your test bench, or your design is correct'''
print(init_print)
time.sleep(3)
print("Now you will be prompted to enter your request.")

