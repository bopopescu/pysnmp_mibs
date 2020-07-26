# PySNMP SMI module. Autogenerated from smidump -f python JUNIPER-POWER-SUPPLY-UNIT-MIB
# by libsmi2pysnmp-0.1.3 at Thu May 22 11:57:55 2014,
# Python version sys.version_info(major=2, minor=7, micro=2, releaselevel='final', serial=0)

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
( jnxContentsContainerIndex, jnxContentsL1Index, jnxContentsL2Index, jnxContentsL3Index, ) = mibBuilder.importSymbols("JUNIPER-MIB", "jnxContentsContainerIndex", "jnxContentsL1Index", "jnxContentsL2Index", "jnxContentsL3Index")
( jnxPsuMIBRoot, ) = mibBuilder.importSymbols("JUNIPER-SMI", "jnxPsuMIBRoot")
( Bits, Integer32, ModuleIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "ModuleIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks")
( DisplayString, TextualConvention, TruthValue, ) = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "TruthValue")

# Objects

jnxPsuMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2636, 3, 58, 1)).setRevisions(("2010-10-27 00:00","2010-05-13 00:00","2010-01-27 00:00",))
if mibBuilder.loadTexts: jnxPsuMIB.setOrganization("Juniper Networks, Inc.")
if mibBuilder.loadTexts: jnxPsuMIB.setContactInfo("Juniper Technical Assistance Center\nJuniper Networks, Inc.\n1194 N. Mathilda Avenue\nSunnyvale, CA 94089\nE-mail: support@juniper.net")
if mibBuilder.loadTexts: jnxPsuMIB.setDescription("The Juniper Supply Unit MIB definitions for enabling\npower monitoring and management of a juniper device.")
jnxPsuNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 58, 1, 1))
jnxPsuObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 58, 1, 2))
jnxPsuScalars = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 58, 1, 2, 1))
jnxPsuAvailableDeviceCount = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 58, 1, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxPsuAvailableDeviceCount.setDescription("Gives the number of PSU units available online in the System.")
jnxPsuAvailableAveragePowerSupply = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 58, 1, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxPsuAvailableAveragePowerSupply.setDescription("Gives the total average power that the System can supply from the\navailable online units in Watts.")
jnxPsuAvailableMaxPowerSupply = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 58, 1, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxPsuAvailableMaxPowerSupply.setDescription("Gives the total maximum power that the System can supply from the \navailable online units in Watts.")
jnxPsuRedundancy = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 58, 1, 2, 1, 4), Integer().subtype(subtypeSpec=SingleValueConstraint(1,3,2,)).subtype(namedValues=NamedValues(("nPlusNRedundancy", 1), ("nPlusOneRedundancy", 2), ("none", 3), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxPsuRedundancy.setDescription("PSU power redundancy configuration.")
jnxPsuChassisPowerReserved = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 58, 1, 2, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxPsuChassisPowerReserved.setDescription("Power reserved for Chassis in Watts.")
jnxPsuChassisPowerAllocated = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 58, 1, 2, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxPsuChassisPowerAllocated.setDescription("Total power allocated for chassis and all the FPCs in Watts.")
jnxPsuRedundantPowerAvailable = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 58, 1, 2, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxPsuRedundantPowerAvailable.setDescription("Power(in Watts) that is still available for allocation\neven while supporting redundancy with the present usage.")
jnxPsuTotalPowerAvailable = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 58, 1, 2, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxPsuTotalPowerAvailable.setDescription("Power(in Watts) which could be made available for further\nallocation without supporting any redundancy with the present usage.")
jnxPsuChassisPowerConsumed = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 58, 1, 2, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxPsuChassisPowerConsumed.setDescription("Total power consumed by the entire system rounded to the nearest integer.\nThis is calculated using the PowerFactor, Current and Voltage values \nof each PSU that is online and connected to the System.")
jnxPsuTemperatureInflow = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 58, 1, 2, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxPsuTemperatureInflow.setDescription("Average inflow temperature calculated from all \nthe available input sensors on the main RE.")
jnxPsuTemperatureOutflow = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 58, 1, 2, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxPsuTemperatureOutflow.setDescription("Average outflow temperature calculated from all \nthe available output sensors on the main RE.")
jnxPsuTemperatureInflowSamples = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 58, 1, 2, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxPsuTemperatureInflowSamples.setDescription("The number of samples being taken while calculating\njnxPsuTemperatureInflow.")
jnxPsuTemperatureOutflowSamples = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 58, 1, 2, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxPsuTemperatureOutflowSamples.setDescription("The number of samples being taken while calculating\njnxPsuTemperatureOutflow.")
jnxPsuTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 58, 1, 2, 2))
if mibBuilder.loadTexts: jnxPsuTable.setDescription("A list of power entries for each PSU component.")
jnxPsuEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 58, 1, 2, 2, 1)).setIndexNames((0, "JUNIPER-MIB", "jnxContentsContainerIndex"), (0, "JUNIPER-MIB", "jnxContentsL1Index"), (0, "JUNIPER-MIB", "jnxContentsL2Index"), (0, "JUNIPER-MIB", "jnxContentsL3Index"))
if mibBuilder.loadTexts: jnxPsuEntry.setDescription("Defines an entry in jnxPsuTable. ")
jnxPsuAvgPower = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 58, 1, 2, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxPsuAvgPower.setDescription("Buffer that contains the average power used, in Watts \nfor each component.")
jnxPsuMaxPower = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 58, 1, 2, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxPsuMaxPower.setDescription("Buffer that contains the max power available, in Watts \nfor each component.")
jnxPsuMode = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 58, 1, 2, 2, 1, 3), Integer().subtype(subtypeSpec=SingleValueConstraint(1,3,)).subtype(namedValues=NamedValues(("single", 1), ("three", 3), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxPsuMode.setDescription("Mode for each PSU component.")
jnxPsuOutletCount = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 58, 1, 2, 2, 1, 4), Integer32().clone(0)).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxPsuOutletCount.setDescription("The number of outlets (regardless of their current state)\npresent on this psu component, default is 0.")
jnxPsuEnvironmentTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 58, 1, 2, 3))
if mibBuilder.loadTexts: jnxPsuEnvironmentTable.setDescription("A list of PSU Environment entries.")
jnxPsuEnvironmentEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 58, 1, 2, 3, 1)).setIndexNames((0, "JUNIPER-MIB", "jnxContentsContainerIndex"), (0, "JUNIPER-MIB", "jnxContentsL1Index"), (0, "JUNIPER-MIB", "jnxContentsL2Index"), (0, "JUNIPER-MIB", "jnxContentsL3Index"))
if mibBuilder.loadTexts: jnxPsuEnvironmentEntry.setDescription("Defines an entry in jnxPsuEnvironmentTable.")
jnxPsuThermalValue = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 58, 1, 2, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxPsuThermalValue.setDescription("Temparature at each component in degrees Celsius rounded to\nthe nearest integer.")
jnxPsuHumidityValue = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 58, 1, 2, 3, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxPsuHumidityValue.setDescription("Humidity at each component in percentage.")
jnxPsuOutletTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 58, 1, 2, 4))
if mibBuilder.loadTexts: jnxPsuOutletTable.setDescription("Gives details of each Power outlet`s state,\ncapacity to supply power, and other details.")
jnxPsuOutletEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 58, 1, 2, 4, 1)).setIndexNames((0, "JUNIPER-MIB", "jnxContentsContainerIndex"), (0, "JUNIPER-MIB", "jnxContentsL1Index"), (0, "JUNIPER-MIB", "jnxContentsL2Index"), (0, "JUNIPER-MIB", "jnxContentsL3Index"))
if mibBuilder.loadTexts: jnxPsuOutletEntry.setDescription("A value contained within the OutletEntry")
jnxPsuOutletName = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 58, 1, 2, 4, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 15))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxPsuOutletName.setDescription("Outlet name associated to the power supply unit for \neach PSU Component.")
jnxPsuOutletDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 58, 1, 2, 4, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxPsuOutletDescription.setDescription("Outlet description associated to the power supply unit for \neach PSU Component.")
jnxPsuOutletAvgPower = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 58, 1, 2, 4, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxPsuOutletAvgPower.setDescription("Buffer that contains the average power used, in Watts for each component.")
jnxPsuOutletMaxPower = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 58, 1, 2, 4, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxPsuOutletMaxPower.setDescription("Buffer that contains the maximum power available, in Watts for each component.")
jnxPsuOutletCurrent = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 58, 1, 2, 4, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxPsuOutletCurrent.setDescription("PSU output current in milliamps rounded to the nearest\ninteger.")
jnxPsuOutletStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 58, 1, 2, 4, 1, 8), Integer().subtype(subtypeSpec=SingleValueConstraint(1,0,)).subtype(namedValues=NamedValues(("off", 0), ("on", 1), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxPsuOutletStatus.setDescription("The value of the operational status for the given outlet.\nThis can also be used to set the outlet state")
jnxPsuOutletVoltage = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 58, 1, 2, 4, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxPsuOutletVoltage.setDescription("Output voltage in Volts rounded to the nearest integer.")
jnxPsuOutletPowerFactorValue = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 58, 1, 2, 4, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxPsuOutletPowerFactorValue.setDescription("Power factor percentage of each PSU (2k/3k).\n\nAlgorithm for calculation of Power Factor is below.\nFor PowerOut values that fall in between 618.93W and 915.24W,\nsay 700W, the appropriate PF ranges from 0.910191 & \n0.917994. Following linear equation could help deduce a\nfairly accurate input power value.\n\nLinear equation y = mx + b (where m is the slope and b is \nthe Y intercept)\n\nSlope m = (y2 - y1) / (x2 - x1)\nY intercept  b = y - mx\n\nPlugging it all together for our example:\n\nm = (915.24 - 618.93) / (0.917994 - 0.910191) = 37973.86\nb = 915.24 - (37973.86 * 0.917994) = -33944.5\n\nfor 700W (y), our efficiency (x) would then be:\n\nx = (700 - (-33944.5)) / 37973.86 = 0.912326 = 91%\n\nPowerIn = 700W /0.912326 = 767.26W ")
jnxPsuOutletPowerConsumed = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 58, 1, 2, 4, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxPsuOutletPowerConsumed.setDescription("Power Consumed by each outlet units in Watts.")
jnxPsuFpcPowerTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 58, 1, 2, 5))
if mibBuilder.loadTexts: jnxPsuFpcPowerTable.setDescription("A list of entries for each FPC(Flexible PIC Concentrator)\ngiving it's assigned priority and power being allocated. \nMore information on FPCs can be found in JUNIPER-MIB.")
jnxPsuFpcPowerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 58, 1, 2, 5, 1)).setIndexNames((0, "JUNIPER-MIB", "jnxContentsContainerIndex"), (0, "JUNIPER-MIB", "jnxContentsL1Index"), (0, "JUNIPER-MIB", "jnxContentsL2Index"), (0, "JUNIPER-MIB", "jnxContentsL3Index"))
if mibBuilder.loadTexts: jnxPsuFpcPowerEntry.setDescription("A value contained within the FpcPowerEntry")
jnxPsuFpcPowerPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 58, 1, 2, 5, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxPsuFpcPowerPriority.setDescription("The Power budget priority assigned to the FPC.\nLower number means higher priority.")
jnxPsuFpcPowerAllocated = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 58, 1, 2, 5, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxPsuFpcPowerAllocated.setDescription("The Power allocated to the FPC in Watts.")

