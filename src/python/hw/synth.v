

module testbench_synth
(
  input clk,
  input rst,
  output out
);

  reg start;
  reg [15-1:0] acc_user_done_rd_data;
  reg [15-1:0] acc_user_done_wr_data;
  wire [15-1:0] yoto_acc_acc_user_request_read;
  reg [15-1:0] acc_user_read_data_valid;
  reg [480-1:0] acc_user_read_data;
  reg [15-1:0] acc_user_available_write;
  wire [15-1:0] yoto_acc_acc_user_request_write;
  wire [480-1:0] yoto_acc_acc_user_write_data;
  wire yoto_acc_acc_user_done;
  wire [480-1:0] data;

  yoto_acc
  yoto_acc
  (
    .clk(clk),
    .rst(rst),
    .start(start),
    .acc_user_done_rd_data(acc_user_done_rd_data),
    .acc_user_done_wr_data(acc_user_done_wr_data),
    .acc_user_request_read(yoto_acc_acc_user_request_read),
    .acc_user_read_data_valid(acc_user_read_data_valid),
    .acc_user_read_data(acc_user_read_data),
    .acc_user_available_write(acc_user_available_write),
    .acc_user_request_write(yoto_acc_acc_user_request_write),
    .acc_user_write_data(yoto_acc_acc_user_write_data),
    .acc_user_done(yoto_acc_acc_user_done)
  );


  always @(posedge clk) begin
    if(rst) begin
      acc_user_done_rd_data <= 0;
      acc_user_done_wr_data <= 0;
      acc_user_read_data_valid <= 0;
      acc_user_read_data <= 0;
      acc_user_available_write <= 0;
    end else begin
      acc_user_done_rd_data <= acc_user_done_rd_data + 1;
      acc_user_done_wr_data <= acc_user_done_wr_data + 1;
      acc_user_read_data_valid <= acc_user_read_data_valid + 1;
      acc_user_read_data <= acc_user_read_data + 1;
      acc_user_available_write <= acc_user_available_write + 1;
    end
  end


  always @(posedge clk) begin
    if(rst) begin
      start <= 0;
    end else begin
      start <= 1;
    end
  end

  assign data = yoto_acc_acc_user_request_read|yoto_acc_acc_user_request_write|yoto_acc_acc_user_write_data|yoto_acc_acc_user_done;
  assign out = ^data;

  initial begin
    start = 0;
    acc_user_done_rd_data = 0;
    acc_user_done_wr_data = 0;
    acc_user_read_data_valid = 0;
    acc_user_read_data = 0;
    acc_user_available_write = 0;
  end


endmodule



