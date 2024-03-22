

module tree18-5x5-NA_0__dot_json_dot
(

);

  localparam data_width = 32;
  localparam fail_rate_producer = 0;
  localparam fail_rate_consumer = 0;
  localparam is_const = "false";
  localparam initial_value = 0;
  localparam max_data_size = 5000;
  reg clk;
  reg rst;
  wire dout_req_6;
  wire dout_ack_6;
  wire [data_width-1:0] dout_6;
  wire dout_req_7;
  wire dout_ack_7;
  wire [data_width-1:0] dout_7;
  wire dout_req_3;
  wire dout_ack_3;
  wire [data_width-1:0] dout_3;
  wire dout_req_9;
  wire dout_ack_9;
  wire [data_width-1:0] dout_9;
  wire dout_req_13;
  wire dout_ack_13;
  wire [data_width-1:0] dout_13;
  wire dout_req_17;
  wire dout_ack_17;
  wire [data_width-1:0] dout_17;
  wire din_req_15;
  wire din_ack_15;
  wire [data_width-1:0] din_15;
  wire [32-1:0] count_producer [0:1-1];
  wire [32-1:0] count_consumer [0:6-1];
  real count_clock;

  wire [6-1:0] consumers_done;
  wire done;
  assign consumers_done[0] = count_consumer[0] >= max_data_size;
  assign consumers_done[1] = count_consumer[1] >= max_data_size;
  assign consumers_done[2] = count_consumer[2] >= max_data_size;
  assign consumers_done[3] = count_consumer[3] >= max_data_size;
  assign consumers_done[4] = count_consumer[4] >= max_data_size;
  assign consumers_done[5] = count_consumer[5] >= max_data_size;
  assign done = &consumers_done;

  initial begin
    clk = 0;
    forever begin
      #1 clk = !clk;
    end
  end


  initial begin
    rst = 0;
    #1;
    rst = 1;
    #1;
    rst = 0;
  end

  integer i;

  always @(posedge clk) begin
    if(rst) begin
      count_clock <= 0;
    end 
    count_clock <= count_clock + 1;
    if(done) begin
      for(i=0; i<6; i=i+1) begin
        $display("tree18-5x5-NA_0__dot_json_dot throughput: %d : %5.2f%%", i, (100.0 * (count_consumer[i] / (count_clock / 4.0))));
      end
      $finish;
    end 
  end


  consumer
  #(
    .consumer_id(0),
    .data_width(data_width),
    .fail_rate(fail_rate_consumer)
  )
  consumer_6
  (
    .clk(clk),
    .rst(rst),
    .req(dout_req_6),
    .ack(dout_ack_6),
    .din(dout_6),
    .count(count_consumer[0])
  );


  consumer
  #(
    .consumer_id(1),
    .data_width(data_width),
    .fail_rate(fail_rate_consumer)
  )
  consumer_7
  (
    .clk(clk),
    .rst(rst),
    .req(dout_req_7),
    .ack(dout_ack_7),
    .din(dout_7),
    .count(count_consumer[1])
  );


  consumer
  #(
    .consumer_id(2),
    .data_width(data_width),
    .fail_rate(fail_rate_consumer)
  )
  consumer_3
  (
    .clk(clk),
    .rst(rst),
    .req(dout_req_3),
    .ack(dout_ack_3),
    .din(dout_3),
    .count(count_consumer[2])
  );


  consumer
  #(
    .consumer_id(3),
    .data_width(data_width),
    .fail_rate(fail_rate_consumer)
  )
  consumer_9
  (
    .clk(clk),
    .rst(rst),
    .req(dout_req_9),
    .ack(dout_ack_9),
    .din(dout_9),
    .count(count_consumer[3])
  );


  consumer
  #(
    .consumer_id(4),
    .data_width(data_width),
    .fail_rate(fail_rate_consumer)
  )
  consumer_13
  (
    .clk(clk),
    .rst(rst),
    .req(dout_req_13),
    .ack(dout_ack_13),
    .din(dout_13),
    .count(count_consumer[4])
  );


  consumer
  #(
    .consumer_id(5),
    .data_width(data_width),
    .fail_rate(fail_rate_consumer)
  )
  consumer_17
  (
    .clk(clk),
    .rst(rst),
    .req(dout_req_17),
    .ack(dout_ack_17),
    .din(dout_17),
    .count(count_consumer[5])
  );


  producer
  #(
    .producer_id(0),
    .data_width(data_width),
    .fail_rate(fail_rate_producer),
    .initial_value(initial_value),
    .is_const(is_const)
  )
  producer_15
  (
    .clk(clk),
    .rst(rst),
    .req(din_req_15),
    .ack(din_ack_15),
    .dout(din_15),
    .count(count_producer[0])
  );


  G
  #(
    .data_width(data_width)
  )
  G
  (
    .clk(clk),
    .rst(rst),
    .dout_req_6(dout_req_6),
    .dout_ack_6(dout_ack_6),
    .dout_6(dout_6),
    .dout_req_7(dout_req_7),
    .dout_ack_7(dout_ack_7),
    .dout_7(dout_7),
    .dout_req_3(dout_req_3),
    .dout_ack_3(dout_ack_3),
    .dout_3(dout_3),
    .dout_req_9(dout_req_9),
    .dout_ack_9(dout_ack_9),
    .dout_9(dout_9),
    .dout_req_13(dout_req_13),
    .dout_ack_13(dout_ack_13),
    .dout_13(dout_13),
    .dout_req_17(dout_req_17),
    .dout_ack_17(dout_ack_17),
    .dout_17(dout_17),
    .din_req_15(din_req_15),
    .din_ack_15(din_ack_15),
    .din_15(din_15)
  );


