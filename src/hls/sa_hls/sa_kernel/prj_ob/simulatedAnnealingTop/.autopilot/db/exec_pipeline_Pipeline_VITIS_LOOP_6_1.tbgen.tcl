set moduleName exec_pipeline_Pipeline_VITIS_LOOP_6_1
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
set C_modelName {exec_pipeline_Pipeline_VITIS_LOOP_6_1}
set C_modelType { void 0 }
set C_modelArgList {
	{ st1_m_fifo_a_m_arr_th_idx_V int 8 regular {array 10 { 0 3 } 0 1 }  }
	{ st1_m_fifo_a_m_arr_cell_V int 8 regular {array 10 { 0 3 } 0 1 }  }
	{ st1_m_fifo_a_m_arr_node_V int 8 regular {array 10 { 0 3 } 0 1 }  }
	{ st1_m_fifo_b_m_arr_th_idx_V int 8 regular {array 10 { 0 3 } 0 1 }  }
	{ st1_m_fifo_b_m_arr_cell_V int 8 regular {array 10 { 0 3 } 0 1 }  }
	{ st1_m_fifo_b_m_arr_node_V int 8 regular {array 10 { 0 3 } 0 1 }  }
	{ st1_m_fifo_a_m_size_V_out int 8 regular {pointer 1}  }
	{ st1_m_fifo_a_m_rear_V_7_out int 8 regular {pointer 1}  }
	{ st1_m_fifo_b_m_size_V_out int 8 regular {pointer 1}  }
	{ st1_m_fifo_b_m_rear_V_7_out int 8 regular {pointer 1}  }
}
set C_modelArgMapList {[ 
	{ "Name" : "st1_m_fifo_a_m_arr_th_idx_V", "interface" : "memory", "bitwidth" : 8, "direction" : "WRITEONLY"} , 
 	{ "Name" : "st1_m_fifo_a_m_arr_cell_V", "interface" : "memory", "bitwidth" : 8, "direction" : "WRITEONLY"} , 
 	{ "Name" : "st1_m_fifo_a_m_arr_node_V", "interface" : "memory", "bitwidth" : 8, "direction" : "WRITEONLY"} , 
 	{ "Name" : "st1_m_fifo_b_m_arr_th_idx_V", "interface" : "memory", "bitwidth" : 8, "direction" : "WRITEONLY"} , 
 	{ "Name" : "st1_m_fifo_b_m_arr_cell_V", "interface" : "memory", "bitwidth" : 8, "direction" : "WRITEONLY"} , 
 	{ "Name" : "st1_m_fifo_b_m_arr_node_V", "interface" : "memory", "bitwidth" : 8, "direction" : "WRITEONLY"} , 
 	{ "Name" : "st1_m_fifo_a_m_size_V_out", "interface" : "wire", "bitwidth" : 8, "direction" : "WRITEONLY"} , 
 	{ "Name" : "st1_m_fifo_a_m_rear_V_7_out", "interface" : "wire", "bitwidth" : 8, "direction" : "WRITEONLY"} , 
 	{ "Name" : "st1_m_fifo_b_m_size_V_out", "interface" : "wire", "bitwidth" : 8, "direction" : "WRITEONLY"} , 
 	{ "Name" : "st1_m_fifo_b_m_rear_V_7_out", "interface" : "wire", "bitwidth" : 8, "direction" : "WRITEONLY"} ]}
