// ==============================================================
// Vitis HLS - High-Level Synthesis from C, C++ and OpenCL v2022.2 (64-bit)
// Tool Version Limit: 2019.12
// Copyright 1986-2022 Xilinx, Inc. All Rights Reserved.
// ==============================================================
/***************************** Include Files *********************************/
#include "xsimulatedannealingtop.h"

/************************** Function Implementation *************************/
#ifndef __linux__
int XSimulatedannealingtop_CfgInitialize(XSimulatedannealingtop *InstancePtr, XSimulatedannealingtop_Config *ConfigPtr) {
    Xil_AssertNonvoid(InstancePtr != NULL);
    Xil_AssertNonvoid(ConfigPtr != NULL);

    InstancePtr->Control_BaseAddress = ConfigPtr->Control_BaseAddress;
    InstancePtr->IsReady = XIL_COMPONENT_IS_READY;

    return XST_SUCCESS;
}
#endif

void XSimulatedannealingtop_Start(XSimulatedannealingtop *InstancePtr) {
    u32 Data;

    Xil_AssertVoid(InstancePtr != NULL);
    Xil_AssertVoid(InstancePtr->IsReady == XIL_COMPONENT_IS_READY);

    Data = XSimulatedannealingtop_ReadReg(InstancePtr->Control_BaseAddress, XSIMULATEDANNEALINGTOP_CONTROL_ADDR_AP_CTRL) & 0x80;
    XSimulatedannealingtop_WriteReg(InstancePtr->Control_BaseAddress, XSIMULATEDANNEALINGTOP_CONTROL_ADDR_AP_CTRL, Data | 0x01);
}

u32 XSimulatedannealingtop_IsDone(XSimulatedannealingtop *InstancePtr) {
    u32 Data;

    Xil_AssertNonvoid(InstancePtr != NULL);
    Xil_AssertNonvoid(InstancePtr->IsReady == XIL_COMPONENT_IS_READY);

    Data = XSimulatedannealingtop_ReadReg(InstancePtr->Control_BaseAddress, XSIMULATEDANNEALINGTOP_CONTROL_ADDR_AP_CTRL);
    return (Data >> 1) & 0x1;
}

u32 XSimulatedannealingtop_IsIdle(XSimulatedannealingtop *InstancePtr) {
    u32 Data;

    Xil_AssertNonvoid(InstancePtr != NULL);
    Xil_AssertNonvoid(InstancePtr->IsReady == XIL_COMPONENT_IS_READY);

    Data = XSimulatedannealingtop_ReadReg(InstancePtr->Control_BaseAddress, XSIMULATEDANNEALINGTOP_CONTROL_ADDR_AP_CTRL);
    return (Data >> 2) & 0x1;
}

u32 XSimulatedannealingtop_IsReady(XSimulatedannealingtop *InstancePtr) {
    u32 Data;

    Xil_AssertNonvoid(InstancePtr != NULL);
    Xil_AssertNonvoid(InstancePtr->IsReady == XIL_COMPONENT_IS_READY);

    Data = XSimulatedannealingtop_ReadReg(InstancePtr->Control_BaseAddress, XSIMULATEDANNEALINGTOP_CONTROL_ADDR_AP_CTRL);
    // check ap_start to see if the pcore is ready for next input
    return !(Data & 0x1);
}

void XSimulatedannealingtop_Continue(XSimulatedannealingtop *InstancePtr) {
    u32 Data;

    Xil_AssertVoid(InstancePtr != NULL);
    Xil_AssertVoid(InstancePtr->IsReady == XIL_COMPONENT_IS_READY);

    Data = XSimulatedannealingtop_ReadReg(InstancePtr->Control_BaseAddress, XSIMULATEDANNEALINGTOP_CONTROL_ADDR_AP_CTRL) & 0x80;
    XSimulatedannealingtop_WriteReg(InstancePtr->Control_BaseAddress, XSIMULATEDANNEALINGTOP_CONTROL_ADDR_AP_CTRL, Data | 0x10);
}

void XSimulatedannealingtop_EnableAutoRestart(XSimulatedannealingtop *InstancePtr) {
    Xil_AssertVoid(InstancePtr != NULL);
    Xil_AssertVoid(InstancePtr->IsReady == XIL_COMPONENT_IS_READY);

    XSimulatedannealingtop_WriteReg(InstancePtr->Control_BaseAddress, XSIMULATEDANNEALINGTOP_CONTROL_ADDR_AP_CTRL, 0x80);
}

