

module test_bench_sa_single_0
(

);

  reg clk;
  reg rst;
  reg start;
  wire done;

  sa_single_16cells
  sa_single_16cells
  (
    .clk(clk),
    .rst(rst),
    .start(start),
    .done(done)
  );


  initial begin
    clk = 0;
    rst = 1;
    start = 0;
  end


  initial begin
    $dumpfile("/home/jeronimo/Documentos/GIT/sa_multi/verilog/test_bench_sa_single_0.vcd");
    $dumpvars(0);
  end


  initial begin
    @(posedge clk);
    @(posedge clk);
    @(posedge clk);
    rst = 0;
    start = 1;
    #1000;
    $finish;
  end

  always #5clk=~clk;

  always @(posedge clk) begin
    if(done) begin
      $display("ACC DONE!");
      $finish;
    end 
  end


  //Simulation sector - End

endmodule



module sa_single_16cells
(
  input clk,
  input rst,
  input start,
  input done
);

  // SA single thread states declaration
  reg [4-1:0] fsm_sa;
  localparam SELECT_CELLS = 4'd0;
  localparam CELL_TO_NODES = 4'd1;
  localparam NEIGHBORHOOD = 4'd2;
  localparam NODES_TO_CELL = 4'd3;
  localparam DISTANCE_CALCULATOR = 4'd4;
  localparam SUM_REDUCTION = 4'd5;
  localparam DECISION = 4'd6;
  localparam CHANGES = 4'd7;
  localparam END = 4'd8;
  // #####

  // counter cells stage variables
  reg [4-1:0] ca;
  reg [4-1:0] cb;
  // #####
  // SA single thread FSM

  always @(posedge clk) begin
    if(rst) begin
      ca <= 4'd0;
      cb <= 4'd0;
      fsm_sa <= CELL_TO_NODES;
    end else begin
      if(start) begin
        case(fsm_sa)
          SELECT_CELLS: begin
            if(ca == 4) begin
              ca <= 4'd0;
              if(cb == 4) begin
                cb <= 4'd0;
                fsm_sa <= END;
              end else begin
                cb <= cb + 4'd1;
                fsm_sa <= CELL_TO_NODES;
              end
            end else begin
              ca <= ca + 4'd1;
              fsm_sa <= CELL_TO_NODES;
            end
          end
          CELL_TO_NODES: begin
            fsm_sa <= SELECT_CELLS;
          end
          NEIGHBORHOOD: begin
            fsm_sa <= NODES_TO_CELL;
          end
          NODES_TO_CELL: begin
            fsm_sa <= DISTANCE_CALCULATOR;
          end
          DISTANCE_CALCULATOR: begin
            fsm_sa <= SUM_REDUCTION;
          end
          SUM_REDUCTION: begin
            fsm_sa <= DECISION;
          end
          DECISION: begin
            fsm_sa <= CHANGES;
            fsm_sa <= SELECT_CELLS;
          end
          CHANGES: begin
            fsm_sa <= SELECT_CELLS;
          end
          END: begin
            fsm_sa <= END;
          end
        endcase
      end 
    end
  end


  initial begin
    fsm_sa = 0;
    ca = 0;
    cb = 0;
  end


endmodule

