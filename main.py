import time
import os

# os.system("cls") #clear the console


# init_print = '''Welcome to AI RTL Debugger!
# This tool is designed to assist you in debugging your RTL code using AI.
# Please note that this tool is in its early stages of development, and may not be fully functional yet.
# This tool uses Google Gemini LLM to analyze the transcript of your ModelSim simulation and provide insights and suggestions for debugging.
# and hence, the output may not be accurate. I hope, that you are a developed, who is using it.
# As you are a developer, please make sure that the file path to your test bench, or your design is correct'''

# print(init_print)
# time.sleep(3)
# print("Now you will be prompted to enter your request.")

def main():

    default_test_request = '''Build a buffer module in systemverilog. The test bench is already present, and will not be given to you.
    I am proving you with the skeleton the design, can you do it?

    `include "GATE_PARAMS.vh"

    module buffer #(parameter WIDTH = NUM_GATES)(
        input  logic [WIDTH-1:0] din,
        output logic [WIDTH-1:0] dout
    );
        
    endmodule

    Just write the code, do not explain anything, not even any sort of em-dashes, just the code, nothing else
    not even this:
    ```systemverilog or

    ``` at the end of code, this code is being directly fed to a compiler, so hence, any extra text, `, or any explaination will 
    push it to failure, just write the code, nothing else, dont even put any types of guards. no extras - this is a 
    strict instruction.
    '''

    return (default_test_request)

