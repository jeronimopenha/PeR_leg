// ==============================================================
// Vitis HLS - High-Level Synthesis from C, C++ and OpenCL v2022.2 (64-bit)
// Tool Version Limit: 2019.12
// Copyright 1986-2022 Xilinx, Inc. All Rights Reserved.
// ==============================================================
#ifndef XSIMULATEDANNEALINGTOP_H
#define XSIMULATEDANNEALINGTOP_H

#ifdef __cplusplus
extern "C" {
#endif

/***************************** Include Files *********************************/
#ifndef __linux__
#include "xil_types.h"
#include "xil_assert.h"
#include "xstatus.h"
#include "xil_io.h"
#else
#include <stdint.h>
#include <assert.h>
#include <dirent.h>
#include <fcntl.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/mman.h>
#include <unistd.h>
#include <stddef.h>
#endif
#include "xsimulatedannealingtop_hw.h"

/**************************** Type Definitions ******************************/
#ifdef __linux__
typedef uint8_t u8;
typedef uint16_t u16;
typedef uint32_t u32;
typedef uint64_t u64;
#else
typedef struct {
    u16 DeviceId;
    u64 Control_BaseAddress;
} XSimulatedannealingtop_Config;
#endif

typedef struct {
    u64 Control_BaseAddress;
    u32 IsReady;
} XSimulatedannealingtop;

typedef u32 word_type;

/***************** Macros (Inline Functions) Definitions *********************/
#ifndef __linux__
#define XSimulatedannealingtop_WriteReg(BaseAddress, RegOffset, Data) \
    Xil_Out32((BaseAddress) + (RegOffset), (u32)(Data))
#define XSimulatedannealingtop_ReadReg(BaseAddress, RegOffset) \
    Xil_In32((BaseAddress) + (RegOffset))
#else
#define XSimulatedannealingtop_WriteReg(BaseAddress, RegOffset, Data) \
    *(volatile u32*)((BaseAddress) + (RegOffset)) = (u32)(Data)
#define XSimulatedannealingtop_ReadReg(BaseAddress, RegOffset) \
    *(volatile u32*)((BaseAddress) + (RegOffset))

#define Xil_AssertVoid(expr)    assert(expr)
#define Xil_AssertNonvoid(expr) assert(expr)

#define XST_SUCCESS             0
#define XST_DEVICE_NOT_FOUND    2
#define XST_OPEN_DEVICE_FAILED  3
#define XIL_COMPONENT_IS_READY  1
#endif

/************************** Function Prototypes *****************************/
#ifndef __linux__
int XSimulatedannealingtop_Initialize(XSimulatedannealingtop *InstancePtr, u16 DeviceId);
XSimulatedannealingtop_Config* XSimulatedannealingtop_LookupConfig(u16 DeviceId);
int XSimulatedannealingtop_CfgInitialize(XSimulatedannealingtop *InstancePtr, XSimulatedannealingtop_Config *ConfigPtr);
#else
int XSimulatedannealingtop_Initialize(XSimulatedannealingtop *InstancePtr, const char* InstanceName);
int XSimulatedannealingtop_Release(XSimulatedannealingtop *InstancePtr);
#endif

void XSimulatedannealingtop_Start(XSimulatedannealingtop *InstancePtr);
u32 XSimulatedannealingtop_IsDone(XSimulatedannealingtop *InstancePtr);
u32 XSimulatedannealingtop_IsIdle(XSimulatedannealingtop *InstancePtr);
u32 XSimulatedannealingtop_IsReady(XSimulatedannealingtop *InstancePtr);
void XSimulatedannealingtop_Continue(XSimulatedannealingtop *InstancePtr);
void XSimulatedannealingtop_EnableAutoRestart(XSimulatedannealingtop *InstancePtr);
void XSimulatedannealingtop_DisableAutoRestart(XSimulatedannealingtop *InstancePtr);

void XSimulatedannealingtop_Set_n2c(XSimulatedannealingtop *InstancePtr, u64 Data);
u64 XSimulatedannealingtop_Get_n2c(XSimulatedannealingtop *InstancePtr);
void XSimulatedannealingtop_Set_c2n(XSimulatedannealingtop *InstancePtr, u64 Data);
u64 XSimulatedannealingtop_Get_c2n(XSimulatedannealingtop *InstancePtr);
void XSimulatedannealingtop_Set_n(XSimulatedannealingtop *InstancePtr, u64 Data);
u64 XSimulatedannealingtop_Get_n(XSimulatedannealingtop *InstancePtr);

void XSimulatedannealingtop_InterruptGlobalEnable(XSimulatedannealingtop *InstancePtr);
void XSimulatedannealingtop_InterruptGlobalDisable(XSimulatedannealingtop *InstancePtr);
void XSimulatedannealingtop_InterruptEnable(XSimulatedannealingtop *InstancePtr, u32 Mask);
void XSimulatedannealingtop_InterruptDisable(XSimulatedannealingtop *InstancePtr, u32 Mask);
void XSimulatedannealingtop_InterruptClear(XSimulatedannealingtop *InstancePtr, u32 Mask);
u32 XSimulatedannealingtop_InterruptGetEnabled(XSimulatedannealingtop *InstancePtr);
u32 XSimulatedannealingtop_InterruptGetStatus(XSimulatedannealingtop *InstancePtr);

#ifdef __cplusplus
}
#endif

#endif
