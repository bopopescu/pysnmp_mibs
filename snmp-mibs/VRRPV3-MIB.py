# PySNMP SMI module. Autogenerated from smidump -f python VRRPV3-MIB
# by libsmi2pysnmp-0.1.3 at Thu May 22 11:58:03 2014,
# Python version sys.version_info(major=2, minor=7, micro=2, releaselevel='final', serial=0)

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
( ifIndex, ) = mibBuilder.importSymbols("IF-MIB", "ifIndex")
( InetAddress, InetAddressType, ) = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType")
( ModuleCompliance, NotificationGroup, ObjectGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
( Bits, Counter32, Counter64, Integer32, Integer32, ModuleIdentity, MibIdentifier, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, TimeTicks, Unsigned32, mib_2, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Integer32", "Integer32", "ModuleIdentity", "MibIdentifier", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "TimeTicks", "Unsigned32", "mib-2")
( MacAddress, RowStatus, TextualConvention, TimeInterval, TimeStamp, TruthValue, ) = mibBuilder.importSymbols("SNMPv2-TC", "MacAddress", "RowStatus", "TextualConvention", "TimeInterval", "TimeStamp", "TruthValue")

# Types

class Vrrpv3VrIdTC(TextualConvention, Integer32):
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec+ValueRangeConstraint(1,255)
    

# Objects

vrrpv3MIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 207)).setRevisions(("2012-02-13 00:00","2012-02-12 00:00",))
if mibBuilder.loadTexts: vrrpv3MIB.setOrganization("IETF VRRP Working Group")
if mibBuilder.loadTexts: vrrpv3MIB.setContactInfo("WG E-Mail: vrrp@ietf.org \n\nEditor:    Kalyan Tata   \n           Nokia\n           313 Fairchild Dr,\n           Mountain View, CA 94043\n           Tata_kalyan@yahoo.com")
if mibBuilder.loadTexts: vrrpv3MIB.setDescription("This MIB describes objects used for managing Virtual  \nRouter Redundancy Protocol version 3 (VRRPv3).  \n\nCopyright (c) 2012 IETF Trust and the persons\nidentified as authors of the code.  All rights\nreserved.\n\nRedistribution and use in source and binary forms,\nwith or without modification, is permitted pursuant\nto, and subject to the license terms contained in,\nthe Simplified BSD License set forth in Section\n4.c of the IETF Trust's Legal Provisions Relating\nto IETF Documents\n(http://trustee.ietf.org/license-info).\n\nThis version of the MIB module is part of RFC 6527.\nPlease see the RFC for full legal notices.")
vrrpv3Notifications = MibIdentifier((1, 3, 6, 1, 2, 1, 207, 0))
vrrpv3Objects = MibIdentifier((1, 3, 6, 1, 2, 1, 207, 1))
vrrpv3Operations = MibIdentifier((1, 3, 6, 1, 2, 1, 207, 1, 1))
vrrpv3OperationsTable = MibTable((1, 3, 6, 1, 2, 1, 207, 1, 1, 1))
if mibBuilder.loadTexts: vrrpv3OperationsTable.setDescription("Unified Operations table for a VRRP router that\nconsists of a sequence (i.e., one or more conceptual \nrows) of 'vrrpv3OperationsEntry' items each of which  \ndescribe the operational characteristics of a virtual \nrouter.")
vrrpv3OperationsEntry = MibTableRow((1, 3, 6, 1, 2, 1, 207, 1, 1, 1, 1)).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "VRRPV3-MIB", "vrrpv3OperationsVrId"), (0, "VRRPV3-MIB", "vrrpv3OperationsInetAddrType"))
if mibBuilder.loadTexts: vrrpv3OperationsEntry.setDescription("An entry in the vrrpv3OperationsTable containing the   \noperational characteristics of a virtual router.\nOn a VRRP router, a given virtual router is\nidentified by a combination of ifIndex, VRID, and\nthe IP version.  ifIndex represents an interface of\nthe router.\n\nA row must be created with vrrpv3OperationsStatus \nset to initialize(1) and cannot transition to \nbackup(2) or main(3) until\nvrrpv3OperationsRowStatus is transitioned to\nactive(1).\n\nThe information in this table is persistent and when  \nwritten the entity SHOULD save the change to non- \nvolatile storage.")
vrrpv3OperationsVrId = MibTableColumn((1, 3, 6, 1, 2, 1, 207, 1, 1, 1, 1, 1), Vrrpv3VrIdTC()).setMaxAccess("noaccess")
if mibBuilder.loadTexts: vrrpv3OperationsVrId.setDescription("This object contains the Virtual Router Identifier  \n(VRID).")
vrrpv3OperationsInetAddrType = MibTableColumn((1, 3, 6, 1, 2, 1, 207, 1, 1, 1, 1, 2), InetAddressType()).setMaxAccess("noaccess")
if mibBuilder.loadTexts: vrrpv3OperationsInetAddrType.setDescription("The IP address type of Vrrpv3OperationsEntry and  \nVrrpv3AssociatedIpAddrEntry.  This value determines  \nthe type for vrrpv3OperationsMainIpAddr,  \nvrrpv3OperationsPrimaryIpAddr, and  \nvrrpv3AssociatedIpAddrAddress.  \n\nipv4(1) and ipv6(2) are the only two values supported  \nin this MIB module.")
vrrpv3OperationsMainIpAddr = MibTableColumn((1, 3, 6, 1, 2, 1, 207, 1, 1, 1, 1, 3), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrrpv3OperationsMainIpAddr.setDescription("The main router's real IP address.  The main router  \nwould set this address to vrrpv3OperationsPrimaryIpAddr  \nwhile transitioning to main state.  For backup  \nrouters, this is the IP address listed as the source in \nVRRP advertisement last received by this virtual  \nrouter.")
vrrpv3OperationsPrimaryIpAddr = MibTableColumn((1, 3, 6, 1, 2, 1, 207, 1, 1, 1, 1, 4), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vrrpv3OperationsPrimaryIpAddr.setDescription("In the case where there is more than one IP  \nAddress (associated IP addresses) for a given  \n'ifIndex', this object is used to specify the IP  \naddress that will become the \nvrrpv3OperationsMainIpAddr', should the virtual  \nrouter transition from backup state to main.")
vrrpv3OperationsVirtualMacAddr = MibTableColumn((1, 3, 6, 1, 2, 1, 207, 1, 1, 1, 1, 5), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrrpv3OperationsVirtualMacAddr.setDescription("The virtual MAC address of the virtual router.  \nAlthough this object can be derived from the  \n'vrrpv3OperationsVrId' object, it is defined so that it  \nis easily obtainable by a management application and  \ncan be included in VRRP-related SNMP notifications.")
vrrpv3OperationsStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 207, 1, 1, 1, 1, 6), Integer().subtype(subtypeSpec=SingleValueConstraint(1,3,2,)).subtype(namedValues=NamedValues(("initialize", 1), ("backup", 2), ("main", 3), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrrpv3OperationsStatus.setDescription("The current state of the virtual router.  This object   \nhas three defined values:  \n\n  - 'initialize', which indicates that the  \n    virtual router is waiting for a startup event.  \n\n  - 'backup', which indicates that the virtual router is  \n    monitoring the availability of the main router.  \n\n  - 'main', which indicates that the virtual router  \n    is forwarding packets for IP addresses that are  \n    associated with this router.")
vrrpv3OperationsPriority = MibTableColumn((1, 3, 6, 1, 2, 1, 207, 1, 1, 1, 1, 7), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 255)).clone(100)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vrrpv3OperationsPriority.setDescription("This object specifies the priority to be used for the  \nvirtual router main election process; higher values  \nimply higher priority.  \n\nA priority of '0', although not settable, is sent by  \nthe main router to indicate that this router has  \nceased to participate in VRRP, and a backup virtual  \nrouter should transition to become a new main.  \n\nA priority of 255 is used for the router that owns the  \nassociated IP address(es) for VRRP over IPv4 and hence \nis not settable. \n\nSetting the values of this object to 0 or 255 should be\nrejected by the agents implementing this MIB module.\nFor example, an SNMP agent would return 'badValue(3)'\nwhen a user tries to set the values 0 or 255 for this\nobject.")
vrrpv3OperationsAddrCount = MibTableColumn((1, 3, 6, 1, 2, 1, 207, 1, 1, 1, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrrpv3OperationsAddrCount.setDescription("The number of IP addresses that are associated with  \nthis virtual router.  This number is equal to the  \nnumber of rows in the vrrpv3AssociatedAddrTable that  \ncorrespond to a given ifIndex/VRID/IP version.")
vrrpv3OperationsAdvInterval = MibTableColumn((1, 3, 6, 1, 2, 1, 207, 1, 1, 1, 1, 9), TimeInterval().subtype(subtypeSpec=ValueRangeConstraint(1, 4095)).clone(100)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vrrpv3OperationsAdvInterval.setDescription("The time interval, in centiseconds, between sending  \nadvertisement messages.  Only the main router sends  \nVRRP advertisements.")
vrrpv3OperationsPreemptMode = MibTableColumn((1, 3, 6, 1, 2, 1, 207, 1, 1, 1, 1, 10), TruthValue().clone('true')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vrrpv3OperationsPreemptMode.setDescription("Controls whether a higher priority virtual router will \npreempt a lower priority main.")
vrrpv3OperationsAcceptMode = MibTableColumn((1, 3, 6, 1, 2, 1, 207, 1, 1, 1, 1, 11), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vrrpv3OperationsAcceptMode.setDescription("Controls whether a virtual router in main state  \nwill accept packets addressed to the address owner's  \nIPv6 address as its own if it is not the IPv6 address  \nowner.  Default is false(2). \nThis object is not relevant for rows representing VRRP \nover IPv4 and should be set to false(2).")
vrrpv3OperationsUpTime = MibTableColumn((1, 3, 6, 1, 2, 1, 207, 1, 1, 1, 1, 12), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrrpv3OperationsUpTime.setDescription("This value represents the amount of time, in\nTimeTicks (hundredth of a second), since this virtual  \nrouter (i.e., the 'vrrpv3OperationsStatus')  \ntransitioned out of 'initialize'.")
vrrpv3OperationsRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 207, 1, 1, 1, 1, 13), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vrrpv3OperationsRowStatus.setDescription("The RowStatus variable should be used in accordance to \ninstallation and removal conventions for conceptual  \nrows. \n\nTo create a row in this table, a manager sets this  \nobject to either createAndGo(4) or createAndWait(5).  \nUntil instances of all corresponding columns are  \nappropriately configured, the value of the  \ncorresponding instance of the  \n'vrrpv3OperationsRowStatus' column will be read as  \nnotReady(3).   \nIn particular, a newly created row cannot be made  \nactive(1) until (minimally) the corresponding instance  \nof vrrpv3OperationsInetAddrType, vrrpv3OperationsVrId,  \nand vrrpv3OperationsPrimaryIpAddr has been set, and  \nthere is at least one active row in the  \n'vrrpv3AssociatedIpAddrTable' defining an associated  \nIP address. \n\nnotInService(2) should be used to administratively  \nbring the row down. \n\nA typical order of operation to add a row is: \n1. Create a row in vrrpv3OperationsTable with  \ncreateAndWait(5). \n2. Create one or more corresponding rows in \nvrrpv3AssociatedIpAddrTable. \n3. Populate the vrrpv3OperationsEntry. \n4. Set vrrpv3OperationsRowStatus to active(1). \n\nA typical order of operation to delete an entry is: \n1. Set vrrpv3OperationsRowStatus to notInService(2). \n2. Set the corresponding rows in  \nvrrpv3AssociatedIpAddrTable to destroy(6) to delete  \nthe entry.  \n3. Set vrrpv3OperationsRowStatus to destroy(6) to  \ndelete the entry.")
vrrpv3AssociatedIpAddrTable = MibTable((1, 3, 6, 1, 2, 1, 207, 1, 1, 2))
if mibBuilder.loadTexts: vrrpv3AssociatedIpAddrTable.setDescription("The table of addresses associated with each virtual  \nrouter.")
vrrpv3AssociatedIpAddrEntry = MibTableRow((1, 3, 6, 1, 2, 1, 207, 1, 1, 2, 1)).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "VRRPV3-MIB", "vrrpv3OperationsVrId"), (0, "VRRPV3-MIB", "vrrpv3OperationsInetAddrType"), (0, "VRRPV3-MIB", "vrrpv3AssociatedIpAddrAddress"))
if mibBuilder.loadTexts: vrrpv3AssociatedIpAddrEntry.setDescription("An entry in the table contains an IP address that is  \nassociated with a virtual router.  The number of rows  \nfor a given IP version, VrID, and ifIndex will equal  \nthe number of IP addresses associated (e.g., backed up)\nby the virtual router (equivalent to\n'vrrpv3OperationsIpAddrCount').  \n\nRows in the table cannot be modified unless the value  \nof 'vrrpv3OperationsStatus' for the corresponding entry\nin the vrrpv3OperationsTable has transitioned to  \ninitialize(1). \n\nThe information in this table is persistent and when  \nwritten the entity SHOULD save the change to non- \nvolatile storage.")
vrrpv3AssociatedIpAddrAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 207, 1, 1, 2, 1, 1), InetAddress().subtype(subtypeSpec=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(4,4),ValueSizeConstraint(16,16),))).setMaxAccess("noaccess")
if mibBuilder.loadTexts: vrrpv3AssociatedIpAddrAddress.setDescription("The assigned IP addresses that a virtual router is  \nresponsible for backing up. \n\nThe IP address type is determined by the value of  \nvrrpv3OperationsInetAddrType in the index of this \nrow.")
vrrpv3AssociatedIpAddrRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 207, 1, 1, 2, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vrrpv3AssociatedIpAddrRowStatus.setDescription("The row status variable, used according to  \ninstallation and removal conventions for conceptual  \nrows.  To create a row in this table, a manager sets  \nthis object to either createAndGo(4) or  \ncreateAndWait(5).  Setting this object to active(1)\nresults in the addition of an associated address for a  \nvirtual router.  Setting this object to notInService(2)\nresults in administratively bringing down the row. \n\nDestroying the entry or setting it to destroy(6)  \nremoves the associated address from the virtual router. \nThe use of other values is implementation-dependent. \n\nImplementations should not allow deletion of the last \nrow corresponding to an active row in  \nvrrpv3OperationsTable. \n\nRefer to the description of vrrpv3OperationsRowStatus\nfor typical row creation and deletion scenarios.")
vrrpv3Statistics = MibIdentifier((1, 3, 6, 1, 2, 1, 207, 1, 2))
vrrpv3RouterChecksumErrors = MibScalar((1, 3, 6, 1, 2, 1, 207, 1, 2, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrrpv3RouterChecksumErrors.setDescription("The total number of VRRP packets received with an \ninvalid VRRP checksum value. \n\nDiscontinuities in the value of this counter can occur  \nat re-initialization of the management system, and at  \nother times as indicated by the value of  \nvrrpv3GlobalStatisticsDiscontinuityTime.")
vrrpv3RouterVersionErrors = MibScalar((1, 3, 6, 1, 2, 1, 207, 1, 2, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrrpv3RouterVersionErrors.setDescription("The total number of VRRP packets received with an  \nunknown or unsupported version number. \n\nDiscontinuities in the value of this counter can occur  \nat re-initialization of the management system, and at  \nother times as indicated by the value of  \nvrrpv3GlobalStatisticsDiscontinuityTime.")
vrrpv3RouterVrIdErrors = MibScalar((1, 3, 6, 1, 2, 1, 207, 1, 2, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrrpv3RouterVrIdErrors.setDescription("The total number of VRRP packets received with a \nVRID that is not valid for any virtual router on this \nrouter. \n\nDiscontinuities in the value of this counter can occur  \nat re-initialization of the management system, and at  \nother times as indicated by the value of  \nvrrpv3GlobalStatisticsDiscontinuityTime.")
vrrpv3GlobalStatisticsDiscontinuityTime = MibScalar((1, 3, 6, 1, 2, 1, 207, 1, 2, 4), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrrpv3GlobalStatisticsDiscontinuityTime.setDescription("The value of sysUpTime on the most recent occasion at  \nwhich one of vrrpv3RouterChecksumErrors,  \nvrrpv3RouterVersionErrors, and vrrpv3RouterVrIdErrors\nsuffered a discontinuity. \n\nIf no such discontinuities have occurred since the last \nre-initialization of the local management subsystem,  \nthen this object contains a zero value.")
vrrpv3StatisticsTable = MibTable((1, 3, 6, 1, 2, 1, 207, 1, 2, 5))
if mibBuilder.loadTexts: vrrpv3StatisticsTable.setDescription("Table of virtual router statistics.")
vrrpv3StatisticsEntry = MibTableRow((1, 3, 6, 1, 2, 1, 207, 1, 2, 5, 1))
if mibBuilder.loadTexts: vrrpv3StatisticsEntry.setDescription("An entry in the table containing statistics\ninformation about a given virtual router.")
vrrpv3StatisticsMainTransitions = MibTableColumn((1, 3, 6, 1, 2, 1, 207, 1, 2, 5, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrrpv3StatisticsMainTransitions.setDescription("The total number of times that this virtual router's  \nstate has transitioned to main state.\n\nDiscontinuities in the value of this counter can occur  \nat re-initialization of the management system, and at  \nother times as indicated by the value of  \nvrrpv3StatisticsRowDiscontinuityTime.")
vrrpv3StatisticsNewMainReason = MibTableColumn((1, 3, 6, 1, 2, 1, 207, 1, 2, 5, 1, 2), Integer().subtype(subtypeSpec=SingleValueConstraint(1,3,2,0,)).subtype(namedValues=NamedValues(("notMain", 0), ("priority", 1), ("preempted", 2), ("mainNoResponse", 3), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrrpv3StatisticsNewMainReason.setDescription("This indicates the reason for the virtual router to  \ntransition to main state.  If the virtual router\nnever transitioned to main state, the value of this\nobject is notMain(0).  Otherwise, this indicates the\nreason this virtual router transitioned to main\nstate the last time.  Used by vrrpv3NewMain\nnotification.")
vrrpv3StatisticsRcvdAdvertisements = MibTableColumn((1, 3, 6, 1, 2, 1, 207, 1, 2, 5, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrrpv3StatisticsRcvdAdvertisements.setDescription("The total number of VRRP advertisements received by  \nthis virtual router.   \n\nDiscontinuities in the value of this counter can occur  \nat re-initialization of the management system, and at  \nother times as indicated by the value of  \nvrrpv3StatisticsRowDiscontinuityTime.")
vrrpv3StatisticsAdvIntervalErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 207, 1, 2, 5, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrrpv3StatisticsAdvIntervalErrors.setDescription("The total number of VRRP advertisement packets  \nreceived for which the advertisement interval is  \ndifferent from the vrrpv3OperationsAdvInterval  \nconfigured on this virtual router. \n\nDiscontinuities in the value of this counter can occur  \nat re-initialization of the management system, and at  \nother times as indicated by the value of  \nvrrpv3StatisticsRowDiscontinuityTime.")
vrrpv3StatisticsIpTtlErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 207, 1, 2, 5, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrrpv3StatisticsIpTtlErrors.setDescription("The total number of VRRP packets received by the  \nvirtual router with IPv4 TTL (for VRRP over IPv4) or\nIPv6 Hop Limit (for VRRP over IPv6) not equal to 255. \n\nDiscontinuities in the value of this counter can occur  \nat re-initialization of the management system, and at  \nother times as indicated by the value of  \nvrrpv3StatisticsRowDiscontinuityTime.")
vrrpv3StatisticsProtoErrReason = MibTableColumn((1, 3, 6, 1, 2, 1, 207, 1, 2, 5, 1, 6), Integer().subtype(subtypeSpec=SingleValueConstraint(2,0,3,1,4,)).subtype(namedValues=NamedValues(("noError", 0), ("ipTtlError", 1), ("versionError", 2), ("checksumError", 3), ("vrIdError", 4), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrrpv3StatisticsProtoErrReason.setDescription("This indicates the reason for the last protocol\nerror.  This SHOULD be set to noError(0) when no\nprotocol errors are encountered.  Used by\nvrrpv3ProtoError notification.")
vrrpv3StatisticsRcvdPriZeroPackets = MibTableColumn((1, 3, 6, 1, 2, 1, 207, 1, 2, 5, 1, 7), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrrpv3StatisticsRcvdPriZeroPackets.setDescription("The total number of VRRP packets received by the  \nvirtual router with a priority of '0'.   \n\nDiscontinuities in the value of this counter can occur  \nat re-initialization of the management system, and at  \nother times as indicated by the value of  \nvrrpv3StatisticsRowDiscontinuityTime.")
vrrpv3StatisticsSentPriZeroPackets = MibTableColumn((1, 3, 6, 1, 2, 1, 207, 1, 2, 5, 1, 8), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrrpv3StatisticsSentPriZeroPackets.setDescription("The total number of VRRP packets sent by the virtual  \nrouter with a priority of '0'.   \n\nDiscontinuities in the value of this counter can occur  \nat re-initialization of the management system, and at  \nother times as indicated by the value of  \nvrrpv3StatisticsRowDiscontinuityTime.")
vrrpv3StatisticsRcvdInvalidTypePackets = MibTableColumn((1, 3, 6, 1, 2, 1, 207, 1, 2, 5, 1, 9), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrrpv3StatisticsRcvdInvalidTypePackets.setDescription("The number of VRRP packets received by the virtual  \nrouter with an invalid value in the 'type' field.   \n\nDiscontinuities in the value of this counter can occur  \nat re-initialization of the management system, and at  \nother times as indicated by the value of  \nvrrpv3StatisticsRowDiscontinuityTime.")
vrrpv3StatisticsAddressListErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 207, 1, 2, 5, 1, 10), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrrpv3StatisticsAddressListErrors.setDescription("The total number of packets received for which the  \naddress list does not match the locally configured \nlist for the virtual router.   \n\nDiscontinuities in the value of this counter can occur  \nat re-initialization of the management system, and at  \nother times as indicated by the value of  \nvrrpv3StatisticsRowDiscontinuityTime.")
vrrpv3StatisticsPacketLengthErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 207, 1, 2, 5, 1, 11), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrrpv3StatisticsPacketLengthErrors.setDescription("The total number of packets received with a packet  \nlength less than the length of the VRRP header.   \n\nDiscontinuities in the value of this counter can occur  \nat re-initialization of the management system, and at  \nother times as indicated by the value of  \nvrrpv3StatisticsRowDiscontinuityTime.")
vrrpv3StatisticsRowDiscontinuityTime = MibTableColumn((1, 3, 6, 1, 2, 1, 207, 1, 2, 5, 1, 12), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrrpv3StatisticsRowDiscontinuityTime.setDescription("The value of sysUpTime on the most recent occasion at  \nwhich any one or more of this entry's counters\nsuffered a discontinuity.\n\nIf no such discontinuities have occurred since the last \nre-initialization of the local management subsystem,  \nthen this object contains a zero value.")
vrrpv3StatisticsRefreshRate = MibTableColumn((1, 3, 6, 1, 2, 1, 207, 1, 2, 5, 1, 13), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrrpv3StatisticsRefreshRate.setDescription("The minimum reasonable polling interval for this entry. \nThis object provides an indication of the minimum  \namount of time required to update the counters in this\nentry.")
vrrpv3Conformance = MibIdentifier((1, 3, 6, 1, 2, 1, 207, 2))
vrrpv3Compliances = MibIdentifier((1, 3, 6, 1, 2, 1, 207, 2, 1))
vrrpv3Groups = MibIdentifier((1, 3, 6, 1, 2, 1, 207, 2, 2))

# Augmentions
vrrpv3OperationsEntry.registerAugmentions(("VRRPV3-MIB", "vrrpv3StatisticsEntry"))
vrrpv3StatisticsEntry.setIndexNames(*vrrpv3OperationsEntry.getIndexNames())

# Notifications

vrrpv3NewMain = NotificationType((1, 3, 6, 1, 2, 1, 207, 0, 1)).setObjects(*(("VRRPV3-MIB", "vrrpv3OperationsMainIpAddr"), ("VRRPV3-MIB", "vrrpv3StatisticsNewMainReason"), ) )
if mibBuilder.loadTexts: vrrpv3NewMain.setDescription("The newMain notification indicates that the sending \nagent has transitioned to main state.")
vrrpv3ProtoError = NotificationType((1, 3, 6, 1, 2, 1, 207, 0, 2)).setObjects(*(("VRRPV3-MIB", "vrrpv3StatisticsProtoErrReason"), ) )
if mibBuilder.loadTexts: vrrpv3ProtoError.setDescription("The notification indicates that the sending agent has  \nencountered the protocol error indicated by  \nvrrpv3StatisticsProtoErrReason.")

# Groups

vrrpv3OperationsGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 207, 2, 2, 1)).setObjects(*(("VRRPV3-MIB", "vrrpv3OperationsPrimaryIpAddr"), ("VRRPV3-MIB", "vrrpv3OperationsPreemptMode"), ("VRRPV3-MIB", "vrrpv3OperationsAddrCount"), ("VRRPV3-MIB", "vrrpv3OperationsStatus"), ("VRRPV3-MIB", "vrrpv3OperationsAdvInterval"), ("VRRPV3-MIB", "vrrpv3OperationsUpTime"), ("VRRPV3-MIB", "vrrpv3OperationsVirtualMacAddr"), ("VRRPV3-MIB", "vrrpv3AssociatedIpAddrRowStatus"), ("VRRPV3-MIB", "vrrpv3OperationsPriority"), ("VRRPV3-MIB", "vrrpv3OperationsMainIpAddr"), ("VRRPV3-MIB", "vrrpv3OperationsRowStatus"), ("VRRPV3-MIB", "vrrpv3OperationsAcceptMode"), ) )
if mibBuilder.loadTexts: vrrpv3OperationsGroup.setDescription("Conformance group for VRRPv3 operations.")
vrrpv3StatisticsGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 207, 2, 2, 2)).setObjects(*(("VRRPV3-MIB", "vrrpv3StatisticsMainTransitions"), ("VRRPV3-MIB", "vrrpv3StatisticsSentPriZeroPackets"), ("VRRPV3-MIB", "vrrpv3StatisticsRcvdAdvertisements"), ("VRRPV3-MIB", "vrrpv3StatisticsPacketLengthErrors"), ("VRRPV3-MIB", "vrrpv3RouterVersionErrors"), ("VRRPV3-MIB", "vrrpv3StatisticsRefreshRate"), ("VRRPV3-MIB", "vrrpv3StatisticsAdvIntervalErrors"), ("VRRPV3-MIB", "vrrpv3StatisticsProtoErrReason"), ("VRRPV3-MIB", "vrrpv3StatisticsIpTtlErrors"), ("VRRPV3-MIB", "vrrpv3StatisticsAddressListErrors"), ("VRRPV3-MIB", "vrrpv3StatisticsNewMainReason"), ("VRRPV3-MIB", "vrrpv3StatisticsRcvdInvalidTypePackets"), ("VRRPV3-MIB", "vrrpv3RouterVrIdErrors"), ("VRRPV3-MIB", "vrrpv3StatisticsRcvdPriZeroPackets"), ("VRRPV3-MIB", "vrrpv3RouterChecksumErrors"), ("VRRPV3-MIB", "vrrpv3StatisticsRowDiscontinuityTime"), ) )
if mibBuilder.loadTexts: vrrpv3StatisticsGroup.setDescription("Conformance group for VRRPv3 statistics.")
vrrpv3StatisticsDiscontinuityGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 207, 2, 2, 3)).setObjects(*(("VRRPV3-MIB", "vrrpv3GlobalStatisticsDiscontinuityTime"), ) )
if mibBuilder.loadTexts: vrrpv3StatisticsDiscontinuityGroup.setDescription("Objects providing information about counter\ndiscontinuities.")
vrrpv3InfoGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 207, 2, 2, 4)).setObjects(*(("VRRPV3-MIB", "vrrpv3StatisticsNewMainReason"), ("VRRPV3-MIB", "vrrpv3StatisticsProtoErrReason"), ) )
if mibBuilder.loadTexts: vrrpv3InfoGroup.setDescription("Conformance group for objects contained in VRRPv3\nnotifications.")
vrrpv3NotificationsGroup = NotificationGroup((1, 3, 6, 1, 2, 1, 207, 2, 2, 5)).setObjects(*(("VRRPV3-MIB", "vrrpv3NewMain"), ("VRRPV3-MIB", "vrrpv3ProtoError"), ) )
if mibBuilder.loadTexts: vrrpv3NotificationsGroup.setDescription("The VRRP MIB Notification Group.")

# Compliances

vrrpv3FullCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 207, 2, 1, 1)).setObjects(*(("VRRPV3-MIB", "vrrpv3StatisticsGroup"), ("VRRPV3-MIB", "vrrpv3InfoGroup"), ("VRRPV3-MIB", "vrrpv3NotificationsGroup"), ("VRRPV3-MIB", "vrrpv3OperationsGroup"), ) )
if mibBuilder.loadTexts: vrrpv3FullCompliance.setDescription("The compliance statement")
vrrpv3ReadOnlyCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 207, 2, 1, 2)).setObjects(*(("VRRPV3-MIB", "vrrpv3StatisticsGroup"), ("VRRPV3-MIB", "vrrpv3StatisticsDiscontinuityGroup"), ("VRRPV3-MIB", "vrrpv3InfoGroup"), ("VRRPV3-MIB", "vrrpv3NotificationsGroup"), ("VRRPV3-MIB", "vrrpv3OperationsGroup"), ) )
if mibBuilder.loadTexts: vrrpv3ReadOnlyCompliance.setDescription("When this MIB module is implemented without support\nfor read-create (i.e., in read-only mode), then such\nan implementation can claim read-only compliance.\nSuch a device can then be monitored, but cannot be\nconfigured with this MIB.")

# Exports

# Module identity
mibBuilder.exportSymbols("VRRPV3-MIB", PYSNMP_MODULE_ID=vrrpv3MIB)

# Types
mibBuilder.exportSymbols("VRRPV3-MIB", Vrrpv3VrIdTC=Vrrpv3VrIdTC)

# Objects
mibBuilder.exportSymbols("VRRPV3-MIB", vrrpv3MIB=vrrpv3MIB, vrrpv3Notifications=vrrpv3Notifications, vrrpv3Objects=vrrpv3Objects, vrrpv3Operations=vrrpv3Operations, vrrpv3OperationsTable=vrrpv3OperationsTable, vrrpv3OperationsEntry=vrrpv3OperationsEntry, vrrpv3OperationsVrId=vrrpv3OperationsVrId, vrrpv3OperationsInetAddrType=vrrpv3OperationsInetAddrType, vrrpv3OperationsMainIpAddr=vrrpv3OperationsMainIpAddr, vrrpv3OperationsPrimaryIpAddr=vrrpv3OperationsPrimaryIpAddr, vrrpv3OperationsVirtualMacAddr=vrrpv3OperationsVirtualMacAddr, vrrpv3OperationsStatus=vrrpv3OperationsStatus, vrrpv3OperationsPriority=vrrpv3OperationsPriority, vrrpv3OperationsAddrCount=vrrpv3OperationsAddrCount, vrrpv3OperationsAdvInterval=vrrpv3OperationsAdvInterval, vrrpv3OperationsPreemptMode=vrrpv3OperationsPreemptMode, vrrpv3OperationsAcceptMode=vrrpv3OperationsAcceptMode, vrrpv3OperationsUpTime=vrrpv3OperationsUpTime, vrrpv3OperationsRowStatus=vrrpv3OperationsRowStatus, vrrpv3AssociatedIpAddrTable=vrrpv3AssociatedIpAddrTable, vrrpv3AssociatedIpAddrEntry=vrrpv3AssociatedIpAddrEntry, vrrpv3AssociatedIpAddrAddress=vrrpv3AssociatedIpAddrAddress, vrrpv3AssociatedIpAddrRowStatus=vrrpv3AssociatedIpAddrRowStatus, vrrpv3Statistics=vrrpv3Statistics, vrrpv3RouterChecksumErrors=vrrpv3RouterChecksumErrors, vrrpv3RouterVersionErrors=vrrpv3RouterVersionErrors, vrrpv3RouterVrIdErrors=vrrpv3RouterVrIdErrors, vrrpv3GlobalStatisticsDiscontinuityTime=vrrpv3GlobalStatisticsDiscontinuityTime, vrrpv3StatisticsTable=vrrpv3StatisticsTable, vrrpv3StatisticsEntry=vrrpv3StatisticsEntry, vrrpv3StatisticsMainTransitions=vrrpv3StatisticsMainTransitions, vrrpv3StatisticsNewMainReason=vrrpv3StatisticsNewMainReason, vrrpv3StatisticsRcvdAdvertisements=vrrpv3StatisticsRcvdAdvertisements, vrrpv3StatisticsAdvIntervalErrors=vrrpv3StatisticsAdvIntervalErrors, vrrpv3StatisticsIpTtlErrors=vrrpv3StatisticsIpTtlErrors, vrrpv3StatisticsProtoErrReason=vrrpv3StatisticsProtoErrReason, vrrpv3StatisticsRcvdPriZeroPackets=vrrpv3StatisticsRcvdPriZeroPackets, vrrpv3StatisticsSentPriZeroPackets=vrrpv3StatisticsSentPriZeroPackets, vrrpv3StatisticsRcvdInvalidTypePackets=vrrpv3StatisticsRcvdInvalidTypePackets, vrrpv3StatisticsAddressListErrors=vrrpv3StatisticsAddressListErrors, vrrpv3StatisticsPacketLengthErrors=vrrpv3StatisticsPacketLengthErrors, vrrpv3StatisticsRowDiscontinuityTime=vrrpv3StatisticsRowDiscontinuityTime, vrrpv3StatisticsRefreshRate=vrrpv3StatisticsRefreshRate, vrrpv3Conformance=vrrpv3Conformance, vrrpv3Compliances=vrrpv3Compliances, vrrpv3Groups=vrrpv3Groups)

# Notifications
mibBuilder.exportSymbols("VRRPV3-MIB", vrrpv3NewMain=vrrpv3NewMain, vrrpv3ProtoError=vrrpv3ProtoError)

# Groups
mibBuilder.exportSymbols("VRRPV3-MIB", vrrpv3OperationsGroup=vrrpv3OperationsGroup, vrrpv3StatisticsGroup=vrrpv3StatisticsGroup, vrrpv3StatisticsDiscontinuityGroup=vrrpv3StatisticsDiscontinuityGroup, vrrpv3InfoGroup=vrrpv3InfoGroup, vrrpv3NotificationsGroup=vrrpv3NotificationsGroup)

# Compliances
mibBuilder.exportSymbols("VRRPV3-MIB", vrrpv3FullCompliance=vrrpv3FullCompliance, vrrpv3ReadOnlyCompliance=vrrpv3ReadOnlyCompliance)
