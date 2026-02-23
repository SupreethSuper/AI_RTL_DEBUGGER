`timescale 1ns / 1ps

module tb_input_buffer;

  logic tb_a;
  logic tb_b;

  input_buffer dut (
    .a (tb_a),
    .b (tb_b)
  );

  initial begin
    tb_a = 0;
    #10;

    $display("Time=%0t, tb_a=%0b, tb_b=%0b", $time, tb_a, tb_b);
    #10;

    tb_a = 1;
    #10;
    $display("Time=%0t, tb_a=%0b, tb_b=%0b", $time, tb_a, tb_b);
    #10;

    tb_a = 0;
    #10;
    $display("Time=%0t, tb_a=%0b, tb_b=%0b", $time, tb_a, tb_b);
    #10;

    tb_a = 1;
    #10;
    $display("Time=%0t, tb_a=%0b, tb_b=%0b", $time, tb_a, tb_b);
    #10;

    $finish;
  end

endmodule