# RTL Port declarations: 
set portNum 38
set portList { 
	{ ap_clk sc_in sc_logic 1 clock -1 } 
	{ ap_rst sc_in sc_logic 1 reset -1 active_high_sync } 
	{ ap_start sc_in sc_logic 1 start -1 } 
	{ ap_done sc_out sc_logic 1 predone -1 } 
	{ ap_idle sc_out sc_logic 1 done -1 } 
	{ ap_ready sc_out sc_logic 1 ready -1 } 
	{ st1_m_fifo_a_m_arr_th_idx_V_address0 sc_out sc_lv 4 signal 0 } 
	{ st1_m_fifo_a_m_arr_th_idx_V_ce0 sc_out sc_logic 1 signal 0 } 
	{ st1_m_fifo_a_m_arr_th_idx_V_we0 sc_out sc_logic 1 signal 0 } 
	{ st1_m_fifo_a_m_arr_th_idx_V_d0 sc_out sc_lv 8 signal 0 } 
	{ st1_m_fifo_a_m_arr_cell_V_address0 sc_out sc_lv 4 signal 1 } 
	{ st1_m_fifo_a_m_arr_cell_V_ce0 sc_out sc_logic 1 signal 1 } 
	{ st1_m_fifo_a_m_arr_cell_V_we0 sc_out sc_logic 1 signal 1 } 
	{ st1_m_fifo_a_m_arr_cell_V_d0 sc_out sc_lv 8 signal 1 } 
	{ st1_m_fifo_a_m_arr_node_V_address0 sc_out sc_lv 4 signal 2 } 
	{ st1_m_fifo_a_m_arr_node_V_ce0 sc_out sc_logic 1 signal 2 } 
	{ st1_m_fifo_a_m_arr_node_V_we0 sc_out sc_logic 1 signal 2 } 
	{ st1_m_fifo_a_m_arr_node_V_d0 sc_out sc_lv 8 signal 2 } 
	{ st1_m_fifo_b_m_arr_th_idx_V_address0 sc_out sc_lv 4 signal 3 } 
	{ st1_m_fifo_b_m_arr_th_idx_V_ce0 sc_out sc_logic 1 signal 3 } 
	{ st1_m_fifo_b_m_arr_th_idx_V_we0 sc_out sc_logic 1 signal 3 } 
	{ st1_m_fifo_b_m_arr_th_idx_V_d0 sc_out sc_lv 8 signal 3 } 
	{ st1_m_fifo_b_m_arr_cell_V_address0 sc_out sc_lv 4 signal 4 } 
	{ st1_m_fifo_b_m_arr_cell_V_ce0 sc_out sc_logic 1 signal 4 } 
	{ st1_m_fifo_b_m_arr_cell_V_we0 sc_out sc_logic 1 signal 4 } 
	{ st1_m_fifo_b_m_arr_cell_V_d0 sc_out sc_lv 8 signal 4 } 
	{ st1_m_fifo_b_m_arr_node_V_address0 sc_out sc_lv 4 signal 5 } 
	{ st1_m_fifo_b_m_arr_node_V_ce0 sc_out sc_logic 1 signal 5 } 
	{ st1_m_fifo_b_m_arr_node_V_we0 sc_out sc_logic 1 signal 5 } 
	{ st1_m_fifo_b_m_arr_node_V_d0 sc_out sc_lv 8 signal 5 } 
	{ st1_m_fifo_a_m_size_V_out sc_out sc_lv 8 signal 6 } 
	{ st1_m_fifo_a_m_size_V_out_ap_vld sc_out sc_logic 1 outvld 6 } 
	{ st1_m_fifo_a_m_rear_V_7_out sc_out sc_lv 8 signal 7 } 
	{ st1_m_fifo_a_m_rear_V_7_out_ap_vld sc_out sc_logic 1 outvld 7 } 
	{ st1_m_fifo_b_m_size_V_out sc_out sc_lv 8 signal 8 } 
	{ st1_m_fifo_b_m_size_V_out_ap_vld sc_out sc_logic 1 outvld 8 } 
	{ st1_m_fifo_b_m_rear_V_7_out sc_out sc_lv 8 signal 9 } 
	{ st1_m_fifo_b_m_rear_V_7_out_ap_vld sc_out sc_logic 1 outvld 9 } 
}
set NewPortList {[ 
	{ "name": "ap_clk", "direction": "in", "datatype": "sc_logic", "bitwidth":1, "type": "clock", "bundle":{"name": "ap_clk", "role": "default" }} , 
 	{ "name": "ap_rst", "direction": "in", "datatype": "sc_logic", "bitwidth":1, "type": "reset", "bundle":{"name": "ap_rst", "role": "default" }} , 
 	{ "name": "ap_start", "direction": "in", "datatype": "sc_logic", "bitwidth":1, "type": "start", "bundle":{"name": "ap_start", "role": "default" }} , 
 	{ "name": "ap_done", "direction": "out", "datatype": "sc_logic", "bitwidth":1, "type": "predone", "bundle":{"name": "ap_done", "role": "default" }} , 
 	{ "name": "ap_idle", "direction": "out", "datatype": "sc_logic", "bitwidth":1, "type": "done", "bundle":{"name": "ap_idle", "role": "default" }} , 
 	{ "name": "ap_ready", "direction": "out", "datatype": "sc_logic", "bitwidth":1, "type": "ready", "bundle":{"name": "ap_ready", "role": "default" }} , 
 	{ "name": "st1_m_fifo_a_m_arr_th_idx_V_address0", "direction": "out", "datatype": "sc_lv", "bitwidth":4, "type": "signal", "bundle":{"name": "st1_m_fifo_a_m_arr_th_idx_V", "role": "address0" }} , 
 	{ "name": "st1_m_fifo_a_m_arr_th_idx_V_ce0", "direction": "out", "datatype": "sc_logic", "bitwidth":1, "type": "signal", "bundle":{"name": "st1_m_fifo_a_m_arr_th_idx_V", "role": "ce0" }} , 
 	{ "name": "st1_m_fifo_a_m_arr_th_idx_V_we0", "direction": "out", "datatype": "sc_logic", "bitwidth":1, "type": "signal", "bundle":{"name": "st1_m_fifo_a_m_arr_th_idx_V", "role": "we0" }} , 
 	{ "name": "st1_m_fifo_a_m_arr_th_idx_V_d0", "direction": "out", "datatype": "sc_lv", "bitwidth":8, "type": "signal", "bundle":{"name": "st1_m_fifo_a_m_arr_th_idx_V", "role": "d0" }} , 
 	{ "name": "st1_m_fifo_a_m_arr_cell_V_address0", "direction": "out", "datatype": "sc_lv", "bitwidth":4, "type": "signal", "bundle":{"name": "st1_m_fifo_a_m_arr_cell_V", "role": "address0" }} , 
 	{ "name": "st1_m_fifo_a_m_arr_cell_V_ce0", "direction": "out", "datatype": "sc_logic", "bitwidth":1, "type": "signal", "bundle":{"name": "st1_m_fifo_a_m_arr_cell_V", "role": "ce0" }} , 
 	{ "name": "st1_m_fifo_a_m_arr_cell_V_we0", "direction": "out", "datatype": "sc_logic", "bitwidth":1, "type": "signal", "bundle":{"name": "st1_m_fifo_a_m_arr_cell_V", "role": "we0" }} , 
 	{ "name": "st1_m_fifo_a_m_arr_cell_V_d0", "direction": "out", "datatype": "sc_lv", "bitwidth":8, "type": "signal", "bundle":{"name": "st1_m_fifo_a_m_arr_cell_V", "role": "d0" }} , 
 	{ "name": "st1_m_fifo_a_m_arr_node_V_address0", "direction": "out", "datatype": "sc_lv", "bitwidth":4, "type": "signal", "bundle":{"name": "st1_m_fifo_a_m_arr_node_V", "role": "address0" }} , 
 	{ "name": "st1_m_fifo_a_m_arr_node_V_ce0", "direction": "out", "datatype": "sc_logic", "bitwidth":1, "type": "signal", "bundle":{"name": "st1_m_fifo_a_m_arr_node_V", "role": "ce0" }} , 
 	{ "name": "st1_m_fifo_a_m_arr_node_V_we0", "direction": "out", "datatype": "sc_logic", "bitwidth":1, "type": "signal", "bundle":{"name": "st1_m_fifo_a_m_arr_node_V", "role": "we0" }} , 
 	{ "name": "st1_m_fifo_a_m_arr_node_V_d0", "direction": "out", "datatype": "sc_lv", "bitwidth":8, "type": "signal", "bundle":{"name": "st1_m_fifo_a_m_arr_node_V", "role": "d0" }} , 
 	{ "name": "st1_m_fifo_b_m_arr_th_idx_V_address0", "direction": "out", "datatype": "sc_lv", "bitwidth":4, "type": "signal", "bundle":{"name": "st1_m_fifo_b_m_arr_th_idx_V", "role": "address0" }} , 
 	{ "name": "st1_m_fifo_b_m_arr_th_idx_V_ce0", "direction": "out", "datatype": "sc_logic", "bitwidth":1, "type": "signal", "bundle":{"name": "st1_m_fifo_b_m_arr_th_idx_V", "role": "ce0" }} , 
 	{ "name": "st1_m_fifo_b_m_arr_th_idx_V_we0", "direction": "out", "datatype": "sc_logic", "bitwidth":1, "type": "signal", "bundle":{"name": "st1_m_fifo_b_m_arr_th_idx_V", "role": "we0" }} , 
 	{ "name": "st1_m_fifo_b_m_arr_th_idx_V_d0", "direction": "out", "datatype": "sc_lv", "bitwidth":8, "type": "signal", "bundle":{"name": "st1_m_fifo_b_m_arr_th_idx_V", "role": "d0" }} , 
 	{ "name": "st1_m_fifo_b_m_arr_cell_V_address0", "direction": "out", "datatype": "sc_lv", "bitwidth":4, "type": "signal", "bundle":{"name": "st1_m_fifo_b_m_arr_cell_V", "role": "address0" }} , 
 	{ "name": "st1_m_fifo_b_m_arr_cell_V_ce0", "direction": "out", "datatype": "sc_logic", "bitwidth":1, "type": "signal", "bundle":{"name": "st1_m_fifo_b_m_arr_cell_V", "role": "ce0" }} , 
 	{ "name": "st1_m_fifo_b_m_arr_cell_V_we0", "direction": "out", "datatype": "sc_logic", "bitwidth":1, "type": "signal", "bundle":{"name": "st1_m_fifo_b_m_arr_cell_V", "role": "we0" }} , 
 	{ "name": "st1_m_fifo_b_m_arr_cell_V_d0", "direction": "out", "datatype": "sc_lv", "bitwidth":8, "type": "signal", "bundle":{"name": "st1_m_fifo_b_m_arr_cell_V", "role": "d0" }} , 
 	{ "name": "st1_m_fifo_b_m_arr_node_V_address0", "direction": "out", "datatype": "sc_lv", "bitwidth":4, "type": "signal", "bundle":{"name": "st1_m_fifo_b_m_arr_node_V", "role": "address0" }} , 
 	{ "name": "st1_m_fifo_b_m_arr_node_V_ce0", "direction": "out", "datatype": "sc_logic", "bitwidth":1, "type": "signal", "bundle":{"name": "st1_m_fifo_b_m_arr_node_V", "role": "ce0" }} , 
 	{ "name": "st1_m_fifo_b_m_arr_node_V_we0", "direction": "out", "datatype": "sc_logic", "bitwidth":1, "type": "signal", "bundle":{"name": "st1_m_fifo_b_m_arr_node_V", "role": "we0" }} , 
 	{ "name": "st1_m_fifo_b_m_arr_node_V_d0", "direction": "out", "datatype": "sc_lv", "bitwidth":8, "type": "signal", "bundle":{"name": "st1_m_fifo_b_m_arr_node_V", "role": "d0" }} , 
 	{ "name": "st1_m_fifo_a_m_size_V_out", "direction": "out", "datatype": "sc_lv", "bitwidth":8, "type": "signal", "bundle":{"name": "st1_m_fifo_a_m_size_V_out", "role": "default" }} , 
 	{ "name": "st1_m_fifo_a_m_size_V_out_ap_vld", "direction": "out", "datatype": "sc_logic", "bitwidth":1, "type": "outvld", "bundle":{"name": "st1_m_fifo_a_m_size_V_out", "role": "ap_vld" }} , 
 	{ "name": "st1_m_fifo_a_m_rear_V_7_out", "direction": "out", "datatype": "sc_lv", "bitwidth":8, "type": "signal", "bundle":{"name": "st1_m_fifo_a_m_rear_V_7_out", "role": "default" }} , 
 	{ "name": "st1_m_fifo_a_m_rear_V_7_out_ap_vld", "direction": "out", "datatype": "sc_logic", "bitwidth":1, "type": "outvld", "bundle":{"name": "st1_m_fifo_a_m_rear_V_7_out", "role": "ap_vld" }} , 
 	{ "name": "st1_m_fifo_b_m_size_V_out", "direction": "out", "datatype": "sc_lv", "bitwidth":8, "type": "signal", "bundle":{"name": "st1_m_fifo_b_m_size_V_out", "role": "default" }} , 
 	{ "name": "st1_m_fifo_b_m_size_V_out_ap_vld", "direction": "out", "datatype": "sc_logic", "bitwidth":1, "type": "outvld", "bundle":{"name": "st1_m_fifo_b_m_size_V_out", "role": "ap_vld" }} , 
 	{ "name": "st1_m_fifo_b_m_rear_V_7_out", "direction": "out", "datatype": "sc_lv", "bitwidth":8, "type": "signal", "bundle":{"name": "st1_m_fifo_b_m_rear_V_7_out", "role": "default" }} , 
 	{ "name": "st1_m_fifo_b_m_rear_V_7_out_ap_vld", "direction": "out", "datatype": "sc_logic", "bitwidth":1, "type": "outvld", "bundle":{"name": "st1_m_fifo_b_m_rear_V_7_out", "role": "ap_vld" }}  ]}

