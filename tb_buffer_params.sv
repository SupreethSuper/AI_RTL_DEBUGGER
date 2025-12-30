`timescale 1ns/1ns


module tb_buffer_params;

    // `include "GATE_DEFINES.vh"
    `include "GATE_PARAMS.vh"

    localparam GATE_NUMS = NUM_GATES;

    // PARAMETERIZED INPUTS
    logic [GATE_NUMS-1:0] input_a;
    logic [GATE_NUMS-1:0] output_c;

    // Clock
    logic clock;

    // Clock generator
    initial clock = 0;
    always #2 clock = ~clock; // 250 MHz equivalent

    // Instantiate DUT (example buffer)
    buffer #(
        .WIDTH(GATE_NUMS)
    ) dut (
        .din(input_a),
        .dout(output_c)
    );

    // Stimulus
    initial begin
        input_a = '0; // Initialize to 0

        #5 input_a = 48;  // Apply decimal value 48
        #10 input_a = 12;
        #10 input_a = 255;

        #20 $finish;
    end

    // Monitor
    initial begin
        $monitor("Time=%0t | input_a=%0d output_c=%0d", $time, input_a, output_c);
    end

endmodule