module yoto_acc
(
  input clk,
  input rst,
  input start,
  input [15-1:0] acc_user_done_rd_data,
  input [15-1:0] acc_user_done_wr_data,
  output [15-1:0] acc_user_request_read,
  input [15-1:0] acc_user_read_data_valid,
  input [480-1:0] acc_user_read_data,
  input [15-1:0] acc_user_available_write,
  output [15-1:0] acc_user_request_write,
  output [480-1:0] acc_user_write_data,
  output acc_user_done
);

  reg start_reg;
  wire [15-1:0] yott_interface_done;
  assign acc_user_done = &yott_interface_done;

  always @(posedge clk) begin
    if(rst) begin
      start_reg <= 0;
    end else begin
      start_reg <= start_reg | start;
    end
  end

  (* keep_hierarchy = "yes" *)

  yott_interface
  yott_interface_0
  (
    .clk(clk),
    .rst(rst),
    .start(start_reg),
    .yott_done_rd_data(acc_user_done_rd_data[0]),
    .yott_done_wr_data(acc_user_done_wr_data[0]),
    .yott_request_read(acc_user_request_read[0]),
    .yott_read_data_valid(acc_user_read_data_valid[0]),
    .yott_read_data(acc_user_read_data[31:0]),
    .yott_available_write(acc_user_available_write[0]),
    .yott_request_write(acc_user_request_write[0]),
    .yott_write_data(acc_user_write_data[31:0]),
    .yott_interface_done(yott_interface_done[0])
  );


  initial begin
    start_reg = 0;
  end

  (* keep_hierarchy = "yes" *)

  yott_interface
  yott_interface_1
  (
    .clk(clk),
    .rst(rst),
    .start(start_reg),
    .yott_done_rd_data(acc_user_done_rd_data[1]),
    .yott_done_wr_data(acc_user_done_wr_data[1]),
    .yott_request_read(acc_user_request_read[1]),
    .yott_read_data_valid(acc_user_read_data_valid[1]),
    .yott_read_data(acc_user_read_data[63:32]),
    .yott_available_write(acc_user_available_write[1]),
    .yott_request_write(acc_user_request_write[1]),
    .yott_write_data(acc_user_write_data[63:32]),
    .yott_interface_done(yott_interface_done[1])
  );


  initial begin
    start_reg = 0;
  end

  (* keep_hierarchy = "yes" *)

  yott_interface
  yott_interface_2
  (
    .clk(clk),
    .rst(rst),
    .start(start_reg),
    .yott_done_rd_data(acc_user_done_rd_data[2]),
    .yott_done_wr_data(acc_user_done_wr_data[2]),
    .yott_request_read(acc_user_request_read[2]),
    .yott_read_data_valid(acc_user_read_data_valid[2]),
    .yott_read_data(acc_user_read_data[95:64]),
    .yott_available_write(acc_user_available_write[2]),
    .yott_request_write(acc_user_request_write[2]),
    .yott_write_data(acc_user_write_data[95:64]),
    .yott_interface_done(yott_interface_done[2])
  );


  initial begin
    start_reg = 0;
  end

  (* keep_hierarchy = "yes" *)

  yott_interface
  yott_interface_3
  (
    .clk(clk),
    .rst(rst),
    .start(start_reg),
    .yott_done_rd_data(acc_user_done_rd_data[3]),
    .yott_done_wr_data(acc_user_done_wr_data[3]),
    .yott_request_read(acc_user_request_read[3]),
    .yott_read_data_valid(acc_user_read_data_valid[3]),
    .yott_read_data(acc_user_read_data[127:96]),
    .yott_available_write(acc_user_available_write[3]),
    .yott_request_write(acc_user_request_write[3]),
    .yott_write_data(acc_user_write_data[127:96]),
    .yott_interface_done(yott_interface_done[3])
  );


  initial begin
    start_reg = 0;
  end

  (* keep_hierarchy = "yes" *)

  yott_interface
  yott_interface_4
  (
    .clk(clk),
    .rst(rst),
    .start(start_reg),
    .yott_done_rd_data(acc_user_done_rd_data[4]),
    .yott_done_wr_data(acc_user_done_wr_data[4]),
    .yott_request_read(acc_user_request_read[4]),
    .yott_read_data_valid(acc_user_read_data_valid[4]),
    .yott_read_data(acc_user_read_data[159:128]),
    .yott_available_write(acc_user_available_write[4]),
    .yott_request_write(acc_user_request_write[4]),
    .yott_write_data(acc_user_write_data[159:128]),
    .yott_interface_done(yott_interface_done[4])
  );


  initial begin
    start_reg = 0;
  end

  (* keep_hierarchy = "yes" *)

  yott_interface
  yott_interface_5
  (
    .clk(clk),
    .rst(rst),
    .start(start_reg),
    .yott_done_rd_data(acc_user_done_rd_data[5]),
    .yott_done_wr_data(acc_user_done_wr_data[5]),
    .yott_request_read(acc_user_request_read[5]),
    .yott_read_data_valid(acc_user_read_data_valid[5]),
    .yott_read_data(acc_user_read_data[191:160]),
    .yott_available_write(acc_user_available_write[5]),
    .yott_request_write(acc_user_request_write[5]),
    .yott_write_data(acc_user_write_data[191:160]),
    .yott_interface_done(yott_interface_done[5])
  );


  initial begin
    start_reg = 0;
  end

  (* keep_hierarchy = "yes" *)

  yott_interface
  yott_interface_6
  (
    .clk(clk),
    .rst(rst),
    .start(start_reg),
    .yott_done_rd_data(acc_user_done_rd_data[6]),
    .yott_done_wr_data(acc_user_done_wr_data[6]),
    .yott_request_read(acc_user_request_read[6]),
    .yott_read_data_valid(acc_user_read_data_valid[6]),
    .yott_read_data(acc_user_read_data[223:192]),
    .yott_available_write(acc_user_available_write[6]),
    .yott_request_write(acc_user_request_write[6]),
    .yott_write_data(acc_user_write_data[223:192]),
    .yott_interface_done(yott_interface_done[6])
  );


  initial begin
    start_reg = 0;
  end

  (* keep_hierarchy = "yes" *)

  yott_interface
  yott_interface_7
  (
    .clk(clk),
    .rst(rst),
    .start(start_reg),
    .yott_done_rd_data(acc_user_done_rd_data[7]),
    .yott_done_wr_data(acc_user_done_wr_data[7]),
    .yott_request_read(acc_user_request_read[7]),
    .yott_read_data_valid(acc_user_read_data_valid[7]),
    .yott_read_data(acc_user_read_data[255:224]),
    .yott_available_write(acc_user_available_write[7]),
    .yott_request_write(acc_user_request_write[7]),
    .yott_write_data(acc_user_write_data[255:224]),
    .yott_interface_done(yott_interface_done[7])
  );


  initial begin
    start_reg = 0;
  end

  (* keep_hierarchy = "yes" *)

  yott_interface
  yott_interface_8
  (
    .clk(clk),
    .rst(rst),
    .start(start_reg),
    .yott_done_rd_data(acc_user_done_rd_data[8]),
    .yott_done_wr_data(acc_user_done_wr_data[8]),
    .yott_request_read(acc_user_request_read[8]),
    .yott_read_data_valid(acc_user_read_data_valid[8]),
    .yott_read_data(acc_user_read_data[287:256]),
    .yott_available_write(acc_user_available_write[8]),
    .yott_request_write(acc_user_request_write[8]),
    .yott_write_data(acc_user_write_data[287:256]),
    .yott_interface_done(yott_interface_done[8])
  );


  initial begin
    start_reg = 0;
  end

  (* keep_hierarchy = "yes" *)

  yott_interface
  yott_interface_9
  (
    .clk(clk),
    .rst(rst),
    .start(start_reg),
    .yott_done_rd_data(acc_user_done_rd_data[9]),
    .yott_done_wr_data(acc_user_done_wr_data[9]),
    .yott_request_read(acc_user_request_read[9]),
    .yott_read_data_valid(acc_user_read_data_valid[9]),
    .yott_read_data(acc_user_read_data[319:288]),
    .yott_available_write(acc_user_available_write[9]),
    .yott_request_write(acc_user_request_write[9]),
    .yott_write_data(acc_user_write_data[319:288]),
    .yott_interface_done(yott_interface_done[9])
  );


  initial begin
    start_reg = 0;
  end

  (* keep_hierarchy = "yes" *)

  yott_interface
  yott_interface_10
  (
    .clk(clk),
    .rst(rst),
    .start(start_reg),
    .yott_done_rd_data(acc_user_done_rd_data[10]),
    .yott_done_wr_data(acc_user_done_wr_data[10]),
    .yott_request_read(acc_user_request_read[10]),
    .yott_read_data_valid(acc_user_read_data_valid[10]),
    .yott_read_data(acc_user_read_data[351:320]),
    .yott_available_write(acc_user_available_write[10]),
    .yott_request_write(acc_user_request_write[10]),
    .yott_write_data(acc_user_write_data[351:320]),
    .yott_interface_done(yott_interface_done[10])
  );


  initial begin
    start_reg = 0;
  end

  (* keep_hierarchy = "yes" *)

  yott_interface
  yott_interface_11
  (
    .clk(clk),
    .rst(rst),
    .start(start_reg),
    .yott_done_rd_data(acc_user_done_rd_data[11]),
    .yott_done_wr_data(acc_user_done_wr_data[11]),
    .yott_request_read(acc_user_request_read[11]),
    .yott_read_data_valid(acc_user_read_data_valid[11]),
    .yott_read_data(acc_user_read_data[383:352]),
    .yott_available_write(acc_user_available_write[11]),
    .yott_request_write(acc_user_request_write[11]),
    .yott_write_data(acc_user_write_data[383:352]),
    .yott_interface_done(yott_interface_done[11])
  );


  initial begin
    start_reg = 0;
  end

  (* keep_hierarchy = "yes" *)

  yott_interface
  yott_interface_12
  (
    .clk(clk),
    .rst(rst),
    .start(start_reg),
    .yott_done_rd_data(acc_user_done_rd_data[12]),
    .yott_done_wr_data(acc_user_done_wr_data[12]),
    .yott_request_read(acc_user_request_read[12]),
    .yott_read_data_valid(acc_user_read_data_valid[12]),
    .yott_read_data(acc_user_read_data[415:384]),
    .yott_available_write(acc_user_available_write[12]),
    .yott_request_write(acc_user_request_write[12]),
    .yott_write_data(acc_user_write_data[415:384]),
    .yott_interface_done(yott_interface_done[12])
  );


  initial begin
    start_reg = 0;
  end

  (* keep_hierarchy = "yes" *)

  yott_interface
  yott_interface_13
  (
    .clk(clk),
    .rst(rst),
    .start(start_reg),
    .yott_done_rd_data(acc_user_done_rd_data[13]),
    .yott_done_wr_data(acc_user_done_wr_data[13]),
    .yott_request_read(acc_user_request_read[13]),
    .yott_read_data_valid(acc_user_read_data_valid[13]),
    .yott_read_data(acc_user_read_data[447:416]),
    .yott_available_write(acc_user_available_write[13]),
    .yott_request_write(acc_user_request_write[13]),
    .yott_write_data(acc_user_write_data[447:416]),
    .yott_interface_done(yott_interface_done[13])
  );


  initial begin
    start_reg = 0;
  end

  (* keep_hierarchy = "yes" *)

  yott_interface
  yott_interface_14
  (
    .clk(clk),
    .rst(rst),
    .start(start_reg),
    .yott_done_rd_data(acc_user_done_rd_data[14]),
    .yott_done_wr_data(acc_user_done_wr_data[14]),
    .yott_request_read(acc_user_request_read[14]),
    .yott_read_data_valid(acc_user_read_data_valid[14]),
    .yott_read_data(acc_user_read_data[479:448]),
    .yott_available_write(acc_user_available_write[14]),
    .yott_request_write(acc_user_request_write[14]),
    .yott_write_data(acc_user_write_data[479:448]),
    .yott_interface_done(yott_interface_done[14])
  );


  initial begin
    start_reg = 0;
  end


