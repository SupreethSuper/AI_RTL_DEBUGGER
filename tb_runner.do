#clean any prev runs
#run command -> vsim -do tb_runner.do
# 1. Stop the current simulation
quit -sim;

# 2. Delete the old work library if it exists to clear stale compiled files
if [file exists work] {
    vdel -all -lib work
}

# 3. Create a fresh library
vlib work
vmap work work

# ... proceed with vlog and vsim
#compile all files
vlog -sv input_buffer.sv;
vlog -sv tb_input_buffer.sv;

#invoking testbench


vsim work.tb_input_buffer

#view waves
add wave -r *;

run -all;
onfinish exit; # to acknowledge finish



