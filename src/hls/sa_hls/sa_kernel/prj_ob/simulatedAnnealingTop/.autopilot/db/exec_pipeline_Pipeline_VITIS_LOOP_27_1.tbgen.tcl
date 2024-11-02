set moduleName exec_pipeline_Pipeline_VITIS_LOOP_27_1
set isTopModule 0
set isCombinational 0
set isDatapathOnly 0
set isPipelined 1
set pipeline_type none
set FunctionProtocol ap_ctrl_hs
set isOneStateSeq 0
set ProfileFlag 0
set StallSigGenFlag 0
set isEnableWaveformDebug 1
set hasInterrupt 0
set C_modelName {exec_pipeline_Pipeline_VITIS_LOOP_27_1}
set C_modelType { void 0 }
set C_modelArgList {
	{ st1_m_fifo_a_m_size_V_reload int 8 regular  }
	{ st1_m_fifo_a_m_rear_V_7_reload int 8 regular  }
	{ st1_m_fifo_b_m_size_V_reload int 8 regular  }
	{ st1_m_fifo_b_m_rear_V_7_reload int 8 regular  }
	{ n2c int 800 regular {array 6 { 2 1 } 1 1 }  }
	{ c2n int 800 regular {array 6 { 2 1 } 1 1 }  }
	{ n int 32 regular {array 100 { 1 1 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 } 1 1 }  }
	{ st0_m_th_valid int 1 regular {array 6 { 2 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 } 1 1 }  }
	{ st0_m_cell_a_V int 8 regular {array 6 { 2 3 } 1 1 }  }
	{ st0_m_cell_b_V int 8 regular {array 6 { 2 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 } 1 1 }  }
	{ st1_m_fifo_a_m_arr_th_idx_V int 8 regular {array 10 { 2 3 } 1 1 }  }
	{ st1_m_fifo_a_m_arr_cell_V int 8 regular {array 10 { 2 3 } 1 1 }  }
	{ st1_m_fifo_a_m_arr_node_V int 8 regular {array 10 { 2 3 } 1 1 }  }
	{ st1_m_fifo_b_m_arr_th_idx_V int 8 regular {array 10 { 2 3 } 1 1 }  }
	{ st1_m_fifo_b_m_arr_cell_V int 8 regular {array 10 { 2 3 } 1 1 }  }
	{ st1_m_fifo_b_m_arr_node_V int 8 regular {array 10 { 2 3 } 1 1 }  }
}
set C_modelArgMapList {[ 
	{ "Name" : "st1_m_fifo_a_m_size_V_reload", "interface" : "wire", "bitwidth" : 8, "direction" : "READONLY"} , 
 	{ "Name" : "st1_m_fifo_a_m_rear_V_7_reload", "interface" : "wire", "bitwidth" : 8, "direction" : "READONLY"} , 
 	{ "Name" : "st1_m_fifo_b_m_size_V_reload", "interface" : "wire", "bitwidth" : 8, "direction" : "READONLY"} , 
 	{ "Name" : "st1_m_fifo_b_m_rear_V_7_reload", "interface" : "wire", "bitwidth" : 8, "direction" : "READONLY"} , 
 	{ "Name" : "n2c", "interface" : "memory", "bitwidth" : 800, "direction" : "READWRITE"} , 
 	{ "Name" : "c2n", "interface" : "memory", "bitwidth" : 800, "direction" : "READWRITE"} , 
 	{ "Name" : "n", "interface" : "memory", "bitwidth" : 32, "direction" : "READONLY"} , 
 	{ "Name" : "st0_m_th_valid", "interface" : "memory", "bitwidth" : 1, "direction" : "READWRITE"} , 
 	{ "Name" : "st0_m_cell_a_V", "interface" : "memory", "bitwidth" : 8, "direction" : "READWRITE"} , 
 	{ "Name" : "st0_m_cell_b_V", "interface" : "memory", "bitwidth" : 8, "direction" : "READWRITE"} , 
 	{ "Name" : "st1_m_fifo_a_m_arr_th_idx_V", "interface" : "memory", "bitwidth" : 8, "direction" : "READWRITE"} , 
 	{ "Name" : "st1_m_fifo_a_m_arr_cell_V", "interface" : "memory", "bitwidth" : 8, "direction" : "READWRITE"} , 
 	{ "Name" : "st1_m_fifo_a_m_arr_node_V", "interface" : "memory", "bitwidth" : 8, "direction" : "READWRITE"} , 
 	{ "Name" : "st1_m_fifo_b_m_arr_th_idx_V", "interface" : "memory", "bitwidth" : 8, "direction" : "READWRITE"} , 
 	{ "Name" : "st1_m_fifo_b_m_arr_cell_V", "interface" : "memory", "bitwidth" : 8, "direction" : "READWRITE"} , 
 	{ "Name" : "st1_m_fifo_b_m_arr_node_V", "interface" : "memory", "bitwidth" : 8, "direction" : "READWRITE"} ]}