endmodule



module yott_interface
(
  input clk,
  input rst,
  input start,
  input yott_done_rd_data,
  input yott_done_wr_data,
  output yott_request_read,
  input yott_read_data_valid,
  input [32-1:0] yott_read_data,
  input yott_available_write,
  output reg yott_request_write,
  output reg [32-1:0] yott_write_data,
  output yott_interface_done
);

  assign yott_interface_done = &{ yott_done_wr_data, yott_done_rd_data };
  reg start_pipe;
  reg pop_data;
  wire available_pop;
  wire [16-1:0] data_out;
  reg [4-1:0] visited_edges;
  wire [32-1:0] total_pipeline_counter;
  reg [5-1:0] fms_sd;
  localparam [5-1:0] fsm_sd_edges_idle = 0;
  localparam [5-1:0] fsm_sd_edges_send_data = 1;
  localparam [5-1:0] fsm_sd_edges_verify = 2;
  localparam [5-1:0] fsm_sd_annotations_idle = 3;
  localparam [5-1:0] fsm_sd_annotations_send_data = 4;
  localparam [5-1:0] fsm_sd_annotations_verify = 5;
  localparam [5-1:0] fsm_sd_n2c_idle = 6;
  localparam [5-1:0] fsm_sd_n2c_send_data = 7;
  localparam [5-1:0] fsm_sd_n2c_verify = 8;
  localparam [5-1:0] fsm_sd_dist_idle = 9;
  localparam [5-1:0] fsm_sd_dist_send_data = 10;
  localparam [5-1:0] fsm_sd_dist_verify = 11;
  localparam [5-1:0] fsm_sd_c_idle = 12;
  localparam [5-1:0] fsm_sd_c_send_data = 13;
  localparam [5-1:0] fsm_sd_c_verify = 14;
  localparam [5-1:0] fsm_sd_vedges_idle = 15;
  localparam [5-1:0] fsm_sd_vedges_send_data = 16;
  localparam [5-1:0] fsm_sd_done = 17;
  wire yott_done;
  reg st3_conf_rd;
  reg [8-1:0] st3_conf_rd_addr;
  wire [4-1:0] st3_conf_rd_data;
  reg st2_conf_wr0;
  reg [8-1:0] st2_conf_addr0;
  reg [8-1:0] st2_conf_data0;
  reg st2_conf_wr1;
  reg [8-1:0] st2_conf_addr1;
  reg [21-1:0] st2_conf_data1;
  reg st3_conf_wr;
  reg [8-1:0] st3_conf_wr_addr;
  reg [4-1:0] st3_conf_wr_data;
  reg st4_conf_wr;
  reg [9-1:0] st4_conf_addr;
  reg [6-1:0] st4_conf_data;
  reg st7_conf_wr;
  reg [8-1:0] st7_conf_addr;
  reg st7_conf_data;

  always @(posedge clk) begin
    if(rst) begin
      st2_conf_wr0 <= 0;
      st2_conf_addr0 <= 0;
      st2_conf_data0 <= 0;
      st2_conf_wr1 <= 0;
      st2_conf_addr1 <= 0;
      st2_conf_data1 <= 0;
      st3_conf_wr <= 0;
      st3_conf_wr_addr <= 0;
      st3_conf_wr_data <= 0;
      st4_conf_wr <= 0;
      st4_conf_addr <= 0;
      st4_conf_data <= 0;
      st7_conf_wr <= 0;
      st7_conf_addr <= 0;
      st7_conf_data <= 0;
      pop_data <= 0;
      start_pipe <= 0;
      fms_sd <= fsm_sd_edges_idle;
    end else begin
      if(start) begin
        st2_conf_wr0 <= 0;
        st2_conf_wr1 <= 0;
        st3_conf_wr <= 0;
        st4_conf_wr <= 0;
        st7_conf_wr <= 0;
        start_pipe <= 0;
        pop_data <= 0;
        case(fms_sd)
          fsm_sd_edges_idle: begin
            if(available_pop) begin
              pop_data <= 1;
              fms_sd <= fsm_sd_edges_send_data;
            end 
          end
          fsm_sd_edges_send_data: begin
            st2_conf_wr0 <= 1;
            st2_conf_data0 <= data_out[7:0];
            fms_sd <= fsm_sd_edges_verify;
          end
          fsm_sd_edges_verify: begin
            if(&st2_conf_addr0) begin
              fms_sd <= fsm_sd_annotations_idle;
            end else begin
              st2_conf_addr0 <= st2_conf_addr0 + 1;
              fms_sd <= fsm_sd_edges_idle;
            end
          end
          fsm_sd_annotations_idle: begin
            if(available_pop) begin
              pop_data <= 1;
              fms_sd <= fsm_sd_annotations_send_data;
            end 
          end
          fsm_sd_annotations_send_data: begin
            st2_conf_wr1 <= 1;
            st2_conf_data1 <= data_out[20:0];
            fms_sd <= fsm_sd_annotations_verify;
          end
          fsm_sd_annotations_verify: begin
            if(&st2_conf_addr1) begin
              fms_sd <= fsm_sd_n2c_idle;
            end else begin
              st2_conf_addr1 <= st2_conf_addr1 + 1;
              fms_sd <= fsm_sd_annotations_idle;
            end
          end
          fsm_sd_n2c_idle: begin
            if(available_pop) begin
              pop_data <= 1;
              fms_sd <= fsm_sd_n2c_send_data;
            end 
          end
          fsm_sd_n2c_send_data: begin
            st3_conf_wr <= 1;
            st3_conf_wr_data <= data_out[3:0];
            fms_sd <= fsm_sd_n2c_verify;
          end
          fsm_sd_n2c_verify: begin
            if(&st3_conf_wr_addr) begin
              fms_sd <= fsm_sd_dist_idle;
            end else begin
              st3_conf_wr_addr <= st3_conf_wr_addr + 1;
              fms_sd <= fsm_sd_n2c_idle;
            end
          end
          fsm_sd_dist_idle: begin
            if(available_pop) begin
              pop_data <= 1;
              fms_sd <= fsm_sd_dist_send_data;
            end 
          end
          fsm_sd_dist_send_data: begin
            st4_conf_wr <= 1;
            st4_conf_data <= data_out[5:0];
            fms_sd <= fsm_sd_dist_verify;
          end
          fsm_sd_dist_verify: begin
            if(&st4_conf_addr) begin
              fms_sd <= fsm_sd_c_idle;
            end else begin
              st4_conf_addr <= st4_conf_addr + 1;
              fms_sd <= fsm_sd_dist_idle;
            end
          end
          fsm_sd_c_idle: begin
            if(available_pop) begin
              pop_data <= 1;
              fms_sd <= fsm_sd_c_send_data;
            end 
          end
          fsm_sd_c_send_data: begin
            st7_conf_wr <= 1;
            st7_conf_data <= data_out[15:0];
            fms_sd <= fsm_sd_c_verify;
          end
          fsm_sd_c_verify: begin
            if(&st7_conf_addr) begin
              fms_sd <= fsm_sd_vedges_idle;
            end else begin
              st7_conf_addr <= st7_conf_addr + 1;
              fms_sd <= fsm_sd_c_idle;
            end
          end
          fsm_sd_vedges_idle: begin
            if(available_pop) begin
              pop_data <= 1;
              fms_sd <= fsm_sd_vedges_send_data;
            end 
          end
          fsm_sd_vedges_send_data: begin
            visited_edges <= data_out[3:0];
            fms_sd <= fsm_sd_done;
          end
          fsm_sd_done: begin
            start_pipe <= 1;
          end
        endcase
      end 
    end
  end


  //Data Consumer - Begin
  reg [2-1:0] fsm_consume;
  localparam fsm_consume_wait = 0;
  localparam fsm_consume_consume = 1;
  localparam fsm_consume_verify = 2;
  localparam fsm_consume_done = 3;

  always @(posedge clk) begin
    if(rst) begin
      st3_conf_rd <= 0;
      st3_conf_rd_addr <= 0;
      yott_request_write <= 0;
      fsm_consume <= fsm_consume_wait;
    end else begin
      st3_conf_rd <= 0;
      yott_request_write <= 0;
      case(fsm_consume)
        fsm_consume_wait: begin
          if(yott_available_write) begin
            if(yott_done) begin
              st3_conf_rd <= 1;
              fsm_consume <= fsm_consume_consume;
            end 
          end 
        end
        fsm_consume_consume: begin
          yott_request_write <= 1;
          yott_write_data <= { 28'd0, st3_conf_rd_data };
          st3_conf_rd_addr <= st3_conf_rd_addr + 1;
          fsm_consume <= fsm_consume_verify;
        end
        fsm_consume_verify: begin
          if(st3_conf_rd_addr == 256) begin
            fsm_consume <= fsm_consume_done;
          end else begin
            fsm_consume <= fsm_consume_wait;
          end
        end
        fsm_consume_done: begin
        end
      endcase
    end
  end

  //Data Consumer - Begin
  (* keep_hierarchy = "yes" *)

  fetch_data_32_16
  fetch_data_32_16
  (
    .clk(clk),
    .rst(rst),
    .start(start),
    .request_read(yott_request_read),
    .data_valid(yott_read_data_valid),
    .read_data(yott_read_data),
    .pop_data(pop_data),
    .available_pop(available_pop),
    .data_out(data_out)
  );


  yott_pipeline_hw
  yott_pipeline_hw
  (
    .clk(clk),
    .rst(rst),
    .start(start_pipe),
    .visited_edges(visited_edges),
    .done(yott_done),
    .st2_conf_wr0(st2_conf_wr0),
    .st2_conf_addr0(st2_conf_addr0),
    .st2_conf_data0(st2_conf_data0),
    .st2_conf_wr1(st2_conf_wr1),
    .st2_conf_addr1(st2_conf_addr1),
    .st2_conf_data1(st2_conf_data1),
    .st3_conf_wr(st3_conf_wr),
    .st3_conf_wr_addr(st3_conf_wr_addr),
    .st3_conf_wr_data(st3_conf_wr_data),
    .st3_conf_rd(st3_conf_rd),
    .st3_conf_rd_addr(st3_conf_rd_addr),
    .st3_conf_rd_data(st3_conf_rd_data),
    .st4_conf_wr(st4_conf_wr),
    .st4_conf_addr(st4_conf_addr),
    .st4_conf_data(st4_conf_data),
    .st7_conf_wr(st7_conf_wr),
    .st7_conf_addr(st7_conf_addr),
    .st7_conf_data(st7_conf_data)
  );


  initial begin
    yott_request_write = 0;
    yott_write_data = 0;
    start_pipe = 0;
    pop_data = 0;
    visited_edges = 0;
    fms_sd = 0;
    st3_conf_rd = 0;
    st3_conf_rd_addr = 0;
    st2_conf_wr0 = 0;
    st2_conf_addr0 = 0;
    st2_conf_data0 = 0;
    st2_conf_wr1 = 0;
    st2_conf_addr1 = 0;
    st2_conf_data1 = 0;
    st3_conf_wr = 0;
    st3_conf_wr_addr = 0;
    st3_conf_wr_data = 0;
    st4_conf_wr = 0;
    st4_conf_addr = 0;
    st4_conf_data = 0;
    st7_conf_wr = 0;
    st7_conf_addr = 0;
    st7_conf_data = 0;
    fsm_consume = 0;
  end


endmodule



module fetch_data_32_16
(
  input clk,
  input start,
  input rst,
  output reg request_read,
  input data_valid,
  input [32-1:0] read_data,
  input pop_data,
  output reg available_pop,
  output [16-1:0] data_out
);

  reg [1-1:0] fsm_read;
  reg [1-1:0] fsm_control;
  reg [32-1:0] data;
  reg [32-1:0] buffer;
  reg [2-1:0] count;
  reg has_buffer;
  reg buffer_read;
  reg en;

  assign data_out = data[15:0];

  always @(posedge clk) begin
    if(rst) begin
      en <= 1'b0;
    end else begin
      en <= (en)? en : start;
    end
  end


  always @(posedge clk) begin
    if(rst) begin
      fsm_read <= 0;
      request_read <= 0;
      has_buffer <= 0;
    end else begin
      request_read <= 0;
      case(fsm_read)
        0: begin
          if(en & data_valid) begin
            buffer <= read_data;
            request_read <= 1;
            has_buffer <= 1;
            fsm_read <= 1;
          end 
        end
        1: begin
          if(buffer_read) begin
            has_buffer <= 0;
            fsm_read <= 0;
          end 
        end
      endcase
    end
  end


  always @(posedge clk) begin
    if(rst) begin
      fsm_control <= 0;
      available_pop <= 0;
      count <= 0;
      buffer_read <= 0;
    end else begin
      buffer_read <= 0;
      case(fsm_control)
        0: begin
          if(has_buffer) begin
            data <= buffer;
            count <= 1;
            buffer_read <= 1;
            available_pop <= 1;
            fsm_control <= 1;
          end 
        end
        1: begin
          if(pop_data & ~count[1]) begin
            count <= count << 1;
            data <= data[31:16];
          end 
          if(pop_data & count[1] & has_buffer) begin
            count <= 1;
            data <= buffer;
            buffer_read <= 1;
          end 
          if(count[1] & pop_data & ~has_buffer) begin
            count <= count << 1;
            data <= data[31:16];
            available_pop <= 0;
            fsm_control <= 0;
          end 
        end
      endcase
    end
  end


  initial begin
    request_read = 0;
    available_pop = 0;
    fsm_read = 0;
    fsm_control = 0;
    data = 0;
    buffer = 0;
    count = 0;
    has_buffer = 0;
    buffer_read = 0;
    en = 0;
  end


endmodule



module yott_pipeline_hw
(
  input clk,
  input rst,
  input start,
  input [4-1:0] visited_edges,
  output done,
  input st2_conf_wr0,
  input [8-1:0] st2_conf_addr0,
  input [8-1:0] st2_conf_data0,
  input st2_conf_wr1,
  input [8-1:0] st2_conf_addr1,
  input [21-1:0] st2_conf_data1,
  input st3_conf_wr,
  input [8-1:0] st3_conf_wr_addr,
  input [4-1:0] st3_conf_wr_data,
  input st3_conf_rd,
  input [8-1:0] st3_conf_rd_addr,
  output [4-1:0] st3_conf_rd_data,
  input st4_conf_wr,
  input [9-1:0] st4_conf_addr,
  input [6-1:0] st4_conf_data,
  input st7_conf_wr,
  input [8-1:0] st7_conf_addr,
  input st7_conf_data
);

  reg start_pipeline;
  reg init_fifo;
  reg [4-1:0] thread_counter;
  reg [3-1:0] fsm_init_fifo;
  localparam init = 3'd0;
  localparam wait_init = 3'd1;
  localparam start_p = 3'd2;

  always @(posedge clk) begin
    if(rst) begin
      start_pipeline <= 1'd0;
      thread_counter <= 4'd0;
      init_fifo <= 1'd0;
      fsm_init_fifo <= init;
    end else begin
      if(start) begin
        case(fsm_init_fifo)
          init: begin
            init_fifo <= 1'd1;
            fsm_init_fifo <= wait_init;
          end
          wait_init: begin
            if(thread_counter == 4'd9) begin
              init_fifo <= 1'd0;
              fsm_init_fifo <= start_p;
            end 
            thread_counter <= thread_counter + 4'd1;
          end
          start_p: begin
            start_pipeline <= 1'd1;
          end
        endcase
      end 
    end
  end

  // St0 wires
  wire [4-1:0] st0_thread_index;
  wire st0_thread_valid;
  wire st0_should_write;
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
  wire [6-1:0] st3_adj_index;
  wire [4-1:0] st3_index_list_edge;
  // -----

  // St4 wires
  wire [4-1:0] st4_thread_index;
  wire st4_thread_valid;
  wire [4-1:0] st4_c_a;
  wire [4-1:0] st4_b;
  wire [4-1:0] st4_c_s;
  wire [12-1:0] st4_cs_c;
  wire [9-1:0] st4_dist_csb;
  // -----

  // St5 wires
  wire [4-1:0] st5_thread_index;
  wire st5_thread_valid;
  wire [4-1:0] st5_b;
  wire [4-1:0] st5_c_s;
  wire [12-1:0] st5_cs_c;
  wire [9-1:0] st5_dist_csb;
  wire [3-1:0] st5_dist_ca_cs;
  // -----

  // St6 wires
  wire [4-1:0] st6_thread_index;
  wire st6_thread_valid;
  wire [4-1:0] st6_b;
  wire [4-1:0] st6_c_s;
  wire [5-1:0] st6_cost;
  wire [3-1:0] st6_dist_ca_cs;
  // -----

  // St7 wires
  wire [4-1:0] st7_thread_index;
  wire st7_thread_valid;
  wire [4-1:0] st7_b;
  wire [4-1:0] st7_c_s;
  wire [5-1:0] st7_cost;
  wire [3-1:0] st7_dist_ca_cs;
  wire st7_cell_free;
  // -----

  // St8 wires
  wire [4-1:0] st8_thread_index;
  wire st8_thread_valid;
  wire [4-1:0] st8_b;
  wire [4-1:0] st8_c_s;
  wire [5-1:0] st8_cost;
  wire [3-1:0] st8_dist_ca_cs;
  wire st8_save_cell;
  wire st8_should_write;
  // -----

  // St9 wires
  wire [4-1:0] st9_thread_index;
  wire st9_thread_valid;
  wire s9_should_write;
  wire [4-1:0] st9_b;
  wire [4-1:0] st9_c_s;
  wire st9_write_enable;
  wire [5-1:0] st9_input_data;
  // -----

  // St0 instantiation

  stage0_yott
  stage0_yott
  (
    .clk(clk),
    .rst(rst),
    .start(start_pipeline),
    .thread_index(st0_thread_index),
    .thread_valid(st0_thread_valid),
    .should_write(st0_should_write),
    .st9_write_enable((init_fifo)? 1'd1 : st9_write_enable),
    .st9_input_data((init_fifo)? { thread_counter, 1'd0 } : st9_input_data)
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
    .index_list_edge(st2_index_list_edge),
    .conf_wr0(st2_conf_wr0),
    .conf_addr0(st2_conf_addr0),
    .conf_data0(st2_conf_data0),
    .conf_wr1(st2_conf_wr1),
    .conf_addr1(st2_conf_addr1),
    .conf_data1(st2_conf_data1)
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
    .st9_c_s(st9_c_s),
    .conf_wr(st3_conf_wr),
    .conf_wr_addr(st3_conf_wr_addr),
    .conf_wr_data(st3_conf_wr_data),
    .conf_rd(st3_conf_rd),
    .conf_rd_addr(st3_conf_rd_addr),
    .conf_rd_data(st3_conf_rd_data)
  );

  // -----
  // St4 instantiation

  stage4_yott
  stage4_yott
  (
    .clk(clk),
    .rst(rst),
    .thread_index(st4_thread_index),
    .thread_valid(st4_thread_valid),
    .c_a(st4_c_a),
    .b(st4_b),
    .c_s(st4_c_s),
    .cs_c(st4_cs_c),
    .dist_csb(st4_dist_csb),
    .st3_thread_index(st3_thread_index),
    .st3_thread_valid(st3_thread_valid),
    .st3_c_a(st3_c_a),
    .st3_b(st3_b),
    .st3_cs_c(st3_cs_c),
    .st3_dist_csb(st3_dist_csb),
    .st3_adj_index(st3_adj_index),
    .st3_index_list_edge(st3_index_list_edge),
    .conf_wr(st4_conf_wr),
    .conf_addr(st4_conf_addr),
    .conf_data(st4_conf_data)
  );

  // -----
  // St5 instantiation

  stage5_yott
  stage5_yott
  (
    .clk(clk),
    .rst(rst),
    .thread_index(st5_thread_index),
    .thread_valid(st5_thread_valid),
    .b(st5_b),
    .c_s(st5_c_s),
    .cs_c(st5_cs_c),
    .dist_csb(st5_dist_csb),
    .dist_ca_cs(st5_dist_ca_cs),
    .st4_thread_index(st5_thread_index),
    .st4_thread_valid(st5_thread_valid),
    .st4_c_a(st4_c_a),
    .st4_b(st4_b),
    .st4_c_s(st4_c_s),
    .st4_cs_c(st4_cs_c),
    .st4_dist_csb(st4_dist_csb)
  );

  // -----
  // St6 instantiation

  stage6_yott
  stage6_yott
  (
    .clk(clk),
    .rst(rst),
    .thread_index(st6_thread_index),
    .thread_valid(st6_thread_valid),
    .b(st6_b),
    .c_s(st6_c_s),
    .cost(st6_cost),
    .dist_ca_cs(st6_dist_ca_cs),
    .st5_thread_index(st5_thread_index),
    .st5_thread_valid(st5_thread_valid),
    .st5_b(st5_b),
    .st5_c_s(st5_c_s),
    .st5_cs_c(st5_cs_c),
    .st5_dist_csb(st5_dist_csb),
    .st5_dist_ca_cs(st5_dist_ca_cs)
  );

  // -----
  // St7 instantiation

  stage7_yott
  stage7_yott
  (
    .clk(clk),
    .rst(rst),
    .thread_index(st7_thread_index),
    .thread_valid(st7_thread_valid),
    .b(st7_b),
    .c_s(st7_c_s),
    .cost(st7_cost),
    .dist_ca_cs(st7_dist_ca_cs),
    .cell_free(st7_cell_free),
    .st6_thread_index(st6_thread_index),
    .st6_thread_valid(st6_thread_valid),
    .st6_b(st6_b),
    .st6_c_s(st6_c_s),
    .st6_cost(st6_cost),
    .st6_dist_ca_cs(st6_dist_ca_cs),
    .st9_thread_index(st9_thread_index),
    .s9_should_write(s9_should_write),
    .st9_c_s(st9_c_s),
    .conf_wr(st7_conf_wr),
    .conf_addr(st7_conf_addr),
    .conf_data(st7_conf_data)
  );

  // -----
  // St8 instantiation

  stage8_yott
  stage8_yott
  (
    .clk(clk),
    .rst(rst),
    .thread_index(st8_thread_index),
    .thread_valid(st8_thread_valid),
    .b(st8_b),
    .c_s(st8_c_s),
    .cost(st8_cost),
    .dist_ca_cs(st8_dist_ca_cs),
    .save_cell(st8_save_cell),
    .should_write(st8_should_write),
    .st7_thread_index(st7_thread_index),
    .st7_thread_valid(st7_thread_valid),
    .st7_b(st7_b),
    .st7_c_s(st7_c_s),
    .st7_cost(st7_cost),
    .st7_dist_ca_cs(st7_dist_ca_cs),
    .st7_cell_free(st7_cell_free)
  );

  // -----
  // St9 instantiation

  stage9_yott
  stage9_yott
  (
    .clk(clk),
    .rst(rst),
    .thread_index(st9_thread_index),
    .thread_valid(st9_thread_valid),
    .b(st9_b),
    .c_s(st9_c_s),
    .should_write(s9_should_write),
    .write_enable(st9_write_enable),
    .input_data(st9_input_data),
    .st8_thread_index(st8_thread_index),
    .st8_thread_valid(st8_thread_valid),
    .st8_b(st8_b),
    .st8_c_s(st8_c_s),
    .st8_cost(st8_cost),
    .st8_dist_ca_cs(st8_dist_ca_cs),
    .st8_save_cell(st8_save_cell),
    .st8_should_write(st8_should_write)
  );

  // -----

  initial begin
    start_pipeline = 0;
    init_fifo = 0;
    thread_counter = 0;
    fsm_init_fifo = 0;
  end


endmodule



module stage0_yott
(
  input clk,
  input rst,
  input start,
  output [4-1:0] thread_index,
  output thread_valid,
  output should_write,
  input st9_write_enable,
  input [5-1:0] st9_input_data
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
    .write_enable(st9_write_enable),
    .input_data(st9_input_data),
    .output_read_enable(st9_write_enable),
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
          thread_valid <= 1'd0;
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
  output reg [4-1:0] index_list_edge,
  input conf_wr0,
  input [8-1:0] conf_addr0,
  input [8-1:0] conf_data0,
  input conf_wr1,
  input [8-1:0] conf_addr1,
  input [21-1:0] conf_data1
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
    .depth(8)
  )
  mem_1r_1w_edges
  (
    .clk(clk),
    .rd_addr({ st1_thread_index, st1_edge_index }),
    .out({ a_t, b_t }),
    .rd(1'b1),
    .wr(conf_wr0),
    .wr_addr(conf_addr0),
    .wr_data(conf_data0)
  );


  mem_1r_1w
  #(
    .width(21),
    .depth(8)
  )
  mem_1r_1w_annotations
  (
    .clk(clk),
    .rd_addr({ st1_thread_index, st1_edge_index }),
    .out({ cs_t, dist_csb_t }),
    .rd(1'b1),
    .wr(conf_wr1),
    .wr_addr(conf_addr1),
    .wr_data(conf_data1)
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
  output reg [6-1:0] adj_index,
  output reg [4-1:0] index_list_edge,
  input [4-1:0] st9_thread_index,
  input st9_thread_valid,
  input s9_should_write,
  input [4-1:0] st9_b,
  input [4-1:0] st9_c_s,
  input conf_wr,
  input [8-1:0] conf_wr_addr,
  input [4-1:0] conf_wr_data,
  input conf_rd,
  input [8-1:0] conf_rd_addr,
  output [4-1:0] conf_rd_data
);

  reg [6-1:0] thread_adj_indexes_r [0:10-1];
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
      adj_index <= 6'd0;
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
        adj_index <= 6'd0;
      end
      if(~s9_should_write && st9_thread_valid) begin
        thread_adj_indexes_r[st9_thread_index] <= thread_adj_indexes_r[st9_thread_index] + 6'd1;
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
  assign mem_wr_data = (conf_wr)? conf_wr_data : st9_c_s;

  mem_2r_1w
  #(
    .width(4),
    .depth(8)
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
    .depth(8)
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



module stage4_yott
(
  input clk,
  input rst,
  output reg [4-1:0] thread_index,
  output reg thread_valid,
  output reg [4-1:0] c_a,
  output reg [4-1:0] b,
  output reg [4-1:0] c_s,
  output reg [12-1:0] cs_c,
  output reg [9-1:0] dist_csb,
  input [4-1:0] st3_thread_index,
  input st3_thread_valid,
  input [4-1:0] st3_c_a,
  input [4-1:0] st3_b,
  input [12-1:0] st3_cs_c,
  input [9-1:0] st3_dist_csb,
  input [6-1:0] st3_adj_index,
  input [4-1:0] st3_index_list_edge,
  input conf_wr,
  input [9-1:0] conf_addr,
  input [6-1:0] conf_data
);

  wire [3-1:0] add_i_t;
  wire [3-1:0] add_j_t;

  always @(posedge clk) begin
    if(rst) begin
      thread_index <= 4'd0;
      thread_valid <= 1'd0;
      c_a <= 4'd0;
      b <= 4'd0;
      c_s <= 4'd0;
      cs_c <= 12'd0;
      dist_csb <= 9'd0;
    end else begin
      thread_index <= st3_thread_index;
      thread_valid <= st3_thread_valid;
      b <= st3_b;
      cs_c <= st3_cs_c;
      c_a <= st3_c_a;
      dist_csb <= st3_dist_csb;
      c_s[1:0] <= st3_c_a[1:0] + add_i_t;
      c_s[7:4] <= st3_c_a[3:2] + add_j_t;
    end
  end


  mem_1r_1w
  #(
    .width(6),
    .depth(9)
  )
  mem_1r_1w
  (
    .clk(clk),
    .rd_addr({ st3_index_list_edge, st3_adj_index[4:0] }),
    .out({ add_i_t, add_j_t }),
    .rd(1'b1),
    .wr(conf_wr),
    .wr_addr(conf_addr),
    .wr_data(conf_data)
  );


  initial begin
    thread_index = 0;
    thread_valid = 0;
    c_a = 0;
    b = 0;
    c_s = 0;
    cs_c = 0;
    dist_csb = 0;
  end


endmodule



module stage5_yott
(
  input clk,
  input rst,
  output reg [4-1:0] thread_index,
  output reg thread_valid,
  output reg [4-1:0] b,
  output reg [4-1:0] c_s,
  output reg [12-1:0] cs_c,
  output reg [9-1:0] dist_csb,
  output reg [3-1:0] dist_ca_cs,
  input [4-1:0] st4_thread_index,
  input st4_thread_valid,
  input [4-1:0] st4_c_a,
  input [4-1:0] st4_b,
  input [4-1:0] st4_c_s,
  input [12-1:0] st4_cs_c,
  input [9-1:0] st4_dist_csb
);

  wire [3-1:0] d1;

  always @(posedge clk) begin
    if(rst) begin
      thread_index <= 4'd0;
      thread_valid <= 1'd0;
      b <= 4'd0;
      c_s <= 4'd0;
      cs_c <= 12'd0;
      dist_csb <= 9'd0;
      dist_ca_cs <= 3'd0;
    end else begin
      thread_index <= st4_thread_index;
      thread_valid <= st4_thread_valid;
      b <= st4_b;
      c_s <= st4_c_s;
      cs_c <= st4_cs_c;
      dist_csb <= st4_dist_csb;
      dist_ca_cs <= d1;
    end
  end


  distance_table
  distance_table
  (
    .source(st4_c_a),
    .target1(st4_c_s),
    .d1(d1)
  );


  initial begin
    thread_index = 0;
    thread_valid = 0;
    b = 0;
    c_s = 0;
    cs_c = 0;
    dist_csb = 0;
    dist_ca_cs = 0;
  end


endmodule



module distance_table
(
  input [4-1:0] source,
  input [4-1:0] target1,
  input [4-1:0] target2,
  input [4-1:0] target3,
  output [3-1:0] d1,
  output [3-1:0] d2,
  output [3-1:0] d3
);

  wire [2-1:0] s_l;
  wire [2-1:0] s_c;
  wire [2-1:0] t1_l;
  wire [2-1:0] t1_c;
  wire [2-1:0] t2_l;
  wire [2-1:0] t2_c;
  wire [2-1:0] t3_l;
  wire [2-1:0] t3_c;

  wire [2-1:0] dist_table [0:2**4-1];

  assign s_l = source[1:0];
  assign s_c = source[3:2];
  assign t1_l = target1[1:0];
  assign t1_c = target1[3:2];
  assign t2_l = target2[1:0];
  assign t2_c = target2[3:2];
  assign t3_l = target3[1:0];
  assign t3_c = target3[3:2];

  assign d1 = dist_table[{ s_l, t1_l }] + dist_table[{ s_c, t1_c }];
  assign d2 = dist_table[{ s_l, t2_l }] + dist_table[{ s_c, t2_c }];
  assign d3 = dist_table[{ s_l, t3_l }] + dist_table[{ s_c, t3_c }];

  assign dist_table[0] = 3'd0;
  assign dist_table[1] = 3'd1;
  assign dist_table[2] = 3'd2;
  assign dist_table[3] = 3'd3;
  assign dist_table[4] = 3'd1;
  assign dist_table[5] = 3'd0;
  assign dist_table[6] = 3'd1;
  assign dist_table[7] = 3'd2;
  assign dist_table[8] = 3'd2;
  assign dist_table[9] = 3'd1;
  assign dist_table[10] = 3'd0;
  assign dist_table[11] = 3'd1;
  assign dist_table[12] = 3'd3;
  assign dist_table[13] = 3'd2;
  assign dist_table[14] = 3'd1;
  assign dist_table[15] = 3'd0;

endmodule



module stage6_yott
(
  input clk,
  input rst,
  output reg [4-1:0] thread_index,
  output reg thread_valid,
  output reg [4-1:0] b,
  output reg [4-1:0] c_s,
  output reg [5-1:0] cost,
  output reg [3-1:0] dist_ca_cs,
  input [4-1:0] st5_thread_index,
  input st5_thread_valid,
  input [4-1:0] st5_b,
  input [4-1:0] st5_c_s,
  input [12-1:0] st5_cs_c,
  input [9-1:0] st5_dist_csb,
  input [3-1:0] st5_dist_ca_cs
);

  wire [3-1:0] d1_t;
  wire [3-1:0] d2_t;
  wire [3-1:0] d3_t;
  wire [3-1:0] sub1_t;
  wire [3-1:0] sub2_t;
  wire [3-1:0] sub3_t;
  assign sub1_t = d1_t - st5_dist_csb[2:0];
  assign sub2_t = d2_t - st5_dist_csb[5:3];
  assign sub3_t = d3_t - st5_dist_csb[8:6];
  wire [5-1:0] cost_t;
  assign cost_t = sub1_t + sub2_t + sub3_t;

  always @(posedge clk) begin
    if(rst) begin
      thread_index <= 4'd0;
      thread_valid <= 'd0;
      b <= 4'd0;
      c_s <= 4'd0;
      cost <= 5'd0;
      dist_ca_cs <= 3'd0;
    end else begin
      thread_index <= st5_thread_index;
      thread_valid <= st5_thread_valid;
      b <= st5_b;
      c_s <= st5_cs_c;
      cost <= cost_t;
      dist_ca_cs <= st5_dist_ca_cs;
    end
  end


  distance_table
  distance_table
  (
    .source(st5_c_s),
    .target1(st5_cs_c[3:0]),
    .target2(st5_cs_c[7:4]),
    .target3(st5_cs_c[11:8]),
    .d1(d1_t),
    .d2(d2_t),
    .d3(d1_t)
  );


  initial begin
    thread_index = 0;
    thread_valid = 0;
    b = 0;
    c_s = 0;
    cost = 0;
    dist_ca_cs = 0;
  end


endmodule



module stage7_yott
(
  input clk,
  input rst,
  output reg [4-1:0] thread_index,
  output reg thread_valid,
  output reg [4-1:0] b,
  output reg [4-1:0] c_s,
  output reg [5-1:0] cost,
  output reg [3-1:0] dist_ca_cs,
  output reg cell_free,
  input [4-1:0] st6_thread_index,
  input st6_thread_valid,
  input [4-1:0] st6_b,
  input [4-1:0] st6_c_s,
  input [5-1:0] st6_cost,
  input [3-1:0] st6_dist_ca_cs,
  input [4-1:0] st9_thread_index,
  input s9_should_write,
  input [4-1:0] st9_c_s,
  input conf_wr,
  input [8-1:0] conf_addr,
  input conf_data
);

  wire cell_free_t;
  wire content_t;
  wire out_of_border_t;
  assign out_of_border_t = (st6_c_s[1:0] > 3'd3) || (st6_c_s[3:2] > 3'd3);
  assign cell_free_t = &{ ~content_t, ~out_of_border_t, st6_thread_valid };

  always @(posedge clk) begin
    if(rst) begin
      thread_index <= 4'd0;
      thread_valid <= 1'd0;
      b <= 4'd0;
      c_s <= 4'd0;
      cost <= 5'd0;
      dist_ca_cs <= 3'd0;
      cell_free <= 1'd0;
    end else begin
      thread_index <= st6_thread_index;
      thread_valid <= st6_thread_valid;
      b <= st6_b;
      c_s <= st6_c_s;
      cost <= st6_cost;
      dist_ca_cs <= st6_dist_ca_cs;
      cell_free <= cell_free_t;
    end
  end

  wire mem_wr;
  wire [8-1:0] mem_addr;
  wire mem_data;
  assign mem_wr = (conf_wr)? conf_wr : s9_should_write;
  assign mem_addr = (conf_wr)? conf_addr : { st9_thread_index, st9_c_s };
  assign mem_data = (conf_wr)? conf_data : 1'd1;

  mem_1r_1w
  #(
    .width(1),
    .depth(8)
  )
  mem_1r_1w
  (
    .clk(clk),
    .rd_addr({ st6_thread_index, st6_c_s }),
    .out(content_t),
    .rd(1'b1),
    .wr(mem_wr),
    .wr_addr(mem_addr),
    .wr_data(mem_data)
  );


  initial begin
    thread_index = 0;
    thread_valid = 0;
    b = 0;
    c_s = 0;
    cost = 0;
    dist_ca_cs = 0;
    cell_free = 0;
  end


endmodule



module stage8_yott
(
  input clk,
  input rst,
  output reg [4-1:0] thread_index,
  output reg thread_valid,
  output reg [4-1:0] b,
  output reg [4-1:0] c_s,
  output reg [5-1:0] cost,
  output reg [3-1:0] dist_ca_cs,
  output reg save_cell,
  output reg should_write,
  input [4-1:0] st7_thread_index,
  input st7_thread_valid,
  input [4-1:0] st7_b,
  input [4-1:0] st7_c_s,
  input [5-1:0] st7_cost,
  input [3-1:0] st7_dist_ca_cs,
  input st7_cell_free
);

  wire save_cell_t;
  wire should_write_t;
  assign should_write_t = st7_cell_free && ((dist_ca_cs < 3) && (cost == 0) || (dist_ca_cs >= 3));
  assign save_cell_t = st7_cell_free && (dist_ca_cs < 3) && ~should_write;

  always @(posedge clk) begin
    if(rst) begin
      thread_index <= 4'd0;
      thread_valid <= 1'd0;
      b <= 4'd0;
      c_s <= 4'd0;
      cost <= 5'd0;
      dist_ca_cs <= 3'd0;
      save_cell <= 1'd0;
      should_write <= 1'd0;
    end else begin
      thread_index <= st7_thread_index;
      thread_valid <= st7_thread_valid;
      b <= st7_b;
      c_s <= st7_c_s;
      cost <= st7_cost;
      dist_ca_cs <= st7_dist_ca_cs;
      save_cell <= save_cell_t;
      should_write <= should_write_t;
    end
  end


  initial begin
    thread_index = 0;
    thread_valid = 0;
    b = 0;
    c_s = 0;
    cost = 0;
    dist_ca_cs = 0;
    save_cell = 0;
    should_write = 0;
  end


endmodule



module stage9_yott
(
  input clk,
  input rst,
  output reg [4-1:0] thread_index,
  output reg thread_valid,
  output reg [4-1:0] b,
  output reg [4-1:0] c_s,
  output reg should_write,
  output reg write_enable,
  output reg [5-1:0] input_data,
  input [4-1:0] st8_thread_index,
  input st8_thread_valid,
  input [4-1:0] st8_b,
  input [4-1:0] st8_c_s,
  input [5-1:0] st8_cost,
  input [3-1:0] st8_dist_ca_cs,
  input st8_save_cell,
  input st8_should_write
);

  reg [3-1:0] threads_current_adj_dists [0:10-1];
  reg [10-1:0] threads_free_cell_valid;
  reg [4-1:0] threads_free_cell0;
  reg [3-1:0] threads_free_cell1;
  wire was_there_change;
  assign was_there_change = st8_dist_ca_cs != threads_current_adj_dists[st8_thread_index];
  wire should;
  assign should = st8_should_write && st8_thread_valid;

  always @(posedge clk) begin
    if(rst) begin
      thread_index <= 4'd0;
      thread_valid <= 1'd0;
      b <= 4'd0;
      c_s <= 4'd0;
      should_write <= 'd0;
      write_enable <= 1'd0;
      input_data <= 5'd0;
      threads_free_cell_valid <= 10'b1111111111;
    end else begin
      write_enable <= st8_thread_valid;
      input_data <= { st8_thread_index, should };
      thread_index <= st8_thread_index;
      thread_valid <= st8_thread_valid;
      b <= st8_b;
      c_s <= st8_c_s;
      should_write <= should;
      if(should) begin
        threads_current_adj_dists[st8_thread_index] <= 3'd1;
        threads_free_cell1[st8_thread_index] <= 3'b111;
        threads_free_cell_valid[st8_thread_index] <= 1'd0;
      end 
      if(~st8_thread_valid) begin
        threads_current_adj_dists[st8_thread_index] <= 1;
        threads_free_cell0[st8_thread_index] <= 4'd0;
        threads_free_cell1[st8_thread_index] <= 3'b111;
      end else begin
        if(st8_save_cell && (st8_cost < threads_free_cell1[st8_thread_index])) begin
          threads_free_cell0[st8_thread_index] <= c_s;
          threads_free_cell1[st8_thread_index] <= st8_cost;
          threads_free_cell_valid[st8_thread_index] <= 1'd1;
        end 
        if(was_there_change) begin
          threads_current_adj_dists[st8_thread_index] <= st8_dist_ca_cs;
          if(threads_free_cell_valid[st8_thread_index]) begin
            c_s <= threads_free_cell0[st8_thread_index];
          end 
        end 
      end
    end
  end

  integer i_initial;

  initial begin
    thread_index = 0;
    thread_valid = 0;
    b = 0;
    c_s = 0;
    should_write = 0;
    write_enable = 0;
    input_data = 0;
    for(i_initial=0; i_initial<10; i_initial=i_initial+1) begin
      threads_current_adj_dists[i_initial] = 0;
    end
    threads_free_cell_valid = 0;
    threads_free_cell0 = 0;
    threads_free_cell1 = 0;
  end


endmodule

