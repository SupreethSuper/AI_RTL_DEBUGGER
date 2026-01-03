#clean any prev runs

quit -sim;

#make a work library
vlib work;
vmap work work;

#compile all files
vlog -sv buffer.sv;
vlog -sv tb_buffer_params.sv;

#invoking testbench

vsim work.tb_buffer_params;


#view waves
add wave -r *;

run -all;



