`include "GATE_PARAMS.vh"

module buffer #(parameter WIDTH = NUM_GATES)(
    input  logic [WIDTH-1:0] din,
    output logic [WIDTH-1:0] dout
);
    assign dout = din;
endmodule
