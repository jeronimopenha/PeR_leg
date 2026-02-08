set moduleName exec_pipeline
set isTopModule 0
set isCombinational 0
set isDatapathOnly 0
set isPipelined 0
set pipeline_type none
set FunctionProtocol ap_ctrl_hs
set isOneStateSeq 0
set ProfileFlag 0
set StallSigGenFlag 0
set isEnableWaveformDebug 1
set hasInterrupt 0
set C_modelName {exec_pipeline}
set C_modelType { void 0 }
set C_modelArgList {
	{ n2c int 800 regular {array 6 { 2 1 } 1 1 }  }
	{ c2n int 800 regular {array 6 { 2 1 } 1 1 }  }
	{ n int 32 regular {array 100 { 1 1 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 } 1 1 }  }
}
set C_modelArgMapList {[ 
	{ "Name" : "n2c", "interface" : "memory", "bitwidth" : 800, "direction" : "READWRITE"} , 
 	{ "Name" : "c2n", "interface" : "memory", "bitwidth" : 800, "direction" : "READWRITE"} , 
 	{ "Name" : "n", "interface" : "memory", "bitwidth" : 32, "direction" : "READONLY"} ]}
# RTL Port declarations: 
set portNum 28
set portList { 
	{ ap_clk sc_in sc_logic 1 clock -1 } 
	{ ap_rst sc_in sc_logic 1 reset -1 active_high_sync } 
	{ ap_start sc_in sc_logic 1 start -1 } 
	{ ap_done sc_out sc_logic 1 predone -1 } 
	{ ap_idle sc_out sc_logic 1 done -1 } 
	{ ap_ready sc_out sc_logic 1 ready -1 } 
	{ n2c_address0 sc_out sc_lv 3 signal 0 } 
	{ n2c_ce0 sc_out sc_logic 1 signal 0 } 
	{ n2c_we0 sc_out sc_lv 100 signal 0 } 
	{ n2c_d0 sc_out sc_lv 800 signal 0 } 
	{ n2c_q0 sc_in sc_lv 800 signal 0 } 
	{ n2c_address1 sc_out sc_lv 3 signal 0 } 
	{ n2c_ce1 sc_out sc_logic 1 signal 0 } 
	{ n2c_q1 sc_in sc_lv 800 signal 0 } 
	{ c2n_address0 sc_out sc_lv 3 signal 1 } 
	{ c2n_ce0 sc_out sc_logic 1 signal 1 } 
	{ c2n_we0 sc_out sc_lv 100 signal 1 } 
	{ c2n_d0 sc_out sc_lv 800 signal 1 } 
	{ c2n_q0 sc_in sc_lv 800 signal 1 } 
	{ c2n_address1 sc_out sc_lv 3 signal 1 } 
	{ c2n_ce1 sc_out sc_logic 1 signal 1 } 
	{ c2n_q1 sc_in sc_lv 800 signal 1 } 
	{ n_address0 sc_out sc_lv 7 signal 2 } 
	{ n_ce0 sc_out sc_logic 1 signal 2 } 
	{ n_q0 sc_in sc_lv 32 signal 2 } 
	{ n_address1 sc_out sc_lv 7 signal 2 } 
	{ n_ce1 sc_out sc_logic 1 signal 2 } 
	{ n_q1 sc_in sc_lv 32 signal 2 } 
}
set NewPortList {[ 
	{ "name": "ap_clk", "direction": "in", "datatype": "sc_logic", "bitwidth":1, "type": "clock", "bundle":{"name": "ap_clk", "role": "default" }} , 
 	{ "name": "ap_rst", "direction": "in", "datatype": "sc_logic", "bitwidth":1, "type": "reset", "bundle":{"name": "ap_rst", "role": "default" }} , 
 	{ "name": "ap_start", "direction": "in", "datatype": "sc_logic", "bitwidth":1, "type": "start", "bundle":{"name": "ap_start", "role": "default" }} , 
 	{ "name": "ap_done", "direction": "out", "datatype": "sc_logic", "bitwidth":1, "type": "predone", "bundle":{"name": "ap_done", "role": "default" }} , 
 	{ "name": "ap_idle", "direction": "out", "datatype": "sc_logic", "bitwidth":1, "type": "done", "bundle":{"name": "ap_idle", "role": "default" }} , 
 	{ "name": "ap_ready", "direction": "out", "datatype": "sc_logic", "bitwidth":1, "type": "ready", "bundle":{"name": "ap_ready", "role": "default" }} , 
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
 	{ "name": "n_q1", "direction": "in", "datatype": "sc_lv", "bitwidth":32, "type": "signal", "bundle":{"name": "n", "role": "q1" }}  ]}

