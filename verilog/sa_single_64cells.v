

module sa_single_64cells
(
  input clk,
  input rst,
  input start,
  input [10-1:0] n_exec,
  output reg done,
  input conf_c2n_rd,
  input [6-1:0] conf_c2n_rd_addr,
  output [7-1:0] conf_c2n_rd_data,
  input conf_wr,
  input conf_c2n_wr,
  input [6-1:0] conf_c2n_wr_addr,
  input [7-1:0] conf_c2n_wr_data,
  input [4-1:0] conf_n_wr,
  input [6-1:0] conf_n_wr_addr,
  input [7-1:0] conf_n_wr_data,
  input [4-1:0] conf_n2c_wr,
  input [6-1:0] conf_n2c_wr_addr,
  input [6-1:0] conf_n2c_wr_data
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
  reg [6-1:0] ca;
  reg [6-1:0] cb;
  // #####

  // cell to nodes stage variables
  reg [6-1:0] na;
  reg na_v;
  reg [6-1:0] nb;
  reg nb_v;
  wire [6-1:0] na_t;
  wire na_v_t;
  wire [6-1:0] nb_t;
  wire nb_v_t;
  // #####

  // neighborhood stage variables
  reg [24-1:0] va;
  reg [4-1:0] va_v;
  reg [24-1:0] vb;
  reg [4-1:0] vb_v;
  wire [24-1:0] va_t;
  wire [4-1:0] va_v_t;
  wire [4-1:0] va_v_m;
  wire [24-1:0] vb_t;
  wire [4-1:0] vb_v_t;
  wire [4-1:0] vb_v_m;

  //here we guarantee that only valid nodes can give us neighbors 
  assign va_v_t = (na_v)? va_v_m : 4'b0;
  assign vb_v_t = (nb_v)? vb_v_m : 4'b0;
  // #####

  // node to cell stage variables
  reg [4-1:0] cva_v;
  reg [24-1:0] cva;
  reg [4-1:0] cvb_v;
  reg [24-1:0] cvb;
  wire [4-1:0] cva_v_t;
  wire [24-1:0] cva_t;
  wire [4-1:0] cvb_v_t;
  wire [24-1:0] cvb_t;

  // This is only for legibility
  assign cva_v_t = va_v;
  assign cvb_v_t = vb_v;
  // #####

  // line column finder stage variables
  reg [6-1:0] lca;
  reg [6-1:0] lcb;
  reg [24-1:0] lcva;
  reg [4-1:0] lcva_v;
  reg [24-1:0] lcvb;
  reg [4-1:0] lcvb_v;
  wire [6-1:0] lca_t;
  wire [6-1:0] lcb_t;
  wire [24-1:0] lcva_t;
  wire [24-1:0] lcvb_t;
  // #####

  // Distance calculator stage variables
  // Before changes
  reg [36-1:0] dva_before;
  reg [36-1:0] dvb_before;
  wire [6-1:0] lca_before;
  wire [6-1:0] lcb_before;
  wire [36-1:0] dva_before_t;
  wire [36-1:0] dvb_before_t;

  assign lca_before = lca;
  assign lcb_before = lcb;

  // After changes
  reg [36-1:0] dva_after;
  reg [36-1:0] dvb_after;
  wire [6-1:0] lca_after;
  wire [6-1:0] lcb_after;
  wire [24-1:0] opva_after;
  wire [24-1:0] opvb_after;
  wire [36-1:0] dva_after_t;
  wire [36-1:0] dvb_after_t;

  assign lca_after = lcb;
  assign lcb_after = lca;
  assign opva_after[5:0] = (lcva[5:0] == lca_after)? lcb_after : lcva[5:0];
  assign opva_after[11:6] = (lcva[11:6] == lca_after)? lcb_after : lcva[11:6];
  assign opva_after[17:12] = (lcva[17:12] == lca_after)? lcb_after : lcva[17:12];
  assign opva_after[23:18] = (lcva[23:18] == lca_after)? lcb_after : lcva[23:18];
  assign opvb_after[5:0] = (lcvb[5:0] == lcb_after)? lca_after : lcvb[5:0];
  assign opvb_after[11:6] = (lcvb[11:6] == lcb_after)? lca_after : lcvb[11:6];
  assign opvb_after[17:12] = (lcvb[17:12] == lcb_after)? lca_after : lcvb[17:12];
  assign opvb_after[23:18] = (lcvb[23:18] == lcb_after)? lca_after : lcvb[23:18];
  // #####

  // Sum Reduction stage variables
  // Sum Before change
  reg [18-1:0] sum_dva_before_p;
  wire [18-1:0] sum_dva_before_p_t;
  reg [18-1:0] sum_dvb_before_p;
  wire [18-1:0] sum_dvb_before_p_t;
  reg [9-1:0] sum_dva_before;
  wire [9-1:0] sum_dva_before_t;
  reg [9-1:0] sum_dvb_before;
  wire [9-1:0] sum_dvb_before_t;

  assign sum_dva_before_p_t[8:0] = dva_before[8:0] + dva_before[17:9];
  assign sum_dva_before_p_t[17:9] = dva_before[26:18] + dva_before[35:27];
  assign sum_dvb_before_p_t[8:0] = dvb_before[8:0] + dvb_before[17:9];
  assign sum_dvb_before_p_t[17:9] = dvb_before[26:18] + dvb_before[35:27];
  assign sum_dva_before_t[8:0] = sum_dva_before_p[8:0] + sum_dva_before_p[17:9];
  assign sum_dvb_before_t[8:0] = sum_dvb_before_p[8:0] + sum_dvb_before_p[17:9];

  // Sum after change
  reg [18-1:0] sum_dva_after_p;
  wire [18-1:0] sum_dva_after_p_t;
  reg [18-1:0] sum_dvb_after_p;
  wire [18-1:0] sum_dvb_after_p_t;
  reg [9-1:0] sum_dva_after;
  wire [9-1:0] sum_dva_after_t;
  reg [9-1:0] sum_dvb_after;
  wire [9-1:0] sum_dvb_after_t;

  assign sum_dva_after_p_t[8:0] = dva_after[8:0] + dva_after[17:9];
  assign sum_dva_after_p_t[17:9] = dva_after[26:18] + dva_after[35:27];
  assign sum_dvb_after_p_t[8:0] = dvb_after[8:0] + dvb_after[17:9];
  assign sum_dvb_after_p_t[17:9] = dvb_after[26:18] + dvb_after[35:27];
  assign sum_dva_after_t[8:0] = sum_dva_after_p[8:0] + sum_dva_after_p[17:9];
  assign sum_dvb_after_t[8:0] = sum_dvb_after_p[8:0] + sum_dvb_after_p[17:9];
  // #####

  // Total cost stage variables
  reg [9-1:0] total_cost_before;
  wire [9-1:0] total_cost_before_t;
  reg [9-1:0] total_cost_after;
  wire [9-1:0] total_cost_after_t;

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
  reg [6-1:0] fsm_mem_c2n_wr_addr;
  reg [7-1:0] fsm_mem_c2n_wr_data;
  reg [6-1:0] fsm_mem_n2c_wr_addr;
  reg [6-1:0] fsm_mem_n2c_wr_data;
  wire [6-1:0] mem_c2n_rd_addr;
  wire mem_c2n_wr;
  wire [6-1:0] mem_c2n_wr_addr;
  wire [7-1:0] mem_c2n_wr_data;
  wire [4-1:0] mem_n_wr;
  wire [6-1:0] mem_n_wr_addr;
  wire [7-1:0] mem_n_wr_data;
  wire [4-1:0] mem_n2c_wr;
  wire [6-1:0] mem_n2c_wr_addr;
  wire [6-1:0] mem_n2c_wr_data;

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
      ca <= 6'd0;
      cb <= 6'd0;
      na <= 6'd0;
      na_v <= 1'd0;
      nb <= 6'd0;
      nb_v <= 1'd0;
      va <= 24'd0;
      va_v <= 4'd0;
      vb <= 24'd0;
      vb_v <= 4'd0;
      lca <= 6'd0;
      lcb <= 6'd0;
      lcva <= 24'd0;
      lcva_v <= 4'd0;
      lcvb <= 24'd0;
      lcvb_v <= 4'd0;
      dva_before <= 36'd0;
      dvb_before <= 36'd0;
      dva_after <= 36'd0;
      dvb_after <= 36'd0;
      sum_dva_before_p <= 18'd0;
      sum_dvb_before_p <= 18'd0;
      sum_dva_after_p <= 18'd0;
      sum_dvb_after_p <= 18'd0;
      sum_dva_before <= 9'd0;
      sum_dvb_before <= 9'd0;
      sum_dva_after <= 9'd0;
      sum_dvb_after <= 9'd0;
      total_cost_before <= 9'd0;
      total_cost_after <= 9'd0;
      fsm_c2n_wr_signal <= 1'd0;
      fsm_n2c_wr_signal <= 1'd0;
      fsm_mem_c2n_wr_addr <= 6'd0;
      fsm_mem_c2n_wr_data <= 7'd0;
      fsm_mem_n2c_wr_addr <= 6'd0;
      fsm_mem_n2c_wr_data <= 6'd0;
      fsm_sa <= CELL_TO_NODES;
    end else begin
      if(start) begin
        fsm_c2n_wr_signal <= 1'd0;
        fsm_n2c_wr_signal <= 1'd0;
        case(fsm_sa)
          SELECT_CELLS: begin
            if(ca == 6'd8) begin
              ca <= 6'd0;
              if(cb == 6'd8) begin
                cb <= 6'd0;
                n_exec_counter <= n_exec_counter + 11'd1;
                fsm_sa <= END;
              end else begin
                cb <= cb + 6'd1;
                fsm_sa <= CELL_TO_NODES;
              end
            end else begin
              ca <= ca + 6'd1;
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

  mem_2r_1w_width7_depth6
  #(
    .READ_F(1),
    .INIT_FILE("/home/jeronimo/Documentos/GIT/sa_multi/verilog/test_bench_sa_single_0_c_n.rom"),
    .WRITE_F(1),
    .OUTPUT_FILE("/home/jeronimo/Documentos/GIT/sa_multi/verilog/test_bench_sa_single_0_c_n_out.rom")
  )
  mem_2r_1w_width7_depth6
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

  mem_2r_1w_width7_depth6
  #(
    .READ_F(1),
    .INIT_FILE("/home/jeronimo/Documentos/GIT/sa_multi/verilog/test_bench_sa_single_0_n0.rom"),
    .WRITE_F(0)
  )
  mem_2r_1w_width7_depth6_0
  (
    .clk(clk),
    .rd(1'd1),
    .rd_addr0(na),
    .rd_addr1(nb),
    .out0({ va_v_m[0], va_t[5:0] }),
    .out1({ vb_v_m[0], vb_t[5:0] }),
    .wr(mem_n_wr[0]),
    .wr_addr(mem_n_wr_addr),
    .wr_data(mem_n_wr_data)
  );


  mem_2r_1w_width7_depth6
  #(
    .READ_F(1),
    .INIT_FILE("/home/jeronimo/Documentos/GIT/sa_multi/verilog/test_bench_sa_single_0_n1.rom"),
    .WRITE_F(0)
  )
  mem_2r_1w_width7_depth6_1
  (
    .clk(clk),
    .rd(1'd1),
    .rd_addr0(na),
    .rd_addr1(nb),
    .out0({ va_v_m[1], va_t[11:6] }),
    .out1({ vb_v_m[1], vb_t[11:6] }),
    .wr(mem_n_wr[1]),
    .wr_addr(mem_n_wr_addr),
    .wr_data(mem_n_wr_data)
  );


  mem_2r_1w_width7_depth6
  #(
    .READ_F(1),
    .INIT_FILE("/home/jeronimo/Documentos/GIT/sa_multi/verilog/test_bench_sa_single_0_n2.rom"),
    .WRITE_F(0)
  )
  mem_2r_1w_width7_depth6_2
  (
    .clk(clk),
    .rd(1'd1),
    .rd_addr0(na),
    .rd_addr1(nb),
    .out0({ va_v_m[2], va_t[17:12] }),
    .out1({ vb_v_m[2], vb_t[17:12] }),
    .wr(mem_n_wr[2]),
    .wr_addr(mem_n_wr_addr),
    .wr_data(mem_n_wr_data)
  );


  mem_2r_1w_width7_depth6
  #(
    .READ_F(1),
    .INIT_FILE("/home/jeronimo/Documentos/GIT/sa_multi/verilog/test_bench_sa_single_0_n3.rom"),
    .WRITE_F(0)
  )
  mem_2r_1w_width7_depth6_3
  (
    .clk(clk),
    .rd(1'd1),
    .rd_addr0(na),
    .rd_addr1(nb),
    .out0({ va_v_m[3], va_t[23:18] }),
    .out1({ vb_v_m[3], vb_t[23:18] }),
    .wr(mem_n_wr[3]),
    .wr_addr(mem_n_wr_addr),
    .wr_data(mem_n_wr_data)
  );

  // #####

  // node to cell stage memory instantiation

  mem_2r_1w_width6_depth6
  #(
    .READ_F(1),
    .INIT_FILE("/home/jeronimo/Documentos/GIT/sa_multi/verilog/test_bench_sa_single_0_n_c.rom"),
    .WRITE_F(1),
    .OUTPUT_FILE("/home/jeronimo/Documentos/GIT/sa_multi/verilog/test_bench_sa_single_0_n_c_out0.rom")
  )
  mem_2r_1w_width6_depth6_0
  (
    .clk(clk),
    .rd(1'd1),
    .rd_addr0(va[5:0]),
    .rd_addr1(vb[5:0]),
    .out0(cva_t[5:0]),
    .out1(cvb_t[5:0]),
    .wr(mem_n2c_wr[0]),
    .wr_addr(mem_n2c_wr_addr),
    .wr_data(mem_n2c_wr_data)
  );


  mem_2r_1w_width6_depth6
  #(
    .READ_F(1),
    .INIT_FILE("/home/jeronimo/Documentos/GIT/sa_multi/verilog/test_bench_sa_single_0_n_c.rom"),
    .WRITE_F(0),
    .OUTPUT_FILE("/home/jeronimo/Documentos/GIT/sa_multi/verilog/test_bench_sa_single_0_n_c_out1.rom")
  )
  mem_2r_1w_width6_depth6_1
  (
    .clk(clk),
    .rd(1'd1),
    .rd_addr0(va[11:6]),
    .rd_addr1(vb[11:6]),
    .out0(cva_t[11:6]),
    .out1(cvb_t[11:6]),
    .wr(mem_n2c_wr[1]),
    .wr_addr(mem_n2c_wr_addr),
    .wr_data(mem_n2c_wr_data)
  );


  mem_2r_1w_width6_depth6
  #(
    .READ_F(1),
    .INIT_FILE("/home/jeronimo/Documentos/GIT/sa_multi/verilog/test_bench_sa_single_0_n_c.rom"),
    .WRITE_F(0),
    .OUTPUT_FILE("/home/jeronimo/Documentos/GIT/sa_multi/verilog/test_bench_sa_single_0_n_c_out2.rom")
  )
  mem_2r_1w_width6_depth6_2
  (
    .clk(clk),
    .rd(1'd1),
    .rd_addr0(va[17:12]),
    .rd_addr1(vb[17:12]),
    .out0(cva_t[17:12]),
    .out1(cvb_t[17:12]),
    .wr(mem_n2c_wr[2]),
    .wr_addr(mem_n2c_wr_addr),
    .wr_data(mem_n2c_wr_data)
  );


  mem_2r_1w_width6_depth6
  #(
    .READ_F(1),
    .INIT_FILE("/home/jeronimo/Documentos/GIT/sa_multi/verilog/test_bench_sa_single_0_n_c.rom"),
    .WRITE_F(0),
    .OUTPUT_FILE("/home/jeronimo/Documentos/GIT/sa_multi/verilog/test_bench_sa_single_0_n_c_out3.rom")
  )
  mem_2r_1w_width6_depth6_3
  (
    .clk(clk),
    .rd(1'd1),
    .rd_addr0(va[23:18]),
    .rd_addr1(vb[23:18]),
    .out0(cva_t[23:18]),
    .out1(cvb_t[23:18]),
    .wr(mem_n2c_wr[3]),
    .wr_addr(mem_n2c_wr_addr),
    .wr_data(mem_n2c_wr_data)
  );

  // #####

  // line column finder stage lc_table instantiation

  lc_table_8_8
  lc_table_8_8_c
  (
    .ca(ca),
    .cb(cb),
    .lca(lca_t),
    .lcb(lcb_t)
  );


  lc_table_8_8
  lc_table_8_8_v_0
  (
    .ca(cva[5:0]),
    .cb(cvb[5:0]),
    .lca(lcva_t[5:0]),
    .lcb(lcvb_t[5:0])
  );


  lc_table_8_8
  lc_table_8_8_v_1
  (
    .ca(cva[11:6]),
    .cb(cvb[11:6]),
    .lca(lcva_t[11:6]),
    .lcb(lcvb_t[11:6])
  );


  lc_table_8_8
  lc_table_8_8_v_2
  (
    .ca(cva[17:12]),
    .cb(cvb[17:12]),
    .lca(lcva_t[17:12]),
    .lcb(lcvb_t[17:12])
  );


  lc_table_8_8
  lc_table_8_8_v_3
  (
    .ca(cva[23:18]),
    .cb(cvb[23:18]),
    .lca(lcva_t[23:18]),
    .lcb(lcvb_t[23:18])
  );

  // #####

  // Distance calculator stage distance talbles instantiation
  // Distance before change

  distance_table_8_8
  distance_table_8_8_dac_0
  (
    .opa0(lca_before),
    .opa1(lcva[5:0]),
    .opav(lcva_v[0]),
    .opb0(lca_before),
    .opb1(lcva[11:6]),
    .opbv(lcva_v[1]),
    .da(dva_before_t[8:0]),
    .db(dva_before_t[17:9])
  );


  distance_table_8_8
  distance_table_8_8_dac_1
  (
    .opa0(lca_before),
    .opa1(lcva[17:12]),
    .opav(lcva_v[2]),
    .opb0(lca_before),
    .opb1(lcva[23:18]),
    .opbv(lcva_v[3]),
    .da(dva_before_t[26:18]),
    .db(dva_before_t[35:27])
  );


  distance_table_8_8
  distance_table_8_8_dbc_0
  (
    .opa0(lcb_before),
    .opa1(lcvb[5:0]),
    .opav(lcvb_v[0]),
    .opb0(lcb_before),
    .opb1(lcvb[11:6]),
    .opbv(lcvb_v[1]),
    .da(dvb_before_t[8:0]),
    .db(dvb_before_t[17:9])
  );


  distance_table_8_8
  distance_table_8_8_dbc_1
  (
    .opa0(lcb_before),
    .opa1(lcvb[17:12]),
    .opav(lcvb_v[2]),
    .opb0(lcb_before),
    .opb1(lcvb[23:18]),
    .opbv(lcvb_v[3]),
    .da(dvb_before_t[26:18]),
    .db(dvb_before_t[35:27])
  );


  // Distance after change

  distance_table_8_8
  distance_table_8_8_das_0
  (
    .opa0(lca_after),
    .opa1(opva_after[5:0]),
    .opav(lcva_v[0]),
    .opb0(lca_after),
    .opb1(opva_after[11:6]),
    .opbv(lcva_v[1]),
    .da(dva_after_t[8:0]),
    .db(dva_after_t[17:9])
  );


  distance_table_8_8
  distance_table_8_8_das_1
  (
    .opa0(lca_after),
    .opa1(opva_after[17:12]),
    .opav(lcva_v[2]),
    .opb0(lca_after),
    .opb1(opva_after[23:18]),
    .opbv(lcva_v[3]),
    .da(dva_after_t[26:18]),
    .db(dva_after_t[35:27])
  );


  distance_table_8_8
  distance_table_8_8_dbs_0
  (
    .opa0(lcb_after),
    .opa1(opvb_after[5:0]),
    .opav(lcvb_v[0]),
    .opb0(lcb_after),
    .opb1(opvb_after[11:6]),
    .opbv(lcvb_v[1]),
    .da(dvb_after_t[8:0]),
    .db(dvb_after_t[17:9])
  );


  distance_table_8_8
  distance_table_8_8_dbs_1
  (
    .opa0(lcb_after),
    .opa1(opvb_after[17:12]),
    .opav(lcvb_v[2]),
    .opb0(lcb_after),
    .opb1(opvb_after[23:18]),
    .opbv(lcvb_v[3]),
    .da(dvb_after_t[26:18]),
    .db(dvb_after_t[35:27])
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



module mem_2r_1w_width7_depth6 #
(
  parameter READ_F = 0,
  parameter INIT_FILE = "mem_file.txt",
  parameter WRITE_F = 0,
  parameter OUTPUT_FILE = "mem_out_file.txt"
)
(
  input clk,
  input rd,
  input [6-1:0] rd_addr0,
  input [6-1:0] rd_addr1,
  output [7-1:0] out0,
  output [7-1:0] out1,
  input wr,
  input [6-1:0] wr_addr,
  input [7-1:0] wr_data
);

  reg [7-1:0] mem [0:2**6-1];
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



module mem_2r_1w_width6_depth6 #
(
  parameter READ_F = 0,
  parameter INIT_FILE = "mem_file.txt",
  parameter WRITE_F = 0,
  parameter OUTPUT_FILE = "mem_out_file.txt"
)
(
  input clk,
  input rd,
  input [6-1:0] rd_addr0,
  input [6-1:0] rd_addr1,
  output [6-1:0] out0,
  output [6-1:0] out1,
  input wr,
  input [6-1:0] wr_addr,
  input [6-1:0] wr_data
);

  reg [6-1:0] mem [0:2**6-1];
  assign out0 = (rd)? mem[rd_addr0] : 6'd0;
  assign out1 = (rd)? mem[rd_addr1] : 6'd0;

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



module lc_table_8_8
(
  input [6-1:0] ca,
  input [6-1:0] cb,
  output [6-1:0] lca,
  output [6-1:0] lcb
);

  wire [6-1:0] lc_table [0:64-1];
  assign lca = lc_table[ca];
  assign lcb = lc_table[cb];
  assign lc_table[0] = { 3'd0, 3'd0 };
  assign lc_table[1] = { 3'd0, 3'd1 };
  assign lc_table[2] = { 3'd0, 3'd2 };
  assign lc_table[3] = { 3'd0, 3'd3 };
  assign lc_table[4] = { 3'd0, 3'd4 };
  assign lc_table[5] = { 3'd0, 3'd5 };
  assign lc_table[6] = { 3'd0, 3'd6 };
  assign lc_table[7] = { 3'd0, 3'd7 };
  assign lc_table[8] = { 3'd1, 3'd0 };
  assign lc_table[9] = { 3'd1, 3'd1 };
  assign lc_table[10] = { 3'd1, 3'd2 };
  assign lc_table[11] = { 3'd1, 3'd3 };
  assign lc_table[12] = { 3'd1, 3'd4 };
  assign lc_table[13] = { 3'd1, 3'd5 };
  assign lc_table[14] = { 3'd1, 3'd6 };
  assign lc_table[15] = { 3'd1, 3'd7 };
  assign lc_table[16] = { 3'd2, 3'd0 };
  assign lc_table[17] = { 3'd2, 3'd1 };
  assign lc_table[18] = { 3'd2, 3'd2 };
  assign lc_table[19] = { 3'd2, 3'd3 };
  assign lc_table[20] = { 3'd2, 3'd4 };
  assign lc_table[21] = { 3'd2, 3'd5 };
  assign lc_table[22] = { 3'd2, 3'd6 };
  assign lc_table[23] = { 3'd2, 3'd7 };
  assign lc_table[24] = { 3'd3, 3'd0 };
  assign lc_table[25] = { 3'd3, 3'd1 };
  assign lc_table[26] = { 3'd3, 3'd2 };
  assign lc_table[27] = { 3'd3, 3'd3 };
  assign lc_table[28] = { 3'd3, 3'd4 };
  assign lc_table[29] = { 3'd3, 3'd5 };
  assign lc_table[30] = { 3'd3, 3'd6 };
  assign lc_table[31] = { 3'd3, 3'd7 };
  assign lc_table[32] = { 3'd4, 3'd0 };
  assign lc_table[33] = { 3'd4, 3'd1 };
  assign lc_table[34] = { 3'd4, 3'd2 };
  assign lc_table[35] = { 3'd4, 3'd3 };
  assign lc_table[36] = { 3'd4, 3'd4 };
  assign lc_table[37] = { 3'd4, 3'd5 };
  assign lc_table[38] = { 3'd4, 3'd6 };
  assign lc_table[39] = { 3'd4, 3'd7 };
  assign lc_table[40] = { 3'd5, 3'd0 };
  assign lc_table[41] = { 3'd5, 3'd1 };
  assign lc_table[42] = { 3'd5, 3'd2 };
  assign lc_table[43] = { 3'd5, 3'd3 };
  assign lc_table[44] = { 3'd5, 3'd4 };
  assign lc_table[45] = { 3'd5, 3'd5 };
  assign lc_table[46] = { 3'd5, 3'd6 };
  assign lc_table[47] = { 3'd5, 3'd7 };
  assign lc_table[48] = { 3'd6, 3'd0 };
  assign lc_table[49] = { 3'd6, 3'd1 };
  assign lc_table[50] = { 3'd6, 3'd2 };
  assign lc_table[51] = { 3'd6, 3'd3 };
  assign lc_table[52] = { 3'd6, 3'd4 };
  assign lc_table[53] = { 3'd6, 3'd5 };
  assign lc_table[54] = { 3'd6, 3'd6 };
  assign lc_table[55] = { 3'd6, 3'd7 };
  assign lc_table[56] = { 3'd7, 3'd0 };
  assign lc_table[57] = { 3'd7, 3'd1 };
  assign lc_table[58] = { 3'd7, 3'd2 };
  assign lc_table[59] = { 3'd7, 3'd3 };
  assign lc_table[60] = { 3'd7, 3'd4 };
  assign lc_table[61] = { 3'd7, 3'd5 };
  assign lc_table[62] = { 3'd7, 3'd6 };
  assign lc_table[63] = { 3'd7, 3'd7 };

endmodule



module distance_table_8_8
(
  input [6-1:0] opa0,
  input [6-1:0] opa1,
  input opav,
  input [6-1:0] opb0,
  input [6-1:0] opb1,
  input opbv,
  output [9-1:0] da,
  output [9-1:0] db
);

  wire [9-1:0] dist_table [0:2**6-1];
  wire [9-1:0] da_t;
  wire [9-1:0] db_t;

  assign da_t = dist_table[{ opa1[2:0], opa0[2:0] }] + dist_table[{ opa1[5:3], opa0[5:3] }];
  assign db_t = dist_table[{ opb1[2:0], opb0[2:0] }] + dist_table[{ opb1[5:3], opb0[5:3] }];

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
  assign dist_table[8] = 1;
  assign dist_table[9] = 0;
  assign dist_table[10] = 1;
  assign dist_table[11] = 2;
  assign dist_table[12] = 3;
  assign dist_table[13] = 4;
  assign dist_table[14] = 5;
  assign dist_table[15] = 6;
  assign dist_table[16] = 2;
  assign dist_table[17] = 1;
  assign dist_table[18] = 0;
  assign dist_table[19] = 1;
  assign dist_table[20] = 2;
  assign dist_table[21] = 3;
  assign dist_table[22] = 4;
  assign dist_table[23] = 5;
  assign dist_table[24] = 3;
  assign dist_table[25] = 2;
  assign dist_table[26] = 1;
  assign dist_table[27] = 0;
  assign dist_table[28] = 1;
  assign dist_table[29] = 2;
  assign dist_table[30] = 3;
  assign dist_table[31] = 4;
  assign dist_table[32] = 4;
  assign dist_table[33] = 3;
  assign dist_table[34] = 2;
  assign dist_table[35] = 1;
  assign dist_table[36] = 0;
  assign dist_table[37] = 1;
  assign dist_table[38] = 2;
  assign dist_table[39] = 3;
  assign dist_table[40] = 5;
  assign dist_table[41] = 4;
  assign dist_table[42] = 3;
  assign dist_table[43] = 2;
  assign dist_table[44] = 1;
  assign dist_table[45] = 0;
  assign dist_table[46] = 1;
  assign dist_table[47] = 2;
  assign dist_table[48] = 6;
  assign dist_table[49] = 5;
  assign dist_table[50] = 4;
  assign dist_table[51] = 3;
  assign dist_table[52] = 2;
  assign dist_table[53] = 1;
  assign dist_table[54] = 0;
  assign dist_table[55] = 1;
  assign dist_table[56] = 7;
  assign dist_table[57] = 6;
  assign dist_table[58] = 5;
  assign dist_table[59] = 4;
  assign dist_table[60] = 3;
  assign dist_table[61] = 2;
  assign dist_table[62] = 1;
  assign dist_table[63] = 0;

endmodule

