
set TopModule "simulatedAnnealingTop"
set ClockPeriod 3.125
set ClockList ap_clk
set HasVivadoClockPeriod 0
set CombLogicFlag 0
set PipelineFlag 0
set DataflowTaskPipelineFlag 1
set TrivialPipelineFlag 0
set noPortSwitchingFlag 0
set FloatingPointFlag 0
set FftOrFirFlag 0
set NbRWValue 0
set intNbAccess 0
set NewDSPMapping 1
set HasDSPModule 0
set ResetLevelFlag 0
set ResetStyle control
set ResetSyncFlag 1
set ResetRegisterFlag 1
set ResetVariableFlag 0
set ResetRegisterNum 3
set FsmEncStyle onehot
set MaxFanout 0
set RtlPrefix {}
set RtlSubPrefix simulatedAnnealingTop_
set ExtraCCFlags {}
set ExtraCLdFlags {}
set SynCheckOptions {}
set PresynOptions {}
set PreprocOptions {}
set SchedOptions {}
set BindOptions {}
set RtlGenOptions {}
set RtlWriterOptions {}
set CbcGenFlag {}
set CasGenFlag {}
set CasMonitorFlag {}
set AutoSimOptions {}
set ExportMCPathFlag 0
set SCTraceFileName mytrace
set SCTraceFileFormat vcd
set SCTraceOption all
set TargetInfo xcu55c:-fsvh2892:-2L-e
set SourceFiles {sc {} c {/home/jeronimocosta/Documentos/GIT/PeR/src/hls/sa_hls/sa_kernel/src/util_sa_hls.cpp /home/jeronimocosta/Documentos/GIT/PeR/src/hls/sa_hls/sa_kernel/src/stage9_sa_hls.cpp /home/jeronimocosta/Documentos/GIT/PeR/src/hls/sa_hls/sa_kernel/src/stage8_sa_hls.cpp /home/jeronimocosta/Documentos/GIT/PeR/src/hls/sa_hls/sa_kernel/src/stage7_sa_hls.cpp /home/jeronimocosta/Documentos/GIT/PeR/src/hls/sa_hls/sa_kernel/src/stage6_sa_hls.cpp /home/jeronimocosta/Documentos/GIT/PeR/src/hls/sa_hls/sa_kernel/src/stage5_sa_hls.cpp /home/jeronimocosta/Documentos/GIT/PeR/src/hls/sa_hls/sa_kernel/src/stage4_sa_hls.cpp /home/jeronimocosta/Documentos/GIT/PeR/src/hls/sa_hls/sa_kernel/src/stage3_sa_hls.cpp /home/jeronimocosta/Documentos/GIT/PeR/src/hls/sa_hls/sa_kernel/src/stage2_sa_hls.cpp /home/jeronimocosta/Documentos/GIT/PeR/src/hls/sa_hls/sa_kernel/src/stage1_sa_hls.cpp /home/jeronimocosta/Documentos/GIT/PeR/src/hls/sa_hls/sa_kernel/src/stage0_sa_hls.cpp /home/jeronimocosta/Documentos/GIT/PeR/src/hls/sa_hls/sa_kernel/src/pipeline_sa_hls.cpp /home/jeronimocosta/Documentos/GIT/PeR/src/hls/sa_hls/sa_kernel/src/fifo_sa_hls.cpp /home/jeronimocosta/Documentos/GIT/PeR/src/hls/sa_hls/sa_kernel/saTop.cpp}}
set SourceFlags {sc {} c {{-I/home/jeronimocosta/Documentos/GIT/PeR/src/hls/sa_hls/sa_kernel/src -std=c++14} {-I/home/jeronimocosta/Documentos/GIT/PeR/src/hls/sa_hls/sa_kernel/src -std=c++14} {-I/home/jeronimocosta/Documentos/GIT/PeR/src/hls/sa_hls/sa_kernel/src -std=c++14} {-I/home/jeronimocosta/Documentos/GIT/PeR/src/hls/sa_hls/sa_kernel/src -std=c++14} {-I/home/jeronimocosta/Documentos/GIT/PeR/src/hls/sa_hls/sa_kernel/src -std=c++14} {-I/home/jeronimocosta/Documentos/GIT/PeR/src/hls/sa_hls/sa_kernel/src -std=c++14} {-I/home/jeronimocosta/Documentos/GIT/PeR/src/hls/sa_hls/sa_kernel/src -std=c++14} {-I/home/jeronimocosta/Documentos/GIT/PeR/src/hls/sa_hls/sa_kernel/src -std=c++14} {-I/home/jeronimocosta/Documentos/GIT/PeR/src/hls/sa_hls/sa_kernel/src -std=c++14} {-I/home/jeronimocosta/Documentos/GIT/PeR/src/hls/sa_hls/sa_kernel/src -std=c++14} {-I/home/jeronimocosta/Documentos/GIT/PeR/src/hls/sa_hls/sa_kernel/src -std=c++14} {-I/home/jeronimocosta/Documentos/GIT/PeR/src/hls/sa_hls/sa_kernel/src -std=c++14} {-I/home/jeronimocosta/Documentos/GIT/PeR/src/hls/sa_hls/sa_kernel/src -std=c++14} {-I/home/jeronimocosta/Documentos/GIT/PeR/src/hls/sa_hls/sa_kernel/src -std=c++14}}}
set DirectiveFile /home/jeronimocosta/Documentos/GIT/PeR/src/hls/sa_hls/sa_kernel/prj_ob/simulatedAnnealingTop/simulatedAnnealingTop.directive
set TBFiles {bc {} c {} sc {} cas {} vhdl {} verilog {}}
set SpecLanguage C
set TVInFiles {bc {} c {} sc {} cas {} vhdl {} verilog {}}
set TVOutFiles {bc {} c {} sc {} cas {} vhdl {} verilog {}}
set TBTops {bc "" c "" sc "" cas "" vhdl "" verilog ""}
set TBInstNames {bc "" c "" sc "" cas "" vhdl "" verilog ""}
set XDCFiles {}
set ExtraGlobalOptions {"area_timing" 1 "clock_gate" 1 "impl_flow" map "power_gate" 0}
set TBTVFileNotFound {}
set AppFile ../hls.app
set ApsFile simulatedAnnealingTop.aps
set AvePath ../..
set DefaultPlatform DefaultPlatform
set multiClockList {}
set SCPortClockMap {}
set intNbAccess 0
set PlatformFiles {{DefaultPlatform {xilinx/virtexuplus/virtexuplus}}}
set HPFPO 0
