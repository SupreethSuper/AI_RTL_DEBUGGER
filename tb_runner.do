#clean any prev runs
#run command -> vsim -do tb_runner.do
quit -sim;

#make a work library
vlib work;
vmap work work;

#compile all files
vlog -sv buffer;
vlog -sv tb_buffer_params;

#invoking testbench

vsim work.tb_buffer_params;


#view waves
add wave -r *;

run -all;
onfinish exit; # to acknowledge finish