void XSimulatedannealingtop_DisableAutoRestart(XSimulatedannealingtop *InstancePtr) {
    Xil_AssertVoid(InstancePtr != NULL);
    Xil_AssertVoid(InstancePtr->IsReady == XIL_COMPONENT_IS_READY);

    XSimulatedannealingtop_WriteReg(InstancePtr->Control_BaseAddress, XSIMULATEDANNEALINGTOP_CONTROL_ADDR_AP_CTRL, 0);
}

void XSimulatedannealingtop_Set_n2c(XSimulatedannealingtop *InstancePtr, u64 Data) {
    Xil_AssertVoid(InstancePtr != NULL);
    Xil_AssertVoid(InstancePtr->IsReady == XIL_COMPONENT_IS_READY);

    XSimulatedannealingtop_WriteReg(InstancePtr->Control_BaseAddress, XSIMULATEDANNEALINGTOP_CONTROL_ADDR_N2C_DATA, (u32)(Data));
    XSimulatedannealingtop_WriteReg(InstancePtr->Control_BaseAddress, XSIMULATEDANNEALINGTOP_CONTROL_ADDR_N2C_DATA + 4, (u32)(Data >> 32));
}

u64 XSimulatedannealingtop_Get_n2c(XSimulatedannealingtop *InstancePtr) {
    u64 Data;

    Xil_AssertNonvoid(InstancePtr != NULL);
    Xil_AssertNonvoid(InstancePtr->IsReady == XIL_COMPONENT_IS_READY);

    Data = XSimulatedannealingtop_ReadReg(InstancePtr->Control_BaseAddress, XSIMULATEDANNEALINGTOP_CONTROL_ADDR_N2C_DATA);
    Data += (u64)XSimulatedannealingtop_ReadReg(InstancePtr->Control_BaseAddress, XSIMULATEDANNEALINGTOP_CONTROL_ADDR_N2C_DATA + 4) << 32;
    return Data;
}

void XSimulatedannealingtop_Set_c2n(XSimulatedannealingtop *InstancePtr, u64 Data) {
    Xil_AssertVoid(InstancePtr != NULL);
    Xil_AssertVoid(InstancePtr->IsReady == XIL_COMPONENT_IS_READY);

    XSimulatedannealingtop_WriteReg(InstancePtr->Control_BaseAddress, XSIMULATEDANNEALINGTOP_CONTROL_ADDR_C2N_DATA, (u32)(Data));
    XSimulatedannealingtop_WriteReg(InstancePtr->Control_BaseAddress, XSIMULATEDANNEALINGTOP_CONTROL_ADDR_C2N_DATA + 4, (u32)(Data >> 32));
}

u64 XSimulatedannealingtop_Get_c2n(XSimulatedannealingtop *InstancePtr) {
    u64 Data;

    Xil_AssertNonvoid(InstancePtr != NULL);
    Xil_AssertNonvoid(InstancePtr->IsReady == XIL_COMPONENT_IS_READY);

    Data = XSimulatedannealingtop_ReadReg(InstancePtr->Control_BaseAddress, XSIMULATEDANNEALINGTOP_CONTROL_ADDR_C2N_DATA);
    Data += (u64)XSimulatedannealingtop_ReadReg(InstancePtr->Control_BaseAddress, XSIMULATEDANNEALINGTOP_CONTROL_ADDR_C2N_DATA + 4) << 32;
    return Data;
}

void XSimulatedannealingtop_Set_n(XSimulatedannealingtop *InstancePtr, u64 Data) {
    Xil_AssertVoid(InstancePtr != NULL);
    Xil_AssertVoid(InstancePtr->IsReady == XIL_COMPONENT_IS_READY);

    XSimulatedannealingtop_WriteReg(InstancePtr->Control_BaseAddress, XSIMULATEDANNEALINGTOP_CONTROL_ADDR_N_DATA, (u32)(Data));
    XSimulatedannealingtop_WriteReg(InstancePtr->Control_BaseAddress, XSIMULATEDANNEALINGTOP_CONTROL_ADDR_N_DATA + 4, (u32)(Data >> 32));
}

