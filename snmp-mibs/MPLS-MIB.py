# PySNMP SMI module. Autogenerated from smidump -f python MPLS-MIB
# by libsmi2pysnmp-0.1.3 at Thu May 22 11:57:54 2014,
# Python version sys.version_info(major=2, minor=7, micro=2, releaselevel='final', serial=0)

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
( jnxMibs, ) = mibBuilder.importSymbols("JUNIPER-SMI", "jnxMibs")
( Bits, Counter32, Counter64, Integer32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Integer32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks")
( DisplayString, TimeStamp, ) = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TimeStamp")

# Objects

mpls = ModuleIdentity((1, 3, 6, 1, 4, 1, 2636, 3, 2)).setRevisions(("2009-02-23 14:45",))
if mibBuilder.loadTexts: mpls.setOrganization("Juniper Networks, Inc.")
if mibBuilder.loadTexts: mpls.setContactInfo("        Juniper Technical Assistance Center\nJuniper Networks, Inc.\n1194 N. Mathilda Avenue\nSunnyvale, CA 94089\nE-mail: support@juniper.net")
if mibBuilder.loadTexts: mpls.setDescription("The MIB module for Multi-Protocol Label Switched Paths.")
mplsLspTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 2, 0))
mplsInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 2, 1))
mplsVersion = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsVersion.setDescription("MPLS version number.")
mplsSignalingProto = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 2, 1, 2), Integer().subtype(subtypeSpec=SingleValueConstraint(4,3,1,2,)).subtype(namedValues=NamedValues(("none", 1), ("other", 2), ("rsvp", 3), ("ldp", 4), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsSignalingProto.setDescription("MPLS signaling protocol.")
mplsConfiguredLsps = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsConfiguredLsps.setDescription("Number of configured LSPs.")
mplsActiveLsps = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 2, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsActiveLsps.setDescription("Number of active LSPs.")
mplsTEInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 2, 2))
mplsTEDistProtocol = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 2, 2, 1), Integer().subtype(subtypeSpec=SingleValueConstraint(3,1,2,4,)).subtype(namedValues=NamedValues(("none", 1), ("isis", 2), ("ospf", 3), ("isis-ospf", 4), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsTEDistProtocol.setDescription("IGP used to distribute Traffic Engineering\ninformation and topology to each LSR for the\npurpose of automatic path computation.")
mplsAdminGroupList = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 2, 2, 2))
if mibBuilder.loadTexts: mplsAdminGroupList.setDescription("List of configured administrative groups.\nAdministrative groups are used to label links in\nthe Traffic Engineering topology in order to place\nconstraints (include and exclude) on LSP paths.")
mplsAdminGroup = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 2, 2, 2, 1)).setIndexNames((0, "MPLS-MIB", "mplsAdminGroupNumber"))
if mibBuilder.loadTexts: mplsAdminGroup.setDescription("A mapping between a configured group number and its\nhuman-readable name.  The group number should be\nbetween 0 and 31, inclusive.")
mplsAdminGroupNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 2, 2, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 31))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsAdminGroupNumber.setDescription("Index of the administrative group.")
mplsAdminGroupName = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 2, 2, 2, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsAdminGroupName.setDescription("Name of the administrative group.")
mplsLspList = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 2, 3))
if mibBuilder.loadTexts: mplsLspList.setDescription("******* Deprecated Object ******\nList of Configured Label Switched Paths. This object\nhas been deprecated and replaced by mplsLspInfoList")
mplsLspEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 2, 3, 1)).setIndexNames((0, "MPLS-MIB", "mplsLspName"))
if mibBuilder.loadTexts: mplsLspEntry.setDescription("******* Deprecated Object ******\nEntry containing information about a particular\nLabel Switched Path. This object has been deprecated \nand replaced by mplsLspInfoEntry")
mplsLspName = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 2, 3, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(32, 32)).setFixedLength(32)).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsLspName.setDescription("******* Deprecated Object ******\nName of the Label Switched Path.\nThis object has been deprecated and replaced by \nmplsLspInfoName")
mplsLspState = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 2, 3, 1, 2), Integer().subtype(subtypeSpec=SingleValueConstraint(5,1,2,4,3,)).subtype(namedValues=NamedValues(("unknown", 1), ("up", 2), ("down", 3), ("notInService", 4), ("backupActive", 5), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsLspState.setDescription("The operational state of the LSP.")
mplsLspOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 2, 3, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsLspOctets.setDescription("The number of octets that have been forwarded\nover current LSP active path. The number reported\nis not realtime, may subject to several minutes\ndelay.  The delay is controllable by mpls statistics\ngathering interval, which by default is once every\n5 minutes.  If mpls statistics gathering is not\nenabled, this number will not increment.")
mplsLspPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 2, 3, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsLspPackets.setDescription("The number of packets that have been forwarded\nover current LSP active path. The number reported\nis not realtime, may subject to several minutes\ndelay.  The delay is controllable by mpls statistics\ngathering interval, which by default is once every\n5 minutes.  If mpls statistics gathering is not\nenabled, this number will not increment.")
mplsLspAge = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 2, 3, 1, 5), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsLspAge.setDescription("The age (i.e., time from creation till now) of\nthis LSP in 10-millisecond periods.")
mplsLspTimeUp = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 2, 3, 1, 6), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsLspTimeUp.setDescription("The total time in 10-millisecond units that this\nLSP has been operational.  For example, the\npercentage up time can be determined by computing\n(mplsLspTimeUp/mplsLspAge * 100 %).")
mplsLspPrimaryTimeUp = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 2, 3, 1, 7), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsLspPrimaryTimeUp.setDescription("The total time in 10-millisecond units that this\nLSP's primary path has been operational.  For\nexample, the percentage contribution of the primary\npath to the operational time is given by\n(mplsLspPrimaryTimeUp/mplsLspTimeUp * 100) %.")
mplsLspTransitions = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 2, 3, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsLspTransitions.setDescription("The number of state transitions (up -> down and\ndown -> up) this LSP has undergone.")
mplsLspLastTransition = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 2, 3, 1, 9), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsLspLastTransition.setDescription("The time in 10-millisecond units since the last\ntransition occurred on this LSP.")
mplsLspPathChanges = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 2, 3, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsLspPathChanges.setDescription("The number of path changes this LSP has had. For\nevery path change (path down, path up, path change),\na corresponding syslog/trap (if enabled) is generated \nfor it.")
mplsLspLastPathChange = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 2, 3, 1, 11), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsLspLastPathChange.setDescription("The time in 10-millisecond units since the last\nchange occurred on this LSP.")
mplsLspConfiguredPaths = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 2, 3, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsLspConfiguredPaths.setDescription("The number of paths configured for this LSP.")
mplsLspStandbyPaths = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 2, 3, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsLspStandbyPaths.setDescription("The number of standby paths configured for\nthis LSP.")
mplsLspOperationalPaths = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 2, 3, 1, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsLspOperationalPaths.setDescription("The number of operational paths for this LSP.\nThis includes the path currently active, as\nwell as operational standby paths.")
mplsLspFrom = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 2, 3, 1, 15), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsLspFrom.setDescription("Source IP address of this LSP.")
mplsLspTo = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 2, 3, 1, 16), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsLspTo.setDescription("Destination IP address of this LSP.")
mplsPathName = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 2, 3, 1, 17), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsPathName.setDescription("The name of the active path for this LSP, if\nany.  If there is none, the name should be\nempty; in that case, the rest of the fields\nin mplsLspEntry are meaningless.")
mplsPathType = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 2, 3, 1, 18), Integer().subtype(subtypeSpec=SingleValueConstraint(3,2,1,5,4,)).subtype(namedValues=NamedValues(("other", 1), ("primary", 2), ("standby", 3), ("secondary", 4), ("bypass", 5), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsPathType.setDescription("The type of path that is active, i.e., a\nprimary path, a standby path, a generic\nsecondary path, or a bypass path.\nThe value other, primary, standby and\nsecondary apply to data LSPs, and are\nmeaningful only if mplsPathName is not\nempty. The value bypass applies to\nbypass tunnels. A bypass tunnel\nmay have an empty mplsPathName.")
mplsPathExplicitRoute = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 2, 3, 1, 19), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 1024))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsPathExplicitRoute.setDescription("The explicit route used to set up this LSP.\nThis may either be the route configured by\nthe user, or a route automatically computed\nto satisfy constraints set by the user. \n This field is a displayable string in the\n format of XXX.XXX.XXX.XXX <space> S/L <newline>\n repeated for each explicit address. The S/L character\n stands for Strict/Loose route.\n This field is meaningless unless mplsPathName \n is not empty")
mplsPathRecordRoute = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 2, 3, 1, 20), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 1024))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsPathRecordRoute.setDescription("The route actually used for this path, as\nrecorded by the signaling protocol. \n This field is a displayable string in the\n format of XXX.XXX.XXX.XXX <space> \n repeated for each address. \n This field is meaningless unless mplsPathName is \n not empty")
mplsPathBandwidth = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 2, 3, 1, 21), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsPathBandwidth.setDescription("The configured bandwidth for this LSP, in units\nof thousands of bits per second (Kbps). This \n field is meaningless unless mplsPathName is not empty")
mplsPathCOS = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 2, 3, 1, 22), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0,7),ValueRangeConstraint(255,255),))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsPathCOS.setDescription("The configured Class Of Service on this path.  If\nthe value is between 0 and 7 inclusive, this value\nwill be inserted in the 3 bit COS field in the\nlabel.  If the value is 255, the value in the COS\nfield of the label will depend on other factors. \n This field is meaningless unless mplsPathName is not empty")
mplsPathInclude = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 2, 3, 1, 23), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsPathInclude.setDescription("This is a configured set of colors (administrative\ngroups) specified as a bit vector (i.e., bit n is 1\nif color n is in the set, where n = 0 is the LSB).\nFor each link that this path goes through, the\nlink MUST have colors associated with it, and\nthe intersection of the link's colors and the\n'include' set MUST be non-null. This field is meaningless\n unless mplsPathName is not empty")
mplsPathExclude = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 2, 3, 1, 24), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsPathExclude.setDescription("This is a configured set of colors (administrative\ngroups) specified as a bit vector (i.e., bit n is 1\nif color n is in the set, where n = 0 is the LSB).\nFor each link that this path goes through, the\nlink MUST have colors associated with it, and\nthe intersection of the link's colors and the\n'exclude' set MUST be null. This field is meaningless\n unless mplsPathName is not empty")
mplsPathSetupPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 2, 3, 1, 25), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsPathSetupPriority.setDescription("The setup priority configured for this path. This \nfield is meaningless unless mplsPathName is not empty")
mplsPathHoldPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 2, 3, 1, 26), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsPathHoldPriority.setDescription("The hold priority configured for this path. This \nfield is meaningless unless mplsPathName is not empty")
mplsPathProperties = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 2, 3, 1, 27), Integer().subtype(subtypeSpec=SingleValueConstraint(16,32,64,8,4,2,1,)).subtype(namedValues=NamedValues(("record-route", 1), ("preemptable", 16), ("adaptive", 2), ("preemptive", 32), ("cspf", 4), ("fast-reroute", 64), ("mergeable", 8), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsPathProperties.setDescription("The set of configured properties for this path,\nexpressed as a bit map.  For example, if the path\nis an adaptive path, the bit corresponding to bit\nvalue xxx is set. This field is meaningless\n unless mplsPathName is not empty")
mplsTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 2, 4))
mplsLspInfoList = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 2, 5))
if mibBuilder.loadTexts: mplsLspInfoList.setDescription("List of Configured Label Switched Paths.")
mplsLspInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 2, 5, 1)).setIndexNames((1, "MPLS-MIB", "mplsLspInfoName"))
if mibBuilder.loadTexts: mplsLspInfoEntry.setDescription("Entry containing information about a particular\nLabel Switched Path.")
mplsLspInfoName = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 2, 5, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("notifyonly")
if mibBuilder.loadTexts: mplsLspInfoName.setDescription("Name of the Label Switched Path.")
mplsLspInfoState = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 2, 5, 1, 2), Integer().subtype(subtypeSpec=SingleValueConstraint(5,1,2,4,3,)).subtype(namedValues=NamedValues(("unknown", 1), ("up", 2), ("down", 3), ("notInService", 4), ("backupActive", 5), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsLspInfoState.setDescription("The operational state of the LSP.")
mplsLspInfoOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 2, 5, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsLspInfoOctets.setDescription("The number of octets that have been forwarded\nover current LSP active path. The number reported\nis not realtime, may subject to several minutes\ndelay.  The delay is controllable by mpls statistics\ngathering interval, which by default is once every\n5 minutes.  If mpls statistics gathering is not\nenabled, this number will not increment.")
mplsLspInfoPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 2, 5, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsLspInfoPackets.setDescription("The number of packets that have been forwarded\nover current LSP active path. The number reported\nis not realtime, may subject to several minutes\ndelay.  The delay is controllable by mpls statistics\ngathering interval, which by default is once every\n5 minutes.  If mpls statistics gathering is not\nenabled, this number will not increment.")
mplsLspInfoAge = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 2, 5, 1, 5), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsLspInfoAge.setDescription("The age (i.e., time from creation till now) of\nthis LSP in 10-millisecond periods.")
mplsLspInfoTimeUp = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 2, 5, 1, 6), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsLspInfoTimeUp.setDescription("The total time in 10-millisecond units that this\nLSP has been operational.  For example, the\npercentage up time can be determined by computing\n(mplsLspInfoTimeUp/mplsLspInfoAge * 100 %).")
mplsLspInfoPrimaryTimeUp = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 2, 5, 1, 7), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsLspInfoPrimaryTimeUp.setDescription("The total time in 10-millisecond units that this\nLSP's primary path has been operational.  For\nexample, the percentage contribution of the primary\npath to the operational time is given by\n(mplsLspInfoPrimaryTimeUp/mplsLspInfoTimeUp * 100) %.")
mplsLspInfoTransitions = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 2, 5, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsLspInfoTransitions.setDescription("The number of state transitions (up -> down and\ndown -> up) this LSP has undergone.")
mplsLspInfoLastTransition = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 2, 5, 1, 9), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsLspInfoLastTransition.setDescription("The time in 10-millisecond units since the last\ntransition occurred on this LSP.")
mplsLspInfoPathChanges = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 2, 5, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsLspInfoPathChanges.setDescription("The number of path changes this LSP has had. For\nevery path change (path down, path up, path change),\na corresponding syslog/trap (if enabled) is generated \nfor it.")
mplsLspInfoLastPathChange = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 2, 5, 1, 11), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsLspInfoLastPathChange.setDescription("The time in 10-millisecond units since the last\nchange occurred on this LSP.")
mplsLspInfoConfiguredPaths = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 2, 5, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsLspInfoConfiguredPaths.setDescription("The number of paths configured for this LSP.")
mplsLspInfoStandbyPaths = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 2, 5, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsLspInfoStandbyPaths.setDescription("The number of standby paths configured for\nthis LSP.")
mplsLspInfoOperationalPaths = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 2, 5, 1, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsLspInfoOperationalPaths.setDescription("The number of operational paths for this LSP.\nThis includes the path currently active, as\nwell as operational standby paths.")
mplsLspInfoFrom = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 2, 5, 1, 15), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsLspInfoFrom.setDescription("Source IP address of this LSP.")
mplsLspInfoTo = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 2, 5, 1, 16), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsLspInfoTo.setDescription("Destination IP address of this LSP.")
mplsPathInfoName = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 2, 5, 1, 17), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsPathInfoName.setDescription("The name of the active path for this LSP, if\nany.  If there is none, the name should be\nempty; in that case, the rest of the fields\nin mplsLspInfoEntry are meaningless.")
mplsPathInfoType = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 2, 5, 1, 18), Integer().subtype(subtypeSpec=SingleValueConstraint(3,2,1,5,4,)).subtype(namedValues=NamedValues(("other", 1), ("primary", 2), ("standby", 3), ("secondary", 4), ("bypass", 5), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsPathInfoType.setDescription("The type of path that is active, i.e., a\nprimary path, a standby path, a generic\nsecondary path, or a bypass path.\nThe value other, primary, standby and\nsecondary apply to data LSPs, and are\nmeaningful only if mplsPathInfoName is not\nempty. The value bypass applies to\nbypass tunnels. A bypass tunnel\nmay have an empty mplsPathInfoName.")
mplsPathInfoExplicitRoute = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 2, 5, 1, 19), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 1024))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsPathInfoExplicitRoute.setDescription("The explicit route used to set up this LSP.\nThis may either be the route configured by\nthe user, or a route automatically computed\nto satisfy constraints set by the user. \n This field is a displayable string in the\n format of XXX.XXX.XXX.XXX <space> S/L <newline>\n repeated for each explicit address. The S/L character\n stands for Strict/Loose route.\n This field is meaningless unless mplsPathInfoName \n is not empty")
mplsPathInfoRecordRoute = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 2, 5, 1, 20), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 1024))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsPathInfoRecordRoute.setDescription("The route actually used for this path, as\nrecorded by the signaling protocol. \n This field is a displayable string in the\n format of XXX.XXX.XXX.XXX <space> \n repeated for each address. \n This field is meaningless unless mplsPathInfoName is \n not empty")
mplsPathInfoBandwidth = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 2, 5, 1, 21), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsPathInfoBandwidth.setDescription("The configured bandwidth for this LSP, in units\nof thousands of bits per second (Kbps). This \n field is meaningless unless mplsPathInfoName is not empty")
mplsPathInfoCOS = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 2, 5, 1, 22), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0,7),ValueRangeConstraint(255,255),))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsPathInfoCOS.setDescription("The configured Class Of Service on this path.  If\nthe value is between 0 and 7 inclusive, this value\nwill be inserted in the 3 bit COS field in the\nlabel.  If the value is 255, the value in the COS\nfield of the label will depend on other factors. \n This field is meaningless unless mplsPathInfoName is not empty")
mplsPathInfoInclude = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 2, 5, 1, 23), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsPathInfoInclude.setDescription("This is a configured set of colors (administrative\ngroups) specified as a bit vector (i.e., bit n is 1\nif color n is in the set, where n = 0 is the LSB).\nFor each link that this path goes through, the\nlink MUST have colors associated with it, and\nthe intersection of the link's colors and the\n'include' set MUST be non-null. This field is meaningless\n unless mplsPathInfoName is not empty")
mplsPathInfoExclude = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 2, 5, 1, 24), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsPathInfoExclude.setDescription("This is a configured set of colors (administrative\ngroups) specified as a bit vector (i.e., bit n is 1\nif color n is in the set, where n = 0 is the LSB).\nFor each link that this path goes through, the\nlink MUST have colors associated with it, and\nthe intersection of the link's colors and the\n'exclude' set MUST be null. This field is meaningless\n unless mplsPathInfoName is not empty")
mplsPathInfoSetupPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 2, 5, 1, 25), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsPathInfoSetupPriority.setDescription("The setup priority configured for this path. This \nfield is meaningless unless mplsPathInfoName is not empty")
mplsPathInfoHoldPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 2, 5, 1, 26), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsPathInfoHoldPriority.setDescription("The hold priority configured for this path. This \nfield is meaningless unless mplsPathInfoName is not empty")
mplsPathInfoProperties = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 2, 5, 1, 27), Integer().subtype(subtypeSpec=SingleValueConstraint(16,32,64,8,4,2,1,)).subtype(namedValues=NamedValues(("record-route", 1), ("preemptable", 16), ("adaptive", 2), ("preemptive", 32), ("cspf", 4), ("fast-reroute", 64), ("mergeable", 8), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsPathInfoProperties.setDescription("The set of configured properties for this path,\nexpressed as a bit map.  For example, if the path\nis an adaptive path, the bit corresponding to bit\nvalue xxx is set. This field is meaningless\n unless mplsPathInfoName is not empty")
mplsLspInfoAggrOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 2, 5, 1, 28), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsLspInfoAggrOctets.setDescription("The number of octets that have beeen forwarded over\ncurrent LSP. This is an aggregate count of octets\nforwarded over all LSP instances from the time\nLSP was up. The number reported is not realtime, may\nbe subject to several minutes delay.  The delay is\ncontrollable by mpls statistics gathering interval,\nwhich by default is once every 5 minutes.  If mpls\nstatistics gathering is not enabled, this number will\nnot increment.")
mplsLspInfoAggrPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 2, 5, 1, 29), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsLspInfoAggrPackets.setDescription("The number of packets that have been forwarded over\ncurrent LSP. This is an aggregate count of packets\nforwarded over all LSP instances from the time\nLSP was up. The number reported is not realtime, may\nbe subject to several minutes delay. The delay is\ncontrollable by mpls statistics gathering interval,\nwhich by default is once every 5 minutes. If mpls\nstatistics gathering is not enabled, this number will\nnot increment.")
mplsPathInfoRecordRouteWithLabels = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 2, 5, 1, 30), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 1024))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsPathInfoRecordRouteWithLabels.setDescription("The route actually used for this path, as\nrecorded by the signaling protocol.\nThis field is a displayable string in the\nformat of XXX.XXX.XXX.XXX <flag/label> <space>\nrepeated for each address.\nThis field is meaningless unless mplsPathInfoName is\nnot empty")