set RtlHierarchyInfo {[
	{"ID" : "0", "Level" : "0", "Path" : "`AUTOTB_DUT_INST", "Parent" : "", "Child" : ["1", "2", "3"],
		"CDFG" : "exec_pipeline_Pipeline_VITIS_LOOP_6_1",
		"Protocol" : "ap_ctrl_hs",
		"ControlExist" : "1", "ap_start" : "1", "ap_ready" : "1", "ap_done" : "1", "ap_continue" : "0", "ap_idle" : "1", "real_start" : "0",
		"Pipeline" : "None", "UnalignedPipeline" : "0", "RewindPipeline" : "0", "ProcessNetwork" : "0",
		"II" : "0",
		"VariableLatency" : "1", "ExactLatency" : "-1", "EstimateLatencyMin" : "51", "EstimateLatencyMax" : "51",
		"Combinational" : "0",
		"Datapath" : "0",
		"ClockEnable" : "0",
		"HasSubDataflow" : "0",
		"InDataflowNetwork" : "0",
		"HasNonBlockingOperation" : "0",
		"IsBlackBox" : "0",
		"Port" : [
			{"Name" : "st1_m_fifo_a_m_arr_th_idx_V", "Type" : "Memory", "Direction" : "O"},
			{"Name" : "st1_m_fifo_a_m_arr_cell_V", "Type" : "Memory", "Direction" : "O"},
			{"Name" : "st1_m_fifo_a_m_arr_node_V", "Type" : "Memory", "Direction" : "O"},
			{"Name" : "st1_m_fifo_b_m_arr_th_idx_V", "Type" : "Memory", "Direction" : "O"},
			{"Name" : "st1_m_fifo_b_m_arr_cell_V", "Type" : "Memory", "Direction" : "O"},
			{"Name" : "st1_m_fifo_b_m_arr_node_V", "Type" : "Memory", "Direction" : "O"},
			{"Name" : "st1_m_fifo_a_m_size_V_out", "Type" : "Vld", "Direction" : "O"},
			{"Name" : "st1_m_fifo_a_m_rear_V_7_out", "Type" : "Vld", "Direction" : "O"},
			{"Name" : "st1_m_fifo_b_m_size_V_out", "Type" : "Vld", "Direction" : "O"},
			{"Name" : "st1_m_fifo_b_m_rear_V_7_out", "Type" : "Vld", "Direction" : "O"}],
		"Loop" : [
			{"Name" : "VITIS_LOOP_6_1", "PipelineType" : "UPC",
				"LoopDec" : {"FSMBitwidth" : "12", "FirstState" : "ap_ST_fsm_pp0_stage0", "FirstStateIter" : "ap_enable_reg_pp0_iter0", "FirstStateBlock" : "ap_block_pp0_stage0_subdone", "LastState" : "ap_ST_fsm_pp0_stage1", "LastStateIter" : "ap_enable_reg_pp0_iter1", "LastStateBlock" : "ap_block_pp0_stage1_subdone", "QuitState" : "ap_ST_fsm_pp0_stage1", "QuitStateIter" : "ap_enable_reg_pp0_iter0", "QuitStateBlock" : "ap_block_pp0_stage1_subdone", "OneDepthLoop" : "0", "has_ap_ctrl" : "1", "has_continue" : "0"}}]},
	{"ID" : "1", "Level" : "1", "Path" : "`AUTOTB_DUT_INST.srem_9ns_5ns_5_13_1_U12", "Parent" : "0"},
	{"ID" : "2", "Level" : "1", "Path" : "`AUTOTB_DUT_INST.srem_9ns_5ns_5_13_1_U13", "Parent" : "0"},
	{"ID" : "3", "Level" : "1", "Path" : "`AUTOTB_DUT_INST.flow_control_loop_pipe_sequential_init_U", "Parent" : "0"}]}


