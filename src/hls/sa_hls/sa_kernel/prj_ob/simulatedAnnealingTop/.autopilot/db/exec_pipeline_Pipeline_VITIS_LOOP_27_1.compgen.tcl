# This script segment is generated automatically by AutoPilot

set name simulatedAnnealingTop_srem_9ns_5ns_8_13_1
if {${::AESL::PGuard_rtl_comp_handler}} {
	::AP::rtl_comp_handler $name BINDTYPE {op} TYPE {srem} IMPL {auto} LATENCY 12 ALLOW_PRAGMA 1
}


set name simulatedAnnealingTop_srem_8s_5ns_5_12_1
if {${::AESL::PGuard_rtl_comp_handler}} {
	::AP::rtl_comp_handler $name BINDTYPE {op} TYPE {srem} IMPL {auto} LATENCY 11 ALLOW_PRAGMA 1
}


set name simulatedAnnealingTop_mul_8ns_10ns_17_1_1
if {${::AESL::PGuard_rtl_comp_handler}} {
	::AP::rtl_comp_handler $name BINDTYPE {op} TYPE {mul} IMPL {auto} LATENCY 0 ALLOW_PRAGMA 1
}


set name simulatedAnnealingTop_urem_8ns_4ns_8_12_1
if {${::AESL::PGuard_rtl_comp_handler}} {
	::AP::rtl_comp_handler $name BINDTYPE {op} TYPE {urem} IMPL {auto} LATENCY 11 ALLOW_PRAGMA 1
}


set name simulatedAnnealingTop_urem_8ns_8ns_8_12_1
if {${::AESL::PGuard_rtl_comp_handler}} {
	::AP::rtl_comp_handler $name BINDTYPE {op} TYPE {urem} IMPL {auto} LATENCY 11 ALLOW_PRAGMA 1
}


set name simulatedAnnealingTop_mul_8s_10ns_18_1_1
if {${::AESL::PGuard_rtl_comp_handler}} {
	::AP::rtl_comp_handler $name BINDTYPE {op} TYPE {mul} IMPL {auto} LATENCY 0 ALLOW_PRAGMA 1
}


if {${::AESL::PGuard_rtl_comp_handler}} {
	::AP::rtl_comp_handler simulatedAnnealingTop_exec_pipeline_Pipeline_VITIS_LOOP_27_1_st3_m_th_idx_offset_ROM_AUTO_1R BINDTYPE {storage} TYPE {rom} IMPL {auto} LATENCY 2 ALLOW_PRAGMA 1
}


# clear list
if {${::AESL::PGuard_autoexp_gen}} {
    cg_default_interface_gen_dc_begin
    cg_default_interface_gen_bundle_begin
    AESL_LIB_XILADAPTER::native_axis_begin
}

# XIL_BRAM:
if {${::AESL::PGuard_autoexp_gen}} {
if {[info proc ::AESL_LIB_XILADAPTER::xil_bram_gen] == "::AESL_LIB_XILADAPTER::xil_bram_gen"} {
eval "::AESL_LIB_XILADAPTER::xil_bram_gen { \
    id 100 \
    name n2c \
    reset_level 1 \
    sync_rst true \
    dir IO \
    corename n2c \
    op interface \
    ports { n2c_address0 { O 3 vector } n2c_ce0 { O 1 bit } n2c_we0 { O 100 vector } n2c_d0 { O 800 vector } n2c_q0 { I 800 vector } n2c_address1 { O 3 vector } n2c_ce1 { O 1 bit } n2c_q1 { I 800 vector } } \
} "
} else {
puts "@W \[IMPL-110\] Cannot find bus interface model in the library. Ignored generation of bus interface for 'n2c'"
}
}