# Augmentions

# Notifications

mplsLspInfoUp = NotificationType((1, 3, 6, 1, 4, 1, 2636, 3, 2, 0, 1)).setObjects(*(("MPLS-MIB", "mplsPathInfoName"), ("MPLS-MIB", "mplsLspInfoName"), ) )
if mibBuilder.loadTexts: mplsLspInfoUp.setDescription("An mplsLspInfoUp trap signifies that the \nspecified LSP is up. The current active\npath for the LSP is mplsPathInfoName.")
mplsLspInfoDown = NotificationType((1, 3, 6, 1, 4, 1, 2636, 3, 2, 0, 2)).setObjects(*(("MPLS-MIB", "mplsPathInfoName"), ("MPLS-MIB", "mplsLspInfoName"), ) )
if mibBuilder.loadTexts: mplsLspInfoDown.setDescription("An mplsLspInfoDown trap signifies that the \nspecified LSP is down, because the current\nactive path mplsPathInfoName went down.")
mplsLspInfoChange = NotificationType((1, 3, 6, 1, 4, 1, 2636, 3, 2, 0, 3)).setObjects(*(("MPLS-MIB", "mplsPathInfoName"), ("MPLS-MIB", "mplsLspInfoName"), ) )
if mibBuilder.loadTexts: mplsLspInfoChange.setDescription("An mplsLspInfoChange trap signifies that the\nthe specified LSP has switched traffic to \n	the new active path 'toLspPath'. The LSP maintains\n	up state before and after the switch over")
mplsLspInfoPathDown = NotificationType((1, 3, 6, 1, 4, 1, 2636, 3, 2, 0, 4)).setObjects(*(("MPLS-MIB", "mplsPathInfoName"), ("MPLS-MIB", "mplsLspInfoName"), ) )
if mibBuilder.loadTexts: mplsLspInfoPathDown.setDescription("An mplsLspInfoPathDown trap signifies that the \nspecified path mplsPathName for the specified\nLSP mplsLspInfoName went down")
mplsLspInfoPathUp = NotificationType((1, 3, 6, 1, 4, 1, 2636, 3, 2, 0, 5)).setObjects(*(("MPLS-MIB", "mplsPathInfoName"), ("MPLS-MIB", "mplsLspInfoName"), ) )
if mibBuilder.loadTexts: mplsLspInfoPathUp.setDescription("An mplsLspInfoPathUp trap signifies that the \nspecified path mplsPathName for the specified\nLSP mplsLspInfoName came up")
mplsLspUp = NotificationType((1, 3, 6, 1, 4, 1, 2636, 3, 2, 4, 1)).setObjects(*(("MPLS-MIB", "mplsPathName"), ("MPLS-MIB", "mplsLspName"), ) )
if mibBuilder.loadTexts: mplsLspUp.setDescription("An mplsLspUp trap signifies that the \nspecified LSP is up. The current active\npath for the LSP is mplsPathName.")
mplsLspDown = NotificationType((1, 3, 6, 1, 4, 1, 2636, 3, 2, 4, 2)).setObjects(*(("MPLS-MIB", "mplsPathName"), ("MPLS-MIB", "mplsLspName"), ) )
if mibBuilder.loadTexts: mplsLspDown.setDescription("An mplsLspDown trap signifies that the \nspecified LSP is down, because the current\nactive path mplsPathName went down.")
mplsLspChange = NotificationType((1, 3, 6, 1, 4, 1, 2636, 3, 2, 4, 3)).setObjects(*(("MPLS-MIB", "mplsPathName"), ("MPLS-MIB", "mplsLspName"), ) )
if mibBuilder.loadTexts: mplsLspChange.setDescription("An mplsLspChange trap signifies that the\nthe specified LSP has switched traffic to \n	the new active path 'toLspPath'. The LSP maintains\n	up state before and after the switch over")
mplsLspPathDown = NotificationType((1, 3, 6, 1, 4, 1, 2636, 3, 2, 4, 4)).setObjects(*(("MPLS-MIB", "mplsPathName"), ("MPLS-MIB", "mplsLspName"), ) )
if mibBuilder.loadTexts: mplsLspPathDown.setDescription("An mplsLspPathDown trap signifies that the \nspecified path mplsPathName for the specified\nLSP mplsLspName went down")
mplsLspPathUp = NotificationType((1, 3, 6, 1, 4, 1, 2636, 3, 2, 4, 5)).setObjects(*(("MPLS-MIB", "mplsPathName"), ("MPLS-MIB", "mplsLspName"), ) )
if mibBuilder.loadTexts: mplsLspPathUp.setDescription("An mplsLspPathUp trap signifies that the \nspecified path mplsPathName for the specified\nLSP mplsLspName came up")

