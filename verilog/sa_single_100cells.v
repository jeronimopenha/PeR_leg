

module sa_single_100cells
(
  input clk,
  input rst,
  input start,
  input [10-1:0] n_exec,
  output reg done,
  input conf_c2n_rd,
  input [7-1:0] conf_c2n_rd_addr,
  output [8-1:0] conf_c2n_rd_data,
  input conf_wr,
  input conf_c2n_wr,
  input [7-1:0] conf_c2n_wr_addr,
  input [8-1:0] conf_c2n_wr_data,
  input [4-1:0] conf_n_wr,
  input [7-1:0] conf_n_wr_addr,
  input [8-1:0] conf_n_wr_data,
  input [4-1:0] conf_n2c_wr,
  input [7-1:0] conf_n2c_wr_addr,
  input [7-1:0] conf_n2c_wr_data
);

  reg [11-1:0] n_exec_counter;
  // SA single thread states declaration
  reg [4-1:0] fsm_sa;
  localparam SELECT_CELLS = 4'd0;
  localparam CELL_TO_NODES = 4'd1;
  localparam NEIGHBORHOOD = 4'd2;
  localparam NODES_TO_CELL = 4'd3;
  localparam LINE_COLUMN_FINDER = 4'd4;
  localparam DISTANCE_CALCULATOR = 4'd5;
  localparam SUM_REDUCTION_P = 4'd6;
  localparam SUM_REDUCTION = 4'd7;
  localparam TOTAL_COST = 4'd8;
  localparam DECISION = 4'd9;
  localparam WRITE_A = 4'd10;
  localparam WRITE_B = 4'd11;
  localparam END = 4'd12;
  // #####

  // select cells stage variables
  reg [7-1:0] ca;
  reg [7-1:0] cb;
  // #####

  // cell to nodes stage variables
  reg [7-1:0] na;
  reg na_v;
  reg [7-1:0] nb;
  reg nb_v;
  wire [7-1:0] na_t;
  wire na_v_t;
  wire [7-1:0] nb_t;
  wire nb_v_t;
  // #####

  // neighborhood stage variables
  reg [28-1:0] va;
  reg [4-1:0] va_v;
  reg [28-1:0] vb;
  reg [4-1:0] vb_v;
  wire [28-1:0] va_t;
  wire [4-1:0] va_v_t;
  wire [4-1:0] va_v_m;
  wire [28-1:0] vb_t;
  wire [4-1:0] vb_v_t;
  wire [4-1:0] vb_v_m;

  //here we guarantee that only valid nodes can give us neighbors 
  assign va_v_t = (na_v)? va_v_m : 4'b0;
  assign vb_v_t = (nb_v)? vb_v_m : 4'b0;
  // #####

  // node to cell stage variables
  reg [4-1:0] cva_v;
  reg [28-1:0] cva;
  reg [4-1:0] cvb_v;
  reg [28-1:0] cvb;
  wire [4-1:0] cva_v_t;
  wire [28-1:0] cva_t;
  wire [4-1:0] cvb_v_t;
  wire [28-1:0] cvb_t;

  // This is only for legibility
  assign cva_v_t = va_v;
  assign cvb_v_t = vb_v;
  // #####

  // line column finder stage variables
  reg [8-1:0] lca;
  reg [8-1:0] lcb;
  reg [32-1:0] lcva;
  reg [4-1:0] lcva_v;
  reg [32-1:0] lcvb;
  reg [4-1:0] lcvb_v;
  wire [8-1:0] lca_t;
  wire [8-1:0] lcb_t;
  wire [32-1:0] lcva_t;
  wire [32-1:0] lcvb_t;
  // #####

  // Distance calculator stage variables
  // Before changes
  reg [40-1:0] dva_before;
  reg [40-1:0] dvb_before;
  wire [8-1:0] lca_before;
  wire [8-1:0] lcb_before;
  wire [40-1:0] dva_before_t;
  wire [40-1:0] dvb_before_t;

  assign lca_before = lca;
  assign lcb_before = lcb;

  // After changes
  reg [40-1:0] dva_after;
  reg [40-1:0] dvb_after;
  wire [8-1:0] lca_after;
  wire [8-1:0] lcb_after;
  wire [32-1:0] opva_after;
  wire [32-1:0] opvb_after;
  wire [40-1:0] dva_after_t;
  wire [40-1:0] dvb_after_t;

  assign lca_after = lcb;
  assign lcb_after = lca;
  assign opva_after[7:0] = (lcva[7:0] == lca_after)? lcb_after : lcva[7:0];
  assign opva_after[15:8] = (lcva[15:8] == lca_after)? lcb_after : lcva[15:8];
  assign opva_after[23:16] = (lcva[23:16] == lca_after)? lcb_after : lcva[23:16];
  assign opva_after[31:24] = (lcva[31:24] == lca_after)? lcb_after : lcva[31:24];
  assign opvb_after[7:0] = (lcvb[7:0] == lcb_after)? lca_after : lcvb[7:0];
  assign opvb_after[15:8] = (lcvb[15:8] == lcb_after)? lca_after : lcvb[15:8];
  assign opvb_after[23:16] = (lcvb[23:16] == lcb_after)? lca_after : lcvb[23:16];
  assign opvb_after[31:24] = (lcvb[31:24] == lcb_after)? lca_after : lcvb[31:24];
  // #####

  // Sum Reduction stage variables
  // Sum Before change
  reg [20-1:0] sum_dva_before_p;
  wire [20-1:0] sum_dva_before_p_t;
  reg [20-1:0] sum_dvb_before_p;
  wire [20-1:0] sum_dvb_before_p_t;
  reg [10-1:0] sum_dva_before;
  wire [10-1:0] sum_dva_before_t;
  reg [10-1:0] sum_dvb_before;
  wire [10-1:0] sum_dvb_before_t;

  assign sum_dva_before_p_t[9:0] = dva_before[9:0] + dva_before[19:10];
  assign sum_dva_before_p_t[19:10] = dva_before[29:20] + dva_before[39:30];
  assign sum_dvb_before_p_t[9:0] = dvb_before[9:0] + dvb_before[19:10];
  assign sum_dvb_before_p_t[19:10] = dvb_before[29:20] + dvb_before[39:30];
  assign sum_dva_before_t[9:0] = sum_dva_before_p[9:0] + sum_dva_before_p[19:10];
  assign sum_dvb_before_t[9:0] = sum_dvb_before_p[9:0] + sum_dvb_before_p[19:10];

  // Sum after change
  reg [20-1:0] sum_dva_after_p;
  wire [20-1:0] sum_dva_after_p_t;
  reg [20-1:0] sum_dvb_after_p;
  wire [20-1:0] sum_dvb_after_p_t;
  reg [10-1:0] sum_dva_after;
  wire [10-1:0] sum_dva_after_t;
  reg [10-1:0] sum_dvb_after;
  wire [10-1:0] sum_dvb_after_t;

  assign sum_dva_after_p_t[9:0] = dva_after[9:0] + dva_after[19:10];
  assign sum_dva_after_p_t[19:10] = dva_after[29:20] + dva_after[39:30];
  assign sum_dvb_after_p_t[9:0] = dvb_after[9:0] + dvb_after[19:10];
  assign sum_dvb_after_p_t[19:10] = dvb_after[29:20] + dvb_after[39:30];
  assign sum_dva_after_t[9:0] = sum_dva_after_p[9:0] + sum_dva_after_p[19:10];
  assign sum_dvb_after_t[9:0] = sum_dvb_after_p[9:0] + sum_dvb_after_p[19:10];
  // #####

  // Total cost stage variables
  reg [10-1:0] total_cost_before;
  wire [10-1:0] total_cost_before_t;
  reg [10-1:0] total_cost_after;
  wire [10-1:0] total_cost_after_t;

  assign total_cost_before_t = sum_dva_before + sum_dvb_before;
  assign total_cost_after_t = sum_dva_after + sum_dvb_after;
  // #####

  // Decision stage variables
  wire decision;

  assign decision = total_cost_after < total_cost_before;
  // #####

  // Write a and b cost stage variables
  reg fsm_c2n_wr_signal;
  reg fsm_n2c_wr_signal;
  reg [7-1:0] fsm_mem_c2n_wr_addr;
  reg [8-1:0] fsm_mem_c2n_wr_data;
  reg [7-1:0] fsm_mem_n2c_wr_addr;
  reg [7-1:0] fsm_mem_n2c_wr_data;
  wire [7-1:0] mem_c2n_rd_addr;
  wire mem_c2n_wr;
  wire [7-1:0] mem_c2n_wr_addr;
  wire [8-1:0] mem_c2n_wr_data;
  wire [4-1:0] mem_n_wr;
  wire [7-1:0] mem_n_wr_addr;
  wire [8-1:0] mem_n_wr_data;
  wire [4-1:0] mem_n2c_wr;
  wire [7-1:0] mem_n2c_wr_addr;
  wire [7-1:0] mem_n2c_wr_data;

  assign mem_c2n_wr = (conf_wr)? conf_c2n_wr : fsm_c2n_wr_signal;
  assign mem_c2n_wr_addr = (conf_wr)? conf_c2n_wr_addr : fsm_mem_c2n_wr_addr;
  assign mem_c2n_wr_data = (conf_wr)? conf_c2n_wr_data : fsm_mem_c2n_wr_data;

  assign mem_n_wr = conf_n_wr;
  assign mem_n_wr_addr = conf_n_wr_addr;
  assign mem_n_wr_data = conf_n_wr_data;

  assign mem_n2c_wr = (conf_wr)? conf_n2c_wr : { 4{ fsm_n2c_wr_signal } };
  assign mem_n2c_wr_addr = (conf_wr)? conf_n2c_wr_addr : fsm_mem_n2c_wr_addr;
  assign mem_n2c_wr_data = (conf_wr)? conf_n2c_wr_data : fsm_mem_n2c_wr_data;

  assign mem_c2n_rd_addr = (conf_c2n_rd)? conf_c2n_rd_addr : ca;
  assign conf_c2n_rd_data = { na_v_t, na_t };
  // #####

  // SA single thread FSM

  always @(posedge clk) begin
    if(rst) begin
      done <= 1'd0;
      n_exec_counter <= 11'd0;
      ca <= 7'd0;
      cb <= 7'd0;
      na <= 7'd0;
      na_v <= 1'd0;
      nb <= 7'd0;
      nb_v <= 1'd0;
      va <= 28'd0;
      va_v <= 4'd0;
      vb <= 28'd0;
      vb_v <= 4'd0;
      lca <= 8'd0;
      lcb <= 8'd0;
      lcva <= 32'd0;
      lcva_v <= 4'd0;
      lcvb <= 32'd0;
      lcvb_v <= 4'd0;
      dva_before <= 40'd0;
      dvb_before <= 40'd0;
      dva_after <= 40'd0;
      dvb_after <= 40'd0;
      sum_dva_before_p <= 20'd0;
      sum_dvb_before_p <= 20'd0;
      sum_dva_after_p <= 20'd0;
      sum_dvb_after_p <= 20'd0;
      sum_dva_before <= 10'd0;
      sum_dvb_before <= 10'd0;
      sum_dva_after <= 10'd0;
      sum_dvb_after <= 10'd0;
      total_cost_before <= 10'd0;
      total_cost_after <= 10'd0;
      fsm_c2n_wr_signal <= 1'd0;
      fsm_n2c_wr_signal <= 1'd0;
      fsm_mem_c2n_wr_addr <= 7'd0;
      fsm_mem_c2n_wr_data <= 8'd0;
      fsm_mem_n2c_wr_addr <= 7'd0;
      fsm_mem_n2c_wr_data <= 7'd0;
      fsm_sa <= CELL_TO_NODES;
    end else begin
      if(start) begin
        fsm_c2n_wr_signal <= 1'd0;
        fsm_n2c_wr_signal <= 1'd0;
        case(fsm_sa)
          SELECT_CELLS: begin
            if(ca == 7'd10) begin
              ca <= 7'd0;
              if(cb == 7'd10) begin
                cb <= 7'd0;
                n_exec_counter <= n_exec_counter + 11'd1;
                fsm_sa <= END;
              end else begin
                cb <= cb + 7'd1;
                fsm_sa <= CELL_TO_NODES;
              end
            end else begin
              ca <= ca + 7'd1;
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
            fsm_sa <= LINE_COLUMN_FINDER;
          end
          LINE_COLUMN_FINDER: begin
            lca <= lca_t;
            lcb <= lcb_t;
            lcva <= lcva_t;
            lcva_v <= cva_v;
            lcvb <= lcvb_t;
            lcvb_v <= cvb_v;
            fsm_sa <= DISTANCE_CALCULATOR;
          end
          DISTANCE_CALCULATOR: begin
            dva_before <= dva_before_t;
            dvb_before <= dvb_before_t;
            dva_after <= dva_after_t;
            dvb_after <= dvb_after_t;
            fsm_sa <= SUM_REDUCTION_P;
          end
          SUM_REDUCTION_P: begin
            sum_dva_before_p <= sum_dva_before_p_t;
            sum_dvb_before_p <= sum_dvb_before_p_t;
            sum_dva_after_p <= sum_dva_after_p_t;
            sum_dvb_after_p <= sum_dvb_after_p_t;
            fsm_sa <= SUM_REDUCTION;
          end
          SUM_REDUCTION: begin
            sum_dva_before <= sum_dva_before_t;
            sum_dvb_before <= sum_dvb_before_t;
            sum_dva_after <= sum_dva_after_t;
            sum_dvb_after <= sum_dvb_after_t;
            fsm_sa <= TOTAL_COST;
          end
          TOTAL_COST: begin
            total_cost_before <= total_cost_before_t;
            total_cost_after <= total_cost_after_t;
            fsm_sa <= DECISION;
          end
          DECISION: begin
            if(decision) begin
              fsm_sa <= WRITE_A;
            end else begin
              fsm_sa <= SELECT_CELLS;
            end
          end
          WRITE_A: begin
            fsm_c2n_wr_signal <= 1'd1;
            fsm_mem_c2n_wr_addr <= cb;
            fsm_mem_c2n_wr_data <= { na_v, na };
            fsm_n2c_wr_signal <= na_v;
            fsm_mem_n2c_wr_addr <= na;
            fsm_mem_n2c_wr_data <= cb;
            fsm_sa <= WRITE_B;
          end
          WRITE_B: begin
            fsm_c2n_wr_signal <= 1'd1;
            fsm_mem_c2n_wr_addr <= ca;
            fsm_mem_c2n_wr_data <= { nb_v, nb };
            fsm_n2c_wr_signal <= nb_v;
            fsm_mem_n2c_wr_addr <= nb;
            fsm_mem_n2c_wr_data <= ca;
            fsm_sa <= SELECT_CELLS;
          end
          END: begin
            if(n_exec_counter == n_exec) begin
              fsm_sa <= SELECT_CELLS;
            end else begin
              done <= 1'd1;
            end
          end
        endcase
      end 
    end
  end

  // cell to nodes stage memory instantiation

  mem_2r_1w_width8_depth7
  #(
    .READ_F(1),
    .INIT_FILE("/home/jeronimo/Documentos/GIT/sa_multi/verilog/test_bench_sa_single_0_c_n.rom"),
    .WRITE_F(1),
    .OUTPUT_FILE("/home/jeronimo/Documentos/GIT/sa_multi/verilog/test_bench_sa_single_0_c_n_out.rom")
  )
  mem_2r_1w_width8_depth7
  (
    .clk(clk),
    .rd(1'd1),
    .rd_addr0(ca),
    .rd_addr1(cb),
    .out0({ na_v_t, na_t }),
    .out1({ nb_v_t, nb_t }),
    .wr(mem_c2n_wr),
    .wr_addr(mem_c2n_wr_addr),
    .wr_data(mem_c2n_wr_data)
  );

  // #####

  // neighborhood stage memory instantiation

  mem_2r_1w_width8_depth7
  #(
    .READ_F(1),
    .INIT_FILE("/home/jeronimo/Documentos/GIT/sa_multi/verilog/test_bench_sa_single_0_n0.rom"),
    .WRITE_F(0)
  )
  mem_2r_1w_width8_depth7_0
  (
    .clk(clk),
    .rd(1'd1),
    .rd_addr0(na),
    .rd_addr1(nb),
    .out0({ va_v_m[0], va_t[6:0] }),
    .out1({ vb_v_m[0], vb_t[6:0] }),
    .wr(mem_n_wr[0]),
    .wr_addr(mem_n_wr_addr),
    .wr_data(mem_n_wr_data)
  );


  mem_2r_1w_width8_depth7
  #(
    .READ_F(1),
    .INIT_FILE("/home/jeronimo/Documentos/GIT/sa_multi/verilog/test_bench_sa_single_0_n1.rom"),
    .WRITE_F(0)
  )
  mem_2r_1w_width8_depth7_1
  (
    .clk(clk),
    .rd(1'd1),
    .rd_addr0(na),
    .rd_addr1(nb),
    .out0({ va_v_m[1], va_t[13:7] }),
    .out1({ vb_v_m[1], vb_t[13:7] }),
    .wr(mem_n_wr[1]),
    .wr_addr(mem_n_wr_addr),
    .wr_data(mem_n_wr_data)
  );


  mem_2r_1w_width8_depth7
  #(
    .READ_F(1),
    .INIT_FILE("/home/jeronimo/Documentos/GIT/sa_multi/verilog/test_bench_sa_single_0_n2.rom"),
    .WRITE_F(0)
  )
  mem_2r_1w_width8_depth7_2
  (
    .clk(clk),
    .rd(1'd1),
    .rd_addr0(na),
    .rd_addr1(nb),
    .out0({ va_v_m[2], va_t[20:14] }),
    .out1({ vb_v_m[2], vb_t[20:14] }),
    .wr(mem_n_wr[2]),
    .wr_addr(mem_n_wr_addr),
    .wr_data(mem_n_wr_data)
  );


  mem_2r_1w_width8_depth7
  #(
    .READ_F(1),
    .INIT_FILE("/home/jeronimo/Documentos/GIT/sa_multi/verilog/test_bench_sa_single_0_n3.rom"),
    .WRITE_F(0)
  )
  mem_2r_1w_width8_depth7_3
  (
    .clk(clk),
    .rd(1'd1),
    .rd_addr0(na),
    .rd_addr1(nb),
    .out0({ va_v_m[3], va_t[27:21] }),
    .out1({ vb_v_m[3], vb_t[27:21] }),
    .wr(mem_n_wr[3]),
    .wr_addr(mem_n_wr_addr),
    .wr_data(mem_n_wr_data)
  );

  // #####

  // node to cell stage memory instantiation

  mem_2r_1w_width7_depth7
  #(
    .READ_F(1),
    .INIT_FILE("/home/jeronimo/Documentos/GIT/sa_multi/verilog/test_bench_sa_single_0_n_c.rom"),
    .WRITE_F(1),
    .OUTPUT_FILE("/home/jeronimo/Documentos/GIT/sa_multi/verilog/test_bench_sa_single_0_n_c_out0.rom")
  )
  mem_2r_1w_width7_depth7_0
  (
    .clk(clk),
    .rd(1'd1),
    .rd_addr0(va[6:0]),
    .rd_addr1(vb[6:0]),
    .out0(cva_t[6:0]),
    .out1(cvb_t[6:0]),
    .wr(mem_n2c_wr[0]),
    .wr_addr(mem_n2c_wr_addr),
    .wr_data(mem_n2c_wr_data)
  );


  mem_2r_1w_width7_depth7
  #(
    .READ_F(1),
    .INIT_FILE("/home/jeronimo/Documentos/GIT/sa_multi/verilog/test_bench_sa_single_0_n_c.rom"),
    .WRITE_F(0),
    .OUTPUT_FILE("/home/jeronimo/Documentos/GIT/sa_multi/verilog/test_bench_sa_single_0_n_c_out1.rom")
  )
  mem_2r_1w_width7_depth7_1
  (
    .clk(clk),
    .rd(1'd1),
    .rd_addr0(va[13:7]),
    .rd_addr1(vb[13:7]),
    .out0(cva_t[13:7]),
    .out1(cvb_t[13:7]),
    .wr(mem_n2c_wr[1]),
    .wr_addr(mem_n2c_wr_addr),
    .wr_data(mem_n2c_wr_data)
  );


  mem_2r_1w_width7_depth7
  #(
    .READ_F(1),
    .INIT_FILE("/home/jeronimo/Documentos/GIT/sa_multi/verilog/test_bench_sa_single_0_n_c.rom"),
    .WRITE_F(0),
    .OUTPUT_FILE("/home/jeronimo/Documentos/GIT/sa_multi/verilog/test_bench_sa_single_0_n_c_out2.rom")
  )
  mem_2r_1w_width7_depth7_2
  (
    .clk(clk),
    .rd(1'd1),
    .rd_addr0(va[20:14]),
    .rd_addr1(vb[20:14]),
    .out0(cva_t[20:14]),
    .out1(cvb_t[20:14]),
    .wr(mem_n2c_wr[2]),
    .wr_addr(mem_n2c_wr_addr),
    .wr_data(mem_n2c_wr_data)
  );


  mem_2r_1w_width7_depth7
  #(
    .READ_F(1),
    .INIT_FILE("/home/jeronimo/Documentos/GIT/sa_multi/verilog/test_bench_sa_single_0_n_c.rom"),
    .WRITE_F(0),
    .OUTPUT_FILE("/home/jeronimo/Documentos/GIT/sa_multi/verilog/test_bench_sa_single_0_n_c_out3.rom")
  )
  mem_2r_1w_width7_depth7_3
  (
    .clk(clk),
    .rd(1'd1),
    .rd_addr0(va[27:21]),
    .rd_addr1(vb[27:21]),
    .out0(cva_t[27:21]),
    .out1(cvb_t[27:21]),
    .wr(mem_n2c_wr[3]),
    .wr_addr(mem_n2c_wr_addr),
    .wr_data(mem_n2c_wr_data)
  );

  // #####

  // line column finder stage lc_table instantiation

  lc_table_10_10
  lc_table_10_10_c
  (
    .ca(ca),
    .cb(cb),
    .lca(lca_t),
    .lcb(lcb_t)
  );


  lc_table_10_10
  lc_table_10_10_v_0
  (
    .ca(cva[6:0]),
    .cb(cvb[6:0]),
    .lca(lcva_t[7:0]),
    .lcb(lcvb_t[7:0])
  );


  lc_table_10_10
  lc_table_10_10_v_1
  (
    .ca(cva[13:7]),
    .cb(cvb[13:7]),
    .lca(lcva_t[15:8]),
    .lcb(lcvb_t[15:8])
  );


  lc_table_10_10
  lc_table_10_10_v_2
  (
    .ca(cva[20:14]),
    .cb(cvb[20:14]),
    .lca(lcva_t[23:16]),
    .lcb(lcvb_t[23:16])
  );


  lc_table_10_10
  lc_table_10_10_v_3
  (
    .ca(cva[27:21]),
    .cb(cvb[27:21]),
    .lca(lcva_t[31:24]),
    .lcb(lcvb_t[31:24])
  );

  // #####

  // Distance calculator stage distance talbles instantiation
  // Distance before change

  distance_table_10_10
  distance_table_10_10_dac_0
  (
    .opa0(lca_before),
    .opa1(lcva[7:0]),
    .opav(lcva_v[0]),
    .opb0(lca_before),
    .opb1(lcva[15:8]),
    .opbv(lcva_v[1]),
    .da(dva_before_t[9:0]),
    .db(dva_before_t[19:10])
  );


  distance_table_10_10
  distance_table_10_10_dac_1
  (
    .opa0(lca_before),
    .opa1(lcva[23:16]),
    .opav(lcva_v[2]),
    .opb0(lca_before),
    .opb1(lcva[31:24]),
    .opbv(lcva_v[3]),
    .da(dva_before_t[29:20]),
    .db(dva_before_t[39:30])
  );


  distance_table_10_10
  distance_table_10_10_dbc_0
  (
    .opa0(lcb_before),
    .opa1(lcvb[7:0]),
    .opav(lcvb_v[0]),
    .opb0(lcb_before),
    .opb1(lcvb[15:8]),
    .opbv(lcvb_v[1]),
    .da(dvb_before_t[9:0]),
    .db(dvb_before_t[19:10])
  );


  distance_table_10_10
  distance_table_10_10_dbc_1
  (
    .opa0(lcb_before),
    .opa1(lcvb[23:16]),
    .opav(lcvb_v[2]),
    .opb0(lcb_before),
    .opb1(lcvb[31:24]),
    .opbv(lcvb_v[3]),
    .da(dvb_before_t[29:20]),
    .db(dvb_before_t[39:30])
  );


  // Distance after change

  distance_table_10_10
  distance_table_10_10_das_0
  (
    .opa0(lca_after),
    .opa1(opva_after[7:0]),
    .opav(lcva_v[0]),
    .opb0(lca_after),
    .opb1(opva_after[15:8]),
    .opbv(lcva_v[1]),
    .da(dva_after_t[9:0]),
    .db(dva_after_t[19:10])
  );


  distance_table_10_10
  distance_table_10_10_das_1
  (
    .opa0(lca_after),
    .opa1(opva_after[23:16]),
    .opav(lcva_v[2]),
    .opb0(lca_after),
    .opb1(opva_after[31:24]),
    .opbv(lcva_v[3]),
    .da(dva_after_t[29:20]),
    .db(dva_after_t[39:30])
  );


  distance_table_10_10
  distance_table_10_10_dbs_0
  (
    .opa0(lcb_after),
    .opa1(opvb_after[7:0]),
    .opav(lcvb_v[0]),
    .opb0(lcb_after),
    .opb1(opvb_after[15:8]),
    .opbv(lcvb_v[1]),
    .da(dvb_after_t[9:0]),
    .db(dvb_after_t[19:10])
  );


  distance_table_10_10
  distance_table_10_10_dbs_1
  (
    .opa0(lcb_after),
    .opa1(opvb_after[23:16]),
    .opav(lcvb_v[2]),
    .opb0(lcb_after),
    .opb1(opvb_after[31:24]),
    .opbv(lcvb_v[3]),
    .da(dvb_after_t[29:20]),
    .db(dvb_after_t[39:30])
  );

  // #####

  initial begin
    done = 0;
    n_exec_counter = 0;
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
    lca = 0;
    lcb = 0;
    lcva = 0;
    lcva_v = 0;
    lcvb = 0;
    lcvb_v = 0;
    dva_before = 0;
    dvb_before = 0;
    dva_after = 0;
    dvb_after = 0;
    sum_dva_before_p = 0;
    sum_dvb_before_p = 0;
    sum_dva_before = 0;
    sum_dvb_before = 0;
    sum_dva_after_p = 0;
    sum_dvb_after_p = 0;
    sum_dva_after = 0;
    sum_dvb_after = 0;
    total_cost_before = 0;
    total_cost_after = 0;
    fsm_c2n_wr_signal = 0;
    fsm_n2c_wr_signal = 0;
    fsm_mem_c2n_wr_addr = 0;
    fsm_mem_c2n_wr_data = 0;
    fsm_mem_n2c_wr_addr = 0;
    fsm_mem_n2c_wr_data = 0;
  end


endmodule



module mem_2r_1w_width8_depth7 #
(
  parameter READ_F = 0,
  parameter INIT_FILE = "mem_file.txt",
  parameter WRITE_F = 0,
  parameter OUTPUT_FILE = "mem_out_file.txt"
)
(
  input clk,
  input rd,
  input [7-1:0] rd_addr0,
  input [7-1:0] rd_addr1,
  output [8-1:0] out0,
  output [8-1:0] out1,
  input wr,
  input [7-1:0] wr_addr,
  input [8-1:0] wr_data
);

  reg [8-1:0] mem [0:2**7-1];
  assign out0 = (rd)? mem[rd_addr0] : 8'd0;
  assign out1 = (rd)? mem[rd_addr1] : 8'd0;

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



module mem_2r_1w_width7_depth7 #
(
  parameter READ_F = 0,
  parameter INIT_FILE = "mem_file.txt",
  parameter WRITE_F = 0,
  parameter OUTPUT_FILE = "mem_out_file.txt"
)
(
  input clk,
  input rd,
  input [7-1:0] rd_addr0,
  input [7-1:0] rd_addr1,
  output [7-1:0] out0,
  output [7-1:0] out1,
  input wr,
  input [7-1:0] wr_addr,
  input [7-1:0] wr_data
);

  reg [7-1:0] mem [0:2**7-1];
  assign out0 = (rd)? mem[rd_addr0] : 7'd0;
  assign out1 = (rd)? mem[rd_addr1] : 7'd0;

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



module lc_table_10_10
(
  input [7-1:0] ca,
  input [7-1:0] cb,
  output [8-1:0] lca,
  output [8-1:0] lcb
);

  wire [8-1:0] lc_table [0:100-1];
  assign lca = lc_table[ca];
  assign lcb = lc_table[cb];
  assign lc_table[0] = { 4'd0, 4'd0 };
  assign lc_table[1] = { 4'd0, 4'd1 };
  assign lc_table[2] = { 4'd0, 4'd2 };
  assign lc_table[3] = { 4'd0, 4'd3 };
  assign lc_table[4] = { 4'd0, 4'd4 };
  assign lc_table[5] = { 4'd0, 4'd5 };
  assign lc_table[6] = { 4'd0, 4'd6 };
  assign lc_table[7] = { 4'd0, 4'd7 };
  assign lc_table[8] = { 4'd0, 4'd8 };
  assign lc_table[9] = { 4'd0, 4'd9 };
  assign lc_table[10] = { 4'd1, 4'd0 };
  assign lc_table[11] = { 4'd1, 4'd1 };
  assign lc_table[12] = { 4'd1, 4'd2 };
  assign lc_table[13] = { 4'd1, 4'd3 };
  assign lc_table[14] = { 4'd1, 4'd4 };
  assign lc_table[15] = { 4'd1, 4'd5 };
  assign lc_table[16] = { 4'd1, 4'd6 };
  assign lc_table[17] = { 4'd1, 4'd7 };
  assign lc_table[18] = { 4'd1, 4'd8 };
  assign lc_table[19] = { 4'd1, 4'd9 };
  assign lc_table[20] = { 4'd2, 4'd0 };
  assign lc_table[21] = { 4'd2, 4'd1 };
  assign lc_table[22] = { 4'd2, 4'd2 };
  assign lc_table[23] = { 4'd2, 4'd3 };
  assign lc_table[24] = { 4'd2, 4'd4 };
  assign lc_table[25] = { 4'd2, 4'd5 };
  assign lc_table[26] = { 4'd2, 4'd6 };
  assign lc_table[27] = { 4'd2, 4'd7 };
  assign lc_table[28] = { 4'd2, 4'd8 };
  assign lc_table[29] = { 4'd2, 4'd9 };
  assign lc_table[30] = { 4'd3, 4'd0 };
  assign lc_table[31] = { 4'd3, 4'd1 };
  assign lc_table[32] = { 4'd3, 4'd2 };
  assign lc_table[33] = { 4'd3, 4'd3 };
  assign lc_table[34] = { 4'd3, 4'd4 };
  assign lc_table[35] = { 4'd3, 4'd5 };
  assign lc_table[36] = { 4'd3, 4'd6 };
  assign lc_table[37] = { 4'd3, 4'd7 };
  assign lc_table[38] = { 4'd3, 4'd8 };
  assign lc_table[39] = { 4'd3, 4'd9 };
  assign lc_table[40] = { 4'd4, 4'd0 };
  assign lc_table[41] = { 4'd4, 4'd1 };
  assign lc_table[42] = { 4'd4, 4'd2 };
  assign lc_table[43] = { 4'd4, 4'd3 };
  assign lc_table[44] = { 4'd4, 4'd4 };
  assign lc_table[45] = { 4'd4, 4'd5 };
  assign lc_table[46] = { 4'd4, 4'd6 };
  assign lc_table[47] = { 4'd4, 4'd7 };
  assign lc_table[48] = { 4'd4, 4'd8 };
  assign lc_table[49] = { 4'd4, 4'd9 };
  assign lc_table[50] = { 4'd5, 4'd0 };
  assign lc_table[51] = { 4'd5, 4'd1 };
  assign lc_table[52] = { 4'd5, 4'd2 };
  assign lc_table[53] = { 4'd5, 4'd3 };
  assign lc_table[54] = { 4'd5, 4'd4 };
  assign lc_table[55] = { 4'd5, 4'd5 };
  assign lc_table[56] = { 4'd5, 4'd6 };
  assign lc_table[57] = { 4'd5, 4'd7 };
  assign lc_table[58] = { 4'd5, 4'd8 };
  assign lc_table[59] = { 4'd5, 4'd9 };
  assign lc_table[60] = { 4'd6, 4'd0 };
  assign lc_table[61] = { 4'd6, 4'd1 };
  assign lc_table[62] = { 4'd6, 4'd2 };
  assign lc_table[63] = { 4'd6, 4'd3 };
  assign lc_table[64] = { 4'd6, 4'd4 };
  assign lc_table[65] = { 4'd6, 4'd5 };
  assign lc_table[66] = { 4'd6, 4'd6 };
  assign lc_table[67] = { 4'd6, 4'd7 };
  assign lc_table[68] = { 4'd6, 4'd8 };
  assign lc_table[69] = { 4'd6, 4'd9 };
  assign lc_table[70] = { 4'd7, 4'd0 };
  assign lc_table[71] = { 4'd7, 4'd1 };
  assign lc_table[72] = { 4'd7, 4'd2 };
  assign lc_table[73] = { 4'd7, 4'd3 };
  assign lc_table[74] = { 4'd7, 4'd4 };
  assign lc_table[75] = { 4'd7, 4'd5 };
  assign lc_table[76] = { 4'd7, 4'd6 };
  assign lc_table[77] = { 4'd7, 4'd7 };
  assign lc_table[78] = { 4'd7, 4'd8 };
  assign lc_table[79] = { 4'd7, 4'd9 };
  assign lc_table[80] = { 4'd8, 4'd0 };
  assign lc_table[81] = { 4'd8, 4'd1 };
  assign lc_table[82] = { 4'd8, 4'd2 };
  assign lc_table[83] = { 4'd8, 4'd3 };
  assign lc_table[84] = { 4'd8, 4'd4 };
  assign lc_table[85] = { 4'd8, 4'd5 };
  assign lc_table[86] = { 4'd8, 4'd6 };
  assign lc_table[87] = { 4'd8, 4'd7 };
  assign lc_table[88] = { 4'd8, 4'd8 };
  assign lc_table[89] = { 4'd8, 4'd9 };
  assign lc_table[90] = { 4'd9, 4'd0 };
  assign lc_table[91] = { 4'd9, 4'd1 };
  assign lc_table[92] = { 4'd9, 4'd2 };
  assign lc_table[93] = { 4'd9, 4'd3 };
  assign lc_table[94] = { 4'd9, 4'd4 };
  assign lc_table[95] = { 4'd9, 4'd5 };
  assign lc_table[96] = { 4'd9, 4'd6 };
  assign lc_table[97] = { 4'd9, 4'd7 };
  assign lc_table[98] = { 4'd9, 4'd8 };
  assign lc_table[99] = { 4'd9, 4'd9 };

endmodule



module distance_table_10_10
(
  input [8-1:0] opa0,
  input [8-1:0] opa1,
  input opav,
  input [8-1:0] opb0,
  input [8-1:0] opb1,
  input opbv,
  output [10-1:0] da,
  output [10-1:0] db
);

  wire [10-1:0] dist_table [0:2**8-1];
  wire [10-1:0] da_t;
  wire [10-1:0] db_t;

  assign da_t = dist_table[{ opa1[3:0], opa0[3:0] }] + dist_table[{ opa1[7:4], opa0[7:4] }];
  assign db_t = dist_table[{ opb1[3:0], opb0[3:0] }] + dist_table[{ opb1[7:4], opb0[7:4] }];

  assign da = (opav)? da_t : 0;
  assign db = (opbv)? db_t : 0;

  assign dist_table[0] = 0;
  assign dist_table[1] = 1;
  assign dist_table[2] = 2;
  assign dist_table[3] = 3;
  assign dist_table[4] = 4;
  assign dist_table[5] = 5;
  assign dist_table[6] = 6;
  assign dist_table[7] = 7;
  assign dist_table[8] = 8;
  assign dist_table[9] = 9;
  assign dist_table[16] = 1;
  assign dist_table[17] = 0;
  assign dist_table[18] = 1;
  assign dist_table[19] = 2;
  assign dist_table[20] = 3;
  assign dist_table[21] = 4;
  assign dist_table[22] = 5;
  assign dist_table[23] = 6;
  assign dist_table[24] = 7;
  assign dist_table[25] = 8;
  assign dist_table[32] = 2;
  assign dist_table[33] = 1;
  assign dist_table[34] = 0;
  assign dist_table[35] = 1;
  assign dist_table[36] = 2;
  assign dist_table[37] = 3;
  assign dist_table[38] = 4;
  assign dist_table[39] = 5;
  assign dist_table[40] = 6;
  assign dist_table[41] = 7;
  assign dist_table[48] = 3;
  assign dist_table[49] = 2;
  assign dist_table[50] = 1;
  assign dist_table[51] = 0;
  assign dist_table[52] = 1;
  assign dist_table[53] = 2;
  assign dist_table[54] = 3;
  assign dist_table[55] = 4;
  assign dist_table[56] = 5;
  assign dist_table[57] = 6;
  assign dist_table[64] = 4;
  assign dist_table[65] = 3;
  assign dist_table[66] = 2;
  assign dist_table[67] = 1;
  assign dist_table[68] = 0;
  assign dist_table[69] = 1;
  assign dist_table[70] = 2;
  assign dist_table[71] = 3;
  assign dist_table[72] = 4;
  assign dist_table[73] = 5;
  assign dist_table[80] = 5;
  assign dist_table[81] = 4;
  assign dist_table[82] = 3;
  assign dist_table[83] = 2;
  assign dist_table[84] = 1;
  assign dist_table[85] = 0;
  assign dist_table[86] = 1;
  assign dist_table[87] = 2;
  assign dist_table[88] = 3;
  assign dist_table[89] = 4;
  assign dist_table[96] = 6;
  assign dist_table[97] = 5;
  assign dist_table[98] = 4;
  assign dist_table[99] = 3;
  assign dist_table[100] = 2;
  assign dist_table[101] = 1;
  assign dist_table[102] = 0;
  assign dist_table[103] = 1;
  assign dist_table[104] = 2;
  assign dist_table[105] = 3;
  assign dist_table[112] = 7;
  assign dist_table[113] = 6;
  assign dist_table[114] = 5;
  assign dist_table[115] = 4;
  assign dist_table[116] = 3;
  assign dist_table[117] = 2;
  assign dist_table[118] = 1;
  assign dist_table[119] = 0;
  assign dist_table[120] = 1;
  assign dist_table[121] = 2;
  assign dist_table[128] = 8;
  assign dist_table[129] = 7;
  assign dist_table[130] = 6;
  assign dist_table[131] = 5;
  assign dist_table[132] = 4;
  assign dist_table[133] = 3;
  assign dist_table[134] = 2;
  assign dist_table[135] = 1;
  assign dist_table[136] = 0;
  assign dist_table[137] = 1;
  assign dist_table[144] = 9;
  assign dist_table[145] = 8;
  assign dist_table[146] = 7;
  assign dist_table[147] = 6;
  assign dist_table[148] = 5;
  assign dist_table[149] = 4;
  assign dist_table[150] = 3;
  assign dist_table[151] = 2;
  assign dist_table[152] = 1;
  assign dist_table[153] = 0;

endmodule

