#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""LPS25HB: 260-1260 hPa absolute digital output barometer"""

__author__     = "ChISL"
__copyright__  = "TBD"
__credits__    = ["STMicroelectronics"]
__license__    = "TBD"
__version__    = "Version 0.1"
__maintainer__ = "https://chisl.io"
__email__      = "info@chisl.io"
__status__     = "Test"

#
#   THIS FILE IS AUTOMATICALLY CREATED
#    D O     N O T     M O D I F Y  !
#

from LPS25HB_constants import *

# name:        LPS25HB
# description: 260-1260 hPa absolute digital output barometer
# manuf:       STMicroelectronics
# version:     Version 0.1
# url:         http://www.st.com/resource/en/datasheet/lps25hb.pdf
# date:        2018-01-04


# Derive from this class and implement read and write
class LPS25HB_Base:
	"""260-1260 hPa absolute digital output barometer"""
	# Register REF_P
	# 8.1-3
	#       Reference pressure
	#       The Reference pressure value is a 24-bit data subtracted from the sensor output measurement and 
	#       it is composed of REF_P_H (0Ah), REF_P_L (09h) and REF_P_XL (08h). The value is expressed as 
	#       2’s complement.
	#       The reference pressure value is subtracted from the sensor output measurement, to detect a 
	#       measured pressure beyond programmed limits (refer to INTERRUPT_CFG (24h) register), and is 
	#       used for the Autozero function. 
	
	
	def setREF_P(self, val):
		"""Set register REF_P"""
		self.write(REG.REF_P, val, 24)
	
	def getREF_P(self):
		"""Get register REF_P"""
		return self.read(REG.REF_P, 24)
	
	# Bits REFL
	# The Reference pressure value is a 24-bit data and it is composed of Section 10.11:
	#           "REF_P_H_17h", Section 10.10: "REF_P_L_16h" and Section 10.9: "REF_P_XL (15h)". 
	
	# Register WHO_AM_I
	# 8.4
	#       Device Who am I 
	
	
	def setWHO_AM_I(self, val):
		"""Set register WHO_AM_I"""
		self.write(REG.WHO_AM_I, val, 8)
	
	def getWHO_AM_I(self):
		"""Get register WHO_AM_I"""
		return self.read(REG.WHO_AM_I, 8)
	
	# Bits WHO_AM_I
	# Register RES_CONF
	# 8.5
	#       Pressure and temperature resolution 
	
	
	def setRES_CONF(self, val):
		"""Set register RES_CONF"""
		self.write(REG.RES_CONF, val, 8)
	
	def getRES_CONF(self):
		"""Get register RES_CONF"""
		return self.read(REG.RES_CONF, 8)
	
	# Bits reserved_0
	# Bits AVGT
	# Temperature internal average configuration. 
	# Bits AVGP
	# Temperature internal average configuration. 
	# Register CTRL_REG1
	# 8.6
	#       Control register 1. 
	
	
	def setCTRL_REG1(self, val):
		"""Set register CTRL_REG1"""
		self.write(REG.CTRL_REG1, val, 8)
	
	def getCTRL_REG1(self):
		"""Get register CTRL_REG1"""
		return self.read(REG.CTRL_REG1, 8)
	
	# Bits PD
	# Power-down control. 
	#           The PD bit allows the turn on of the device. The device is in power-down mode when PD is set 
	#           to ‘0’ (default value after boot). The device is active when PD is set to ‘1’. 
	
	# Bits ODR
	# Output data rate selection. 
	#           When ODR[2,0] are set to ‘000’ the device enables one-shot mode. When ‘ONESHOT’ bit in 
	#           CTRL_REG2 (21h) is set to ‘1’, a new set of data for pressure and temperature is acquired. 
	
	# Bits DIFF_EN
	# Interrupt generation enable.
	#           The DIFF_EN bit is used to enable the computing of differential pressure output. 
	#           It is recommended to enable DIFF_EN after the configuration of REF_P_H (0Ah), 
	#           REF_P_L (09h), REF_P_XL (08h), THS_P_H (31h) and THS_P_L (30h). 
	
	# Bits BDU
	# Block data update. 
	#           The BDU bit is used to inhibit the update of the output registers between the reading of the upper 
	#           and lower register parts. In default mode (BDU = ‘0’), the lower and upper register parts are 
	#           updated continuously. When the BDU is activated (BDU = ‘1’), the content of the output registers 
	#           is not updated until both MSB and LSB are read, avoiding the reading of values related to different 
	#           samples.
	
	# Bits RESET_AZ
	# Reset Autozero function. 
	#           The RESET_AZ bit is used to reset the AutoZero function. Resetting REF_P_H (0Ah), REF_P_L (09h) and 
	#           REF_P_XL (08h) sets the pressure reference registers RPDS_H (3Ah) and RPDS_L (39h) to the default value. 
	#           RESET_AZ is self-cleared. For the AutoZero function please refer to CTRL_REG2 (21h). 
	
	# Bits SIM
	# SPI Serial Interface Mode selection. 
	# Register CTRL_REG2
	# 8.7
	#       Control register 2 
	
	
	def setCTRL_REG2(self, val):
		"""Set register CTRL_REG2"""
		self.write(REG.CTRL_REG2, val, 8)
	
	def getCTRL_REG2(self):
		"""Get register CTRL_REG2"""
		return self.read(REG.CTRL_REG2, 8)
	
	# Bits BOOT
	# Reboot memory content. 
	#           The bit is self-cleared when the BOOT is completed. 
	#           The BOOT bit is used to refresh the content of the internal registers stored in the Flash 
	#           memory block. At device power-up the content of the Flash memory block is transferred to 
	#           the internal registers related to the trimming functions to allow correct behavior of the 
	#           device itself. If for any reason the content of the trimming registers is modified, it is 
	#           sufficient to use this bit to restore the correct values. When the BOOT bit is set to ‘1’, 
	#           the content of the internal Flash is copied inside the corresponding internal registers and 
	#           is used to calibrate the device. These values are factory trimmed and they are different for 
	#           every device. They allow correct behavior of the device and normally they should not be changed. 
	#           The boot process takes 2.2 msec. At the end of the boot process, the BOOT bit is set to ‘0’ 
	#           automatically. 
	
	# Bits FIFO_EN
	# FIFO enable. 
	# Bits STOP_ON_FTH
	# Enable the FTH_FIFO bit in FIFO_STATUS (2Fh) for monitoring of FIFO level. 
	# Bits FIFO_MEAN_DEC
	# Enable to decimate the output pressure to 1Hz with FIFO Mean mode. 
	#           FIFO_MEAN_DEC bit is to decimate the output pressure to 1Hz with FIFO Mean mode. 
	#           When this bit is ‘1’, the output is decimated to 1 Hz as the moving average is being 
	#           taken at the rate of the ODR. Otherwise, averaged pressure data will be updated 
	#           according to the ODR defined. 
	
	# Bits I2C_DIS
	# Disable I2C interface. 
	# Bits SWRESET
	# Software reset. 
	#           SWRESET is the software reset bit. The device is reset to the power-on configuration after 
	#           SWRESET bit is set to '1'. The software reset process takes 4 μsec. When BOOT follows, 
	#           the recommended sequence is SWRESET first and then BOOT. 
	
	# Bits AUTOZERO
	# Autozero enable. 
	#           AUTOZERO, when set to ‘1’, the actual pressure output value is copied in REF_P_H (0Ah), 
	#           REF_P_L (09h) and REF_P_XL (08h). When this bit is enabled, the register content of REF_P is 
	#           subtracted from the pressure output value. 
	
	# Bits ONE_SHOT
	# One-shot enable. 
	#           The ONE_SHOT bit is used to start a new conversion when the ODR[2,0] bits in CTRL_REG1 (20h) 
	#           are set to ‘000’. Writing a ‘1’ in ONE_SHOT triggers a single measurement of pressure and temperature. 
	#           Once the measurement is done, the ONE_SHOT bit will self-clear, the new data are available in 
	#           the output registers, and the STATUS_REG bits are updated. 
	
	# Register CTRL_REG3
	# 8.8
	#       Control register 3 - INT_DRDY pin control register 
	#       The device features one set of programmable interrupt sources (INT) that can be configured to 
	#       trigger different pressure events. Figure 19 shows the block diagram of the interrupt generation 
	#       block and output pressure data.
	#       The device may also be configured to generate, through the INT_DRDY pin, a Data Ready 
	#       signal (DRDY) which indicates when a new measured pressure data is available, thus simplifying 
	#       data synchronization in digital systems or optimizing system power consumption.
	
	
	def setCTRL_REG3(self, val):
		"""Set register CTRL_REG3"""
		self.write(REG.CTRL_REG3, val, 8)
	
	def getCTRL_REG3(self):
		"""Get register CTRL_REG3"""
		return self.read(REG.CTRL_REG3, 8)
	
	# Bits INT_H_L
	# Interrupt active-high/low. 
	# Bits PP_OD
	# Push-pull/open drain selection on interrupt pads. 
	# Bits reserved_0
	# Bits INT_S
	# Data signal on INT_DRDY pin control bits. 
	# Register CTRL_REG4
	# Interrupt configuration 
	
	def setCTRL_REG4(self, val):
		"""Set register CTRL_REG4"""
		self.write(REG.CTRL_REG4, val, 8)
	
	def getCTRL_REG4(self):
		"""Get register CTRL_REG4"""
		return self.read(REG.CTRL_REG4, 8)
	
	# Bits reserved_0
	# Bits F_EMPTY
	# FIFO empty flag on INT_DRDY pin. 
	# Bits F_FTH
	# FIFO threshold (watermark) status on INT_DRDY pin to indicate that FIFO is filled 
	#           up to the threshold level. 
	
	# Bits F_OVR
	# FIFO overrun interrupt on INT_DRDY pin to indicate that FIFO is full in FIFO mode or 
	#           that an overrun occurred in Stream mode. 
	
	# Bits DRDY
	# Data-ready signal on INT_DRDY pin. 
	# Register INTERRUPT_CFG
	# 8.1
	#       Interrupt configuration 
	
	
	def setINTERRUPT_CFG(self, val):
		"""Set register INTERRUPT_CFG"""
		self.write(REG.INTERRUPT_CFG, val, 8)
	
	def getINTERRUPT_CFG(self):
		"""Get register INTERRUPT_CFG"""
		return self.read(REG.INTERRUPT_CFG, 8)
	
	# Bits reserved_0
	# Bits LIR
	# Latch interrupt request to the INT_SOURCE (25h) register. 
	# Bits PLE
	# Enable interrupt generation on differential pressure low event. 
	# Bits PHE
	# Enable interrupt generation on differential pressure high event. 
	# Register INT_SOURCE
	# 8.15
	#       Interrupt source 
	#       INT_SOURCE register is cleared by reading it.
	
	
	def setINT_SOURCE(self, val):
		"""Set register INT_SOURCE"""
		self.write(REG.INT_SOURCE, val, 8)
	
	def getINT_SOURCE(self):
		"""Get register INT_SOURCE"""
		return self.read(REG.INT_SOURCE, 8)
	
	# Bits reserved_0
	# Bits IA
	# Interrupt active. 
	# Bits PL
	# Differential pressure Low. 
	# Bits PH
	# Differential pressure High. 
	# Register STATUS_REG
	# 8.12
	#       Status register. 
	#       This register is updated every ODR cycle, regardless of the BDU value in CTRL_REG1 (20h). 
	
	
	def setSTATUS_REG(self, val):
		"""Set register STATUS_REG"""
		self.write(REG.STATUS_REG, val, 8)
	
	def getSTATUS_REG(self):
		"""Get register STATUS_REG"""
		return self.read(REG.STATUS_REG, 8)
	
	# Bits reserved_0
	# Bits T_OR
	# Temperature data overrun. 
	# Bits P_OR
	# Pressure data overrun. 
	# Bits unused_1
	# Bits T_DA
	# Temperature data available. 
	# Bits P_DA
	# Pressure data available. 
	# Register PRESS_OUT
	# 8.13-15
	#       The pressure output value is a 24-bit data that contains the measured pressure. 
	#       It is composed of PRESS_OUT_H (2Ah), PRESS_OUT_L (29h) and PRESS_OUT_XL (28h). 
	#       The value is expressed as 2’s complement. 
	
	
	def setPRESS_OUT(self, val):
		"""Set register PRESS_OUT"""
		self.write(REG.PRESS_OUT, val, 24)
	
	def getPRESS_OUT(self):
		"""Get register PRESS_OUT"""
		return self.read(REG.PRESS_OUT, 24)
	
	# Bits PRESS_OUT
	# Register TEMP_OUT
	# 8.16-17
	#       Temperature output value
	#       The temperature output value is a 16-bit data that contains the measured temperature. 
	#       It is composed of TEMP_OUT_H (2Ch) and TEMP_OUT_L (2Bh). The value is expressed as 2’s complement. 
	
	
	def setTEMP_OUT(self, val):
		"""Set register TEMP_OUT"""
		self.write(REG.TEMP_OUT, val, 16)
	
	def getTEMP_OUT(self):
		"""Get register TEMP_OUT"""
		return self.read(REG.TEMP_OUT, 16)
	
	# Bits TEMP_OUT
	# Register FIFO_CTRL
	# 8.18
	#       FIFO control register 
	#       FIFO Mean mode: The FIFO can be used for implementing a HW moving average on the pressure measurements. 
	#       The number of samples of the moving average can be 2, 4, 8, 16 or 32 samples by selecting the FIFO Mean 
	#       mode sample size as per Table 23. Different configurations are not allowed. 
	
	
	def setFIFO_CTRL(self, val):
		"""Set register FIFO_CTRL"""
		self.write(REG.FIFO_CTRL, val, 8)
	
	def getFIFO_CTRL(self):
		"""Get register FIFO_CTRL"""
		return self.read(REG.FIFO_CTRL, 8)
	
	# Bits F_MODE
	# FIFO mode selection. 
	# Bits WTM
	# FIFO threshold (watermark) level selection. 
	#           Please note that when using the FIFO Mean mode it is not possible to access the FIFO content. 
	
	# Register FIFO_STATUS
	# 8.19
	#       FIFO status 
	
	
	def setFIFO_STATUS(self, val):
		"""Set register FIFO_STATUS"""
		self.write(REG.FIFO_STATUS, val, 8)
	
	def getFIFO_STATUS(self):
		"""Get register FIFO_STATUS"""
		return self.read(REG.FIFO_STATUS, 8)
	
	# Bits FTH_FIFO
	# FIFO threshold status. 
	# Bits OVR
	# FIFO overrun status. 
	# Bits EMPTY_FIFO
	# Empty FIFO bit status. 
	# Bits FSS
	# FIFO stored data level. 
	#           5'b00000: FIFO empty @ EMPTY_FIFO "1" or 1st sample stored in FIFO@EMPTY_FIFO "0"; 
	#           5'b11111: FIFO is full and has 32 unread samples 
	
	# Register THS_P
	# 8.20-21 
	#         Threshold value for pressure interrupt generation.
	#         This register contains the threshold value for pressure interrupt generation. 
	#         The threshold value for pressure interrupt generation is a 16-bit register composed 
	#         of THS_P_H (31h) and THS_P_L (30h). The value is expressed as unsigned number: 
	#         Interrupt threshold(hPA) = (THS_P)/16. 
	
	
	def setTHS_P(self, val):
		"""Set register THS_P"""
		self.write(REG.THS_P, val, 16)
	
	def getTHS_P(self):
		"""Get register THS_P"""
		return self.read(REG.THS_P, 16)
	
	# Bits THS
	# Refer to Section 10.2: "THS_P_L (0Ch)" 
	# Register RPDS
	# 8.22-23
	#       Pressure offset 
	
	
	def setRPDS(self, val):
		"""Set register RPDS"""
		self.write(REG.RPDS, val, 16)
	
	def getRPDS(self):
		"""Get register RPDS"""
		return self.read(REG.RPDS, 16)
	
	# Bits RPDS