endmodule



module consumer #
(
  parameter consumer_id = 0,
  parameter data_width = 8,
  parameter fail_rate = 0
)
(
  input clk,
  input rst,
  output reg req,
  input ack,
  input [data_width-1:0] din,
  output reg [32-1:0] count
);

  reg stop;
  real randd;

  always @(posedge clk) begin
    if(rst) begin
      req <= 0;
      count <= 0;
      stop <= 0;
      randd <= $abs($random%101)+1;
    end else begin
      req <= 0;
      randd <= $abs($random%101)+1;
      stop <= (randd > fail_rate)? 0 : 1;
      if(!stop) begin
        req <= 1;
      end 
      if(ack) begin
        count <= count + 1;
      end 
    end
  end


endmodule



module producer #
(
  parameter producer_id = 0,
  parameter data_width = 8,
  parameter fail_rate = 0,
  parameter is_const = "false",
  parameter initial_value = 0
)
(
  input clk,
  input rst,
  input req,
  output reg ack,
  output reg [data_width-1:0] dout,
  output reg [32-1:0] count
);

  reg [data_width-1:0] dout_next;
  reg stop;
  real randd;

  always @(posedge clk) begin
    if(rst) begin
      dout <= initial_value;
      dout_next <= initial_value;
      ack <= 0;
      count <= 0;
      stop <= 0;
      randd <= $abs($random%101)+1;
    end else begin
      ack <= 0;
      randd <= $abs($random%101)+1;
      stop <= (randd > fail_rate)? 0 : 1;
      if(req & ~ack & !stop) begin
        ack <= 1;
        dout <= dout_next;
        if(is_const == "false") begin
          dout_next <= dout_next + 1;
        end 
        count <= count + 1;
      end 
    end
  end


endmodule