set ArgLastReadFirstWriteLatency {
	exec_pipeline_Pipeline_VITIS_LOOP_6_1 {
		st1_m_fifo_a_m_arr_th_idx_V {Type O LastRead -1 FirstWrite 12}
		st1_m_fifo_a_m_arr_cell_V {Type O LastRead -1 FirstWrite 12}
		st1_m_fifo_a_m_arr_node_V {Type O LastRead -1 FirstWrite 12}
		st1_m_fifo_b_m_arr_th_idx_V {Type O LastRead -1 FirstWrite 13}
		st1_m_fifo_b_m_arr_cell_V {Type O LastRead -1 FirstWrite 13}
		st1_m_fifo_b_m_arr_node_V {Type O LastRead -1 FirstWrite 13}
		st1_m_fifo_a_m_size_V_out {Type O LastRead -1 FirstWrite 1}
		st1_m_fifo_a_m_rear_V_7_out {Type O LastRead -1 FirstWrite 1}
		st1_m_fifo_b_m_size_V_out {Type O LastRead -1 FirstWrite 1}
		st1_m_fifo_b_m_rear_V_7_out {Type O LastRead -1 FirstWrite 1}}}

set hasDtUnsupportedChannel 0

set PerformanceInfo {[
	{"Name" : "Latency", "Min" : "51", "Max" : "51"}
	, {"Name" : "Interval", "Min" : "51", "Max" : "51"}
]}