# XIL_BRAM:
if {${::AESL::PGuard_autoexp_gen}} {
if {[info proc ::AESL_LIB_XILADAPTER::xil_bram_gen] == "::AESL_LIB_XILADAPTER::xil_bram_gen"} {
eval "::AESL_LIB_XILADAPTER::xil_bram_gen { \
    id 101 \
    name c2n \
    reset_level 1 \
    sync_rst true \
    dir IO \
    corename c2n \
    op interface \
    ports { c2n_address0 { O 3 vector } c2n_ce0 { O 1 bit } c2n_we0 { O 100 vector } c2n_d0 { O 800 vector } c2n_q0 { I 800 vector } c2n_address1 { O 3 vector } c2n_ce1 { O 1 bit } c2n_q1 { I 800 vector } } \
} "
} else {
puts "@W \[IMPL-110\] Cannot find bus interface model in the library. Ignored generation of bus interface for 'c2n'"
}
}


# XIL_BRAM:
if {${::AESL::PGuard_autoexp_gen}} {
if {[info proc ::AESL_LIB_XILADAPTER::xil_bram_gen] == "::AESL_LIB_XILADAPTER::xil_bram_gen"} {
eval "::AESL_LIB_XILADAPTER::xil_bram_gen { \
    id 102 \
    name n \
    reset_level 1 \
    sync_rst true \
    dir I \
    corename n \
    op interface \
    ports { n_address0 { O 7 vector } n_ce0 { O 1 bit } n_q0 { I 32 vector } n_address1 { O 7 vector } n_ce1 { O 1 bit } n_q1 { I 32 vector } } \
} "
} else {
puts "@W \[IMPL-110\] Cannot find bus interface model in the library. Ignored generation of bus interface for 'n'"
}
}


# XIL_BRAM:
if {${::AESL::PGuard_autoexp_gen}} {
if {[info proc ::AESL_LIB_XILADAPTER::xil_bram_gen] == "::AESL_LIB_XILADAPTER::xil_bram_gen"} {
eval "::AESL_LIB_XILADAPTER::xil_bram_gen { \
    id 103 \
    name st0_m_th_valid \
    reset_level 1 \
    sync_rst true \
    dir IO \
    corename st0_m_th_valid \
    op interface \
    ports { st0_m_th_valid_address0 { O 3 vector } st0_m_th_valid_ce0 { O 1 bit } st0_m_th_valid_we0 { O 1 bit } st0_m_th_valid_d0 { O 1 vector } st0_m_th_valid_q0 { I 1 vector } } \
} "
} else {
puts "@W \[IMPL-110\] Cannot find bus interface model in the library. Ignored generation of bus interface for 'st0_m_th_valid'"
}
}


# XIL_BRAM:
if {${::AESL::PGuard_autoexp_gen}} {
if {[info proc ::AESL_LIB_XILADAPTER::xil_bram_gen] == "::AESL_LIB_XILADAPTER::xil_bram_gen"} {
eval "::AESL_LIB_XILADAPTER::xil_bram_gen { \
    id 104 \
    name st0_m_cell_a_V \
    reset_level 1 \
    sync_rst true \
    dir IO \
    corename st0_m_cell_a_V \
    op interface \
    ports { st0_m_cell_a_V_address0 { O 3 vector } st0_m_cell_a_V_ce0 { O 1 bit } st0_m_cell_a_V_we0 { O 1 bit } st0_m_cell_a_V_d0 { O 8 vector } st0_m_cell_a_V_q0 { I 8 vector } } \
} "
} else {
puts "@W \[IMPL-110\] Cannot find bus interface model in the library. Ignored generation of bus interface for 'st0_m_cell_a_V'"
}
}


# XIL_BRAM:
if {${::AESL::PGuard_autoexp_gen}} {
if {[info proc ::AESL_LIB_XILADAPTER::xil_bram_gen] == "::AESL_LIB_XILADAPTER::xil_bram_gen"} {
eval "::AESL_LIB_XILADAPTER::xil_bram_gen { \
    id 105 \
    name st0_m_cell_b_V \
    reset_level 1 \
    sync_rst true \
    dir IO \
    corename st0_m_cell_b_V \
    op interface \
    ports { st0_m_cell_b_V_address0 { O 3 vector } st0_m_cell_b_V_ce0 { O 1 bit } st0_m_cell_b_V_we0 { O 1 bit } st0_m_cell_b_V_d0 { O 8 vector } st0_m_cell_b_V_q0 { I 8 vector } } \
} "
} else {
puts "@W \[IMPL-110\] Cannot find bus interface model in the library. Ignored generation of bus interface for 'st0_m_cell_b_V'"
}
}


