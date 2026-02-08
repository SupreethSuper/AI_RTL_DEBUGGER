# administrator.py
# This code does not run AI

import os
import time
from transcript_reader import get_final_error_count
from main import main as contents
from AI_handler import AI_handler as gemini_prompts
from design_writer import design_writer
from file_handlers import tb_path as path_to_testbench
from file_handlers import design_path as path_to_design

test_bench_runner_do_file_path = r"tb_runner.do"

class Main:
    def __init__(self):
        self.startup_flag = False
        self.startup_loop_counter = -1
        self.error_counts = get_final_error_count()
        self.design_valid = True


    def startup(self):
        os.system("cls")
        os.system("echo Welcome to the AI RTL Debugger!")
        time.sleep(3)
        os.system("cls")

        # self.startup_flag = True
        # self.startup_loop_counter += 1

        if (self.design_valid == False):
            self.parse_design()

        self.main_runner()

    def main_runner(self):
        if not self.startup_flag:
            self.error_state()
        else:
            os.system(f'''vsim -c -do "do {test_bench_runner_do_file_path}; quit -f''')

    def error_state(self):
        os.system("echo There has been an error in the startup process. Restarting...")
        self.startup_loop_counter += 1
        if(self.startup_loop_counter > 2):
            os.system("cls")
            os.system("echo Too many errors. Exiting. Contact the developer.")
            exit(1)
        time.sleep(2)
        self.startup()
    
    def parse_design(self):
        os.system("cls")
        os.system("echo handing over to the AI to design it")

        sv_text = gemini_prompts(contents())  # <-- must return SV code as a string
        gen_design_path = path_to_design()
        out_path = design_writer(gen_design_path, sv_text, mode="atomic")

        print(f"[OK] Wrote design to: {out_path}")
        self.design_valid = True
        self.startup()




if __name__ == "__main__":
    app = Main()
    app.startup()
