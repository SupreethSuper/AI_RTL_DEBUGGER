# administrator.py
# This code does not run AI

import os
import time

test_bench_runner_do_file_path = r"tb_runner.do"

class Main:
    def __init__(self):
        self.startup_flag = False
        self.startup_loop_counter = -1

    def startup(self):
        os.system("cls")
        os.system("echo Welcome to the AI RTL Debugger!")
        time.sleep(3)
        os.system("cls")

        self.startup_flag = True
        self.startup_loop_counter += 1

        self.main_runner()

    def main_runner(self):
        if not self.startup_flag:
            self.error_state()
        else:
            os.system(f"vsim -do {test_bench_runner_do_file_path}")

    def error_state(self):
        os.system("echo There has been an error in the startup process. Restarting...")
        time.sleep(2)
        self.startup()


if __name__ == "__main__":
    app = Main()
    app.startup()
