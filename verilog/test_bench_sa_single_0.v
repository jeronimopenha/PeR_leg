

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

  // select cells stage variables
  reg [4-1:0] ca;
  reg [4-1:0] cb;
  // #####

  // cell to nodes stage variables
  reg [4-1:0] na;
  reg na_v;
  reg [4-1:0] nb;
  reg nb_v;
  wire [4-1:0] na_t;
  wire na_v_t;
  wire [4-1:0] nb_t;
  wire nb_v_t;
  // #####

  // neighborhood stage variables
  reg [16-1:0] va;
  reg [4-1:0] va_v;
  reg [16-1:0] vb;
  reg [4-1:0] vb_v;
  wire [16-1:0] va_t;
  wire [4-1:0] va_v_t;
  wire [4-1:0] va_v_m;
  wire [16-1:0] vb_t;
  wire [4-1:0] vb_v_t;
  wire [4-1:0] vb_v_m;

  //here we guarantee that only valid nodes can give neighbors 
  assign va_v_t = (na_v)? va_v_m : 4'b0;
  assign vb_v_t = (nb_v)? vb_v_m : 4'b0;
  // #####

  // node to cell stage variables
  reg [4-1:0] cva_v;
  reg [16-1:0] cva;
  reg [4-1:0] cvb_v;
  reg [16-1:0] cvb;
  wire [4-1:0] cva_v_t;
  wire [16-1:0] cva_t;
  wire [4-1:0] cvb_v_t;
  wire [16-1:0] cvb_t;

  // This is only for legibility
  // #####
  assign cva_v_t = va_v;
  assign cvb_v_t = vb_v;

  // SA single thread FSM

  always @(posedge clk) begin
    if(rst) begin
      ca <= 4'd0;
      cb <= 4'd0;
      na <= 4'd0;
      na_v <= 1'd0;
      nb <= 4'd0;
      nb_v <= 1'd0;
      va <= 16'd0;
      va_v <= 4'd0;
      vb <= 16'd0;
      vb_v <= 4'd0;
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
            if(&{ ~na_v_t, ~nb_v_t }) begin
              fsm_sa <= SELECT_CELLS;
            end else begin
              na <= na_t;
              na_v <= na_v_t;
              nb <= nb_t;
              nb_v <= nb_v_t;
              fsm_sa <= NEIGHBORHOOD;
            end
          end
          NEIGHBORHOOD: begin
            va <= va_t;
            va_v <= va_v_t;
            vb <= vb_t;
            vb_v <= vb_v_t;
            fsm_sa <= NODES_TO_CELL;
          end
          NODES_TO_CELL: begin
            cva_v <= cva_v_t;
            cva <= cva_t;
            cvb_v <= cvb_v_t;
            cvb <= cvb;
            fsm_sa <= DISTANCE_CALCULATOR;
          end
          DISTANCE_CALCULATOR: begin
            fsm_sa <= SELECT_CELLS;
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

  // cell to nodes stage memory instantiation

  mem_2r_1w_width5_depth4
  #(
    .READ_F(1),
    .INIT_FILE("/home/jeronimo/Documentos/GIT/sa_multi/verilog/test_bench_sa_single_0_c_n.rom"),
    .WRITE_F(1),
    .OUTPUT_FILE("/home/jeronimo/Documentos/GIT/sa_multi/verilog/test_bench_sa_single_0_c_n_out.rom")
  )
  mem_2r_1w_width5_depth4
  (
    .clk(clk),
    .rd(1'd1),
    .rd_addr0(ca),
    .rd_addr1(cb),
    .out0({ na_v_t, na_t }),
    .out1({ nb_v_t, nb_t }),
    .wr(1'd0),
    .wr_addr(4'd0),
    .wr_data(5'd0)
  );

  // #####

  // neighborhood stage memory instantiation

  mem_2r_1w_width5_depth4
  #(
    .READ_F(1),
    .INIT_FILE("/home/jeronimo/Documentos/GIT/sa_multi/verilog/test_bench_sa_single_0_n0.rom"),
    .WRITE_F(0)
  )
  mem_2r_1w_width5_depth4_0
  (
    .clk(clk),
    .rd_addr0(na),
    .rd_addr1(nb),
    .out0({ va_v_m[0], va_t[3:0] }),
    .out1({ vb_v_m[0], vb_t[3:0] }),
    .wr(1'd0),
    .wr_addr(4'd0),
    .wr_data(5'd0)
  );


  mem_2r_1w_width5_depth4
  #(
    .READ_F(1),
    .INIT_FILE("/home/jeronimo/Documentos/GIT/sa_multi/verilog/test_bench_sa_single_0_n1.rom"),
    .WRITE_F(0)
  )
  mem_2r_1w_width5_depth4_1
  (
    .clk(clk),
    .rd_addr0(na),
    .rd_addr1(nb),
    .out0({ va_v_m[1], va_t[7:4] }),
    .out1({ vb_v_m[1], vb_t[7:4] }),
    .wr(1'd0),
    .wr_addr(4'd0),
    .wr_data(5'd0)
  );


  mem_2r_1w_width5_depth4
  #(
    .READ_F(1),
    .INIT_FILE("/home/jeronimo/Documentos/GIT/sa_multi/verilog/test_bench_sa_single_0_n2.rom"),
    .WRITE_F(0)
  )
  mem_2r_1w_width5_depth4_2
  (
    .clk(clk),
    .rd_addr0(na),
    .rd_addr1(nb),
    .out0({ va_v_m[2], va_t[11:8] }),
    .out1({ vb_v_m[2], vb_t[11:8] }),
    .wr(1'd0),
    .wr_addr(4'd0),
    .wr_data(5'd0)
  );


  mem_2r_1w_width5_depth4
  #(
    .READ_F(1),
    .INIT_FILE("/home/jeronimo/Documentos/GIT/sa_multi/verilog/test_bench_sa_single_0_n3.rom"),
    .WRITE_F(0)
  )
  mem_2r_1w_width5_depth4_3
  (
    .clk(clk),
    .rd_addr0(na),
    .rd_addr1(nb),
    .out0({ va_v_m[3], va_t[15:12] }),
    .out1({ vb_v_m[3], vb_t[15:12] }),
    .wr(1'd0),
    .wr_addr(4'd0),
    .wr_data(5'd0)
  );

  // #####

  // node to cell stage memory instantiation
  // #####

  initial begin
    fsm_sa = 0;
    ca = 0;
    cb = 0;
    na = 0;
    na_v = 0;
    nb = 0;
    nb_v = 0;
    va = 0;
    va_v = 0;
    vb = 0;
    vb_v = 0;
    cva_v = 0;
    cva = 0;
    cvb_v = 0;
    cvb = 0;
  end


endmodule



module mem_2r_1w_width5_depth4 #
(
  parameter READ_F = 0,
  parameter INIT_FILE = "mem_file.txt",
  parameter WRITE_F = 0,
  parameter OUTPUT_FILE = "mem_out_file.txt"
)
(
  input clk,
  input rd,
  input [4-1:0] rd_addr0,
  input [4-1:0] rd_addr1,
  output [5-1:0] out0,
  output [5-1:0] out1,
  input wr,
  input [4-1:0] wr_addr,
  input [5-1:0] wr_data
);

  reg [5-1:0] mem [0:2**4-1];
  assign out0 = (rd)? mem[rd_addr0] : 5'd0;
  assign out1 = (rd)? mem[rd_addr1] : 5'd0;

  always @(posedge clk) begin
    if(wr) begin
      mem[wr_addr] <= wr_data;
    end 
  end

  //synthesis translate_off

  always @(posedge clk) begin
    if(wr && WRITE_F) begin
      $writememb(OUTPUT_FILE, mem);
    end 
  end

  //synthesis translate_on

  initial begin
    if(READ_F) begin
      $readmemb(INIT_FILE, mem);
    end 
  end


endmodule

