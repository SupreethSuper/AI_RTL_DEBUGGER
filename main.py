import time
import os

os.system("cls") #clear the console



# This tool is designed to assist you in debugging your RTL code using AI.
# Please note that this tool is in its early stages of development, and may not be fully functional yet.
# This tool uses Google Gemini LLM to analyze the transcript of your ModelSim simulation and provide insights and suggestions for debugging.
# and hence, the output may not be accurate. I hope, that you are a developed, who is using it.
# As you are a developer, please make sure that the file path to your test bench, or your design is correct'''

# print(init_print)
# time.sleep(3)
# print("Now you will be prompted to enter your request.")

def main():

    default_test_request = '''
    
    The pdf file is the test plan, you need to stritly adhere to it

'''
    return default_test_request


def dump():
    vcd_dump = "dump vcd files in the testbench" #optional   
    return vcd_dump

def end_statement():
    end_statement = '''Just write the code, do not explain anything, not even any sort of em-dashes, just the code, nothing else
    not even this:
    ```systemverilog or

    ``` at the end of code, this code is being directly fed to a compiler, so hence, any extra text, `, or any explaination will 
    push it to failure, just write the code, nothing else, dont even put any types of guards. no extras - this is a 
    strict instruction. not even 1 line of explaining is tolerated, and its highly prohibited, only sv test code'''
    return end_statement


def plans():
    text = '''
    
    module input_buffer(

    input logic a,
    output logic b

);


this is the design code, you need to create a testbench called as tb_input_buffer;
    '''
    return text
def combiner():

    dumper = dump()
    ender = end_statement()
    code_plans = plans()
    pdf_runner = main()
    # return (code_plans + dumper + ender)

    return (code_plans + ender)

