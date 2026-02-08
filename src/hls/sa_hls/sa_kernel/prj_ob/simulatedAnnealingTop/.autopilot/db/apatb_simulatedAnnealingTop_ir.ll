; ModuleID = '/home/jeronimocosta/Documentos/GIT/PeR/src/hls/sa_hls/sa_kernel/prj_ob/simulatedAnnealingTop/.autopilot/db/a.g.ld.5.gdce.bc'
source_filename = "llvm-link"
target datalayout = "e-m:e-i64:64-i128:128-i256:256-i512:512-i1024:1024-i2048:2048-i4096:4096-n8:16:32:64-S128-v16:16-v24:32-v32:32-v48:64-v96:128-v192:256-v256:256-v512:512-v1024:1024"
target triple = "fpga64-xilinx-none"

%"struct.ap_int<8>" = type { %"struct.ap_int_base<8, true>" }
%"struct.ap_int_base<8, true>" = type { %"struct.ssdm_int<8, true>" }
%"struct.ssdm_int<8, true>" = type { i8 }

; Function Attrs: inaccessiblemem_or_argmemonly noinline
define void @apatb_simulatedAnnealingTop_ir(%"struct.ap_int<8>"* noalias nocapture nonnull readonly %n2c, %"struct.ap_int<8>"* noalias nocapture nonnull %c2n, %"struct.ap_int<8>"* noalias nocapture nonnull readonly %n) local_unnamed_addr #0 {
entry:
  %n2c_copy = alloca i8, align 512
  %c2n_copy = alloca i8, align 512
  %n_copy = alloca i8, align 512
  call fastcc void @copy_in(%"struct.ap_int<8>"* nonnull %n2c, i8* nonnull align 512 %n2c_copy, %"struct.ap_int<8>"* nonnull %c2n, i8* nonnull align 512 %c2n_copy, %"struct.ap_int<8>"* nonnull %n, i8* nonnull align 512 %n_copy)
  call void @apatb_simulatedAnnealingTop_hw(i8* %n2c_copy, i8* %c2n_copy, i8* %n_copy)
  call void @copy_back(%"struct.ap_int<8>"* %n2c, i8* %n2c_copy, %"struct.ap_int<8>"* %c2n, i8* %c2n_copy, %"struct.ap_int<8>"* %n, i8* %n_copy)
  ret void
}

; Function Attrs: argmemonly noinline norecurse
define internal fastcc void @copy_in(%"struct.ap_int<8>"* noalias readonly "unpacked"="0", i8* noalias nocapture align 512 "unpacked"="1.0.0.0", %"struct.ap_int<8>"* noalias readonly "unpacked"="2", i8* noalias nocapture align 512 "unpacked"="3.0.0.0", %"struct.ap_int<8>"* noalias readonly "unpacked"="4", i8* noalias nocapture align 512 "unpacked"="5.0.0.0") unnamed_addr #1 {
entry:
  call fastcc void @"onebyonecpy_hls.p0struct.ap_int<8>"(i8* align 512 %1, %"struct.ap_int<8>"* %0)
  call fastcc void @"onebyonecpy_hls.p0struct.ap_int<8>"(i8* align 512 %3, %"struct.ap_int<8>"* %2)
  call fastcc void @"onebyonecpy_hls.p0struct.ap_int<8>"(i8* align 512 %5, %"struct.ap_int<8>"* %4)
  ret void
}

; Function Attrs: argmemonly noinline norecurse
define internal fastcc void @copy_out(%"struct.ap_int<8>"* noalias "unpacked"="0", i8* noalias nocapture readonly align 512 "unpacked"="1.0.0.0", %"struct.ap_int<8>"* noalias "unpacked"="2", i8* noalias nocapture readonly align 512 "unpacked"="3.0.0.0", %"struct.ap_int<8>"* noalias "unpacked"="4", i8* noalias nocapture readonly align 512 "unpacked"="5.0.0.0") unnamed_addr #2 {
entry:
  call fastcc void @"onebyonecpy_hls.p0struct.ap_int<8>.1069.1083.1097"(%"struct.ap_int<8>"* %0, i8* align 512 %1)
  call fastcc void @"onebyonecpy_hls.p0struct.ap_int<8>.1069.1083.1097"(%"struct.ap_int<8>"* %2, i8* align 512 %3)
  call fastcc void @"onebyonecpy_hls.p0struct.ap_int<8>.1069.1083.1097"(%"struct.ap_int<8>"* %4, i8* align 512 %5)
  ret void
}

