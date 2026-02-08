set SynModuleInfo {
  {SRCNAME simulatedAnnealingTop_Pipeline_1 MODELNAME simulatedAnnealingTop_Pipeline_1 RTLNAME simulatedAnnealingTop_simulatedAnnealingTop_Pipeline_1
    SUBMODULES {
      {MODELNAME simulatedAnnealingTop_flow_control_loop_pipe_sequential_init RTLNAME simulatedAnnealingTop_flow_control_loop_pipe_sequential_init BINDTYPE interface TYPE internal_upc_flow_control INSTNAME simulatedAnnealingTop_flow_control_loop_pipe_sequential_init_U}
    }
  }
  {SRCNAME simulatedAnnealingTop_Pipeline_2 MODELNAME simulatedAnnealingTop_Pipeline_2 RTLNAME simulatedAnnealingTop_simulatedAnnealingTop_Pipeline_2}
  {SRCNAME simulatedAnnealingTop_Pipeline_3 MODELNAME simulatedAnnealingTop_Pipeline_3 RTLNAME simulatedAnnealingTop_simulatedAnnealingTop_Pipeline_3}
  {SRCNAME exec_pipeline_Pipeline_VITIS_LOOP_6_1 MODELNAME exec_pipeline_Pipeline_VITIS_LOOP_6_1 RTLNAME simulatedAnnealingTop_exec_pipeline_Pipeline_VITIS_LOOP_6_1
    SUBMODULES {
      {MODELNAME simulatedAnnealingTop_srem_9ns_5ns_5_13_1 RTLNAME simulatedAnnealingTop_srem_9ns_5ns_5_13_1 BINDTYPE op TYPE srem IMPL auto LATENCY 12 ALLOW_PRAGMA 1}
    }
  }
  {SRCNAME exec_pipeline_Pipeline_VITIS_LOOP_27_1 MODELNAME exec_pipeline_Pipeline_VITIS_LOOP_27_1 RTLNAME simulatedAnnealingTop_exec_pipeline_Pipeline_VITIS_LOOP_27_1
    SUBMODULES {
      {MODELNAME simulatedAnnealingTop_srem_9ns_5ns_8_13_1 RTLNAME simulatedAnnealingTop_srem_9ns_5ns_8_13_1 BINDTYPE op TYPE srem IMPL auto LATENCY 12 ALLOW_PRAGMA 1}
      {MODELNAME simulatedAnnealingTop_srem_8s_5ns_5_12_1 RTLNAME simulatedAnnealingTop_srem_8s_5ns_5_12_1 BINDTYPE op TYPE srem IMPL auto LATENCY 11 ALLOW_PRAGMA 1}
      {MODELNAME simulatedAnnealingTop_mul_8ns_10ns_17_1_1 RTLNAME simulatedAnnealingTop_mul_8ns_10ns_17_1_1 BINDTYPE op TYPE mul IMPL auto LATENCY 0 ALLOW_PRAGMA 1}
      {MODELNAME simulatedAnnealingTop_urem_8ns_4ns_8_12_1 RTLNAME simulatedAnnealingTop_urem_8ns_4ns_8_12_1 BINDTYPE op TYPE urem IMPL auto LATENCY 11 ALLOW_PRAGMA 1}
      {MODELNAME simulatedAnnealingTop_urem_8ns_8ns_8_12_1 RTLNAME simulatedAnnealingTop_urem_8ns_8ns_8_12_1 BINDTYPE op TYPE urem IMPL auto LATENCY 11 ALLOW_PRAGMA 1}
      {MODELNAME simulatedAnnealingTop_mul_8s_10ns_18_1_1 RTLNAME simulatedAnnealingTop_mul_8s_10ns_18_1_1 BINDTYPE op TYPE mul IMPL auto LATENCY 0 ALLOW_PRAGMA 1}
      {MODELNAME simulatedAnnealingTop_exec_pipeline_Pipeline_VITIS_LOOP_27_1_st3_m_th_idx_offset_ROM_AUTO_1R RTLNAME simulatedAnnealingTop_exec_pipeline_Pipeline_VITIS_LOOP_27_1_st3_m_th_idx_offset_ROM_AUTO_1R BINDTYPE storage TYPE rom IMPL auto LATENCY 2 ALLOW_PRAGMA 1}
    }
  }
  {SRCNAME exec_pipeline MODELNAME exec_pipeline RTLNAME simulatedAnnealingTop_exec_pipeline
    SUBMODULES {
      {MODELNAME simulatedAnnealingTop_exec_pipeline_st0_m_cell_a_V_RAM_AUTO_1R1W RTLNAME simulatedAnnealingTop_exec_pipeline_st0_m_cell_a_V_RAM_AUTO_1R1W BINDTYPE storage TYPE ram IMPL auto LATENCY 2 ALLOW_PRAGMA 1}
      {MODELNAME simulatedAnnealingTop_exec_pipeline_st0_m_cell_b_V_RAM_1WNR_AUTO_1R1W RTLNAME simulatedAnnealingTop_exec_pipeline_st0_m_cell_b_V_RAM_1WNR_AUTO_1R1W BINDTYPE storage TYPE ram_1wnr IMPL auto LATENCY 2 ALLOW_PRAGMA 1}
      {MODELNAME simulatedAnnealingTop_exec_pipeline_st0_m_th_valid_RAM_1WNR_AUTO_1R1W RTLNAME simulatedAnnealingTop_exec_pipeline_st0_m_th_valid_RAM_1WNR_AUTO_1R1W BINDTYPE storage TYPE ram_1wnr IMPL auto LATENCY 2 ALLOW_PRAGMA 1}
      {MODELNAME simulatedAnnealingTop_exec_pipeline_st1_m_fifo_a_m_arr_th_idx_V_RAM_AUTO_1R1W RTLNAME simulatedAnnealingTop_exec_pipeline_st1_m_fifo_a_m_arr_th_idx_V_RAM_AUTO_1R1W BINDTYPE storage TYPE ram IMPL auto LATENCY 2 ALLOW_PRAGMA 1}
    }
  }
  {SRCNAME simulatedAnnealingTop_Pipeline_4 MODELNAME simulatedAnnealingTop_Pipeline_4 RTLNAME simulatedAnnealingTop_simulatedAnnealingTop_Pipeline_4}
  {SRCNAME simulatedAnnealingTop MODELNAME simulatedAnnealingTop RTLNAME simulatedAnnealingTop IS_TOP 1
    SUBMODULES {
      {MODELNAME simulatedAnnealingTop_n2c_l_V_RAM_AUTO_1R1W RTLNAME simulatedAnnealingTop_n2c_l_V_RAM_AUTO_1R1W BINDTYPE storage TYPE ram IMPL auto LATENCY 2 ALLOW_PRAGMA 1}
      {MODELNAME simulatedAnnealingTop_n_l_V_RAM_1WNR_AUTO_1R1W RTLNAME simulatedAnnealingTop_n_l_V_RAM_1WNR_AUTO_1R1W BINDTYPE storage TYPE ram_1wnr IMPL auto LATENCY 2 ALLOW_PRAGMA 1}
      {MODELNAME simulatedAnnealingTop_gmem_m_axi RTLNAME simulatedAnnealingTop_gmem_m_axi BINDTYPE interface TYPE adapter IMPL m_axi}
      {MODELNAME simulatedAnnealingTop_control_s_axi RTLNAME simulatedAnnealingTop_control_s_axi BINDTYPE interface TYPE interface_s_axilite}
    }
  }
}