# XIL_BRAM:
if {${::AESL::PGuard_autoexp_gen}} {
if {[info proc ::AESL_LIB_XILADAPTER::xil_bram_gen] == "::AESL_LIB_XILADAPTER::xil_bram_gen"} {
eval "::AESL_LIB_XILADAPTER::xil_bram_gen { \
    id 106 \
    name st1_m_fifo_a_m_arr_th_idx_V \
    reset_level 1 \
    sync_rst true \
    dir IO \
    corename st1_m_fifo_a_m_arr_th_idx_V \
    op interface \
    ports { st1_m_fifo_a_m_arr_th_idx_V_address0 { O 4 vector } st1_m_fifo_a_m_arr_th_idx_V_ce0 { O 1 bit } st1_m_fifo_a_m_arr_th_idx_V_we0 { O 1 bit } st1_m_fifo_a_m_arr_th_idx_V_d0 { O 8 vector } st1_m_fifo_a_m_arr_th_idx_V_q0 { I 8 vector } } \
} "
} else {
puts "@W \[IMPL-110\] Cannot find bus interface model in the library. Ignored generation of bus interface for 'st1_m_fifo_a_m_arr_th_idx_V'"
}
}


# XIL_BRAM:
if {${::AESL::PGuard_autoexp_gen}} {
if {[info proc ::AESL_LIB_XILADAPTER::xil_bram_gen] == "::AESL_LIB_XILADAPTER::xil_bram_gen"} {
eval "::AESL_LIB_XILADAPTER::xil_bram_gen { \
    id 107 \
    name st1_m_fifo_a_m_arr_cell_V \
    reset_level 1 \
    sync_rst true \
    dir IO \
    corename st1_m_fifo_a_m_arr_cell_V \
    op interface \
    ports { st1_m_fifo_a_m_arr_cell_V_address0 { O 4 vector } st1_m_fifo_a_m_arr_cell_V_ce0 { O 1 bit } st1_m_fifo_a_m_arr_cell_V_we0 { O 1 bit } st1_m_fifo_a_m_arr_cell_V_d0 { O 8 vector } st1_m_fifo_a_m_arr_cell_V_q0 { I 8 vector } } \
} "
} else {
puts "@W \[IMPL-110\] Cannot find bus interface model in the library. Ignored generation of bus interface for 'st1_m_fifo_a_m_arr_cell_V'"
}
}


# XIL_BRAM:
if {${::AESL::PGuard_autoexp_gen}} {
if {[info proc ::AESL_LIB_XILADAPTER::xil_bram_gen] == "::AESL_LIB_XILADAPTER::xil_bram_gen"} {
eval "::AESL_LIB_XILADAPTER::xil_bram_gen { \
    id 108 \
    name st1_m_fifo_a_m_arr_node_V \
    reset_level 1 \
    sync_rst true \
    dir IO \
    corename st1_m_fifo_a_m_arr_node_V \
    op interface \
    ports { st1_m_fifo_a_m_arr_node_V_address0 { O 4 vector } st1_m_fifo_a_m_arr_node_V_ce0 { O 1 bit } st1_m_fifo_a_m_arr_node_V_we0 { O 1 bit } st1_m_fifo_a_m_arr_node_V_d0 { O 8 vector } st1_m_fifo_a_m_arr_node_V_q0 { I 8 vector } } \
} "
} else {
puts "@W \[IMPL-110\] Cannot find bus interface model in the library. Ignored generation of bus interface for 'st1_m_fifo_a_m_arr_node_V'"
}
}