; Function Attrs: argmemonly noinline norecurse
define internal fastcc void @"onebyonecpy_hls.p0struct.ap_int<8>.1069.1083.1097"(%"struct.ap_int<8>"* noalias "unpacked"="0", i8* noalias nocapture readonly align 512 "unpacked"="1.0.0.0") unnamed_addr #3 {
entry:
  %2 = icmp eq %"struct.ap_int<8>"* %0, null
  br i1 %2, label %ret, label %copy

copy:                                             ; preds = %entry
  %.01.0.05 = getelementptr %"struct.ap_int<8>", %"struct.ap_int<8>"* %0, i32 0, i32 0, i32 0, i32 0
  %3 = load i8, i8* %1, align 512
  store i8 %3, i8* %.01.0.05, align 1
  br label %ret

ret:                                              ; preds = %copy, %entry
  ret void
}

; Function Attrs: argmemonly noinline norecurse
define internal fastcc void @"onebyonecpy_hls.p0struct.ap_int<8>"(i8* noalias nocapture align 512 "unpacked"="0.0.0.0", %"struct.ap_int<8>"* noalias readonly "unpacked"="1") unnamed_addr #3 {
entry:
  %2 = icmp eq %"struct.ap_int<8>"* %1, null
  br i1 %2, label %ret, label %copy

copy:                                             ; preds = %entry
  %.0.0.04 = getelementptr %"struct.ap_int<8>", %"struct.ap_int<8>"* %1, i32 0, i32 0, i32 0, i32 0
  %3 = load i8, i8* %.0.0.04, align 1
  store i8 %3, i8* %0, align 512
  br label %ret

ret:                                              ; preds = %copy, %entry
  ret void
}

declare void @apatb_simulatedAnnealingTop_hw(i8*, i8*, i8*)

; Function Attrs: argmemonly noinline norecurse
define internal fastcc void @copy_back(%"struct.ap_int<8>"* noalias "unpacked"="0", i8* noalias nocapture readonly align 512 "unpacked"="1.0.0.0", %"struct.ap_int<8>"* noalias "unpacked"="2", i8* noalias nocapture readonly align 512 "unpacked"="3.0.0.0", %"struct.ap_int<8>"* noalias "unpacked"="4", i8* noalias nocapture readonly align 512 "unpacked"="5.0.0.0") unnamed_addr #2 {
entry:
  call fastcc void @"onebyonecpy_hls.p0struct.ap_int<8>.1069.1083.1097"(%"struct.ap_int<8>"* %2, i8* align 512 %3)
  ret void
}

define void @simulatedAnnealingTop_hw_stub_wrapper(i8*, i8*, i8*) #4 {
entry:
  %3 = alloca %"struct.ap_int<8>"
  %4 = alloca %"struct.ap_int<8>"
  %5 = alloca %"struct.ap_int<8>"
  call void @copy_out(%"struct.ap_int<8>"* %3, i8* %0, %"struct.ap_int<8>"* %4, i8* %1, %"struct.ap_int<8>"* %5, i8* %2)
  call void @simulatedAnnealingTop_hw_stub(%"struct.ap_int<8>"* %3, %"struct.ap_int<8>"* %4, %"struct.ap_int<8>"* %5)
  call void @copy_in(%"struct.ap_int<8>"* %3, i8* %0, %"struct.ap_int<8>"* %4, i8* %1, %"struct.ap_int<8>"* %5, i8* %2)
  ret void
}

declare void @simulatedAnnealingTop_hw_stub(%"struct.ap_int<8>"*, %"struct.ap_int<8>"*, %"struct.ap_int<8>"*)

attributes #0 = { inaccessiblemem_or_argmemonly noinline "fpga.wrapper.func"="wrapper" }
attributes #1 = { argmemonly noinline norecurse "fpga.wrapper.func"="copyin" }
attributes #2 = { argmemonly noinline norecurse "fpga.wrapper.func"="copyout" }
attributes #3 = { argmemonly noinline norecurse "fpga.wrapper.func"="onebyonecpy_hls" }
attributes #4 = { "fpga.wrapper.func"="stub" }

!llvm.dbg.cu = !{}
!llvm.ident = !{!0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0, !0}
!llvm.module.flags = !{!1, !2, !3}
!blackbox_cfg = !{!4}

!0 = !{!"clang version 7.0.0 "}
!1 = !{i32 2, !"Dwarf Version", i32 4}
!2 = !{i32 2, !"Debug Info Version", i32 3}
!3 = !{i32 1, !"wchar_size", i32 4}
!4 = !{}
