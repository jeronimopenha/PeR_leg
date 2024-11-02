# This script segment is generated automatically by AutoPilot

set name simulatedAnnealingTop_srem_9ns_5ns_5_13_1
if {${::AESL::PGuard_rtl_comp_handler}} {
	::AP::rtl_comp_handler $name BINDTYPE {op} TYPE {srem} IMPL {auto} LATENCY 12 ALLOW_PRAGMA 1
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
    id 15 \
    name st1_m_fifo_a_m_arr_th_idx_V \
    reset_level 1 \
    sync_rst true \
    dir O \
    corename st1_m_fifo_a_m_arr_th_idx_V \
    op interface \
    ports { st1_m_fifo_a_m_arr_th_idx_V_address0 { O 4 vector } st1_m_fifo_a_m_arr_th_idx_V_ce0 { O 1 bit } st1_m_fifo_a_m_arr_th_idx_V_we0 { O 1 bit } st1_m_fifo_a_m_arr_th_idx_V_d0 { O 8 vector } } \
} "
} else {
puts "@W \[IMPL-110\] Cannot find bus interface model in the library. Ignored generation of bus interface for 'st1_m_fifo_a_m_arr_th_idx_V'"
}
}


# XIL_BRAM:
if {${::AESL::PGuard_autoexp_gen}} {
if {[info proc ::AESL_LIB_XILADAPTER::xil_bram_gen] == "::AESL_LIB_XILADAPTER::xil_bram_gen"} {
eval "::AESL_LIB_XILADAPTER::xil_bram_gen { \
    id 16 \
    name st1_m_fifo_a_m_arr_cell_V \
    reset_level 1 \
    sync_rst true \
    dir O \
    corename st1_m_fifo_a_m_arr_cell_V \
    op interface \
    ports { st1_m_fifo_a_m_arr_cell_V_address0 { O 4 vector } st1_m_fifo_a_m_arr_cell_V_ce0 { O 1 bit } st1_m_fifo_a_m_arr_cell_V_we0 { O 1 bit } st1_m_fifo_a_m_arr_cell_V_d0 { O 8 vector } } \
} "
} else {
puts "@W \[IMPL-110\] Cannot find bus interface model in the library. Ignored generation of bus interface for 'st1_m_fifo_a_m_arr_cell_V'"
}
}


# XIL_BRAM:
if {${::AESL::PGuard_autoexp_gen}} {
if {[info proc ::AESL_LIB_XILADAPTER::xil_bram_gen] == "::AESL_LIB_XILADAPTER::xil_bram_gen"} {
eval "::AESL_LIB_XILADAPTER::xil_bram_gen { \
    id 17 \
    name st1_m_fifo_a_m_arr_node_V \
    reset_level 1 \
    sync_rst true \
    dir O \
    corename st1_m_fifo_a_m_arr_node_V \
    op interface \
    ports { st1_m_fifo_a_m_arr_node_V_address0 { O 4 vector } st1_m_fifo_a_m_arr_node_V_ce0 { O 1 bit } st1_m_fifo_a_m_arr_node_V_we0 { O 1 bit } st1_m_fifo_a_m_arr_node_V_d0 { O 8 vector } } \
} "
} else {
puts "@W \[IMPL-110\] Cannot find bus interface model in the library. Ignored generation of bus interface for 'st1_m_fifo_a_m_arr_node_V'"
}
}


# XIL_BRAM:
if {${::AESL::PGuard_autoexp_gen}} {
if {[info proc ::AESL_LIB_XILADAPTER::xil_bram_gen] == "::AESL_LIB_XILADAPTER::xil_bram_gen"} {
eval "::AESL_LIB_XILADAPTER::xil_bram_gen { \
    id 18 \
    name st1_m_fifo_b_m_arr_th_idx_V \
    reset_level 1 \
    sync_rst true \
    dir O \
    corename st1_m_fifo_b_m_arr_th_idx_V \
    op interface \
    ports { st1_m_fifo_b_m_arr_th_idx_V_address0 { O 4 vector } st1_m_fifo_b_m_arr_th_idx_V_ce0 { O 1 bit } st1_m_fifo_b_m_arr_th_idx_V_we0 { O 1 bit } st1_m_fifo_b_m_arr_th_idx_V_d0 { O 8 vector } } \
} "
} else {
puts "@W \[IMPL-110\] Cannot find bus interface model in the library. Ignored generation of bus interface for 'st1_m_fifo_b_m_arr_th_idx_V'"
}
}


