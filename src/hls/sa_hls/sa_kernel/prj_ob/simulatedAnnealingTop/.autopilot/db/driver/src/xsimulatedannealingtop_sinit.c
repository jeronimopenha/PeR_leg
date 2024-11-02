// ==============================================================
// Vitis HLS - High-Level Synthesis from C, C++ and OpenCL v2022.2 (64-bit)
// Tool Version Limit: 2019.12
// Copyright 1986-2022 Xilinx, Inc. All Rights Reserved.
// ==============================================================
#ifndef __linux__

#include "xstatus.h"
#include "xparameters.h"
#include "xsimulatedannealingtop.h"

extern XSimulatedannealingtop_Config XSimulatedannealingtop_ConfigTable[];

XSimulatedannealingtop_Config *XSimulatedannealingtop_LookupConfig(u16 DeviceId) {
	XSimulatedannealingtop_Config *ConfigPtr = NULL;

	int Index;

	for (Index = 0; Index < XPAR_XSIMULATEDANNEALINGTOP_NUM_INSTANCES; Index++) {
		if (XSimulatedannealingtop_ConfigTable[Index].DeviceId == DeviceId) {
			ConfigPtr = &XSimulatedannealingtop_ConfigTable[Index];
			break;
		}
	}

	return ConfigPtr;
}

int XSimulatedannealingtop_Initialize(XSimulatedannealingtop *InstancePtr, u16 DeviceId) {
	XSimulatedannealingtop_Config *ConfigPtr;

	Xil_AssertNonvoid(InstancePtr != NULL);

	ConfigPtr = XSimulatedannealingtop_LookupConfig(DeviceId);
	if (ConfigPtr == NULL) {
		InstancePtr->IsReady = 0;
		return (XST_DEVICE_NOT_FOUND);
	}

	return XSimulatedannealingtop_CfgInitialize(InstancePtr, ConfigPtr);
}

#endif

