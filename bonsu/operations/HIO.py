#############################################
##   Filename: HIO.py
##
##    Copyright (C) 2011 Marcus C. Newton
##
## This program is free software: you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation, either version 3 of the License, or
## (at your option) any later version.
##
## This program is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.
##
## You should have received a copy of the GNU General Public License
## along with this program.  If not, see <http://www.gnu.org/licenses/>.
##
## Contact: Bonsu.Devel@gmail.com
#############################################
import wx
import sys
import os
import numpy
from .wrap import WrapArray
def HIO\
	(
		self,
		beta,
		startiter,
		numiter
	):
	def updatereal():
		wx.CallAfter(self.ancestor.GetPage(1).UpdateReal,)
	def updaterecip():
		wx.CallAfter(self.ancestor.GetPage(1).UpdateRecip,)
	def updatelog():
		try:
			n = self.citer_flow[0]
			res = self.ancestor.GetPage(0).residual[n]
			string = "Iteration: %06d, Residual: %1.9f" %(n,res)
			self.ancestor.GetPage(0).queue_info.put(string)
		except:
			pass
	seqdata = self.seqdata
	expdata = self.expdata
	support = self.support
	residual = self.residual
	citer_flow = self.citer_flow
	visual_amp_real = self.visual_amp_real
	visual_amp_recip = self.visual_amp_recip
	visual_phase_real = self.visual_phase_real
	visual_phase_recip = self.visual_phase_recip
	rho_m1 = numpy.array( seqdata, copy=True, dtype=numpy.cdouble)
	nn=numpy.asarray( seqdata.shape, numpy.int32 )
	ndim=int(seqdata.ndim)
	from ..lib.prfftw import hio
	hio(seqdata,expdata,support,\
	beta,startiter,numiter,ndim,rho_m1,nn,residual,citer_flow,\
	visual_amp_real,visual_phase_real,visual_amp_recip,visual_phase_recip,\
	updatereal,updaterecip, updatelog)
def HIOMask\
	(
		self,
		beta,
		startiter,
		numiter
	):
	def updatereal():
		wx.CallAfter(self.ancestor.GetPage(1).UpdateReal,)
	def updaterecip():
		wx.CallAfter(self.ancestor.GetPage(1).UpdateRecip,)
	def updatelog():
		try:
			n = self.citer_flow[0]
			res = self.ancestor.GetPage(0).residual[n]
			string = "Iteration: %06d, Residual: %1.9f" %(n,res)
			self.ancestor.GetPage(0).queue_info.put(string)
		except:
			pass
	seqdata = self.seqdata
	expdata = self.expdata
	support = self.support
	mask = self.mask
	residual = self.residual
	citer_flow = self.citer_flow
	visual_amp_real = self.visual_amp_real
	visual_amp_recip = self.visual_amp_recip
	visual_phase_real = self.visual_phase_real
	visual_phase_recip = self.visual_phase_recip
	rho_m1 = numpy.array( seqdata, copy=True, dtype=numpy.cdouble)
	nn=numpy.asarray( seqdata.shape, numpy.int32 )
	ndim=int(seqdata.ndim)
	from ..lib.prfftw import hiomask
	hiomask(seqdata,expdata,support, mask,\
	beta,startiter,numiter,ndim,rho_m1,nn,residual,citer_flow,\
	visual_amp_real,visual_phase_real,visual_amp_recip,visual_phase_recip,\
	updatereal,updaterecip, updatelog)
def HIOPlus\
	(
		self,
		beta,
		startiter,
		numiter
	):
	def updatereal():
		wx.CallAfter(self.ancestor.GetPage(1).UpdateReal,)
	def updaterecip():
		wx.CallAfter(self.ancestor.GetPage(1).UpdateRecip,)
	def updatelog():
		try:
			n = self.citer_flow[0]
			res = self.ancestor.GetPage(0).residual[n]
			string = "Iteration: %06d, Residual: %1.9f" %(n,res)
			self.ancestor.GetPage(0).queue_info.put(string)
		except:
			pass
	seqdata = self.seqdata
	expdata = self.expdata
	support = self.support
	mask = self.mask
	residual = self.residual
	citer_flow = self.citer_flow
	visual_amp_real = self.visual_amp_real
	visual_amp_recip = self.visual_amp_recip
	visual_phase_real = self.visual_phase_real
	visual_phase_recip = self.visual_phase_recip
	rho_m1 = numpy.array( seqdata, copy=True, dtype=numpy.cdouble)
	nn=numpy.asarray( seqdata.shape, numpy.int32 )
	ndim=int(seqdata.ndim)
	from ..lib.prfftw import hioplus
	hioplus(seqdata,expdata,support, mask,\
	beta,startiter,numiter,ndim,rho_m1,nn,residual,citer_flow,\
	visual_amp_real,visual_phase_real,visual_amp_recip,visual_phase_recip,\
	updatereal,updaterecip, updatelog)
