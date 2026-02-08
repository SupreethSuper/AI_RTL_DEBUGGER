`timescale 1ns/1ns

module tb_buffer_params;

    // `include "GATE_DEFINES.vh"
    `include "GATE_PARAMS.vh"

    localparam GATE_NUMS = NUM_GATES;

    // PARAMETERIZED INPUTS
    logic [GATE_NUMS-1:0] input_a;
    logic [GATE_NUMS-1:0] output_c;

    int error_count;
    int run_count;

    logic [GATE_NUMS - 1 : 0] seed; // Seed for randomization

    initial begin
        error_count = 0; // initialize error count
        run_count   = 10000; // initialize run count
    end

    // Clock (not required for a pure buffer, but kept since you already had it)
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

    // ====================== self checking testbench ======================
    // Keep while-loop as requested
    task automatic apply_stimulus();
        logic [GATE_NUMS-1:0] value;

        seed = $urandom; // Randomize seed for each run
        value = $urandom(seed); // Get initial random value

        while (run_count != 0) begin
            run_count--;

            value   = $urandom();
            input_a = value;

            #1; // allow combinational settle

            // For a buffer: expected output == input
            if (output_c !== value) begin
                $display("ERROR @%0t : input_a=%0h expected=%0h output_c=%0h",
                         $time, value, value, output_c);
                error_count++;
            end
        end
    endtask

    // Call the task (this is what actually runs the self-check)
    initial begin
        input_a = '0;
        #5;

        apply_stimulus();

        if (error_count == 0)
            $display("=== PASS ===");
        else begin
            $display("=== FAIL : %0d errors ===", error_count);
            $fatal(1, "Self-checking TB failed");
        end

        $finish;
    end

    final begin
        $display("===============FINISH HAS BEEN CALLED=============================");
        $display("Final error count: %0d", error_count);
    end

    // Monitor
    // initial begin
    //     $monitor("Time=%0t | input_a=%0d output_c=%0d", $time, input_a, output_c);
    // end

    // Dump waves
    initial begin
        $dumpfile("tb_buffer.vcd");
        $dumpvars(0, tb_buffer_params);
    end

endmodule