# XIL_BRAM:
if {${::AESL::PGuard_autoexp_gen}} {
if {[info proc ::AESL_LIB_XILADAPTER::xil_bram_gen] == "::AESL_LIB_XILADAPTER::xil_bram_gen"} {
eval "::AESL_LIB_XILADAPTER::xil_bram_gen { \
    id 109 \
    name st1_m_fifo_b_m_arr_th_idx_V \
    reset_level 1 \
    sync_rst true \
    dir IO \
    corename st1_m_fifo_b_m_arr_th_idx_V \
    op interface \
    ports { st1_m_fifo_b_m_arr_th_idx_V_address0 { O 4 vector } st1_m_fifo_b_m_arr_th_idx_V_ce0 { O 1 bit } st1_m_fifo_b_m_arr_th_idx_V_we0 { O 1 bit } st1_m_fifo_b_m_arr_th_idx_V_d0 { O 8 vector } st1_m_fifo_b_m_arr_th_idx_V_q0 { I 8 vector } } \
} "
} else {
puts "@W \[IMPL-110\] Cannot find bus interface model in the library. Ignored generation of bus interface for 'st1_m_fifo_b_m_arr_th_idx_V'"
}
}


# XIL_BRAM:
if {${::AESL::PGuard_autoexp_gen}} {
if {[info proc ::AESL_LIB_XILADAPTER::xil_bram_gen] == "::AESL_LIB_XILADAPTER::xil_bram_gen"} {
eval "::AESL_LIB_XILADAPTER::xil_bram_gen { \
    id 110 \
    name st1_m_fifo_b_m_arr_cell_V \
    reset_level 1 \
    sync_rst true \
    dir IO \
    corename st1_m_fifo_b_m_arr_cell_V \
    op interface \
    ports { st1_m_fifo_b_m_arr_cell_V_address0 { O 4 vector } st1_m_fifo_b_m_arr_cell_V_ce0 { O 1 bit } st1_m_fifo_b_m_arr_cell_V_we0 { O 1 bit } st1_m_fifo_b_m_arr_cell_V_d0 { O 8 vector } st1_m_fifo_b_m_arr_cell_V_q0 { I 8 vector } } \
} "
} else {
puts "@W \[IMPL-110\] Cannot find bus interface model in the library. Ignored generation of bus interface for 'st1_m_fifo_b_m_arr_cell_V'"
}
}


# XIL_BRAM:
if {${::AESL::PGuard_autoexp_gen}} {
if {[info proc ::AESL_LIB_XILADAPTER::xil_bram_gen] == "::AESL_LIB_XILADAPTER::xil_bram_gen"} {
eval "::AESL_LIB_XILADAPTER::xil_bram_gen { \
    id 111 \
    name st1_m_fifo_b_m_arr_node_V \
    reset_level 1 \
    sync_rst true \
    dir IO \
    corename st1_m_fifo_b_m_arr_node_V \
    op interface \
    ports { st1_m_fifo_b_m_arr_node_V_address0 { O 4 vector } st1_m_fifo_b_m_arr_node_V_ce0 { O 1 bit } st1_m_fifo_b_m_arr_node_V_we0 { O 1 bit } st1_m_fifo_b_m_arr_node_V_d0 { O 8 vector } st1_m_fifo_b_m_arr_node_V_q0 { I 8 vector } } \
} "
} else {
puts "@W \[IMPL-110\] Cannot find bus interface model in the library. Ignored generation of bus interface for 'st1_m_fifo_b_m_arr_node_V'"
}
}


# Direct connection:
if {${::AESL::PGuard_autoexp_gen}} {
eval "cg_default_interface_gen_dc { \
    id 96 \
    name st1_m_fifo_a_m_size_V_reload \
    type other \
    dir I \
    reset_level 1 \
    sync_rst true \
    corename dc_st1_m_fifo_a_m_size_V_reload \
    op interface \
    ports { st1_m_fifo_a_m_size_V_reload { I 8 vector } } \
} "
}

# Direct connection:
if {${::AESL::PGuard_autoexp_gen}} {
eval "cg_default_interface_gen_dc { \
    id 97 \
    name st1_m_fifo_a_m_rear_V_7_reload \
    type other \
    dir I \
    reset_level 1 \
    sync_rst true \
    corename dc_st1_m_fifo_a_m_rear_V_7_reload \
    op interface \
    ports { st1_m_fifo_a_m_rear_V_7_reload { I 8 vector } } \
} "
}