module G #
(
  parameter data_width = 32
)
(
  input clk,
  input rst,
  input dout_req_6,
  output dout_ack_6,
  output [data_width-1:0] dout_6,
  input dout_req_7,
  output dout_ack_7,
  output [data_width-1:0] dout_7,
  input dout_req_3,
  output dout_ack_3,
  output [data_width-1:0] dout_3,
  input dout_req_9,
  output dout_ack_9,
  output [data_width-1:0] dout_9,
  input dout_req_13,
  output dout_ack_13,
  output [data_width-1:0] dout_13,
  input dout_req_17,
  output dout_ack_17,
  output [data_width-1:0] dout_17,
  output din_req_15,
  input din_ack_15,
  input [data_width-1:0] din_15
);

  wire req_0_6;
  wire ack_0;
  wire [data_width-1:0] d0;
  wire req_1_0;
  wire ack_1;
  wire [data_width-1:0] d1;
  wire req_2_1;
  wire req_2_8;
  wire ack_2;
  wire [data_width-1:0] d2;
  wire req_8_12;
  wire req_8_16;
  wire ack_8;
  wire [data_width-1:0] d8;
  wire req_12_4;
  wire ack_12;
  wire [data_width-1:0] d12;
  wire req_16_5;
  wire ack_16;
  wire [data_width-1:0] d16;
  wire req_4_7;
  wire ack_4;
  wire [data_width-1:0] d4;
  wire req_5_3;
  wire req_5_9;
  wire ack_5;
  wire [data_width-1:0] d5;
  wire req_10_13;
  wire ack_10;
  wire [data_width-1:0] d10;
  wire req_11_17;
  wire ack_11;
  wire [data_width-1:0] d11;
  wire req_14_11;
  wire ack_14;
  wire [data_width-1:0] d14;
  wire req_15_2;
  wire req_15_10;
  wire req_15_14;
  wire ack_15;
  wire [data_width-1:0] d15;

  async_operator
  #(
    .data_width(data_width),
    .op("add"),
    .immediate(0),
    .input_size(1),
    .output_size(1)
  )
  add_0
  (
    .clk(clk),
    .rst(rst),
    .req_l({req_1_0}),
    .ack_l({ack_1}),
    .req_r({req_0_6}),
    .ack_r(ack_0),
    .din({d1}),
    .dout(d0)
  );


  async_operator
  #(
    .data_width(data_width),
    .op("out"),
    .immediate(0),
    .input_size(1),
    .output_size(1)
  )
  out_6
  (
    .clk(clk),
    .rst(rst),
    .req_l(req_0_6),
    .ack_l(ack_0),
    .req_r(dout_req_6),
    .ack_r(dout_ack_6),
    .din(d0),
    .dout(dout_6)
  );


  async_operator
  #(
    .data_width(data_width),
    .op("add"),
    .immediate(0),
    .input_size(1),
    .output_size(1)
  )
  add_1
  (
    .clk(clk),
    .rst(rst),
    .req_l({req_2_1}),
    .ack_l({ack_2}),
    .req_r({req_1_0}),
    .ack_r(ack_1),
    .din({d2}),
    .dout(d1)
  );


  async_operator
  #(
    .data_width(data_width),
    .op("add"),
    .immediate(0),
    .input_size(1),
    .output_size(2)
  )
  add_2
  (
    .clk(clk),
    .rst(rst),
    .req_l({req_15_2}),
    .ack_l({ack_15}),
    .req_r({req_2_1, req_2_8}),
    .ack_r(ack_2),
    .din({d15}),
    .dout(d2)
  );


  async_operator
  #(
    .data_width(data_width),
    .op("add"),
    .immediate(0),
    .input_size(1),
    .output_size(2)
  )
  add_8
  (
    .clk(clk),
    .rst(rst),
    .req_l({req_2_8}),
    .ack_l({ack_2}),
    .req_r({req_8_12, req_8_16}),
    .ack_r(ack_8),
    .din({d2}),
    .dout(d8)
  );


  async_operator
  #(
    .data_width(data_width),
    .op("add"),
    .immediate(0),
    .input_size(1),
    .output_size(1)
  )
  add_12
  (
    .clk(clk),
    .rst(rst),
    .req_l({req_8_12}),
    .ack_l({ack_8}),
    .req_r({req_12_4}),
    .ack_r(ack_12),
    .din({d8}),
    .dout(d12)
  );


  async_operator
  #(
    .data_width(data_width),
    .op("add"),
    .immediate(0),
    .input_size(1),
    .output_size(1)
  )
  add_16
  (
    .clk(clk),
    .rst(rst),
    .req_l({req_8_16}),
    .ack_l({ack_8}),
    .req_r({req_16_5}),
    .ack_r(ack_16),
    .din({d8}),
    .dout(d16)
  );


  async_operator
  #(
    .data_width(data_width),
    .op("add"),
    .immediate(0),
    .input_size(1),
    .output_size(1)
  )
  add_4
  (
    .clk(clk),
    .rst(rst),
    .req_l({req_12_4}),
    .ack_l({ack_12}),
    .req_r({req_4_7}),
    .ack_r(ack_4),
    .din({d12}),
    .dout(d4)
  );


  async_operator
  #(
    .data_width(data_width),
    .op("out"),
    .immediate(0),
    .input_size(1),
    .output_size(1)
  )
  out_7
  (
    .clk(clk),
    .rst(rst),
    .req_l(req_4_7),
    .ack_l(ack_4),
    .req_r(dout_req_7),
    .ack_r(dout_ack_7),
    .din(d4),
    .dout(dout_7)
  );


  async_operator
  #(
    .data_width(data_width),
    .op("add"),
    .immediate(0),
    .input_size(1),
    .output_size(2)
  )
  add_5
  (
    .clk(clk),
    .rst(rst),
    .req_l({req_16_5}),
    .ack_l({ack_16}),
    .req_r({req_5_3, req_5_9}),
    .ack_r(ack_5),
    .din({d16}),
    .dout(d5)
  );


  async_operator
  #(
    .data_width(data_width),
    .op("out"),
    .immediate(0),
    .input_size(1),
    .output_size(1)
  )
  out_3
  (
    .clk(clk),
    .rst(rst),
    .req_l(req_5_3),
    .ack_l(ack_5),
    .req_r(dout_req_3),
    .ack_r(dout_ack_3),
    .din(d5),
    .dout(dout_3)
  );


  async_operator
  #(
    .data_width(data_width),
    .op("out"),
    .immediate(0),
    .input_size(1),
    .output_size(1)
  )
  out_9
  (
    .clk(clk),
    .rst(rst),
    .req_l(req_5_9),
    .ack_l(ack_5),
    .req_r(dout_req_9),
    .ack_r(dout_ack_9),
    .din(d5),
    .dout(dout_9)
  );


  async_operator
  #(
    .data_width(data_width),
    .op("add"),
    .immediate(0),
    .input_size(1),
    .output_size(1)
  )
  add_10
  (
    .clk(clk),
    .rst(rst),
    .req_l({req_15_10}),
    .ack_l({ack_15}),
    .req_r({req_10_13}),
    .ack_r(ack_10),
    .din({d15}),
    .dout(d10)
  );


  async_operator
  #(
    .data_width(data_width),
    .op("out"),
    .immediate(0),
    .input_size(1),
    .output_size(1)
  )
  out_13
  (
    .clk(clk),
    .rst(rst),
    .req_l(req_10_13),
    .ack_l(ack_10),
    .req_r(dout_req_13),
    .ack_r(dout_ack_13),
    .din(d10),
    .dout(dout_13)
  );


  async_operator
  #(
    .data_width(data_width),
    .op("add"),
    .immediate(0),
    .input_size(1),
    .output_size(1)
  )
  add_11
  (
    .clk(clk),
    .rst(rst),
    .req_l({req_14_11}),
    .ack_l({ack_14}),
    .req_r({req_11_17}),
    .ack_r(ack_11),
    .din({d14}),
    .dout(d11)
  );


  async_operator
  #(
    .data_width(data_width),
    .op("out"),
    .immediate(0),
    .input_size(1),
    .output_size(1)
  )
  out_17
  (
    .clk(clk),
    .rst(rst),
    .req_l(req_11_17),
    .ack_l(ack_11),
    .req_r(dout_req_17),
    .ack_r(dout_ack_17),
    .din(d11),
    .dout(dout_17)
  );


  async_operator
  #(
    .data_width(data_width),
    .op("add"),
    .immediate(0),
    .input_size(1),
    .output_size(1)
  )
  add_14
  (
    .clk(clk),
    .rst(rst),
    .req_l({req_15_14}),
    .ack_l({ack_15}),
    .req_r({req_14_11}),
    .ack_r(ack_14),
    .din({d15}),
    .dout(d14)
  );


  async_operator
  #(
    .data_width(data_width),
    .op("in"),
    .immediate(0),
    .input_size(1),
    .output_size(3)
  )
  in_15
  (
    .clk(clk),
    .rst(rst),
    .req_l(din_req_15),
    .ack_l(din_ack_15),
    .req_r({req_15_2, req_15_10, req_15_14}),
    .ack_r(ack_15),
    .din(din_15),
    .dout(d15)
  );