set RtlHierarchyInfo {[
	{"ID" : "0", "Level" : "0", "Path" : "`AUTOTB_DUT_INST", "Parent" : "", "Child" : ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "14"],
		"CDFG" : "exec_pipeline",
		"Protocol" : "ap_ctrl_hs",
		"ControlExist" : "1", "ap_start" : "1", "ap_ready" : "1", "ap_done" : "1", "ap_continue" : "0", "ap_idle" : "1", "real_start" : "0",
		"Pipeline" : "None", "UnalignedPipeline" : "0", "RewindPipeline" : "0", "ProcessNetwork" : "0",
		"II" : "0",
		"VariableLatency" : "1", "ExactLatency" : "-1", "EstimateLatencyMin" : "120000079", "EstimateLatencyMax" : "120000079",
		"Combinational" : "0",
		"Datapath" : "0",
		"ClockEnable" : "0",
		"HasSubDataflow" : "0",
		"InDataflowNetwork" : "0",
		"HasNonBlockingOperation" : "0",
		"IsBlackBox" : "0",
		"Port" : [
			{"Name" : "n2c", "Type" : "Memory", "Direction" : "IO",
				"SubConnect" : [
					{"ID" : "14", "SubInstance" : "grp_exec_pipeline_Pipeline_VITIS_LOOP_27_1_fu_267", "Port" : "n2c", "Inst_start_state" : "7", "Inst_end_state" : "8"}]},
			{"Name" : "c2n", "Type" : "Memory", "Direction" : "IO",
				"SubConnect" : [
					{"ID" : "14", "SubInstance" : "grp_exec_pipeline_Pipeline_VITIS_LOOP_27_1_fu_267", "Port" : "c2n", "Inst_start_state" : "7", "Inst_end_state" : "8"}]},
			{"Name" : "n", "Type" : "Memory", "Direction" : "I",
				"SubConnect" : [
					{"ID" : "14", "SubInstance" : "grp_exec_pipeline_Pipeline_VITIS_LOOP_27_1_fu_267", "Port" : "n", "Inst_start_state" : "7", "Inst_end_state" : "8"}]},
			{"Name" : "st3_m_th_idx_offset", "Type" : "Memory", "Direction" : "I",
				"SubConnect" : [
					{"ID" : "14", "SubInstance" : "grp_exec_pipeline_Pipeline_VITIS_LOOP_27_1_fu_267", "Port" : "st3_m_th_idx_offset", "Inst_start_state" : "7", "Inst_end_state" : "8"}]},
			{"Name" : "st1_m_th_idx_offset", "Type" : "Memory", "Direction" : "I",
				"SubConnect" : [
					{"ID" : "14", "SubInstance" : "grp_exec_pipeline_Pipeline_VITIS_LOOP_27_1_fu_267", "Port" : "st1_m_th_idx_offset", "Inst_start_state" : "7", "Inst_end_state" : "8"}]}]},
	{"ID" : "1", "Level" : "1", "Path" : "`AUTOTB_DUT_INST.st0_m_cell_a_V_U", "Parent" : "0"},
	{"ID" : "2", "Level" : "1", "Path" : "`AUTOTB_DUT_INST.st0_m_cell_b_V_U", "Parent" : "0"},
	{"ID" : "3", "Level" : "1", "Path" : "`AUTOTB_DUT_INST.st0_m_th_valid_U", "Parent" : "0"},
	{"ID" : "4", "Level" : "1", "Path" : "`AUTOTB_DUT_INST.st1_m_fifo_a_m_arr_th_idx_V_U", "Parent" : "0"},
	{"ID" : "5", "Level" : "1", "Path" : "`AUTOTB_DUT_INST.st1_m_fifo_a_m_arr_cell_V_U", "Parent" : "0"},
	{"ID" : "6", "Level" : "1", "Path" : "`AUTOTB_DUT_INST.st1_m_fifo_a_m_arr_node_V_U", "Parent" : "0"},
	{"ID" : "7", "Level" : "1", "Path" : "`AUTOTB_DUT_INST.st1_m_fifo_b_m_arr_th_idx_V_U", "Parent" : "0"},
	{"ID" : "8", "Level" : "1", "Path" : "`AUTOTB_DUT_INST.st1_m_fifo_b_m_arr_cell_V_U", "Parent" : "0"},
	{"ID" : "9", "Level" : "1", "Path" : "`AUTOTB_DUT_INST.st1_m_fifo_b_m_arr_node_V_U", "Parent" : "0"},
	{"ID" : "10", "Level" : "1", "Path" : "`AUTOTB_DUT_INST.grp_exec_pipeline_Pipeline_VITIS_LOOP_6_1_fu_253", "Parent" : "0", "Child" : ["11", "12", "13"],
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
	{"ID" : "11", "Level" : "2", "Path" : "`AUTOTB_DUT_INST.grp_exec_pipeline_Pipeline_VITIS_LOOP_6_1_fu_253.srem_9ns_5ns_5_13_1_U12", "Parent" : "10"},
	{"ID" : "12", "Level" : "2", "Path" : "`AUTOTB_DUT_INST.grp_exec_pipeline_Pipeline_VITIS_LOOP_6_1_fu_253.srem_9ns_5ns_5_13_1_U13", "Parent" : "10"},
	{"ID" : "13", "Level" : "2", "Path" : "`AUTOTB_DUT_INST.grp_exec_pipeline_Pipeline_VITIS_LOOP_6_1_fu_253.flow_control_loop_pipe_sequential_init_U", "Parent" : "10"},
	{"ID" : "14", "Level" : "1", "Path" : "`AUTOTB_DUT_INST.grp_exec_pipeline_Pipeline_VITIS_LOOP_27_1_fu_267", "Parent" : "0", "Child" : ["15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58", "59", "60", "61", "62", "63", "64", "65", "66", "67", "68", "69", "70", "71", "72", "73", "74", "75", "76", "77", "78", "79", "80", "81"],
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
	{"ID" : "15", "Level" : "2", "Path" : "`AUTOTB_DUT_INST.grp_exec_pipeline_Pipeline_VITIS_LOOP_27_1_fu_267.st3_m_th_idx_offset_U", "Parent" : "14"},
	{"ID" : "16", "Level" : "2", "Path" : "`AUTOTB_DUT_INST.grp_exec_pipeline_Pipeline_VITIS_LOOP_27_1_fu_267.st1_m_th_idx_offset_U", "Parent" : "14"},
	{"ID" : "17", "Level" : "2", "Path" : "`AUTOTB_DUT_INST.grp_exec_pipeline_Pipeline_VITIS_LOOP_27_1_fu_267.srem_9ns_5ns_5_13_1_U25", "Parent" : "14"},
	{"ID" : "18", "Level" : "2", "Path" : "`AUTOTB_DUT_INST.grp_exec_pipeline_Pipeline_VITIS_LOOP_27_1_fu_267.srem_9ns_5ns_5_13_1_U26", "Parent" : "14"},
	{"ID" : "19", "Level" : "2", "Path" : "`AUTOTB_DUT_INST.grp_exec_pipeline_Pipeline_VITIS_LOOP_27_1_fu_267.srem_9ns_5ns_8_13_1_U27", "Parent" : "14"},
	{"ID" : "20", "Level" : "2", "Path" : "`AUTOTB_DUT_INST.grp_exec_pipeline_Pipeline_VITIS_LOOP_27_1_fu_267.srem_9ns_5ns_8_13_1_U28", "Parent" : "14"},
	{"ID" : "21", "Level" : "2", "Path" : "`AUTOTB_DUT_INST.grp_exec_pipeline_Pipeline_VITIS_LOOP_27_1_fu_267.srem_8s_5ns_5_12_1_U29", "Parent" : "14"},
	{"ID" : "22", "Level" : "2", "Path" : "`AUTOTB_DUT_INST.grp_exec_pipeline_Pipeline_VITIS_LOOP_27_1_fu_267.srem_8s_5ns_5_12_1_U30", "Parent" : "14"},
	{"ID" : "23", "Level" : "2", "Path" : "`AUTOTB_DUT_INST.grp_exec_pipeline_Pipeline_VITIS_LOOP_27_1_fu_267.mul_8ns_10ns_17_1_1_U31", "Parent" : "14"},
	{"ID" : "24", "Level" : "2", "Path" : "`AUTOTB_DUT_INST.grp_exec_pipeline_Pipeline_VITIS_LOOP_27_1_fu_267.urem_8ns_4ns_8_12_1_U32", "Parent" : "14"},
	{"ID" : "25", "Level" : "2", "Path" : "`AUTOTB_DUT_INST.grp_exec_pipeline_Pipeline_VITIS_LOOP_27_1_fu_267.mul_8ns_10ns_17_1_1_U33", "Parent" : "14"},
	{"ID" : "26", "Level" : "2", "Path" : "`AUTOTB_DUT_INST.grp_exec_pipeline_Pipeline_VITIS_LOOP_27_1_fu_267.urem_8ns_4ns_8_12_1_U34", "Parent" : "14"},
	{"ID" : "27", "Level" : "2", "Path" : "`AUTOTB_DUT_INST.grp_exec_pipeline_Pipeline_VITIS_LOOP_27_1_fu_267.mul_8ns_10ns_17_1_1_U35", "Parent" : "14"},
	{"ID" : "28", "Level" : "2", "Path" : "`AUTOTB_DUT_INST.grp_exec_pipeline_Pipeline_VITIS_LOOP_27_1_fu_267.urem_8ns_4ns_8_12_1_U36", "Parent" : "14"},
	{"ID" : "29", "Level" : "2", "Path" : "`AUTOTB_DUT_INST.grp_exec_pipeline_Pipeline_VITIS_LOOP_27_1_fu_267.srem_8s_5ns_5_12_1_U37", "Parent" : "14"},
	{"ID" : "30", "Level" : "2", "Path" : "`AUTOTB_DUT_INST.grp_exec_pipeline_Pipeline_VITIS_LOOP_27_1_fu_267.urem_8ns_4ns_8_12_1_U38", "Parent" : "14"},
	{"ID" : "31", "Level" : "2", "Path" : "`AUTOTB_DUT_INST.grp_exec_pipeline_Pipeline_VITIS_LOOP_27_1_fu_267.urem_8ns_4ns_8_12_1_U39", "Parent" : "14"},
	{"ID" : "32", "Level" : "2", "Path" : "`AUTOTB_DUT_INST.grp_exec_pipeline_Pipeline_VITIS_LOOP_27_1_fu_267.srem_8s_5ns_5_12_1_U40", "Parent" : "14"},
	{"ID" : "33", "Level" : "2", "Path" : "`AUTOTB_DUT_INST.grp_exec_pipeline_Pipeline_VITIS_LOOP_27_1_fu_267.srem_8s_5ns_5_12_1_U41", "Parent" : "14"},
	{"ID" : "34", "Level" : "2", "Path" : "`AUTOTB_DUT_INST.grp_exec_pipeline_Pipeline_VITIS_LOOP_27_1_fu_267.srem_8s_5ns_5_12_1_U42", "Parent" : "14"},
	{"ID" : "35", "Level" : "2", "Path" : "`AUTOTB_DUT_INST.grp_exec_pipeline_Pipeline_VITIS_LOOP_27_1_fu_267.srem_8s_5ns_5_12_1_U43", "Parent" : "14"},
	{"ID" : "36", "Level" : "2", "Path" : "`AUTOTB_DUT_INST.grp_exec_pipeline_Pipeline_VITIS_LOOP_27_1_fu_267.mul_8ns_10ns_17_1_1_U44", "Parent" : "14"},
	{"ID" : "37", "Level" : "2", "Path" : "`AUTOTB_DUT_INST.grp_exec_pipeline_Pipeline_VITIS_LOOP_27_1_fu_267.urem_8ns_4ns_8_12_1_U45", "Parent" : "14"},
	{"ID" : "38", "Level" : "2", "Path" : "`AUTOTB_DUT_INST.grp_exec_pipeline_Pipeline_VITIS_LOOP_27_1_fu_267.srem_8s_5ns_5_12_1_U46", "Parent" : "14"},
	{"ID" : "39", "Level" : "2", "Path" : "`AUTOTB_DUT_INST.grp_exec_pipeline_Pipeline_VITIS_LOOP_27_1_fu_267.srem_8s_5ns_5_12_1_U47", "Parent" : "14"},
	{"ID" : "40", "Level" : "2", "Path" : "`AUTOTB_DUT_INST.grp_exec_pipeline_Pipeline_VITIS_LOOP_27_1_fu_267.mul_8ns_10ns_17_1_1_U48", "Parent" : "14"},
	{"ID" : "41", "Level" : "2", "Path" : "`AUTOTB_DUT_INST.grp_exec_pipeline_Pipeline_VITIS_LOOP_27_1_fu_267.urem_8ns_8ns_8_12_1_U49", "Parent" : "14"},
	{"ID" : "42", "Level" : "2", "Path" : "`AUTOTB_DUT_INST.grp_exec_pipeline_Pipeline_VITIS_LOOP_27_1_fu_267.mul_8ns_10ns_17_1_1_U50", "Parent" : "14"},
	{"ID" : "43", "Level" : "2", "Path" : "`AUTOTB_DUT_INST.grp_exec_pipeline_Pipeline_VITIS_LOOP_27_1_fu_267.urem_8ns_8ns_8_12_1_U51", "Parent" : "14"},
	{"ID" : "44", "Level" : "2", "Path" : "`AUTOTB_DUT_INST.grp_exec_pipeline_Pipeline_VITIS_LOOP_27_1_fu_267.urem_8ns_8ns_8_12_1_U52", "Parent" : "14"},
	{"ID" : "45", "Level" : "2", "Path" : "`AUTOTB_DUT_INST.grp_exec_pipeline_Pipeline_VITIS_LOOP_27_1_fu_267.mul_8ns_10ns_17_1_1_U53", "Parent" : "14"},
	{"ID" : "46", "Level" : "2", "Path" : "`AUTOTB_DUT_INST.grp_exec_pipeline_Pipeline_VITIS_LOOP_27_1_fu_267.urem_8ns_8ns_8_12_1_U54", "Parent" : "14"},
	{"ID" : "47", "Level" : "2", "Path" : "`AUTOTB_DUT_INST.grp_exec_pipeline_Pipeline_VITIS_LOOP_27_1_fu_267.urem_8ns_8ns_8_12_1_U55", "Parent" : "14"},
	{"ID" : "48", "Level" : "2", "Path" : "`AUTOTB_DUT_INST.grp_exec_pipeline_Pipeline_VITIS_LOOP_27_1_fu_267.urem_8ns_4ns_8_12_1_U56", "Parent" : "14"},
	{"ID" : "49", "Level" : "2", "Path" : "`AUTOTB_DUT_INST.grp_exec_pipeline_Pipeline_VITIS_LOOP_27_1_fu_267.urem_8ns_4ns_8_12_1_U57", "Parent" : "14"},
	{"ID" : "50", "Level" : "2", "Path" : "`AUTOTB_DUT_INST.grp_exec_pipeline_Pipeline_VITIS_LOOP_27_1_fu_267.urem_8ns_4ns_8_12_1_U58", "Parent" : "14"},
	{"ID" : "51", "Level" : "2", "Path" : "`AUTOTB_DUT_INST.grp_exec_pipeline_Pipeline_VITIS_LOOP_27_1_fu_267.urem_8ns_4ns_8_12_1_U59", "Parent" : "14"},
	{"ID" : "52", "Level" : "2", "Path" : "`AUTOTB_DUT_INST.grp_exec_pipeline_Pipeline_VITIS_LOOP_27_1_fu_267.urem_8ns_4ns_8_12_1_U60", "Parent" : "14"},
	{"ID" : "53", "Level" : "2", "Path" : "`AUTOTB_DUT_INST.grp_exec_pipeline_Pipeline_VITIS_LOOP_27_1_fu_267.srem_8s_5ns_5_12_1_U61", "Parent" : "14"},
	{"ID" : "54", "Level" : "2", "Path" : "`AUTOTB_DUT_INST.grp_exec_pipeline_Pipeline_VITIS_LOOP_27_1_fu_267.mul_8ns_10ns_17_1_1_U62", "Parent" : "14"},
	{"ID" : "55", "Level" : "2", "Path" : "`AUTOTB_DUT_INST.grp_exec_pipeline_Pipeline_VITIS_LOOP_27_1_fu_267.mul_8ns_10ns_17_1_1_U63", "Parent" : "14"},
	{"ID" : "56", "Level" : "2", "Path" : "`AUTOTB_DUT_INST.grp_exec_pipeline_Pipeline_VITIS_LOOP_27_1_fu_267.srem_8s_5ns_5_12_1_U64", "Parent" : "14"},
	{"ID" : "57", "Level" : "2", "Path" : "`AUTOTB_DUT_INST.grp_exec_pipeline_Pipeline_VITIS_LOOP_27_1_fu_267.srem_8s_5ns_5_12_1_U65", "Parent" : "14"},
	{"ID" : "58", "Level" : "2", "Path" : "`AUTOTB_DUT_INST.grp_exec_pipeline_Pipeline_VITIS_LOOP_27_1_fu_267.srem_8s_5ns_5_12_1_U66", "Parent" : "14"},
	{"ID" : "59", "Level" : "2", "Path" : "`AUTOTB_DUT_INST.grp_exec_pipeline_Pipeline_VITIS_LOOP_27_1_fu_267.srem_8s_5ns_5_12_1_U67", "Parent" : "14"},
	{"ID" : "60", "Level" : "2", "Path" : "`AUTOTB_DUT_INST.grp_exec_pipeline_Pipeline_VITIS_LOOP_27_1_fu_267.mul_8ns_10ns_17_1_1_U68", "Parent" : "14"},
	{"ID" : "61", "Level" : "2", "Path" : "`AUTOTB_DUT_INST.grp_exec_pipeline_Pipeline_VITIS_LOOP_27_1_fu_267.mul_8ns_10ns_17_1_1_U69", "Parent" : "14"},
	{"ID" : "62", "Level" : "2", "Path" : "`AUTOTB_DUT_INST.grp_exec_pipeline_Pipeline_VITIS_LOOP_27_1_fu_267.mul_8ns_10ns_17_1_1_U70", "Parent" : "14"},
	{"ID" : "63", "Level" : "2", "Path" : "`AUTOTB_DUT_INST.grp_exec_pipeline_Pipeline_VITIS_LOOP_27_1_fu_267.mul_8ns_10ns_17_1_1_U71", "Parent" : "14"},
	{"ID" : "64", "Level" : "2", "Path" : "`AUTOTB_DUT_INST.grp_exec_pipeline_Pipeline_VITIS_LOOP_27_1_fu_267.mul_8ns_10ns_17_1_1_U72", "Parent" : "14"},
	{"ID" : "65", "Level" : "2", "Path" : "`AUTOTB_DUT_INST.grp_exec_pipeline_Pipeline_VITIS_LOOP_27_1_fu_267.mul_8ns_10ns_17_1_1_U73", "Parent" : "14"},
	{"ID" : "66", "Level" : "2", "Path" : "`AUTOTB_DUT_INST.grp_exec_pipeline_Pipeline_VITIS_LOOP_27_1_fu_267.mul_8ns_10ns_17_1_1_U74", "Parent" : "14"},
	{"ID" : "67", "Level" : "2", "Path" : "`AUTOTB_DUT_INST.grp_exec_pipeline_Pipeline_VITIS_LOOP_27_1_fu_267.mul_8s_10ns_18_1_1_U75", "Parent" : "14"},
	{"ID" : "68", "Level" : "2", "Path" : "`AUTOTB_DUT_INST.grp_exec_pipeline_Pipeline_VITIS_LOOP_27_1_fu_267.mul_8s_10ns_18_1_1_U76", "Parent" : "14"},
	{"ID" : "69", "Level" : "2", "Path" : "`AUTOTB_DUT_INST.grp_exec_pipeline_Pipeline_VITIS_LOOP_27_1_fu_267.mul_8s_10ns_18_1_1_U77", "Parent" : "14"},
	{"ID" : "70", "Level" : "2", "Path" : "`AUTOTB_DUT_INST.grp_exec_pipeline_Pipeline_VITIS_LOOP_27_1_fu_267.mul_8s_10ns_18_1_1_U78", "Parent" : "14"},
	{"ID" : "71", "Level" : "2", "Path" : "`AUTOTB_DUT_INST.grp_exec_pipeline_Pipeline_VITIS_LOOP_27_1_fu_267.mul_8s_10ns_18_1_1_U79", "Parent" : "14"},
	{"ID" : "72", "Level" : "2", "Path" : "`AUTOTB_DUT_INST.grp_exec_pipeline_Pipeline_VITIS_LOOP_27_1_fu_267.mul_8s_10ns_18_1_1_U80", "Parent" : "14"},
	{"ID" : "73", "Level" : "2", "Path" : "`AUTOTB_DUT_INST.grp_exec_pipeline_Pipeline_VITIS_LOOP_27_1_fu_267.mul_8s_10ns_18_1_1_U81", "Parent" : "14"},
	{"ID" : "74", "Level" : "2", "Path" : "`AUTOTB_DUT_INST.grp_exec_pipeline_Pipeline_VITIS_LOOP_27_1_fu_267.mul_8s_10ns_18_1_1_U82", "Parent" : "14"},
	{"ID" : "75", "Level" : "2", "Path" : "`AUTOTB_DUT_INST.grp_exec_pipeline_Pipeline_VITIS_LOOP_27_1_fu_267.mul_8s_10ns_18_1_1_U83", "Parent" : "14"},
	{"ID" : "76", "Level" : "2", "Path" : "`AUTOTB_DUT_INST.grp_exec_pipeline_Pipeline_VITIS_LOOP_27_1_fu_267.mul_8s_10ns_18_1_1_U84", "Parent" : "14"},
	{"ID" : "77", "Level" : "2", "Path" : "`AUTOTB_DUT_INST.grp_exec_pipeline_Pipeline_VITIS_LOOP_27_1_fu_267.mul_8s_10ns_18_1_1_U85", "Parent" : "14"},
	{"ID" : "78", "Level" : "2", "Path" : "`AUTOTB_DUT_INST.grp_exec_pipeline_Pipeline_VITIS_LOOP_27_1_fu_267.mul_8s_10ns_18_1_1_U86", "Parent" : "14"},
	{"ID" : "79", "Level" : "2", "Path" : "`AUTOTB_DUT_INST.grp_exec_pipeline_Pipeline_VITIS_LOOP_27_1_fu_267.mul_8s_10ns_18_1_1_U87", "Parent" : "14"},
	{"ID" : "80", "Level" : "2", "Path" : "`AUTOTB_DUT_INST.grp_exec_pipeline_Pipeline_VITIS_LOOP_27_1_fu_267.mul_8s_10ns_18_1_1_U88", "Parent" : "14"},
	{"ID" : "81", "Level" : "2", "Path" : "`AUTOTB_DUT_INST.grp_exec_pipeline_Pipeline_VITIS_LOOP_27_1_fu_267.flow_control_loop_pipe_sequential_init_U", "Parent" : "14"}]}


set ArgLastReadFirstWriteLatency {
	exec_pipeline {
		n2c {Type IO LastRead 23 FirstWrite 13}
		c2n {Type IO LastRead 18 FirstWrite 13}
		n {Type I LastRead 22 FirstWrite -1}
		st3_m_th_idx_offset {Type I LastRead -1 FirstWrite -1}
		st1_m_th_idx_offset {Type I LastRead -1 FirstWrite -1}}
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
		st1_m_fifo_b_m_rear_V_7_out {Type O LastRead -1 FirstWrite 1}}
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
	{"Name" : "Latency", "Min" : "120000079", "Max" : "120000079"}
	, {"Name" : "Interval", "Min" : "120000079", "Max" : "120000079"}
]}