# Direct connection:
if {${::AESL::PGuard_autoexp_gen}} {
eval "cg_default_interface_gen_dc { \
    id 98 \
    name st1_m_fifo_b_m_size_V_reload \
    type other \
    dir I \
    reset_level 1 \
    sync_rst true \
    corename dc_st1_m_fifo_b_m_size_V_reload \
    op interface \
    ports { st1_m_fifo_b_m_size_V_reload { I 8 vector } } \
} "
}

# Direct connection:
if {${::AESL::PGuard_autoexp_gen}} {
eval "cg_default_interface_gen_dc { \
    id 99 \
    name st1_m_fifo_b_m_rear_V_7_reload \
    type other \
    dir I \
    reset_level 1 \
    sync_rst true \
    corename dc_st1_m_fifo_b_m_rear_V_7_reload \
    op interface \
    ports { st1_m_fifo_b_m_rear_V_7_reload { I 8 vector } } \
} "
}

# Direct connection:
if {${::AESL::PGuard_autoexp_gen}} {
eval "cg_default_interface_gen_dc { \
    id -1 \
    name ap_ctrl \
    type ap_ctrl \
    reset_level 1 \
    sync_rst true \
    corename ap_ctrl \
    op interface \
    ports { ap_start { I 1 bit } ap_ready { O 1 bit } ap_done { O 1 bit } ap_idle { O 1 bit } } \
} "
}


# Adapter definition:
set PortName ap_clk
set DataWd 1 
if {${::AESL::PGuard_autoexp_gen}} {
if {[info proc cg_default_interface_gen_clock] == "cg_default_interface_gen_clock"} {
eval "cg_default_interface_gen_clock { \
    id -2 \
    name ${PortName} \
    reset_level 1 \
    sync_rst true \
    corename apif_ap_clk \
    data_wd ${DataWd} \
    op interface \
}"
} else {
puts "@W \[IMPL-113\] Cannot find bus interface model in the library. Ignored generation of bus interface for '${PortName}'"
}
}


# Adapter definition:
set PortName ap_rst
set DataWd 1 
if {${::AESL::PGuard_autoexp_gen}} {
if {[info proc cg_default_interface_gen_reset] == "cg_default_interface_gen_reset"} {
eval "cg_default_interface_gen_reset { \
    id -3 \
    name ${PortName} \
    reset_level 1 \
    sync_rst true \
    corename apif_ap_rst \
    data_wd ${DataWd} \
    op interface \
}"
} else {
puts "@W \[IMPL-114\] Cannot find bus interface model in the library. Ignored generation of bus interface for '${PortName}'"
}
}



# merge
if {${::AESL::PGuard_autoexp_gen}} {
    cg_default_interface_gen_dc_end
    cg_default_interface_gen_bundle_end
    AESL_LIB_XILADAPTER::native_axis_end
}


# flow_control definition:
set InstName simulatedAnnealingTop_flow_control_loop_pipe_sequential_init_U
set CompName simulatedAnnealingTop_flow_control_loop_pipe_sequential_init
set name flow_control_loop_pipe_sequential_init
if {${::AESL::PGuard_autocg_gen} && ${::AESL::PGuard_autocg_ipmgen}} {
if {[info proc ::AESL_LIB_VIRTEX::xil_gen_UPC_flow_control] == "::AESL_LIB_VIRTEX::xil_gen_UPC_flow_control"} {
eval "::AESL_LIB_VIRTEX::xil_gen_UPC_flow_control { \
    name ${name} \
    prefix simulatedAnnealingTop_ \
}"
} else {
puts "@W \[IMPL-107\] Cannot find ::AESL_LIB_VIRTEX::xil_gen_UPC_flow_control, check your platform lib"
}
}


if {${::AESL::PGuard_rtl_comp_handler}} {
	::AP::rtl_comp_handler $CompName BINDTYPE interface TYPE internal_upc_flow_control INSTNAME $InstName
}


