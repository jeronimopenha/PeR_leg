

module yoto_pipeline_hw
(
  input clk,
  input rst,
  input start,
  input [4-1:0] visited_edges,
  output done
);

  // St0 wires
  wire [4-1:0] st0_thread_index;
  wire st0_thread_valid;
  wire st0_should_write;
  wire st0_fifo_write_enable;
  wire [5-1:0] st0_fifo_input_data;
  // -----

  // St1 wires
  wire [4-1:0] st1_thread_index;
  wire st1_thread_valid;
  wire [4-1:0] st1_edge_index;
  // -----

  // St2 wires
  wire [4-1:0] st2_thread_index;
  wire st2_thread_valid;
  wire [4-1:0] st2_a;
  wire [4-1:0] st2_b;
  wire [12-1:0] st2_cs;
  wire [9-1:0] st2_dist_csb;
  wire [4-1:0] st2_index_list_edge;
  // -----

  // St3 wires
  wire [4-1:0] st3_thread_index;
  wire st3_thread_valid;
  wire [4-1:0] st3_c_a;
  wire [4-1:0] st3_b;
  wire [12-1:0] st3_cs_c;
  wire [9-1:0] st3_dist_csb;
  wire [4-1:0] st3_adj_index;
  wire [4-1:0] st3_index_list_edge;
  // -----

  // St4 wires
  // -----

  // St5 wires
  // -----

  // St6 wires
  // -----

  // St7 wires
  // -----

  // St8 wires
  // -----

  // St9 wires
  wire [4-1:0] st9_thread_index;
  wire [4-1:0] st9_thread_valid;
  wire s9_should_write;
  wire [4-1:0] st9_b;
  wire [2-1:0] st9_cs_i;
  wire [2-1:0] st9_cs_j;
  // -----

  // St10 wires
  // -----

  // St0 instantiation

  stage0_yott
  stage0_yott
  (
    .clk(clk),
    .rst(rst),
    .start(start),
    .thread_index(st0_thread_index),
    .thread_valid(st0_thread_valid),
    .should_write(st0_should_write),
    .fifo_write_enable(st0_fifo_write_enable),
    .fifo_input_data(st0_fifo_input_data)
  );

  // -----
  // St1 instantiation

  stage1_yott
  stage1_yott
  (
    .clk(clk),
    .rst(rst),
    .st0_thread_index(st0_thread_index),
    .st0_thread_valid(st0_thread_valid),
    .st0_should_write(st0_should_write),
    .visited_edges(visited_edges),
    .thread_index(st1_thread_index),
    .thread_valid(st1_thread_valid),
    .edge_index(st1_edge_index),
    .done(done)
  );

  // -----
  // St2 instantiation

  stage2_yott
  stage2_yott
  (
    .clk(clk),
    .rst(rst),
    .st1_thread_index(st1_thread_index),
    .st1_thread_valid(st1_thread_valid),
    .st1_edge_index(st1_edge_index),
    .thread_index(st2_thread_index),
    .thread_valid(st2_thread_valid),
    .a(st2_a),
    .b(st2_b),
    .cs(st2_cs),
    .dist_csb(st2_dist_csb),
    .index_list_edge(st2_index_list_edge)
  );

  // -----
  // St3 instantiation

  stage3_yott
  stage3_yott
  (
    .clk(clk),
    .rst(rst),
    .st2_thread_index(st2_thread_index),
    .st2_thread_valid(st2_thread_valid),
    .st2_a(st2_a),
    .st2_b(st2_b),
    .st2_cs(st2_cs),
    .st2_dist_csb(st2_dist_csb),
    .st2_index_list_edge(st2_index_list_edge),
    .thread_index(st3_thread_index),
    .thread_valid(st3_thread_valid),
    .c_a(st3_c_a),
    .b(st3_b),
    .cs_c(st3_cs_c),
    .dist_csb(st3_dist_csb),
    .adj_index(st3_adj_index),
    .index_list_edge(st3_index_list_edge),
    .st9_thread_index(st9_thread_index),
    .st9_thread_valid(st9_thread_valid),
    .s9_should_write(s9_should_write),
    .st9_b(st9_b),
    .st9_cs_j(st9_cs_j),
    .st9_cs_i(st9_cs_i)
  );

  // -----
  // St4 instantiation
  // -----
  // St5 instantiation
  // -----
  // St6 instantiation
  // -----
  // St7 instantiation
  // -----
  // St8 instantiation
  // -----
  // St9 instantiation
  // -----
  // St10 instantiation
  // -----