# RTL Port declarations: 
set portNum 77
set portList { 
	{ ap_clk sc_in sc_logic 1 clock -1 } 
	{ ap_rst sc_in sc_logic 1 reset -1 active_high_sync } 
	{ ap_start sc_in sc_logic 1 start -1 } 
	{ ap_done sc_out sc_logic 1 predone -1 } 
	{ ap_idle sc_out sc_logic 1 done -1 } 
	{ ap_ready sc_out sc_logic 1 ready -1 } 
	{ st1_m_fifo_a_m_size_V_reload sc_in sc_lv 8 signal 0 } 
	{ st1_m_fifo_a_m_rear_V_7_reload sc_in sc_lv 8 signal 1 } 
	{ st1_m_fifo_b_m_size_V_reload sc_in sc_lv 8 signal 2 } 
	{ st1_m_fifo_b_m_rear_V_7_reload sc_in sc_lv 8 signal 3 } 
	{ n2c_address0 sc_out sc_lv 3 signal 4 } 
	{ n2c_ce0 sc_out sc_logic 1 signal 4 } 
	{ n2c_we0 sc_out sc_lv 100 signal 4 } 
	{ n2c_d0 sc_out sc_lv 800 signal 4 } 
	{ n2c_q0 sc_in sc_lv 800 signal 4 } 
	{ n2c_address1 sc_out sc_lv 3 signal 4 } 
	{ n2c_ce1 sc_out sc_logic 1 signal 4 } 
	{ n2c_q1 sc_in sc_lv 800 signal 4 } 
	{ c2n_address0 sc_out sc_lv 3 signal 5 } 
	{ c2n_ce0 sc_out sc_logic 1 signal 5 } 
	{ c2n_we0 sc_out sc_lv 100 signal 5 } 
	{ c2n_d0 sc_out sc_lv 800 signal 5 } 
	{ c2n_q0 sc_in sc_lv 800 signal 5 } 
	{ c2n_address1 sc_out sc_lv 3 signal 5 } 
	{ c2n_ce1 sc_out sc_logic 1 signal 5 } 
	{ c2n_q1 sc_in sc_lv 800 signal 5 } 
	{ n_address0 sc_out sc_lv 7 signal 6 } 
	{ n_ce0 sc_out sc_logic 1 signal 6 } 
	{ n_q0 sc_in sc_lv 32 signal 6 } 
	{ n_address1 sc_out sc_lv 7 signal 6 } 
	{ n_ce1 sc_out sc_logic 1 signal 6 } 
	{ n_q1 sc_in sc_lv 32 signal 6 } 
	{ st0_m_th_valid_address0 sc_out sc_lv 3 signal 7 } 
	{ st0_m_th_valid_ce0 sc_out sc_logic 1 signal 7 } 
	{ st0_m_th_valid_we0 sc_out sc_logic 1 signal 7 } 
	{ st0_m_th_valid_d0 sc_out sc_lv 1 signal 7 } 
	{ st0_m_th_valid_q0 sc_in sc_lv 1 signal 7 } 
	{ st0_m_cell_a_V_address0 sc_out sc_lv 3 signal 8 } 
	{ st0_m_cell_a_V_ce0 sc_out sc_logic 1 signal 8 } 
	{ st0_m_cell_a_V_we0 sc_out sc_logic 1 signal 8 } 
	{ st0_m_cell_a_V_d0 sc_out sc_lv 8 signal 8 } 
	{ st0_m_cell_a_V_q0 sc_in sc_lv 8 signal 8 } 
	{ st0_m_cell_b_V_address0 sc_out sc_lv 3 signal 9 } 
	{ st0_m_cell_b_V_ce0 sc_out sc_logic 1 signal 9 } 
	{ st0_m_cell_b_V_we0 sc_out sc_logic 1 signal 9 } 
	{ st0_m_cell_b_V_d0 sc_out sc_lv 8 signal 9 } 
	{ st0_m_cell_b_V_q0 sc_in sc_lv 8 signal 9 } 
	{ st1_m_fifo_a_m_arr_th_idx_V_address0 sc_out sc_lv 4 signal 10 } 
	{ st1_m_fifo_a_m_arr_th_idx_V_ce0 sc_out sc_logic 1 signal 10 } 
	{ st1_m_fifo_a_m_arr_th_idx_V_we0 sc_out sc_logic 1 signal 10 } 
	{ st1_m_fifo_a_m_arr_th_idx_V_d0 sc_out sc_lv 8 signal 10 } 
	{ st1_m_fifo_a_m_arr_th_idx_V_q0 sc_in sc_lv 8 signal 10 } 
	{ st1_m_fifo_a_m_arr_cell_V_address0 sc_out sc_lv 4 signal 11 } 
	{ st1_m_fifo_a_m_arr_cell_V_ce0 sc_out sc_logic 1 signal 11 } 
	{ st1_m_fifo_a_m_arr_cell_V_we0 sc_out sc_logic 1 signal 11 } 
	{ st1_m_fifo_a_m_arr_cell_V_d0 sc_out sc_lv 8 signal 11 } 
	{ st1_m_fifo_a_m_arr_cell_V_q0 sc_in sc_lv 8 signal 11 } 
	{ st1_m_fifo_a_m_arr_node_V_address0 sc_out sc_lv 4 signal 12 } 
	{ st1_m_fifo_a_m_arr_node_V_ce0 sc_out sc_logic 1 signal 12 } 
	{ st1_m_fifo_a_m_arr_node_V_we0 sc_out sc_logic 1 signal 12 } 
	{ st1_m_fifo_a_m_arr_node_V_d0 sc_out sc_lv 8 signal 12 } 
	{ st1_m_fifo_a_m_arr_node_V_q0 sc_in sc_lv 8 signal 12 } 
	{ st1_m_fifo_b_m_arr_th_idx_V_address0 sc_out sc_lv 4 signal 13 } 
	{ st1_m_fifo_b_m_arr_th_idx_V_ce0 sc_out sc_logic 1 signal 13 } 
	{ st1_m_fifo_b_m_arr_th_idx_V_we0 sc_out sc_logic 1 signal 13 } 
	{ st1_m_fifo_b_m_arr_th_idx_V_d0 sc_out sc_lv 8 signal 13 } 
	{ st1_m_fifo_b_m_arr_th_idx_V_q0 sc_in sc_lv 8 signal 13 } 
	{ st1_m_fifo_b_m_arr_cell_V_address0 sc_out sc_lv 4 signal 14 } 
	{ st1_m_fifo_b_m_arr_cell_V_ce0 sc_out sc_logic 1 signal 14 } 
	{ st1_m_fifo_b_m_arr_cell_V_we0 sc_out sc_logic 1 signal 14 } 
	{ st1_m_fifo_b_m_arr_cell_V_d0 sc_out sc_lv 8 signal 14 } 
	{ st1_m_fifo_b_m_arr_cell_V_q0 sc_in sc_lv 8 signal 14 } 
	{ st1_m_fifo_b_m_arr_node_V_address0 sc_out sc_lv 4 signal 15 } 
	{ st1_m_fifo_b_m_arr_node_V_ce0 sc_out sc_logic 1 signal 15 } 
	{ st1_m_fifo_b_m_arr_node_V_we0 sc_out sc_logic 1 signal 15 } 
	{ st1_m_fifo_b_m_arr_node_V_d0 sc_out sc_lv 8 signal 15 } 
	{ st1_m_fifo_b_m_arr_node_V_q0 sc_in sc_lv 8 signal 15 } 
}
set NewPortList {[ 
	{ "name": "ap_clk", "direction": "in", "datatype": "sc_logic", "bitwidth":1, "type": "clock", "bundle":{"name": "ap_clk", "role": "default" }} , 
 	{ "name": "ap_rst", "direction": "in", "datatype": "sc_logic", "bitwidth":1, "type": "reset", "bundle":{"name": "ap_rst", "role": "default" }} , 
 	{ "name": "ap_start", "direction": "in", "datatype": "sc_logic", "bitwidth":1, "type": "start", "bundle":{"name": "ap_start", "role": "default" }} , 
 	{ "name": "ap_done", "direction": "out", "datatype": "sc_logic", "bitwidth":1, "type": "predone", "bundle":{"name": "ap_done", "role": "default" }} , 
 	{ "name": "ap_idle", "direction": "out", "datatype": "sc_logic", "bitwidth":1, "type": "done", "bundle":{"name": "ap_idle", "role": "default" }} , 
 	{ "name": "ap_ready", "direction": "out", "datatype": "sc_logic", "bitwidth":1, "type": "ready", "bundle":{"name": "ap_ready", "role": "default" }} , 
 	{ "name": "st1_m_fifo_a_m_size_V_reload", "direction": "in", "datatype": "sc_lv", "bitwidth":8, "type": "signal", "bundle":{"name": "st1_m_fifo_a_m_size_V_reload", "role": "default" }} , 
 	{ "name": "st1_m_fifo_a_m_rear_V_7_reload", "direction": "in", "datatype": "sc_lv", "bitwidth":8, "type": "signal", "bundle":{"name": "st1_m_fifo_a_m_rear_V_7_reload", "role": "default" }} , 
 	{ "name": "st1_m_fifo_b_m_size_V_reload", "direction": "in", "datatype": "sc_lv", "bitwidth":8, "type": "signal", "bundle":{"name": "st1_m_fifo_b_m_size_V_reload", "role": "default" }} , 
 	{ "name": "st1_m_fifo_b_m_rear_V_7_reload", "direction": "in", "datatype": "sc_lv", "bitwidth":8, "type": "signal", "bundle":{"name": "st1_m_fifo_b_m_rear_V_7_reload", "role": "default" }} , 
 	{ "name": "n2c_address0", "direction": "out", "datatype": "sc_lv", "bitwidth":3, "type": "signal", "bundle":{"name": "n2c", "role": "address0" }} , 
 	{ "name": "n2c_ce0", "direction": "out", "datatype": "sc_logic", "bitwidth":1, "type": "signal", "bundle":{"name": "n2c", "role": "ce0" }} , 
 	{ "name": "n2c_we0", "direction": "out", "datatype": "sc_lv", "bitwidth":100, "type": "signal", "bundle":{"name": "n2c", "role": "we0" }} , 
 	{ "name": "n2c_d0", "direction": "out", "datatype": "sc_lv", "bitwidth":800, "type": "signal", "bundle":{"name": "n2c", "role": "d0" }} , 
 	{ "name": "n2c_q0", "direction": "in", "datatype": "sc_lv", "bitwidth":800, "type": "signal", "bundle":{"name": "n2c", "role": "q0" }} , 
 	{ "name": "n2c_address1", "direction": "out", "datatype": "sc_lv", "bitwidth":3, "type": "signal", "bundle":{"name": "n2c", "role": "address1" }} , 
 	{ "name": "n2c_ce1", "direction": "out", "datatype": "sc_logic", "bitwidth":1, "type": "signal", "bundle":{"name": "n2c", "role": "ce1" }} , 
 	{ "name": "n2c_q1", "direction": "in", "datatype": "sc_lv", "bitwidth":800, "type": "signal", "bundle":{"name": "n2c", "role": "q1" }} , 
 	{ "name": "c2n_address0", "direction": "out", "datatype": "sc_lv", "bitwidth":3, "type": "signal", "bundle":{"name": "c2n", "role": "address0" }} , 
 	{ "name": "c2n_ce0", "direction": "out", "datatype": "sc_logic", "bitwidth":1, "type": "signal", "bundle":{"name": "c2n", "role": "ce0" }} , 
 	{ "name": "c2n_we0", "direction": "out", "datatype": "sc_lv", "bitwidth":100, "type": "signal", "bundle":{"name": "c2n", "role": "we0" }} , 
 	{ "name": "c2n_d0", "direction": "out", "datatype": "sc_lv", "bitwidth":800, "type": "signal", "bundle":{"name": "c2n", "role": "d0" }} , 
 	{ "name": "c2n_q0", "direction": "in", "datatype": "sc_lv", "bitwidth":800, "type": "signal", "bundle":{"name": "c2n", "role": "q0" }} , 
 	{ "name": "c2n_address1", "direction": "out", "datatype": "sc_lv", "bitwidth":3, "type": "signal", "bundle":{"name": "c2n", "role": "address1" }} , 
 	{ "name": "c2n_ce1", "direction": "out", "datatype": "sc_logic", "bitwidth":1, "type": "signal", "bundle":{"name": "c2n", "role": "ce1" }} , 
 	{ "name": "c2n_q1", "direction": "in", "datatype": "sc_lv", "bitwidth":800, "type": "signal", "bundle":{"name": "c2n", "role": "q1" }} , 
 	{ "name": "n_address0", "direction": "out", "datatype": "sc_lv", "bitwidth":7, "type": "signal", "bundle":{"name": "n", "role": "address0" }} , 
 	{ "name": "n_ce0", "direction": "out", "datatype": "sc_logic", "bitwidth":1, "type": "signal", "bundle":{"name": "n", "role": "ce0" }} , 
 	{ "name": "n_q0", "direction": "in", "datatype": "sc_lv", "bitwidth":32, "type": "signal", "bundle":{"name": "n", "role": "q0" }} , 
 	{ "name": "n_address1", "direction": "out", "datatype": "sc_lv", "bitwidth":7, "type": "signal", "bundle":{"name": "n", "role": "address1" }} , 
 	{ "name": "n_ce1", "direction": "out", "datatype": "sc_logic", "bitwidth":1, "type": "signal", "bundle":{"name": "n", "role": "ce1" }} , 
 	{ "name": "n_q1", "direction": "in", "datatype": "sc_lv", "bitwidth":32, "type": "signal", "bundle":{"name": "n", "role": "q1" }} , 
 	{ "name": "st0_m_th_valid_address0", "direction": "out", "datatype": "sc_lv", "bitwidth":3, "type": "signal", "bundle":{"name": "st0_m_th_valid", "role": "address0" }} , 
 	{ "name": "st0_m_th_valid_ce0", "direction": "out", "datatype": "sc_logic", "bitwidth":1, "type": "signal", "bundle":{"name": "st0_m_th_valid", "role": "ce0" }} , 
 	{ "name": "st0_m_th_valid_we0", "direction": "out", "datatype": "sc_logic", "bitwidth":1, "type": "signal", "bundle":{"name": "st0_m_th_valid", "role": "we0" }} , 
 	{ "name": "st0_m_th_valid_d0", "direction": "out", "datatype": "sc_lv", "bitwidth":1, "type": "signal", "bundle":{"name": "st0_m_th_valid", "role": "d0" }} , 
 	{ "name": "st0_m_th_valid_q0", "direction": "in", "datatype": "sc_lv", "bitwidth":1, "type": "signal", "bundle":{"name": "st0_m_th_valid", "role": "q0" }} , 
 	{ "name": "st0_m_cell_a_V_address0", "direction": "out", "datatype": "sc_lv", "bitwidth":3, "type": "signal", "bundle":{"name": "st0_m_cell_a_V", "role": "address0" }} , 
 	{ "name": "st0_m_cell_a_V_ce0", "direction": "out", "datatype": "sc_logic", "bitwidth":1, "type": "signal", "bundle":{"name": "st0_m_cell_a_V", "role": "ce0" }} , 
 	{ "name": "st0_m_cell_a_V_we0", "direction": "out", "datatype": "sc_logic", "bitwidth":1, "type": "signal", "bundle":{"name": "st0_m_cell_a_V", "role": "we0" }} , 
 	{ "name": "st0_m_cell_a_V_d0", "direction": "out", "datatype": "sc_lv", "bitwidth":8, "type": "signal", "bundle":{"name": "st0_m_cell_a_V", "role": "d0" }} , 
 	{ "name": "st0_m_cell_a_V_q0", "direction": "in", "datatype": "sc_lv", "bitwidth":8, "type": "signal", "bundle":{"name": "st0_m_cell_a_V", "role": "q0" }} , 
 	{ "name": "st0_m_cell_b_V_address0", "direction": "out", "datatype": "sc_lv", "bitwidth":3, "type": "signal", "bundle":{"name": "st0_m_cell_b_V", "role": "address0" }} , 
 	{ "name": "st0_m_cell_b_V_ce0", "direction": "out", "datatype": "sc_logic", "bitwidth":1, "type": "signal", "bundle":{"name": "st0_m_cell_b_V", "role": "ce0" }} , 
 	{ "name": "st0_m_cell_b_V_we0", "direction": "out", "datatype": "sc_logic", "bitwidth":1, "type": "signal", "bundle":{"name": "st0_m_cell_b_V", "role": "we0" }} , 
 	{ "name": "st0_m_cell_b_V_d0", "direction": "out", "datatype": "sc_lv", "bitwidth":8, "type": "signal", "bundle":{"name": "st0_m_cell_b_V", "role": "d0" }} , 
 	{ "name": "st0_m_cell_b_V_q0", "direction": "in", "datatype": "sc_lv", "bitwidth":8, "type": "signal", "bundle":{"name": "st0_m_cell_b_V", "role": "q0" }} , 
 	{ "name": "st1_m_fifo_a_m_arr_th_idx_V_address0", "direction": "out", "datatype": "sc_lv", "bitwidth":4, "type": "signal", "bundle":{"name": "st1_m_fifo_a_m_arr_th_idx_V", "role": "address0" }} , 
 	{ "name": "st1_m_fifo_a_m_arr_th_idx_V_ce0", "direction": "out", "datatype": "sc_logic", "bitwidth":1, "type": "signal", "bundle":{"name": "st1_m_fifo_a_m_arr_th_idx_V", "role": "ce0" }} , 
 	{ "name": "st1_m_fifo_a_m_arr_th_idx_V_we0", "direction": "out", "datatype": "sc_logic", "bitwidth":1, "type": "signal", "bundle":{"name": "st1_m_fifo_a_m_arr_th_idx_V", "role": "we0" }} , 
 	{ "name": "st1_m_fifo_a_m_arr_th_idx_V_d0", "direction": "out", "datatype": "sc_lv", "bitwidth":8, "type": "signal", "bundle":{"name": "st1_m_fifo_a_m_arr_th_idx_V", "role": "d0" }} , 
 	{ "name": "st1_m_fifo_a_m_arr_th_idx_V_q0", "direction": "in", "datatype": "sc_lv", "bitwidth":8, "type": "signal", "bundle":{"name": "st1_m_fifo_a_m_arr_th_idx_V", "role": "q0" }} , 
 	{ "name": "st1_m_fifo_a_m_arr_cell_V_address0", "direction": "out", "datatype": "sc_lv", "bitwidth":4, "type": "signal", "bundle":{"name": "st1_m_fifo_a_m_arr_cell_V", "role": "address0" }} , 
 	{ "name": "st1_m_fifo_a_m_arr_cell_V_ce0", "direction": "out", "datatype": "sc_logic", "bitwidth":1, "type": "signal", "bundle":{"name": "st1_m_fifo_a_m_arr_cell_V", "role": "ce0" }} , 
 	{ "name": "st1_m_fifo_a_m_arr_cell_V_we0", "direction": "out", "datatype": "sc_logic", "bitwidth":1, "type": "signal", "bundle":{"name": "st1_m_fifo_a_m_arr_cell_V", "role": "we0" }} , 
 	{ "name": "st1_m_fifo_a_m_arr_cell_V_d0", "direction": "out", "datatype": "sc_lv", "bitwidth":8, "type": "signal", "bundle":{"name": "st1_m_fifo_a_m_arr_cell_V", "role": "d0" }} , 
 	{ "name": "st1_m_fifo_a_m_arr_cell_V_q0", "direction": "in", "datatype": "sc_lv", "bitwidth":8, "type": "signal", "bundle":{"name": "st1_m_fifo_a_m_arr_cell_V", "role": "q0" }} , 
 	{ "name": "st1_m_fifo_a_m_arr_node_V_address0", "direction": "out", "datatype": "sc_lv", "bitwidth":4, "type": "signal", "bundle":{"name": "st1_m_fifo_a_m_arr_node_V", "role": "address0" }} , 
 	{ "name": "st1_m_fifo_a_m_arr_node_V_ce0", "direction": "out", "datatype": "sc_logic", "bitwidth":1, "type": "signal", "bundle":{"name": "st1_m_fifo_a_m_arr_node_V", "role": "ce0" }} , 
 	{ "name": "st1_m_fifo_a_m_arr_node_V_we0", "direction": "out", "datatype": "sc_logic", "bitwidth":1, "type": "signal", "bundle":{"name": "st1_m_fifo_a_m_arr_node_V", "role": "we0" }} , 
 	{ "name": "st1_m_fifo_a_m_arr_node_V_d0", "direction": "out", "datatype": "sc_lv", "bitwidth":8, "type": "signal", "bundle":{"name": "st1_m_fifo_a_m_arr_node_V", "role": "d0" }} , 
 	{ "name": "st1_m_fifo_a_m_arr_node_V_q0", "direction": "in", "datatype": "sc_lv", "bitwidth":8, "type": "signal", "bundle":{"name": "st1_m_fifo_a_m_arr_node_V", "role": "q0" }} , 
 	{ "name": "st1_m_fifo_b_m_arr_th_idx_V_address0", "direction": "out", "datatype": "sc_lv", "bitwidth":4, "type": "signal", "bundle":{"name": "st1_m_fifo_b_m_arr_th_idx_V", "role": "address0" }} , 
 	{ "name": "st1_m_fifo_b_m_arr_th_idx_V_ce0", "direction": "out", "datatype": "sc_logic", "bitwidth":1, "type": "signal", "bundle":{"name": "st1_m_fifo_b_m_arr_th_idx_V", "role": "ce0" }} , 
 	{ "name": "st1_m_fifo_b_m_arr_th_idx_V_we0", "direction": "out", "datatype": "sc_logic", "bitwidth":1, "type": "signal", "bundle":{"name": "st1_m_fifo_b_m_arr_th_idx_V", "role": "we0" }} , 
 	{ "name": "st1_m_fifo_b_m_arr_th_idx_V_d0", "direction": "out", "datatype": "sc_lv", "bitwidth":8, "type": "signal", "bundle":{"name": "st1_m_fifo_b_m_arr_th_idx_V", "role": "d0" }} , 
 	{ "name": "st1_m_fifo_b_m_arr_th_idx_V_q0", "direction": "in", "datatype": "sc_lv", "bitwidth":8, "type": "signal", "bundle":{"name": "st1_m_fifo_b_m_arr_th_idx_V", "role": "q0" }} , 
 	{ "name": "st1_m_fifo_b_m_arr_cell_V_address0", "direction": "out", "datatype": "sc_lv", "bitwidth":4, "type": "signal", "bundle":{"name": "st1_m_fifo_b_m_arr_cell_V", "role": "address0" }} , 
 	{ "name": "st1_m_fifo_b_m_arr_cell_V_ce0", "direction": "out", "datatype": "sc_logic", "bitwidth":1, "type": "signal", "bundle":{"name": "st1_m_fifo_b_m_arr_cell_V", "role": "ce0" }} , 
 	{ "name": "st1_m_fifo_b_m_arr_cell_V_we0", "direction": "out", "datatype": "sc_logic", "bitwidth":1, "type": "signal", "bundle":{"name": "st1_m_fifo_b_m_arr_cell_V", "role": "we0" }} , 
 	{ "name": "st1_m_fifo_b_m_arr_cell_V_d0", "direction": "out", "datatype": "sc_lv", "bitwidth":8, "type": "signal", "bundle":{"name": "st1_m_fifo_b_m_arr_cell_V", "role": "d0" }} , 
 	{ "name": "st1_m_fifo_b_m_arr_cell_V_q0", "direction": "in", "datatype": "sc_lv", "bitwidth":8, "type": "signal", "bundle":{"name": "st1_m_fifo_b_m_arr_cell_V", "role": "q0" }} , 
 	{ "name": "st1_m_fifo_b_m_arr_node_V_address0", "direction": "out", "datatype": "sc_lv", "bitwidth":4, "type": "signal", "bundle":{"name": "st1_m_fifo_b_m_arr_node_V", "role": "address0" }} , 
 	{ "name": "st1_m_fifo_b_m_arr_node_V_ce0", "direction": "out", "datatype": "sc_logic", "bitwidth":1, "type": "signal", "bundle":{"name": "st1_m_fifo_b_m_arr_node_V", "role": "ce0" }} , 
 	{ "name": "st1_m_fifo_b_m_arr_node_V_we0", "direction": "out", "datatype": "sc_logic", "bitwidth":1, "type": "signal", "bundle":{"name": "st1_m_fifo_b_m_arr_node_V", "role": "we0" }} , 
 	{ "name": "st1_m_fifo_b_m_arr_node_V_d0", "direction": "out", "datatype": "sc_lv", "bitwidth":8, "type": "signal", "bundle":{"name": "st1_m_fifo_b_m_arr_node_V", "role": "d0" }} , 
 	{ "name": "st1_m_fifo_b_m_arr_node_V_q0", "direction": "in", "datatype": "sc_lv", "bitwidth":8, "type": "signal", "bundle":{"name": "st1_m_fifo_b_m_arr_node_V", "role": "q0" }}  ]}

