

module sa_single_16cells
(
  input clk,
  input rst,
  input start,
  input [10-1:0] n_exec,
  output reg done,
  input conf_c2n_rd,
  input [4-1:0] conf_c2n_rd_addr,
  output [5-1:0] conf_c2n_rd_data,
  input conf_wr,
  input conf_c2n_wr,
  input [4-1:0] conf_c2n_wr_addr,
  input [5-1:0] conf_c2n_wr_data,
  input [4-1:0] conf_n_wr,
  input [4-1:0] conf_n_wr_addr,
  input [5-1:0] conf_n_wr_data,
  input [4-1:0] conf_n2c_wr,
  input [4-1:0] conf_n2c_wr_addr,
  input [4-1:0] conf_n2c_wr_data
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

  //here we guarantee that only valid nodes can give us neighbors 
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
  assign cva_v_t = va_v;
  assign cvb_v_t = vb_v;
  // #####

  // line column finder stage variables
  reg [4-1:0] lca;
  reg [4-1:0] lcb;
  reg [16-1:0] lcva;
  reg [4-1:0] lcva_v;
  reg [16-1:0] lcvb;
  reg [4-1:0] lcvb_v;
  wire [4-1:0] lca_t;
  wire [4-1:0] lcb_t;
  wire [16-1:0] lcva_t;
  wire [16-1:0] lcvb_t;
  // #####

  // Distance calculator stage variables
  // Before changes
  reg [28-1:0] dva_before;
  reg [28-1:0] dvb_before;
  wire [4-1:0] lca_before;
  wire [4-1:0] lcb_before;
  wire [28-1:0] dva_before_t;
  wire [28-1:0] dvb_before_t;

  assign lca_before = lca;
  assign lcb_before = lcb;

  // After changes
  reg [28-1:0] dva_after;
  reg [28-1:0] dvb_after;
  wire [4-1:0] lca_after;
  wire [4-1:0] lcb_after;
  wire [16-1:0] opva_after;
  wire [16-1:0] opvb_after;
  wire [28-1:0] dva_after_t;
  wire [28-1:0] dvb_after_t;

  assign lca_after = lcb;
  assign lcb_after = lca;
  assign opva_after[3:0] = (lcva[3:0] == lca_after)? lcb_after : lcva[3:0];
  assign opva_after[7:4] = (lcva[7:4] == lca_after)? lcb_after : lcva[7:4];
  assign opva_after[11:8] = (lcva[11:8] == lca_after)? lcb_after : lcva[11:8];
  assign opva_after[15:12] = (lcva[15:12] == lca_after)? lcb_after : lcva[15:12];
  assign opvb_after[3:0] = (lcvb[3:0] == lcb_after)? lca_after : lcvb[3:0];
  assign opvb_after[7:4] = (lcvb[7:4] == lcb_after)? lca_after : lcvb[7:4];
  assign opvb_after[11:8] = (lcvb[11:8] == lcb_after)? lca_after : lcvb[11:8];
  assign opvb_after[15:12] = (lcvb[15:12] == lcb_after)? lca_after : lcvb[15:12];
  // #####

  // Sum Reduction stage variables
  // Sum Before change
  reg [14-1:0] sum_dva_before_p;
  wire [14-1:0] sum_dva_before_p_t;
  reg [14-1:0] sum_dvb_before_p;
  wire [14-1:0] sum_dvb_before_p_t;
  reg [7-1:0] sum_dva_before;
  wire [7-1:0] sum_dva_before_t;
  reg [7-1:0] sum_dvb_before;
  wire [7-1:0] sum_dvb_before_t;

  assign sum_dva_before_p_t[6:0] = dva_before[6:0] + dva_before[13:7];
  assign sum_dva_before_p_t[13:7] = dva_before[20:14] + dva_before[27:21];
  assign sum_dvb_before_p_t[6:0] = dvb_before[6:0] + dvb_before[13:7];
  assign sum_dvb_before_p_t[13:7] = dvb_before[20:14] + dvb_before[27:21];
  assign sum_dva_before_t[6:0] = sum_dva_before_p[6:0] + sum_dva_before_p[13:7];
  assign sum_dvb_before_t[6:0] = sum_dvb_before_p[6:0] + sum_dvb_before_p[13:7];

  // Sum after change
  reg [14-1:0] sum_dva_after_p;
  wire [14-1:0] sum_dva_after_p_t;
  reg [14-1:0] sum_dvb_after_p;
  wire [14-1:0] sum_dvb_after_p_t;
  reg [7-1:0] sum_dva_after;
  wire [7-1:0] sum_dva_after_t;
  reg [7-1:0] sum_dvb_after;
  wire [7-1:0] sum_dvb_after_t;

  assign sum_dva_after_p_t[6:0] = dva_after[6:0] + dva_after[13:7];
  assign sum_dva_after_p_t[13:7] = dva_after[20:14] + dva_after[27:21];
  assign sum_dvb_after_p_t[6:0] = dvb_after[6:0] + dvb_after[13:7];
  assign sum_dvb_after_p_t[13:7] = dvb_after[20:14] + dvb_after[27:21];
  assign sum_dva_after_t[6:0] = sum_dva_after_p[6:0] + sum_dva_after_p[13:7];
  assign sum_dvb_after_t[6:0] = sum_dvb_after_p[6:0] + sum_dvb_after_p[13:7];
  // #####

  // Total cost stage variables
  reg [7-1:0] total_cost_before;
  wire [7-1:0] total_cost_before_t;
  reg [7-1:0] total_cost_after;
  wire [7-1:0] total_cost_after_t;

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
  reg [4-1:0] fsm_mem_c2n_wr_addr;
  reg [5-1:0] fsm_mem_c2n_wr_data;
  reg [4-1:0] fsm_mem_n2c_wr_addr;
  reg [4-1:0] fsm_mem_n2c_wr_data;
  wire [4-1:0] mem_c2n_rd_addr;
  wire mem_c2n_wr;
  wire [4-1:0] mem_c2n_wr_addr;
  wire [5-1:0] mem_c2n_wr_data;
  wire [4-1:0] mem_n_wr;
  wire [4-1:0] mem_n_wr_addr;
  wire [5-1:0] mem_n_wr_data;
  wire [4-1:0] mem_n2c_wr;
  wire [4-1:0] mem_n2c_wr_addr;
  wire [4-1:0] mem_n2c_wr_data;

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
      lca <= 4'd0;
      lcb <= 4'd0;
      lcva <= 16'd0;
      lcva_v <= 4'd0;
      lcvb <= 16'd0;
      lcvb_v <= 4'd0;
      dva_before <= 28'd0;
      dvb_before <= 28'd0;
      dva_after <= 28'd0;
      dvb_after <= 28'd0;
      sum_dva_before_p <= 14'd0;
      sum_dvb_before_p <= 14'd0;
      sum_dva_after_p <= 14'd0;
      sum_dvb_after_p <= 14'd0;
      sum_dva_before <= 7'd0;
      sum_dvb_before <= 7'd0;
      sum_dva_after <= 7'd0;
      sum_dvb_after <= 7'd0;
      total_cost_before <= 7'd0;
      total_cost_after <= 7'd0;
      fsm_c2n_wr_signal <= 1'd0;
      fsm_n2c_wr_signal <= 1'd0;
      fsm_mem_c2n_wr_addr <= 4'd0;
      fsm_mem_c2n_wr_data <= 5'd0;
      fsm_mem_n2c_wr_addr <= 4'd0;
      fsm_mem_n2c_wr_data <= 4'd0;
      fsm_sa <= CELL_TO_NODES;
    end else begin
      if(start) begin
        fsm_c2n_wr_signal <= 1'd0;
        fsm_n2c_wr_signal <= 1'd0;
        case(fsm_sa)
          SELECT_CELLS: begin
            if(ca == 4'd4) begin
              ca <= 4'd0;
              if(cb == 4'd4) begin
                cb <= 4'd0;
                n_exec_counter <= n_exec_counter + 11'd1;
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
    .wr(mem_c2n_wr),
    .wr_addr(mem_c2n_wr_addr),
    .wr_data(mem_c2n_wr_data)
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
    .rd(1'd1),
    .rd_addr0(na),
    .rd_addr1(nb),
    .out0({ va_v_m[0], va_t[3:0] }),
    .out1({ vb_v_m[0], vb_t[3:0] }),
    .wr(mem_n_wr[0]),
    .wr_addr(mem_n_wr_addr),
    .wr_data(mem_n_wr_data)
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
    .rd(1'd1),
    .rd_addr0(na),
    .rd_addr1(nb),
    .out0({ va_v_m[1], va_t[7:4] }),
    .out1({ vb_v_m[1], vb_t[7:4] }),
    .wr(mem_n_wr[1]),
    .wr_addr(mem_n_wr_addr),
    .wr_data(mem_n_wr_data)
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
    .rd(1'd1),
    .rd_addr0(na),
    .rd_addr1(nb),
    .out0({ va_v_m[2], va_t[11:8] }),
    .out1({ vb_v_m[2], vb_t[11:8] }),
    .wr(mem_n_wr[2]),
    .wr_addr(mem_n_wr_addr),
    .wr_data(mem_n_wr_data)
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
    .rd(1'd1),
    .rd_addr0(na),
    .rd_addr1(nb),
    .out0({ va_v_m[3], va_t[15:12] }),
    .out1({ vb_v_m[3], vb_t[15:12] }),
    .wr(mem_n_wr[3]),
    .wr_addr(mem_n_wr_addr),
    .wr_data(mem_n_wr_data)
  );

  // #####

  // node to cell stage memory instantiation

  mem_2r_1w_width4_depth4
  #(
    .READ_F(1),
    .INIT_FILE("/home/jeronimo/Documentos/GIT/sa_multi/verilog/test_bench_sa_single_0_n_c.rom"),
    .WRITE_F(1),
    .OUTPUT_FILE("/home/jeronimo/Documentos/GIT/sa_multi/verilog/test_bench_sa_single_0_n_c_out0.rom")
  )
  mem_2r_1w_width4_depth4_0
  (
    .clk(clk),
    .rd(1'd1),
    .rd_addr0(va[3:0]),
    .rd_addr1(vb[3:0]),
    .out0(cva_t[3:0]),
    .out1(cvb_t[3:0]),
    .wr(mem_n2c_wr[0]),
    .wr_addr(mem_n2c_wr_addr),
    .wr_data(mem_n2c_wr_data)
  );


  mem_2r_1w_width4_depth4
  #(
    .READ_F(1),
    .INIT_FILE("/home/jeronimo/Documentos/GIT/sa_multi/verilog/test_bench_sa_single_0_n_c.rom"),
    .WRITE_F(0),
    .OUTPUT_FILE("/home/jeronimo/Documentos/GIT/sa_multi/verilog/test_bench_sa_single_0_n_c_out1.rom")
  )
  mem_2r_1w_width4_depth4_1
  (
    .clk(clk),
    .rd(1'd1),
    .rd_addr0(va[7:4]),
    .rd_addr1(vb[7:4]),
    .out0(cva_t[7:4]),
    .out1(cvb_t[7:4]),
    .wr(mem_n2c_wr[1]),
    .wr_addr(mem_n2c_wr_addr),
    .wr_data(mem_n2c_wr_data)
  );


  mem_2r_1w_width4_depth4
  #(
    .READ_F(1),
    .INIT_FILE("/home/jeronimo/Documentos/GIT/sa_multi/verilog/test_bench_sa_single_0_n_c.rom"),
    .WRITE_F(0),
    .OUTPUT_FILE("/home/jeronimo/Documentos/GIT/sa_multi/verilog/test_bench_sa_single_0_n_c_out2.rom")
  )
  mem_2r_1w_width4_depth4_2
  (
    .clk(clk),
    .rd(1'd1),
    .rd_addr0(va[11:8]),
    .rd_addr1(vb[11:8]),
    .out0(cva_t[11:8]),
    .out1(cvb_t[11:8]),
    .wr(mem_n2c_wr[2]),
    .wr_addr(mem_n2c_wr_addr),
    .wr_data(mem_n2c_wr_data)
  );


  mem_2r_1w_width4_depth4
  #(
    .READ_F(1),
    .INIT_FILE("/home/jeronimo/Documentos/GIT/sa_multi/verilog/test_bench_sa_single_0_n_c.rom"),
    .WRITE_F(0),
    .OUTPUT_FILE("/home/jeronimo/Documentos/GIT/sa_multi/verilog/test_bench_sa_single_0_n_c_out3.rom")
  )
  mem_2r_1w_width4_depth4_3
  (
    .clk(clk),
    .rd(1'd1),
    .rd_addr0(va[15:12]),
    .rd_addr1(vb[15:12]),
    .out0(cva_t[15:12]),
    .out1(cvb_t[15:12]),
    .wr(mem_n2c_wr[3]),
    .wr_addr(mem_n2c_wr_addr),
    .wr_data(mem_n2c_wr_data)
  );

  // #####

  // line column finder stage lc_table instantiation

  lc_table_4_4
  lc_table_4_4_c
  (
    .ca(ca),
    .cb(cb),
    .lca(lca_t),
    .lcb(lcb_t)
  );


  lc_table_4_4
  lc_table_4_4_v_0
  (
    .ca(cva[3:0]),
    .cb(cvb[3:0]),
    .lca(lcva_t[3:0]),
    .lcb(lcvb_t[3:0])
  );


  lc_table_4_4
  lc_table_4_4_v_1
  (
    .ca(cva[7:4]),
    .cb(cvb[7:4]),
    .lca(lcva_t[7:4]),
    .lcb(lcvb_t[7:4])
  );


  lc_table_4_4
  lc_table_4_4_v_2
  (
    .ca(cva[11:8]),
    .cb(cvb[11:8]),
    .lca(lcva_t[11:8]),
    .lcb(lcvb_t[11:8])
  );


  lc_table_4_4
  lc_table_4_4_v_3
  (
    .ca(cva[15:12]),
    .cb(cvb[15:12]),
    .lca(lcva_t[15:12]),
    .lcb(lcvb_t[15:12])
  );

  // #####

  // Distance calculator stage distance talbles instantiation
  // Distance before change

  distance_table_4_4
  distance_table_4_4_dac_0
  (
    .opa0(lca_before),
    .opa1(lcva[3:0]),
    .opav(lcva_v[0]),
    .opb0(lca_before),
    .opb1(lcva[7:4]),
    .opbv(lcva_v[1]),
    .da(dva_before_t[6:0]),
    .db(dva_before_t[13:7])
  );


  distance_table_4_4
  distance_table_4_4_dac_1
  (
    .opa0(lca_before),
    .opa1(lcva[11:8]),
    .opav(lcva_v[2]),
    .opb0(lca_before),
    .opb1(lcva[15:12]),
    .opbv(lcva_v[3]),
    .da(dva_before_t[20:14]),
    .db(dva_before_t[27:21])
  );


  distance_table_4_4
  distance_table_4_4_dbc_0
  (
    .opa0(lcb_before),
    .opa1(lcvb[3:0]),
    .opav(lcvb_v[0]),
    .opb0(lcb_before),
    .opb1(lcvb[7:4]),
    .opbv(lcvb_v[1]),
    .da(dvb_before_t[6:0]),
    .db(dvb_before_t[13:7])
  );


  distance_table_4_4
  distance_table_4_4_dbc_1
  (
    .opa0(lcb_before),
    .opa1(lcvb[11:8]),
    .opav(lcvb_v[2]),
    .opb0(lcb_before),
    .opb1(lcvb[15:12]),
    .opbv(lcvb_v[3]),
    .da(dvb_before_t[20:14]),
    .db(dvb_before_t[27:21])
  );


  // Distance after change

  distance_table_4_4
  distance_table_4_4_das_0
  (
    .opa0(lca_after),
    .opa1(opva_after[3:0]),
    .opav(lcva_v[0]),
    .opb0(lca_after),
    .opb1(opva_after[7:4]),
    .opbv(lcva_v[1]),
    .da(dva_after_t[6:0]),
    .db(dva_after_t[13:7])
  );


  distance_table_4_4
  distance_table_4_4_das_1
  (
    .opa0(lca_after),
    .opa1(opva_after[11:8]),
    .opav(lcva_v[2]),
    .opb0(lca_after),
    .opb1(opva_after[15:12]),
    .opbv(lcva_v[3]),
    .da(dva_after_t[20:14]),
    .db(dva_after_t[27:21])
  );


  distance_table_4_4
  distance_table_4_4_dbs_0
  (
    .opa0(lcb_after),
    .opa1(opvb_after[3:0]),
    .opav(lcvb_v[0]),
    .opb0(lcb_after),
    .opb1(opvb_after[7:4]),
    .opbv(lcvb_v[1]),
    .da(dvb_after_t[6:0]),
    .db(dvb_after_t[13:7])
  );


  distance_table_4_4
  distance_table_4_4_dbs_1
  (
    .opa0(lcb_after),
    .opa1(opvb_after[11:8]),
    .opav(lcvb_v[2]),
    .opb0(lcb_after),
    .opb1(opvb_after[15:12]),
    .opbv(lcvb_v[3]),
    .da(dvb_after_t[20:14]),
    .db(dvb_after_t[27:21])
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



module mem_2r_1w_width4_depth4 #
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
  output [4-1:0] out0,
  output [4-1:0] out1,
  input wr,
  input [4-1:0] wr_addr,
  input [4-1:0] wr_data
);

  reg [4-1:0] mem [0:2**4-1];
  assign out0 = (rd)? mem[rd_addr0] : 4'd0;
  assign out1 = (rd)? mem[rd_addr1] : 4'd0;

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



module lc_table_4_4
(
  input [4-1:0] ca,
  input [4-1:0] cb,
  output [4-1:0] lca,
  output [4-1:0] lcb
);

  wire [4-1:0] lc_table [0:16-1];
  assign lca = lc_table[ca];
  assign lcb = lc_table[cb];
  assign lc_table[0] = { 2'd0, 2'd0 };
  assign lc_table[1] = { 2'd0, 2'd1 };
  assign lc_table[2] = { 2'd0, 2'd2 };
  assign lc_table[3] = { 2'd0, 2'd3 };
  assign lc_table[4] = { 2'd1, 2'd0 };
  assign lc_table[5] = { 2'd1, 2'd1 };
  assign lc_table[6] = { 2'd1, 2'd2 };
  assign lc_table[7] = { 2'd1, 2'd3 };
  assign lc_table[8] = { 2'd2, 2'd0 };
  assign lc_table[9] = { 2'd2, 2'd1 };
  assign lc_table[10] = { 2'd2, 2'd2 };
  assign lc_table[11] = { 2'd2, 2'd3 };
  assign lc_table[12] = { 2'd3, 2'd0 };
  assign lc_table[13] = { 2'd3, 2'd1 };
  assign lc_table[14] = { 2'd3, 2'd2 };
  assign lc_table[15] = { 2'd3, 2'd3 };

endmodule



module distance_table_4_4
(
  input [4-1:0] opa0,
  input [4-1:0] opa1,
  input opav,
  input [4-1:0] opb0,
  input [4-1:0] opb1,
  input opbv,
  output [7-1:0] da,
  output [7-1:0] db
);

  wire [7-1:0] dist_table [0:2**4-1];
  wire [7-1:0] da_t;
  wire [7-1:0] db_t;

  assign da_t = dist_table[{ opa1[1:0], opa0[1:0] }] + dist_table[{ opa1[3:2], opa0[3:2] }];
  assign db_t = dist_table[{ opb1[1:0], opb0[1:0] }] + dist_table[{ opb1[3:2], opb0[3:2] }];

  assign da = (opav)? da_t : 0;
  assign db = (opbv)? db_t : 0;

  assign dist_table[0] = 0;
  assign dist_table[1] = 1;
  assign dist_table[2] = 2;
  assign dist_table[3] = 3;
  assign dist_table[4] = 1;
  assign dist_table[5] = 0;
  assign dist_table[6] = 1;
  assign dist_table[7] = 2;
  assign dist_table[8] = 2;
  assign dist_table[9] = 1;
  assign dist_table[10] = 0;
  assign dist_table[11] = 1;
  assign dist_table[12] = 3;
  assign dist_table[13] = 2;
  assign dist_table[14] = 1;
  assign dist_table[15] = 0;

endmodule