endmodule



module stage0_yott
(
  input clk,
  input rst,
  input start,
  output [4-1:0] thread_index,
  output thread_valid,
  output should_write,
  input fifo_write_enable,
  input [5-1:0] fifo_input_data
);

  reg fifo_output_read_enable;
  wire fifo_output_valid;
  wire [5-1:0] fifo_output_data;
  wire fifo_empty;
  wire fifo_almostempty;
  wire fifo_full;
  wire fifo_almostfull;
  wire [6-1:0] fifo_data_count;
  reg flag_wait;

  assign thread_index = fifo_output_data[4:1];
  assign thread_valid = fifo_output_valid;
  assign should_write = fifo_output_data[0];

  always @(posedge clk) begin
    if(rst) begin
      fifo_output_read_enable <= 1'b0;
      flag_wait <= 1'b0;
    end else begin
      if(start) begin
        fifo_output_read_enable <= 1'b0;
        if(fifo_almostempty) begin
          if(~flag_wait) begin
            fifo_output_read_enable <= 1'b1;
          end 
          flag_wait <= ~flag_wait;
        end else if(~fifo_empty) begin
          fifo_output_read_enable <= 1'b1;
        end 
      end 
    end
  end


  fifo
  #(
    .FIFO_WIDTH(5),
    .FIFO_DEPTH_BITS(5),
    .FIFO_ALMOSTFULL_THRESHOLD(2 ** 5 - 4),
    .FIFO_ALMOSTEMPTY_THRESHOLD(4)
  )
  fifo
  (
    .clk(clk),
    .rst(rst),
    .write_enable(fifo_write_enable),
    .input_data(fifo_input_data),
    .output_read_enable(fifo_write_enable),
    .output_valid(fifo_output_valid),
    .output_data(fifo_output_data),
    .empty(fifo_empty),
    .almostempty(fifo_almostempty),
    .full(fifo_full),
    .almostfull(fifo_almostfull),
    .data_count(fifo_data_count)
  );


  initial begin
    fifo_output_read_enable = 0;
    flag_wait = 0;
  end


endmodule



module fifo #
(
  parameter FIFO_WIDTH = 32,
  parameter FIFO_DEPTH_BITS = 8,
  parameter FIFO_ALMOSTFULL_THRESHOLD = 2 ** FIFO_DEPTH_BITS - 4,
  parameter FIFO_ALMOSTEMPTY_THRESHOLD = 4
)
(
  input clk,
  input rst,
  input write_enable,
  input [FIFO_WIDTH-1:0] input_data,
  input output_read_enable,
  output reg output_valid,
  output reg [FIFO_WIDTH-1:0] output_data,
  output reg empty,
  output reg almostempty,
  output reg full,
  output reg almostfull,
  output reg [FIFO_DEPTH_BITS+1-1:0] data_count
);

  reg [FIFO_DEPTH_BITS-1:0] read_pointer;
  reg [FIFO_DEPTH_BITS-1:0] write_pointer;
  reg [FIFO_WIDTH-1:0] mem [0:2**FIFO_DEPTH_BITS-1];

  always @(posedge clk) begin
    if(rst) begin
      empty <= 1;
      almostempty <= 1;
      full <= 0;
      almostfull <= 0;
      read_pointer <= 0;
      write_pointer <= 0;
      data_count <= 0;
    end else begin
      case({ write_enable, output_read_enable })
        3: begin
          read_pointer <= read_pointer + 1;
          write_pointer <= write_pointer + 1;
        end
        2: begin
          if(~full) begin
            write_pointer <= write_pointer + 1;
            data_count <= data_count + 1;
            empty <= 0;
            if(data_count == FIFO_ALMOSTEMPTY_THRESHOLD - 1) begin
              almostempty <= 0;
            end 
            if(data_count == 2 ** FIFO_DEPTH_BITS - 1) begin
              full <= 1;
            end 
            if(data_count == FIFO_ALMOSTFULL_THRESHOLD - 1) begin
              almostfull <= 1;
            end 
          end 
        end
        1: begin
          if(~empty) begin
            read_pointer <= read_pointer + 1;
            data_count <= data_count - 1;
            full <= 0;
            if(data_count == FIFO_ALMOSTFULL_THRESHOLD) begin
              almostfull <= 0;
            end 
            if(data_count == 1) begin
              empty <= 1;
            end 
            if(data_count == FIFO_ALMOSTEMPTY_THRESHOLD) begin
              almostempty <= 1;
            end 
          end 
        end
      endcase
    end
  end


  always @(posedge clk) begin
    if(rst) begin
      output_valid <= 0;
    end else begin
      output_valid <= 0;
      if(write_enable == 1) begin
        mem[write_pointer] <= input_data;
      end 
      if(output_read_enable == 1) begin
        output_data <= mem[read_pointer];
        output_valid <= 1;
      end 
    end
  end