# XIL_BRAM:
if {${::AESL::PGuard_autoexp_gen}} {
if {[info proc ::AESL_LIB_XILADAPTER::xil_bram_gen] == "::AESL_LIB_XILADAPTER::xil_bram_gen"} {
eval "::AESL_LIB_XILADAPTER::xil_bram_gen { \
    id 19 \
    name st1_m_fifo_b_m_arr_cell_V \
    reset_level 1 \
    sync_rst true \
    dir O \
    corename st1_m_fifo_b_m_arr_cell_V \
    op interface \
    ports { st1_m_fifo_b_m_arr_cell_V_address0 { O 4 vector } st1_m_fifo_b_m_arr_cell_V_ce0 { O 1 bit } st1_m_fifo_b_m_arr_cell_V_we0 { O 1 bit } st1_m_fifo_b_m_arr_cell_V_d0 { O 8 vector } } \
} "
} else {
puts "@W \[IMPL-110\] Cannot find bus interface model in the library. Ignored generation of bus interface for 'st1_m_fifo_b_m_arr_cell_V'"
}
}


# XIL_BRAM:
if {${::AESL::PGuard_autoexp_gen}} {
if {[info proc ::AESL_LIB_XILADAPTER::xil_bram_gen] == "::AESL_LIB_XILADAPTER::xil_bram_gen"} {
eval "::AESL_LIB_XILADAPTER::xil_bram_gen { \
    id 20 \
    name st1_m_fifo_b_m_arr_node_V \
    reset_level 1 \
    sync_rst true \
    dir O \
    corename st1_m_fifo_b_m_arr_node_V \
    op interface \
    ports { st1_m_fifo_b_m_arr_node_V_address0 { O 4 vector } st1_m_fifo_b_m_arr_node_V_ce0 { O 1 bit } st1_m_fifo_b_m_arr_node_V_we0 { O 1 bit } st1_m_fifo_b_m_arr_node_V_d0 { O 8 vector } } \
} "
} else {
puts "@W \[IMPL-110\] Cannot find bus interface model in the library. Ignored generation of bus interface for 'st1_m_fifo_b_m_arr_node_V'"
}
}


# Direct connection:
if {${::AESL::PGuard_autoexp_gen}} {
eval "cg_default_interface_gen_dc { \
    id 21 \
    name st1_m_fifo_a_m_size_V_out \
    type other \
    dir O \
    reset_level 1 \
    sync_rst true \
    corename dc_st1_m_fifo_a_m_size_V_out \
    op interface \
    ports { st1_m_fifo_a_m_size_V_out { O 8 vector } st1_m_fifo_a_m_size_V_out_ap_vld { O 1 bit } } \
} "
}

# Direct connection:
if {${::AESL::PGuard_autoexp_gen}} {
eval "cg_default_interface_gen_dc { \
    id 22 \
    name st1_m_fifo_a_m_rear_V_7_out \
    type other \
    dir O \
    reset_level 1 \
    sync_rst true \
    corename dc_st1_m_fifo_a_m_rear_V_7_out \
    op interface \
    ports { st1_m_fifo_a_m_rear_V_7_out { O 8 vector } st1_m_fifo_a_m_rear_V_7_out_ap_vld { O 1 bit } } \
} "
}

# Direct connection:
if {${::AESL::PGuard_autoexp_gen}} {
eval "cg_default_interface_gen_dc { \
    id 23 \
    name st1_m_fifo_b_m_size_V_out \
    type other \
    dir O \
    reset_level 1 \
    sync_rst true \
    corename dc_st1_m_fifo_b_m_size_V_out \
    op interface \
    ports { st1_m_fifo_b_m_size_V_out { O 8 vector } st1_m_fifo_b_m_size_V_out_ap_vld { O 1 bit } } \
} "
}

# Direct connection:
if {${::AESL::PGuard_autoexp_gen}} {
eval "cg_default_interface_gen_dc { \
    id 24 \
    name st1_m_fifo_b_m_rear_V_7_out \
    type other \
    dir O \
    reset_level 1 \
    sync_rst true \
    corename dc_st1_m_fifo_b_m_rear_V_7_out \
    op interface \
    ports { st1_m_fifo_b_m_rear_V_7_out { O 8 vector } st1_m_fifo_b_m_rear_V_7_out_ap_vld { O 1 bit } } \
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