# Augmentions

# Exports

# Module identity
mibBuilder.exportSymbols("JUNIPER-POWER-SUPPLY-UNIT-MIB", PYSNMP_MODULE_ID=jnxPsuMIB)

# Objects
mibBuilder.exportSymbols("JUNIPER-POWER-SUPPLY-UNIT-MIB", jnxPsuMIB=jnxPsuMIB, jnxPsuNotifications=jnxPsuNotifications, jnxPsuObjects=jnxPsuObjects, jnxPsuScalars=jnxPsuScalars, jnxPsuAvailableDeviceCount=jnxPsuAvailableDeviceCount, jnxPsuAvailableAveragePowerSupply=jnxPsuAvailableAveragePowerSupply, jnxPsuAvailableMaxPowerSupply=jnxPsuAvailableMaxPowerSupply, jnxPsuRedundancy=jnxPsuRedundancy, jnxPsuChassisPowerReserved=jnxPsuChassisPowerReserved, jnxPsuChassisPowerAllocated=jnxPsuChassisPowerAllocated, jnxPsuRedundantPowerAvailable=jnxPsuRedundantPowerAvailable, jnxPsuTotalPowerAvailable=jnxPsuTotalPowerAvailable, jnxPsuChassisPowerConsumed=jnxPsuChassisPowerConsumed, jnxPsuTemperatureInflow=jnxPsuTemperatureInflow, jnxPsuTemperatureOutflow=jnxPsuTemperatureOutflow, jnxPsuTemperatureInflowSamples=jnxPsuTemperatureInflowSamples, jnxPsuTemperatureOutflowSamples=jnxPsuTemperatureOutflowSamples, jnxPsuTable=jnxPsuTable, jnxPsuEntry=jnxPsuEntry, jnxPsuAvgPower=jnxPsuAvgPower, jnxPsuMaxPower=jnxPsuMaxPower, jnxPsuMode=jnxPsuMode, jnxPsuOutletCount=jnxPsuOutletCount, jnxPsuEnvironmentTable=jnxPsuEnvironmentTable, jnxPsuEnvironmentEntry=jnxPsuEnvironmentEntry, jnxPsuThermalValue=jnxPsuThermalValue, jnxPsuHumidityValue=jnxPsuHumidityValue, jnxPsuOutletTable=jnxPsuOutletTable, jnxPsuOutletEntry=jnxPsuOutletEntry, jnxPsuOutletName=jnxPsuOutletName, jnxPsuOutletDescription=jnxPsuOutletDescription, jnxPsuOutletAvgPower=jnxPsuOutletAvgPower, jnxPsuOutletMaxPower=jnxPsuOutletMaxPower, jnxPsuOutletCurrent=jnxPsuOutletCurrent, jnxPsuOutletStatus=jnxPsuOutletStatus, jnxPsuOutletVoltage=jnxPsuOutletVoltage, jnxPsuOutletPowerFactorValue=jnxPsuOutletPowerFactorValue, jnxPsuOutletPowerConsumed=jnxPsuOutletPowerConsumed, jnxPsuFpcPowerTable=jnxPsuFpcPowerTable, jnxPsuFpcPowerEntry=jnxPsuFpcPowerEntry, jnxPsuFpcPowerPriority=jnxPsuFpcPowerPriority, jnxPsuFpcPowerAllocated=jnxPsuFpcPowerAllocated)