set RtlHierarchyInfo {[
	{"ID" : "0", "Level" : "0", "Path" : "`AUTOTB_DUT_INST", "Parent" : "", "Child" : ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58", "59", "60", "61", "62", "63", "64", "65", "66", "67"],
		"CDFG" : "exec_pipeline_Pipeline_VITIS_LOOP_27_1",
		"Protocol" : "ap_ctrl_hs",
		"ControlExist" : "1", "ap_start" : "1", "ap_ready" : "1", "ap_done" : "1", "ap_continue" : "0", "ap_idle" : "1", "real_start" : "0",
		"Pipeline" : "None", "UnalignedPipeline" : "0", "RewindPipeline" : "0", "ProcessNetwork" : "0",
		"II" : "0",
		"VariableLatency" : "1", "ExactLatency" : "-1", "EstimateLatencyMin" : "120000021", "EstimateLatencyMax" : "120000021",
		"Combinational" : "0",
		"Datapath" : "0",
		"ClockEnable" : "0",
		"HasSubDataflow" : "0",
		"InDataflowNetwork" : "0",
		"HasNonBlockingOperation" : "0",
		"IsBlackBox" : "0",
		"Port" : [
			{"Name" : "st1_m_fifo_a_m_size_V_reload", "Type" : "None", "Direction" : "I"},
			{"Name" : "st1_m_fifo_a_m_rear_V_7_reload", "Type" : "None", "Direction" : "I"},
			{"Name" : "st1_m_fifo_b_m_size_V_reload", "Type" : "None", "Direction" : "I"},
			{"Name" : "st1_m_fifo_b_m_rear_V_7_reload", "Type" : "None", "Direction" : "I"},
			{"Name" : "n2c", "Type" : "Memory", "Direction" : "IO"},
			{"Name" : "c2n", "Type" : "Memory", "Direction" : "IO"},
			{"Name" : "n", "Type" : "Memory", "Direction" : "I"},
			{"Name" : "st0_m_th_valid", "Type" : "Memory", "Direction" : "IO"},
			{"Name" : "st0_m_cell_a_V", "Type" : "Memory", "Direction" : "IO"},
			{"Name" : "st0_m_cell_b_V", "Type" : "Memory", "Direction" : "IO"},
			{"Name" : "st1_m_fifo_a_m_arr_th_idx_V", "Type" : "Memory", "Direction" : "IO"},
			{"Name" : "st1_m_fifo_a_m_arr_cell_V", "Type" : "Memory", "Direction" : "IO"},
			{"Name" : "st1_m_fifo_a_m_arr_node_V", "Type" : "Memory", "Direction" : "IO"},
			{"Name" : "st1_m_fifo_b_m_arr_th_idx_V", "Type" : "Memory", "Direction" : "IO"},
			{"Name" : "st1_m_fifo_b_m_arr_cell_V", "Type" : "Memory", "Direction" : "IO"},
			{"Name" : "st1_m_fifo_b_m_arr_node_V", "Type" : "Memory", "Direction" : "IO"},
			{"Name" : "st3_m_th_idx_offset", "Type" : "Memory", "Direction" : "I"},
			{"Name" : "st1_m_th_idx_offset", "Type" : "Memory", "Direction" : "I"}],
		"Loop" : [
			{"Name" : "VITIS_LOOP_27_1", "PipelineType" : "UPC",
				"LoopDec" : {"FSMBitwidth" : "12", "FirstState" : "ap_ST_fsm_pp0_stage0", "FirstStateIter" : "ap_enable_reg_pp0_iter0", "FirstStateBlock" : "ap_block_pp0_stage0_subdone", "LastState" : "ap_ST_fsm_pp0_stage7", "LastStateIter" : "ap_enable_reg_pp0_iter2", "LastStateBlock" : "ap_block_pp0_stage7_subdone", "QuitState" : "ap_ST_fsm_pp0_stage7", "QuitStateIter" : "ap_enable_reg_pp0_iter2", "QuitStateBlock" : "ap_block_pp0_stage7_subdone", "OneDepthLoop" : "0", "has_ap_ctrl" : "1", "has_continue" : "0"}}]},
	{"ID" : "1", "Level" : "1", "Path" : "`AUTOTB_DUT_INST.st3_m_th_idx_offset_U", "Parent" : "0"},
	{"ID" : "2", "Level" : "1", "Path" : "`AUTOTB_DUT_INST.st1_m_th_idx_offset_U", "Parent" : "0"},
	{"ID" : "3", "Level" : "1", "Path" : "`AUTOTB_DUT_INST.srem_9ns_5ns_5_13_1_U25", "Parent" : "0"},
	{"ID" : "4", "Level" : "1", "Path" : "`AUTOTB_DUT_INST.srem_9ns_5ns_5_13_1_U26", "Parent" : "0"},
	{"ID" : "5", "Level" : "1", "Path" : "`AUTOTB_DUT_INST.srem_9ns_5ns_8_13_1_U27", "Parent" : "0"},
	{"ID" : "6", "Level" : "1", "Path" : "`AUTOTB_DUT_INST.srem_9ns_5ns_8_13_1_U28", "Parent" : "0"},
	{"ID" : "7", "Level" : "1", "Path" : "`AUTOTB_DUT_INST.srem_8s_5ns_5_12_1_U29", "Parent" : "0"},
	{"ID" : "8", "Level" : "1", "Path" : "`AUTOTB_DUT_INST.srem_8s_5ns_5_12_1_U30", "Parent" : "0"},
	{"ID" : "9", "Level" : "1", "Path" : "`AUTOTB_DUT_INST.mul_8ns_10ns_17_1_1_U31", "Parent" : "0"},
	{"ID" : "10", "Level" : "1", "Path" : "`AUTOTB_DUT_INST.urem_8ns_4ns_8_12_1_U32", "Parent" : "0"},
	{"ID" : "11", "Level" : "1", "Path" : "`AUTOTB_DUT_INST.mul_8ns_10ns_17_1_1_U33", "Parent" : "0"},
	{"ID" : "12", "Level" : "1", "Path" : "`AUTOTB_DUT_INST.urem_8ns_4ns_8_12_1_U34", "Parent" : "0"},
	{"ID" : "13", "Level" : "1", "Path" : "`AUTOTB_DUT_INST.mul_8ns_10ns_17_1_1_U35", "Parent" : "0"},
	{"ID" : "14", "Level" : "1", "Path" : "`AUTOTB_DUT_INST.urem_8ns_4ns_8_12_1_U36", "Parent" : "0"},
	{"ID" : "15", "Level" : "1", "Path" : "`AUTOTB_DUT_INST.srem_8s_5ns_5_12_1_U37", "Parent" : "0"},
	{"ID" : "16", "Level" : "1", "Path" : "`AUTOTB_DUT_INST.urem_8ns_4ns_8_12_1_U38", "Parent" : "0"},
	{"ID" : "17", "Level" : "1", "Path" : "`AUTOTB_DUT_INST.urem_8ns_4ns_8_12_1_U39", "Parent" : "0"},
	{"ID" : "18", "Level" : "1", "Path" : "`AUTOTB_DUT_INST.srem_8s_5ns_5_12_1_U40", "Parent" : "0"},
	{"ID" : "19", "Level" : "1", "Path" : "`AUTOTB_DUT_INST.srem_8s_5ns_5_12_1_U41", "Parent" : "0"},
	{"ID" : "20", "Level" : "1", "Path" : "`AUTOTB_DUT_INST.srem_8s_5ns_5_12_1_U42", "Parent" : "0"},
	{"ID" : "21", "Level" : "1", "Path" : "`AUTOTB_DUT_INST.srem_8s_5ns_5_12_1_U43", "Parent" : "0"},
	{"ID" : "22", "Level" : "1", "Path" : "`AUTOTB_DUT_INST.mul_8ns_10ns_17_1_1_U44", "Parent" : "0"},
	{"ID" : "23", "Level" : "1", "Path" : "`AUTOTB_DUT_INST.urem_8ns_4ns_8_12_1_U45", "Parent" : "0"},
	{"ID" : "24", "Level" : "1", "Path" : "`AUTOTB_DUT_INST.srem_8s_5ns_5_12_1_U46", "Parent" : "0"},
	{"ID" : "25", "Level" : "1", "Path" : "`AUTOTB_DUT_INST.srem_8s_5ns_5_12_1_U47", "Parent" : "0"},
	{"ID" : "26", "Level" : "1", "Path" : "`AUTOTB_DUT_INST.mul_8ns_10ns_17_1_1_U48", "Parent" : "0"},
	{"ID" : "27", "Level" : "1", "Path" : "`AUTOTB_DUT_INST.urem_8ns_8ns_8_12_1_U49", "Parent" : "0"},
	{"ID" : "28", "Level" : "1", "Path" : "`AUTOTB_DUT_INST.mul_8ns_10ns_17_1_1_U50", "Parent" : "0"},
	{"ID" : "29", "Level" : "1", "Path" : "`AUTOTB_DUT_INST.urem_8ns_8ns_8_12_1_U51", "Parent" : "0"},
	{"ID" : "30", "Level" : "1", "Path" : "`AUTOTB_DUT_INST.urem_8ns_8ns_8_12_1_U52", "Parent" : "0"},
	{"ID" : "31", "Level" : "1", "Path" : "`AUTOTB_DUT_INST.mul_8ns_10ns_17_1_1_U53", "Parent" : "0"},
	{"ID" : "32", "Level" : "1", "Path" : "`AUTOTB_DUT_INST.urem_8ns_8ns_8_12_1_U54", "Parent" : "0"},
	{"ID" : "33", "Level" : "1", "Path" : "`AUTOTB_DUT_INST.urem_8ns_8ns_8_12_1_U55", "Parent" : "0"},
	{"ID" : "34", "Level" : "1", "Path" : "`AUTOTB_DUT_INST.urem_8ns_4ns_8_12_1_U56", "Parent" : "0"},
	{"ID" : "35", "Level" : "1", "Path" : "`AUTOTB_DUT_INST.urem_8ns_4ns_8_12_1_U57", "Parent" : "0"},
	{"ID" : "36", "Level" : "1", "Path" : "`AUTOTB_DUT_INST.urem_8ns_4ns_8_12_1_U58", "Parent" : "0"},
	{"ID" : "37", "Level" : "1", "Path" : "`AUTOTB_DUT_INST.urem_8ns_4ns_8_12_1_U59", "Parent" : "0"},
	{"ID" : "38", "Level" : "1", "Path" : "`AUTOTB_DUT_INST.urem_8ns_4ns_8_12_1_U60", "Parent" : "0"},
	{"ID" : "39", "Level" : "1", "Path" : "`AUTOTB_DUT_INST.srem_8s_5ns_5_12_1_U61", "Parent" : "0"},
	{"ID" : "40", "Level" : "1", "Path" : "`AUTOTB_DUT_INST.mul_8ns_10ns_17_1_1_U62", "Parent" : "0"},
	{"ID" : "41", "Level" : "1", "Path" : "`AUTOTB_DUT_INST.mul_8ns_10ns_17_1_1_U63", "Parent" : "0"},
	{"ID" : "42", "Level" : "1", "Path" : "`AUTOTB_DUT_INST.srem_8s_5ns_5_12_1_U64", "Parent" : "0"},
	{"ID" : "43", "Level" : "1", "Path" : "`AUTOTB_DUT_INST.srem_8s_5ns_5_12_1_U65", "Parent" : "0"},
	{"ID" : "44", "Level" : "1", "Path" : "`AUTOTB_DUT_INST.srem_8s_5ns_5_12_1_U66", "Parent" : "0"},
	{"ID" : "45", "Level" : "1", "Path" : "`AUTOTB_DUT_INST.srem_8s_5ns_5_12_1_U67", "Parent" : "0"},
	{"ID" : "46", "Level" : "1", "Path" : "`AUTOTB_DUT_INST.mul_8ns_10ns_17_1_1_U68", "Parent" : "0"},
	{"ID" : "47", "Level" : "1", "Path" : "`AUTOTB_DUT_INST.mul_8ns_10ns_17_1_1_U69", "Parent" : "0"},
	{"ID" : "48", "Level" : "1", "Path" : "`AUTOTB_DUT_INST.mul_8ns_10ns_17_1_1_U70", "Parent" : "0"},
	{"ID" : "49", "Level" : "1", "Path" : "`AUTOTB_DUT_INST.mul_8ns_10ns_17_1_1_U71", "Parent" : "0"},
	{"ID" : "50", "Level" : "1", "Path" : "`AUTOTB_DUT_INST.mul_8ns_10ns_17_1_1_U72", "Parent" : "0"},
	{"ID" : "51", "Level" : "1", "Path" : "`AUTOTB_DUT_INST.mul_8ns_10ns_17_1_1_U73", "Parent" : "0"},
	{"ID" : "52", "Level" : "1", "Path" : "`AUTOTB_DUT_INST.mul_8ns_10ns_17_1_1_U74", "Parent" : "0"},
	{"ID" : "53", "Level" : "1", "Path" : "`AUTOTB_DUT_INST.mul_8s_10ns_18_1_1_U75", "Parent" : "0"},
	{"ID" : "54", "Level" : "1", "Path" : "`AUTOTB_DUT_INST.mul_8s_10ns_18_1_1_U76", "Parent" : "0"},
	{"ID" : "55", "Level" : "1", "Path" : "`AUTOTB_DUT_INST.mul_8s_10ns_18_1_1_U77", "Parent" : "0"},
	{"ID" : "56", "Level" : "1", "Path" : "`AUTOTB_DUT_INST.mul_8s_10ns_18_1_1_U78", "Parent" : "0"},
	{"ID" : "57", "Level" : "1", "Path" : "`AUTOTB_DUT_INST.mul_8s_10ns_18_1_1_U79", "Parent" : "0"},
	{"ID" : "58", "Level" : "1", "Path" : "`AUTOTB_DUT_INST.mul_8s_10ns_18_1_1_U80", "Parent" : "0"},
	{"ID" : "59", "Level" : "1", "Path" : "`AUTOTB_DUT_INST.mul_8s_10ns_18_1_1_U81", "Parent" : "0"},
	{"ID" : "60", "Level" : "1", "Path" : "`AUTOTB_DUT_INST.mul_8s_10ns_18_1_1_U82", "Parent" : "0"},
	{"ID" : "61", "Level" : "1", "Path" : "`AUTOTB_DUT_INST.mul_8s_10ns_18_1_1_U83", "Parent" : "0"},
	{"ID" : "62", "Level" : "1", "Path" : "`AUTOTB_DUT_INST.mul_8s_10ns_18_1_1_U84", "Parent" : "0"},
	{"ID" : "63", "Level" : "1", "Path" : "`AUTOTB_DUT_INST.mul_8s_10ns_18_1_1_U85", "Parent" : "0"},
	{"ID" : "64", "Level" : "1", "Path" : "`AUTOTB_DUT_INST.mul_8s_10ns_18_1_1_U86", "Parent" : "0"},
	{"ID" : "65", "Level" : "1", "Path" : "`AUTOTB_DUT_INST.mul_8s_10ns_18_1_1_U87", "Parent" : "0"},
	{"ID" : "66", "Level" : "1", "Path" : "`AUTOTB_DUT_INST.mul_8s_10ns_18_1_1_U88", "Parent" : "0"},
	{"ID" : "67", "Level" : "1", "Path" : "`AUTOTB_DUT_INST.flow_control_loop_pipe_sequential_init_U", "Parent" : "0"}]}