endmodule



module stage1_yott
(
  input clk,
  input rst,
  input [4-1:0] st0_thread_index,
  input st0_thread_valid,
  input st0_should_write,
  input [4-1:0] visited_edges,
  output reg [4-1:0] thread_index,
  output reg thread_valid,
  output reg [4-1:0] edge_index,
  output reg done
);

  reg [10-1:0] thread_done;
  reg [4-1:0] edges_indexes [0:10-1];
  wire [4-1:0] next_edge_index;
  wire done_flag;
  reg running;

  assign next_edge_index = edges_indexes[thread_index] + { 3'd0, st0_should_write };
  assign done_flag = next_edge_index == visited_edges;

  always @(posedge clk) begin
    if(rst) begin
      edge_index <= 4'd0;
      thread_done <= 10'd0;
      running <= 1'd0;
      done <= 1'd0;
      thread_valid <= 1'd0;
    end else begin
      thread_valid <= st0_thread_valid;
      thread_index <= st0_thread_index;
      if(st0_thread_valid) begin
        if(st0_thread_index == 4'd9) begin
          running <= 1'd1;
        end 
        if(~running) begin
          edges_indexes[st0_thread_index] <= 5'd0;
        end else begin
          edges_indexes[st0_thread_index] <= next_edge_index;
          edge_index <= next_edge_index;
        end
        if(done_flag) begin
          thread_done[st0_thread_index] <= 1'd1;
        end 
        if(&thread_done) begin
          done <= 1'd1;
        end 
      end 
    end
  end

  integer i_initial;

  initial begin
    thread_index = 0;
    thread_valid = 0;
    edge_index = 0;
    done = 0;
    thread_done = 0;
    for(i_initial=0; i_initial<10; i_initial=i_initial+1) begin
      edges_indexes[i_initial] = 0;
    end
    running = 0;
  end


endmodule



module stage2_yott
(
  input clk,
  input rst,
  input [4-1:0] st1_thread_index,
  input st1_thread_valid,
  input [4-1:0] st1_edge_index,
  output reg [4-1:0] thread_index,
  output reg thread_valid,
  output reg [4-1:0] a,
  output reg [4-1:0] b,
  output reg [12-1:0] cs,
  output reg [9-1:0] dist_csb,
  output reg [4-1:0] index_list_edge
);

  wire [4-1:0] a_t;
  wire [4-1:0] b_t;
  wire [12-1:0] cs_t;
  wire [9-1:0] dist_csb_t;

  always @(posedge rst) begin
    if(rst) begin
      thread_index <= 4'd0;
      thread_valid <= 1'd0;
      index_list_edge <= 4'd0;
      a <= 4'd0;
      b <= 4'd0;
      cs <= 12'd0;
      dist_csb <= 9'd0;
    end else begin
      thread_index <= st1_thread_index;
      thread_valid <= st1_thread_valid;
      a <= a_t;
      b <= b_t;
      cs <= cs_t;
      dist_csb <= dist_csb_t;
      index_list_edge <= st1_thread_index ^ st1_edge_index;
    end
  end


  mem_1r_1w
  #(
    .width(8),
    .depth(8),
    .read_f(1),
    .init_file("")
  )
  mem_1r_1w_edges
  (
    .clk(clk),
    .rd_addr({ st1_thread_index, st1_edge_index }),
    .out({ a_t, b_t }),
    .rd(1'b1)
  );


  mem_1r_1w
  #(
    .width(21),
    .depth(8),
    .read_f(1),
    .init_file("")
  )
  mem_1r_1w_annotations
  (
    .clk(clk),
    .rd_addr({ st1_thread_index, st1_edge_index }),
    .out({ cs_t, dist_csb_t }),
    .rd(1'b1)
  );


  initial begin
    thread_index = 0;
    thread_valid = 0;
    a = 0;
    b = 0;
    cs = 0;
    dist_csb = 0;
    index_list_edge = 0;
  end


endmodule



module mem_1r_1w #
(
  parameter width = 8,
  parameter depth = 4,
  parameter read_f = 0,
  parameter init_file = "mem_file.txt",
  parameter write_f = 0,
  parameter output_file = "mem_out_file.txt"
)
(
  input clk,
  input rd,
  input [depth-1:0] rd_addr,
  output reg [width-1:0] out,
  input wr,
  input [depth-1:0] wr_addr,
  input [width-1:0] wr_data
);

  (* ram_style = "M20K" *) reg [width-1:0] mem[0:2**depth-1];
  /*
  reg [width-1:0] mem [0:2**depth-1];
  */

  always @(posedge clk) begin
    if(wr) begin
      mem[wr_addr] <= wr_data;
    end 
    if(rd) begin
      out <= mem[rd_addr];
    end 
  end


endmodule



module stage3_yott
(
  input clk,
  input rst,
  input [4-1:0] st2_thread_index,
  input st2_thread_valid,
  input [4-1:0] st2_a,
  input [4-1:0] st2_b,
  input [12-1:0] st2_cs,
  input [9-1:0] st2_dist_csb,
  input [4-1:0] st2_index_list_edge,
  output reg [4-1:0] thread_index,
  output reg thread_valid,
  output reg [4-1:0] c_a,
  output reg [4-1:0] b,
  output reg [12-1:0] cs_c,
  output reg [9-1:0] dist_csb,
  output reg [4-1:0] adj_index,
  output reg [4-1:0] index_list_edge,
  input [4-1:0] st9_thread_index,
  input [4-1:0] st9_thread_valid,
  input s9_should_write,
  input [4-1:0] st9_b,
  input [2-1:0] st9_cs_i,
  input [2-1:0] st9_cs_j,
  input conf_wr,
  input [8-1:0] conf_wr_addr,
  input [4-1:0] conf_wr_data,
  input conf_rd,
  input [8-1:0] conf_rd_addr,
  output [4-1:0] conf_rd_data
);

  reg [4-1:0] thread_adj_indexes_r [0:10-1];
  wire [4-1:0] c_a_t;
  wire [12-1:0] cs_c_t;

  always @(posedge clk) begin
    if(rst) begin
      thread_index <= 4'd0;
      thread_valid <= 1'd0;
      c_a <= 4'd0;
      b <= 4'd0;
      cs_c <= 12'd0;
      dist_csb <= 9'd0;
      adj_index <= 4'd0;
      index_list_edge <= 4'd0;
    end else begin
      thread_index <= st2_thread_index;
      thread_valid <= st2_thread_valid;
      b <= st2_b;
      c_a <= c_a_t;
      cs_c <= cs_c_t;
      dist_csb <= st2_dist_csb;
      index_list_edge <= st2_index_list_edge;
      if(st2_thread_valid) begin
        adj_index <= thread_adj_indexes_r[st2_thread_index];
      end else begin
        adj_index <= 4'd0;
      end
      if(~s9_should_write && st9_thread_valid) begin
        thread_adj_indexes_r[st9_thread_index] <= thread_adj_indexes_r[st9_thread_index] + 4'd1;
      end 
    end
  end

  assign conf_rd_data = c_a_t;
  wire [8-1:0] mem_rd_addr0;
  wire [8-1:0] mem_rd_addr1;
  wire [8-1:0] mem_rd_addr2;
  wire [8-1:0] mem_rd_addr3;
  wire [8-1:0] mem_wr_addr;
  wire mem_wr;
  wire [4-1:0] mem_wr_data;
  assign mem_rd_addr0 = (conf_rd)? conf_rd_addr : { st2_thread_index, st2_a };
  assign mem_rd_addr1 = (conf_rd)? conf_rd_addr : { st2_thread_index, st2_cs[3:0] };
  assign mem_rd_addr2 = (conf_rd)? conf_rd_addr : { st2_thread_index, st2_cs[7:4] };
  assign mem_rd_addr3 = (conf_rd)? conf_rd_addr : { st2_thread_index, st2_cs[11:8] };
  assign mem_wr_addr = (conf_wr)? conf_wr_addr : { st9_thread_index, st9_b };
  assign mem_wr = (conf_wr)? conf_wr : s9_should_write;
  assign mem_wr_data = (conf_wr)? conf_wr_data : { st9_cs_i, st9_cs_j };

  mem_2r_1w
  #(
    .width(4),
    .depth(8),
    .read_f(1),
    .init_file(""),
    .write_f(1),
    .output_file("")
  )
  mem_2r_1w_0
  (
    .clk(clk),
    .rd_addr0(mem_rd_addr0),
    .rd_addr1(mem_rd_addr1),
    .out0(c_a_t),
    .out1(cs_c_t[3:0]),
    .rd(1'b1),
    .wr(mem_wr),
    .wr_addr(mem_wr_addr),
    .wr_data(mem_wr_data)
  );


  mem_2r_1w
  #(
    .width(4),
    .depth(8),
    .read_f(1),
    .init_file(""),
    .write_f(1),
    .output_file("")
  )
  mem_2r_1w_1
  (
    .clk(clk),
    .rd_addr0(mem_rd_addr2),
    .rd_addr1(mem_rd_addr3),
    .out0(cs_c_t[7:4]),
    .out1(cs_c_t[11:8]),
    .rd(1'b1),
    .wr(mem_wr),
    .wr_addr(mem_wr_addr),
    .wr_data(mem_wr_data)
  );

  integer i_initial;

  initial begin
    thread_index = 0;
    thread_valid = 0;
    c_a = 0;
    b = 0;
    cs_c = 0;
    dist_csb = 0;
    adj_index = 0;
    index_list_edge = 0;
    for(i_initial=0; i_initial<10; i_initial=i_initial+1) begin
      thread_adj_indexes_r[i_initial] = 0;
    end
  end


endmodule



module mem_2r_1w #
(
  parameter width = 8,
  parameter depth = 4,
  parameter read_f = 0,
  parameter init_file = "mem_file.txt",
  parameter write_f = 0,
  parameter output_file = "mem_out_file.txt"
)
(
  input clk,
  input rd,
  input [depth-1:0] rd_addr0,
  input [depth-1:0] rd_addr1,
  output reg [width-1:0] out0,
  output reg [width-1:0] out1,
  input wr,
  input [depth-1:0] wr_addr,
  input [width-1:0] wr_data
);

  (* ram_style = "M20K" *) reg [width-1:0] mem[0:2**depth-1];
  /*
  reg [width-1:0] mem [0:2**depth-1];
  */

  always @(posedge clk) begin
    if(wr) begin
      mem[wr_addr] <= wr_data;
    end 
    if(rd) begin
      out0 <= mem[rd_addr0];
      out1 <= mem[rd_addr1];
    end 
  end


endmodule