def PCHIO\
	(
		self,
		beta,
		startiter,
		numiter,
		phasemax,
		phasemin
	):
	def updatereal():
		wx.CallAfter(self.ancestor.GetPage(1).UpdateReal,)
	def updaterecip():
		wx.CallAfter(self.ancestor.GetPage(1).UpdateRecip,)
	def updatelog():
		try:
			n = self.citer_flow[0]
			res = self.ancestor.GetPage(0).residual[n]
			string = "Iteration: %06d, Residual: %1.9f" %(n,res)
			self.ancestor.GetPage(0).queue_info.put(string)
		except:
			pass
	seqdata = self.seqdata
	expdata = self.expdata
	support = self.support
	mask = self.mask
	residual = self.residual
	citer_flow = self.citer_flow
	visual_amp_real = self.visual_amp_real
	visual_amp_recip = self.visual_amp_recip
	visual_phase_real = self.visual_phase_real
	visual_phase_recip = self.visual_phase_recip
	rho_m1 = numpy.array( seqdata, copy=True, dtype=numpy.cdouble)
	nn=numpy.asarray( seqdata.shape, numpy.int32 )
	ndim=int(seqdata.ndim)
	from ..lib.prfftw import pchio
	pchio(seqdata,expdata,support, mask,\
	beta,startiter,numiter,ndim,phasemax,phasemin,rho_m1,nn,residual,citer_flow,\
	visual_amp_real,visual_phase_real,visual_amp_recip,visual_phase_recip,\
	updatereal,updaterecip, updatelog)
def PGCHIO\
	(
		self,
		beta,
		startiter,
		numiter,
		phasemax,
		phasemin,
		qx,
		qy,
		qz
	):
	def updatereal():
		wx.CallAfter(self.ancestor.GetPage(1).UpdateReal,)
	def updaterecip():
		wx.CallAfter(self.ancestor.GetPage(1).UpdateRecip,)
	def updatelog():
		try:
			n = self.citer_flow[0]
			res = self.ancestor.GetPage(0).residual[n]
			string = "Iteration: %06d, Residual: %1.9f" %(n,res)
			self.ancestor.GetPage(0).queue_info.put(string)
		except:
			pass
	seqdata = self.seqdata
	expdata = self.expdata
	support = self.support
	mask = self.mask
	residual = self.residual
	citer_flow = self.citer_flow
	visual_amp_real = self.visual_amp_real
	visual_amp_recip = self.visual_amp_recip
	visual_phase_real = self.visual_phase_real
	visual_phase_recip = self.visual_phase_recip
	rho_m1 = numpy.array( seqdata, copy=True, dtype=numpy.cdouble)
	tmpdata = numpy.array( seqdata, copy=True, dtype=numpy.cdouble)
	nn=numpy.asarray( seqdata.shape, numpy.int32 )
	ndim=int(seqdata.ndim)
	from ..lib.prfftw import pgchio
	pgchio(seqdata,expdata,support, mask,tmpdata,\
	beta,startiter,numiter,ndim,phasemax,phasemin,qx,qy,qz,rho_m1,nn,residual,citer_flow,\
	visual_amp_real,visual_phase_real,visual_amp_recip,visual_phase_recip,\
	updatereal,updaterecip, updatelog)
def HIOMaskPC\
	(
	self,
	beta,
	startiter,
	numiter,
	niterrlpre,
	niterrl,
	niterrlinterval,
	gammaHWHM,
	zex, zey, zez,
	reset_gamma
	):
	def updatereal():
		wx.CallAfter(self.ancestor.GetPage(1).UpdateReal,)
	def updaterecip():
		wx.CallAfter(self.ancestor.GetPage(1).UpdateRecip,)
	def updatelog():
		try:
			n = self.citer_flow[0]
			res = self.ancestor.GetPage(0).residual[n]
			string = "Iteration: %06d, Residual: %1.9f" %(n,res)
			self.ancestor.GetPage(0).queue_info.put(string)
		except:
			pass
	seqdata = self.seqdata
	expdata = self.expdata
	support = self.support
	mask = self.mask
	residual = self.residual
	citer_flow = self.citer_flow
	visual_amp_real = self.visual_amp_real
	visual_amp_recip = self.visual_amp_recip
	visual_phase_real = self.visual_phase_real
	visual_phase_recip = self.visual_phase_recip
	rho_m1 = numpy.array( seqdata, copy=True, dtype=numpy.cdouble)
	nn=numpy.asarray( seqdata.shape, numpy.int32 )
	ndim=int(seqdata.ndim)
	from ..lib.prfftw import hiomaskpc
	hiomaskpc(seqdata,expdata,support, mask,\
	gammaHWHM, reset_gamma, niterrl, niterrlpre, niterrlinterval, zex, zey, zez,
	beta,startiter,numiter,ndim,rho_m1,nn,residual,citer_flow,\
	visual_amp_real,visual_phase_real,visual_amp_recip,visual_phase_recip,\
	updatereal,updaterecip, updatelog)