u64 XSimulatedannealingtop_Get_n(XSimulatedannealingtop *InstancePtr) {
    u64 Data;

    Xil_AssertNonvoid(InstancePtr != NULL);
    Xil_AssertNonvoid(InstancePtr->IsReady == XIL_COMPONENT_IS_READY);

    Data = XSimulatedannealingtop_ReadReg(InstancePtr->Control_BaseAddress, XSIMULATEDANNEALINGTOP_CONTROL_ADDR_N_DATA);
    Data += (u64)XSimulatedannealingtop_ReadReg(InstancePtr->Control_BaseAddress, XSIMULATEDANNEALINGTOP_CONTROL_ADDR_N_DATA + 4) << 32;
    return Data;
}

void XSimulatedannealingtop_InterruptGlobalEnable(XSimulatedannealingtop *InstancePtr) {
    Xil_AssertVoid(InstancePtr != NULL);
    Xil_AssertVoid(InstancePtr->IsReady == XIL_COMPONENT_IS_READY);

    XSimulatedannealingtop_WriteReg(InstancePtr->Control_BaseAddress, XSIMULATEDANNEALINGTOP_CONTROL_ADDR_GIE, 1);
}

void XSimulatedannealingtop_InterruptGlobalDisable(XSimulatedannealingtop *InstancePtr) {
    Xil_AssertVoid(InstancePtr != NULL);
    Xil_AssertVoid(InstancePtr->IsReady == XIL_COMPONENT_IS_READY);

    XSimulatedannealingtop_WriteReg(InstancePtr->Control_BaseAddress, XSIMULATEDANNEALINGTOP_CONTROL_ADDR_GIE, 0);
}

void XSimulatedannealingtop_InterruptEnable(XSimulatedannealingtop *InstancePtr, u32 Mask) {
    u32 Register;

    Xil_AssertVoid(InstancePtr != NULL);
    Xil_AssertVoid(InstancePtr->IsReady == XIL_COMPONENT_IS_READY);

    Register =  XSimulatedannealingtop_ReadReg(InstancePtr->Control_BaseAddress, XSIMULATEDANNEALINGTOP_CONTROL_ADDR_IER);
    XSimulatedannealingtop_WriteReg(InstancePtr->Control_BaseAddress, XSIMULATEDANNEALINGTOP_CONTROL_ADDR_IER, Register | Mask);
}

void XSimulatedannealingtop_InterruptDisable(XSimulatedannealingtop *InstancePtr, u32 Mask) {
    u32 Register;

    Xil_AssertVoid(InstancePtr != NULL);
    Xil_AssertVoid(InstancePtr->IsReady == XIL_COMPONENT_IS_READY);

    Register =  XSimulatedannealingtop_ReadReg(InstancePtr->Control_BaseAddress, XSIMULATEDANNEALINGTOP_CONTROL_ADDR_IER);
    XSimulatedannealingtop_WriteReg(InstancePtr->Control_BaseAddress, XSIMULATEDANNEALINGTOP_CONTROL_ADDR_IER, Register & (~Mask));
}

void XSimulatedannealingtop_InterruptClear(XSimulatedannealingtop *InstancePtr, u32 Mask) {
    Xil_AssertVoid(InstancePtr != NULL);
    Xil_AssertVoid(InstancePtr->IsReady == XIL_COMPONENT_IS_READY);

    XSimulatedannealingtop_WriteReg(InstancePtr->Control_BaseAddress, XSIMULATEDANNEALINGTOP_CONTROL_ADDR_ISR, Mask);
}

u32 XSimulatedannealingtop_InterruptGetEnabled(XSimulatedannealingtop *InstancePtr) {
    Xil_AssertNonvoid(InstancePtr != NULL);
    Xil_AssertNonvoid(InstancePtr->IsReady == XIL_COMPONENT_IS_READY);

    return XSimulatedannealingtop_ReadReg(InstancePtr->Control_BaseAddress, XSIMULATEDANNEALINGTOP_CONTROL_ADDR_IER);
}

u32 XSimulatedannealingtop_InterruptGetStatus(XSimulatedannealingtop *InstancePtr) {
    Xil_AssertNonvoid(InstancePtr != NULL);
    Xil_AssertNonvoid(InstancePtr->IsReady == XIL_COMPONENT_IS_READY);

    return XSimulatedannealingtop_ReadReg(InstancePtr->Control_BaseAddress, XSIMULATEDANNEALINGTOP_CONTROL_ADDR_ISR);
}