set PipelineEnableSignalInfo {[
]}

set Spec2ImplPortList { 
	n2c { ap_memory {  { n2c_address0 mem_address 1 3 }  { n2c_ce0 mem_ce 1 1 }  { n2c_we0 mem_we 1 100 }  { n2c_d0 mem_din 1 800 }  { n2c_q0 mem_dout 0 800 }  { n2c_address1 MemPortADDR2 1 3 }  { n2c_ce1 MemPortCE2 1 1 }  { n2c_q1 MemPortDOUT2 0 800 } } }
	c2n { ap_memory {  { c2n_address0 mem_address 1 3 }  { c2n_ce0 mem_ce 1 1 }  { c2n_we0 mem_we 1 100 }  { c2n_d0 mem_din 1 800 }  { c2n_q0 mem_dout 0 800 }  { c2n_address1 MemPortADDR2 1 3 }  { c2n_ce1 MemPortCE2 1 1 }  { c2n_q1 MemPortDOUT2 0 800 } } }
	n { ap_memory {  { n_address0 mem_address 1 7 }  { n_ce0 mem_ce 1 1 }  { n_q0 mem_dout 0 32 }  { n_address1 MemPortADDR2 1 7 }  { n_ce1 MemPortCE2 1 1 }  { n_q1 MemPortDOUT2 0 32 } } }
}