set PipelineEnableSignalInfo {[
	{"Pipeline" : "0", "EnableSignal" : "ap_enable_pp0"}
]}

set Spec2ImplPortList { 
	st1_m_fifo_a_m_arr_th_idx_V { ap_memory {  { st1_m_fifo_a_m_arr_th_idx_V_address0 mem_address 1 4 }  { st1_m_fifo_a_m_arr_th_idx_V_ce0 mem_ce 1 1 }  { st1_m_fifo_a_m_arr_th_idx_V_we0 mem_we 1 1 }  { st1_m_fifo_a_m_arr_th_idx_V_d0 mem_din 1 8 } } }
	st1_m_fifo_a_m_arr_cell_V { ap_memory {  { st1_m_fifo_a_m_arr_cell_V_address0 mem_address 1 4 }  { st1_m_fifo_a_m_arr_cell_V_ce0 mem_ce 1 1 }  { st1_m_fifo_a_m_arr_cell_V_we0 mem_we 1 1 }  { st1_m_fifo_a_m_arr_cell_V_d0 mem_din 1 8 } } }
	st1_m_fifo_a_m_arr_node_V { ap_memory {  { st1_m_fifo_a_m_arr_node_V_address0 mem_address 1 4 }  { st1_m_fifo_a_m_arr_node_V_ce0 mem_ce 1 1 }  { st1_m_fifo_a_m_arr_node_V_we0 mem_we 1 1 }  { st1_m_fifo_a_m_arr_node_V_d0 mem_din 1 8 } } }
	st1_m_fifo_b_m_arr_th_idx_V { ap_memory {  { st1_m_fifo_b_m_arr_th_idx_V_address0 mem_address 1 4 }  { st1_m_fifo_b_m_arr_th_idx_V_ce0 mem_ce 1 1 }  { st1_m_fifo_b_m_arr_th_idx_V_we0 mem_we 1 1 }  { st1_m_fifo_b_m_arr_th_idx_V_d0 mem_din 1 8 } } }
	st1_m_fifo_b_m_arr_cell_V { ap_memory {  { st1_m_fifo_b_m_arr_cell_V_address0 mem_address 1 4 }  { st1_m_fifo_b_m_arr_cell_V_ce0 mem_ce 1 1 }  { st1_m_fifo_b_m_arr_cell_V_we0 mem_we 1 1 }  { st1_m_fifo_b_m_arr_cell_V_d0 mem_din 1 8 } } }
	st1_m_fifo_b_m_arr_node_V { ap_memory {  { st1_m_fifo_b_m_arr_node_V_address0 mem_address 1 4 }  { st1_m_fifo_b_m_arr_node_V_ce0 mem_ce 1 1 }  { st1_m_fifo_b_m_arr_node_V_we0 mem_we 1 1 }  { st1_m_fifo_b_m_arr_node_V_d0 mem_din 1 8 } } }
	st1_m_fifo_a_m_size_V_out { ap_vld {  { st1_m_fifo_a_m_size_V_out out_data 1 8 }  { st1_m_fifo_a_m_size_V_out_ap_vld out_vld 1 1 } } }
	st1_m_fifo_a_m_rear_V_7_out { ap_vld {  { st1_m_fifo_a_m_rear_V_7_out out_data 1 8 }  { st1_m_fifo_a_m_rear_V_7_out_ap_vld out_vld 1 1 } } }
	st1_m_fifo_b_m_size_V_out { ap_vld {  { st1_m_fifo_b_m_size_V_out out_data 1 8 }  { st1_m_fifo_b_m_size_V_out_ap_vld out_vld 1 1 } } }
	st1_m_fifo_b_m_rear_V_7_out { ap_vld {  { st1_m_fifo_b_m_rear_V_7_out out_data 1 8 }  { st1_m_fifo_b_m_rear_V_7_out_ap_vld out_vld 1 1 } } }
}