set ArgLastReadFirstWriteLatency {
	exec_pipeline_Pipeline_VITIS_LOOP_27_1 {
		st1_m_fifo_a_m_size_V_reload {Type I LastRead 0 FirstWrite -1}
		st1_m_fifo_a_m_rear_V_7_reload {Type I LastRead 0 FirstWrite -1}
		st1_m_fifo_b_m_size_V_reload {Type I LastRead 0 FirstWrite -1}
		st1_m_fifo_b_m_rear_V_7_reload {Type I LastRead 0 FirstWrite -1}
		n2c {Type IO LastRead 23 FirstWrite 13}
		c2n {Type IO LastRead 18 FirstWrite 13}
		n {Type I LastRead 22 FirstWrite -1}
		st0_m_th_valid {Type IO LastRead 2 FirstWrite 1}
		st0_m_cell_a_V {Type IO LastRead 3 FirstWrite 2}
		st0_m_cell_b_V {Type IO LastRead 4 FirstWrite 3}
		st1_m_fifo_a_m_arr_th_idx_V {Type IO LastRead 13 FirstWrite 12}
		st1_m_fifo_a_m_arr_cell_V {Type IO LastRead 13 FirstWrite 12}
		st1_m_fifo_a_m_arr_node_V {Type IO LastRead 13 FirstWrite 12}
		st1_m_fifo_b_m_arr_th_idx_V {Type IO LastRead 13 FirstWrite 12}
		st1_m_fifo_b_m_arr_cell_V {Type IO LastRead 13 FirstWrite 12}
		st1_m_fifo_b_m_arr_node_V {Type IO LastRead 13 FirstWrite 12}
		st3_m_th_idx_offset {Type I LastRead -1 FirstWrite -1}
		st1_m_th_idx_offset {Type I LastRead -1 FirstWrite -1}}}