# Exports

# Module identity
mibBuilder.exportSymbols("MPLS-MIB", PYSNMP_MODULE_ID=mpls)

# Objects
mibBuilder.exportSymbols("MPLS-MIB", mpls=mpls, mplsLspTraps=mplsLspTraps, mplsInfo=mplsInfo, mplsVersion=mplsVersion, mplsSignalingProto=mplsSignalingProto, mplsConfiguredLsps=mplsConfiguredLsps, mplsActiveLsps=mplsActiveLsps, mplsTEInfo=mplsTEInfo, mplsTEDistProtocol=mplsTEDistProtocol, mplsAdminGroupList=mplsAdminGroupList, mplsAdminGroup=mplsAdminGroup, mplsAdminGroupNumber=mplsAdminGroupNumber, mplsAdminGroupName=mplsAdminGroupName, mplsLspList=mplsLspList, mplsLspEntry=mplsLspEntry, mplsLspName=mplsLspName, mplsLspState=mplsLspState, mplsLspOctets=mplsLspOctets, mplsLspPackets=mplsLspPackets, mplsLspAge=mplsLspAge, mplsLspTimeUp=mplsLspTimeUp, mplsLspPrimaryTimeUp=mplsLspPrimaryTimeUp, mplsLspTransitions=mplsLspTransitions, mplsLspLastTransition=mplsLspLastTransition, mplsLspPathChanges=mplsLspPathChanges, mplsLspLastPathChange=mplsLspLastPathChange, mplsLspConfiguredPaths=mplsLspConfiguredPaths, mplsLspStandbyPaths=mplsLspStandbyPaths, mplsLspOperationalPaths=mplsLspOperationalPaths, mplsLspFrom=mplsLspFrom, mplsLspTo=mplsLspTo, mplsPathName=mplsPathName, mplsPathType=mplsPathType, mplsPathExplicitRoute=mplsPathExplicitRoute, mplsPathRecordRoute=mplsPathRecordRoute, mplsPathBandwidth=mplsPathBandwidth, mplsPathCOS=mplsPathCOS, mplsPathInclude=mplsPathInclude, mplsPathExclude=mplsPathExclude, mplsPathSetupPriority=mplsPathSetupPriority, mplsPathHoldPriority=mplsPathHoldPriority, mplsPathProperties=mplsPathProperties, mplsTraps=mplsTraps, mplsLspInfoList=mplsLspInfoList, mplsLspInfoEntry=mplsLspInfoEntry, mplsLspInfoName=mplsLspInfoName, mplsLspInfoState=mplsLspInfoState, mplsLspInfoOctets=mplsLspInfoOctets, mplsLspInfoPackets=mplsLspInfoPackets, mplsLspInfoAge=mplsLspInfoAge, mplsLspInfoTimeUp=mplsLspInfoTimeUp, mplsLspInfoPrimaryTimeUp=mplsLspInfoPrimaryTimeUp, mplsLspInfoTransitions=mplsLspInfoTransitions, mplsLspInfoLastTransition=mplsLspInfoLastTransition, mplsLspInfoPathChanges=mplsLspInfoPathChanges, mplsLspInfoLastPathChange=mplsLspInfoLastPathChange, mplsLspInfoConfiguredPaths=mplsLspInfoConfiguredPaths, mplsLspInfoStandbyPaths=mplsLspInfoStandbyPaths, mplsLspInfoOperationalPaths=mplsLspInfoOperationalPaths, mplsLspInfoFrom=mplsLspInfoFrom, mplsLspInfoTo=mplsLspInfoTo, mplsPathInfoName=mplsPathInfoName, mplsPathInfoType=mplsPathInfoType, mplsPathInfoExplicitRoute=mplsPathInfoExplicitRoute, mplsPathInfoRecordRoute=mplsPathInfoRecordRoute, mplsPathInfoBandwidth=mplsPathInfoBandwidth, mplsPathInfoCOS=mplsPathInfoCOS, mplsPathInfoInclude=mplsPathInfoInclude, mplsPathInfoExclude=mplsPathInfoExclude, mplsPathInfoSetupPriority=mplsPathInfoSetupPriority, mplsPathInfoHoldPriority=mplsPathInfoHoldPriority, mplsPathInfoProperties=mplsPathInfoProperties, mplsLspInfoAggrOctets=mplsLspInfoAggrOctets, mplsLspInfoAggrPackets=mplsLspInfoAggrPackets, mplsPathInfoRecordRouteWithLabels=mplsPathInfoRecordRouteWithLabels)

# Notifications
mibBuilder.exportSymbols("MPLS-MIB", mplsLspInfoUp=mplsLspInfoUp, mplsLspInfoDown=mplsLspInfoDown, mplsLspInfoChange=mplsLspInfoChange, mplsLspInfoPathDown=mplsLspInfoPathDown, mplsLspInfoPathUp=mplsLspInfoPathUp, mplsLspUp=mplsLspUp, mplsLspDown=mplsLspDown, mplsLspChange=mplsLspChange, mplsLspPathDown=mplsLspPathDown, mplsLspPathUp=mplsLspPathUp)