endmodule



module async_operator #
(
  parameter data_width = 32,
  parameter op = "reg",
  parameter immediate = 32,
  parameter input_size = 1,
  parameter output_size = 1
)
(
  input clk,
  input rst,
  output reg [input_size-1:0] req_l,
  input [input_size-1:0] ack_l,
  input [output_size-1:0] req_r,
  output ack_r,
  input [data_width*input_size-1:0] din,
  output [data_width-1:0] dout
);

  reg [data_width*input_size-1:0] din_r;
  wire has_all;
  wire req_r_all;
  reg [output_size-1:0] ack_r_all;
  reg [input_size-1:0] has;
  integer i;
  genvar g;
  assign has_all = &has;
  assign req_r_all = &req_r;
  assign ack_r = &ack_r_all;

  always @(posedge clk) begin
    if(rst) begin
      has <= { input_size{ 1'b0 } };
      ack_r_all <= { output_size{ 1'b0 } };
      req_l <= { input_size{ 1'b0 } };
    end else begin
      for(i=0; i<input_size; i=i+1) begin
        if(~has[i] & ~req_l[i]) begin
          req_l[i] <= 1'b1;
        end 
        if(ack_l[i]) begin
          has[i] <= 1'b1;
          req_l[i] <= 1'b0;
        end 
      end
      if(has_all & req_r_all) begin
        ack_r_all <= { output_size{ 1'b1 } };
        has <= { input_size{ 1'b0 } };
      end 
      if(~has_all) begin
        ack_r_all <= { output_size{ 1'b0 } };
      end 
    end
  end


  generate for(g=0; g<input_size; g=g+1) begin : rcv

    always @(posedge ack_l[g]) begin
      din_r[data_width*(g+1)-1:data_width*g] <= din[data_width*(g+1)-1:data_width*g];
    end

  end
  endgenerate


  operator
  #(
    .input_size(input_size),
    .op(op),
    .immediate(immediate),
    .data_width(data_width)
  )
  operator
  (
    .din(din_r),
    .dout(dout)
  );


endmodule



module operator #
(
  parameter input_size = 1,
  parameter op = "reg",
  parameter immediate = 0,
  parameter data_width = 32
)
(
  input [data_width*input_size-1:0] din,
  output [data_width-1:0] dout
);


  generate if(input_size == 1) begin : gen_op
    if((op === "reg") || (op === "in") || (op === "out")) begin
      assign dout = din;
    end 
    if(op === "addi") begin
      assign dout = din+immediate;
    end 
    if(op === "subi") begin
      assign dout = din-immediate;
    end 
    if(op === "muli") begin
      assign dout = din*immediate;
    end 
  end else begin
    if(input_size == 2) begin
      if(op === "add") begin
        assign dout = din[data_width-1:0]+din[data_width*2-1:data_width];
      end 
      if(op === "sub") begin
        assign dout = din[data_width-1:0]-din[data_width*2-1:data_width];
      end 
      if(op === "mul") begin
        assign dout = din[data_width-1:0]*din[data_width*2-1:data_width];
      end 
    end else begin
      if(input_size == 3) begin
        if(op === "add") begin
          assign dout = din[data_width-1:0]+din[data_width*2-1:data_width]+din[data_width*3-1:data_width*2];
        end 
        if(op === "sub") begin
          assign dout = din[data_width-1:0]-din[data_width*2-1:data_width]-din[data_width*3-1:data_width*2];
        end 
        if(op === "mul") begin
          assign dout = din[data_width-1:0]*din[data_width*2-1:data_width]*din[data_width*3-1:data_width*2];
        end 
      end 
    end
  end
  endgenerate


endmodule