set hasDtUnsupportedChannel 0

set PerformanceInfo {[
	{"Name" : "Latency", "Min" : "120000021", "Max" : "120000021"}
	, {"Name" : "Interval", "Min" : "120000021", "Max" : "120000021"}
]}

set PipelineEnableSignalInfo {[
	{"Pipeline" : "0", "EnableSignal" : "ap_enable_pp0"}
]}

set Spec2ImplPortList { 
	st1_m_fifo_a_m_size_V_reload { ap_none {  { st1_m_fifo_a_m_size_V_reload in_data 0 8 } } }
	st1_m_fifo_a_m_rear_V_7_reload { ap_none {  { st1_m_fifo_a_m_rear_V_7_reload in_data 0 8 } } }
	st1_m_fifo_b_m_size_V_reload { ap_none {  { st1_m_fifo_b_m_size_V_reload in_data 0 8 } } }
	st1_m_fifo_b_m_rear_V_7_reload { ap_none {  { st1_m_fifo_b_m_rear_V_7_reload in_data 0 8 } } }
	n2c { ap_memory {  { n2c_address0 mem_address 1 3 }  { n2c_ce0 mem_ce 1 1 }  { n2c_we0 mem_we 1 100 }  { n2c_d0 mem_din 1 800 }  { n2c_q0 mem_dout 0 800 }  { n2c_address1 MemPortADDR2 1 3 }  { n2c_ce1 MemPortCE2 1 1 }  { n2c_q1 MemPortDOUT2 0 800 } } }
	c2n { ap_memory {  { c2n_address0 mem_address 1 3 }  { c2n_ce0 mem_ce 1 1 }  { c2n_we0 mem_we 1 100 }  { c2n_d0 mem_din 1 800 }  { c2n_q0 in_data 0 800 }  { c2n_address1 MemPortADDR2 1 3 }  { c2n_ce1 MemPortCE2 1 1 }  { c2n_q1 in_data 0 800 } } }
	n { ap_memory {  { n_address0 mem_address 1 7 }  { n_ce0 mem_ce 1 1 }  { n_q0 in_data 0 32 }  { n_address1 MemPortADDR2 1 7 }  { n_ce1 MemPortCE2 1 1 }  { n_q1 in_data 0 32 } } }
	st0_m_th_valid { ap_memory {  { st0_m_th_valid_address0 mem_address 1 3 }  { st0_m_th_valid_ce0 mem_ce 1 1 }  { st0_m_th_valid_we0 mem_we 1 1 }  { st0_m_th_valid_d0 mem_din 1 1 }  { st0_m_th_valid_q0 in_data 0 1 } } }
	st0_m_cell_a_V { ap_memory {  { st0_m_cell_a_V_address0 mem_address 1 3 }  { st0_m_cell_a_V_ce0 mem_ce 1 1 }  { st0_m_cell_a_V_we0 mem_we 1 1 }  { st0_m_cell_a_V_d0 mem_din 1 8 }  { st0_m_cell_a_V_q0 in_data 0 8 } } }
	st0_m_cell_b_V { ap_memory {  { st0_m_cell_b_V_address0 mem_address 1 3 }  { st0_m_cell_b_V_ce0 mem_ce 1 1 }  { st0_m_cell_b_V_we0 mem_we 1 1 }  { st0_m_cell_b_V_d0 mem_din 1 8 }  { st0_m_cell_b_V_q0 in_data 0 8 } } }
	st1_m_fifo_a_m_arr_th_idx_V { ap_memory {  { st1_m_fifo_a_m_arr_th_idx_V_address0 mem_address 1 4 }  { st1_m_fifo_a_m_arr_th_idx_V_ce0 mem_ce 1 1 }  { st1_m_fifo_a_m_arr_th_idx_V_we0 mem_we 1 1 }  { st1_m_fifo_a_m_arr_th_idx_V_d0 mem_din 1 8 }  { st1_m_fifo_a_m_arr_th_idx_V_q0 in_data 0 8 } } }
	st1_m_fifo_a_m_arr_cell_V { ap_memory {  { st1_m_fifo_a_m_arr_cell_V_address0 mem_address 1 4 }  { st1_m_fifo_a_m_arr_cell_V_ce0 mem_ce 1 1 }  { st1_m_fifo_a_m_arr_cell_V_we0 mem_we 1 1 }  { st1_m_fifo_a_m_arr_cell_V_d0 mem_din 1 8 }  { st1_m_fifo_a_m_arr_cell_V_q0 in_data 0 8 } } }
	st1_m_fifo_a_m_arr_node_V { ap_memory {  { st1_m_fifo_a_m_arr_node_V_address0 mem_address 1 4 }  { st1_m_fifo_a_m_arr_node_V_ce0 mem_ce 1 1 }  { st1_m_fifo_a_m_arr_node_V_we0 mem_we 1 1 }  { st1_m_fifo_a_m_arr_node_V_d0 mem_din 1 8 }  { st1_m_fifo_a_m_arr_node_V_q0 in_data 0 8 } } }
	st1_m_fifo_b_m_arr_th_idx_V { ap_memory {  { st1_m_fifo_b_m_arr_th_idx_V_address0 mem_address 1 4 }  { st1_m_fifo_b_m_arr_th_idx_V_ce0 mem_ce 1 1 }  { st1_m_fifo_b_m_arr_th_idx_V_we0 mem_we 1 1 }  { st1_m_fifo_b_m_arr_th_idx_V_d0 mem_din 1 8 }  { st1_m_fifo_b_m_arr_th_idx_V_q0 in_data 0 8 } } }
	st1_m_fifo_b_m_arr_cell_V { ap_memory {  { st1_m_fifo_b_m_arr_cell_V_address0 mem_address 1 4 }  { st1_m_fifo_b_m_arr_cell_V_ce0 mem_ce 1 1 }  { st1_m_fifo_b_m_arr_cell_V_we0 mem_we 1 1 }  { st1_m_fifo_b_m_arr_cell_V_d0 mem_din 1 8 }  { st1_m_fifo_b_m_arr_cell_V_q0 in_data 0 8 } } }
	st1_m_fifo_b_m_arr_node_V { ap_memory {  { st1_m_fifo_b_m_arr_node_V_address0 mem_address 1 4 }  { st1_m_fifo_b_m_arr_node_V_ce0 mem_ce 1 1 }  { st1_m_fifo_b_m_arr_node_V_we0 mem_we 1 1 }  { st1_m_fifo_b_m_arr_node_V_d0 mem_din 1 8 }  { st1_m_fifo_b_m_arr_node_V_q0 in_data 0 8 } } }
}
