# PySNMP SMI module. Autogenerated from smidump -f python RFC1158-MIB
# by libsmi2pysnmp-0.1.3 at Thu May 22 11:58:09 2014,
# Python version sys.version_info(major=2, minor=7, micro=2, releaselevel='final', serial=0)

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
( Counter, Gauge, IpAddress, NetworkAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, mgmt, ) = mibBuilder.importSymbols("RFC1155-SMI", "Counter", "Gauge", "IpAddress", "NetworkAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "mgmt")
( Bits, Integer32, MibIdentifier, TimeTicks, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "MibIdentifier", "TimeTicks")

# Types

class DisplayString(OctetString):
    pass


# Objects

nullSpecific = MibIdentifier((0, 0))
mib_2 = MibIdentifier((1, 3, 6, 1, 2, 1)).setLabel("mib-2")
system = MibIdentifier((1, 3, 6, 1, 2, 1, 1))
sysDescr = MibScalar((1, 3, 6, 1, 2, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
sysObjectID = MibScalar((1, 3, 6, 1, 2, 1, 1, 2), ObjectIdentifier()).setMaxAccess("readonly")
sysUpTime = MibScalar((1, 3, 6, 1, 2, 1, 1, 3), TimeTicks()).setMaxAccess("readonly")
sysContact = MibScalar((1, 3, 6, 1, 2, 1, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
sysName = MibScalar((1, 3, 6, 1, 2, 1, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
sysLocation = MibScalar((1, 3, 6, 1, 2, 1, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
sysServices = MibScalar((1, 3, 6, 1, 2, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 127))).setMaxAccess("readonly")
interfaces = MibIdentifier((1, 3, 6, 1, 2, 1, 2))
ifNumber = MibScalar((1, 3, 6, 1, 2, 1, 2, 1), Integer32()).setMaxAccess("readonly")
ifTable = MibTable((1, 3, 6, 1, 2, 1, 2, 2))
ifEntry = MibTableRow((1, 3, 6, 1, 2, 1, 2, 2, 1))
ifIndex = MibScalar((1, 3, 6, 1, 2, 1, 2, 2, 1, 1), Integer32()).setMaxAccess("readonly")
ifDescr = MibScalar((1, 3, 6, 1, 2, 1, 2, 2, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
ifType = MibScalar((1, 3, 6, 1, 2, 1, 2, 2, 1, 3), Integer().subtype(subtypeSpec=SingleValueConstraint(18,22,19,5,4,28,12,26,7,1,17,16,8,24,14,20,6,21,15,23,13,11,25,9,3,27,2,10,)).subtype(namedValues=NamedValues(("other", 1), ("iso88026-man", 10), ("starLan", 11), ("proteon-10Mbit", 12), ("proteon-80Mbit", 13), ("hyperchannel", 14), ("fddi", 15), ("lapb", 16), ("sdlc", 17), ("t1-carrier", 18), ("cept", 19), ("regular1822", 2), ("basicISDN", 20), ("primaryISDN", 21), ("propPointToPointSerial", 22), ("terminalServer-asyncPort", 23), ("softwareLoopback", 24), ("eon", 25), ("ethernet-3Mbit", 26), ("nsip", 27), ("slip", 28), ("hdh1822", 3), ("ddn-x25", 4), ("rfc877-x25", 5), ("ethernet-csmacd", 6), ("iso88023-csmacd", 7), ("iso88024-tokenBus", 8), ("iso88025-tokenRing", 9), ))).setMaxAccess("readonly")
ifMtu = MibScalar((1, 3, 6, 1, 2, 1, 2, 2, 1, 4), Integer32()).setMaxAccess("readonly")
ifSpeed = MibScalar((1, 3, 6, 1, 2, 1, 2, 2, 1, 5), Gauge()).setMaxAccess("readonly")
ifPhysAddress = MibScalar((1, 3, 6, 1, 2, 1, 2, 2, 1, 6), OctetString()).setMaxAccess("readonly")
ifAdminStatus = MibScalar((1, 3, 6, 1, 2, 1, 2, 2, 1, 7), Integer().subtype(subtypeSpec=SingleValueConstraint(2,3,1,)).subtype(namedValues=NamedValues(("up", 1), ("down", 2), ("testing", 3), ))).setMaxAccess("readwrite")
ifOperStatus = MibScalar((1, 3, 6, 1, 2, 1, 2, 2, 1, 8), Integer().subtype(subtypeSpec=SingleValueConstraint(2,3,1,)).subtype(namedValues=NamedValues(("up", 1), ("down", 2), ("testing", 3), ))).setMaxAccess("readonly")
ifLastChange = MibScalar((1, 3, 6, 1, 2, 1, 2, 2, 1, 9), TimeTicks()).setMaxAccess("readonly")
ifInOctets = MibScalar((1, 3, 6, 1, 2, 1, 2, 2, 1, 10), Counter()).setMaxAccess("readonly")
ifInUcastPkts = MibScalar((1, 3, 6, 1, 2, 1, 2, 2, 1, 11), Counter()).setMaxAccess("readonly")
ifInNUcastPkts = MibScalar((1, 3, 6, 1, 2, 1, 2, 2, 1, 12), Counter()).setMaxAccess("readonly")
ifInDiscards = MibScalar((1, 3, 6, 1, 2, 1, 2, 2, 1, 13), Counter()).setMaxAccess("readonly")
ifInErrors = MibScalar((1, 3, 6, 1, 2, 1, 2, 2, 1, 14), Counter()).setMaxAccess("readonly")
ifInUnknownProtos = MibScalar((1, 3, 6, 1, 2, 1, 2, 2, 1, 15), Counter()).setMaxAccess("readonly")
ifOutOctets = MibScalar((1, 3, 6, 1, 2, 1, 2, 2, 1, 16), Counter()).setMaxAccess("readonly")
ifOutUcastPkts = MibScalar((1, 3, 6, 1, 2, 1, 2, 2, 1, 17), Counter()).setMaxAccess("readonly")
ifOutNUcastPkts = MibScalar((1, 3, 6, 1, 2, 1, 2, 2, 1, 18), Counter()).setMaxAccess("readonly")
ifOutDiscards = MibScalar((1, 3, 6, 1, 2, 1, 2, 2, 1, 19), Counter()).setMaxAccess("readonly")
ifOutErrors = MibScalar((1, 3, 6, 1, 2, 1, 2, 2, 1, 20), Counter()).setMaxAccess("readonly")
ifOutQLen = MibScalar((1, 3, 6, 1, 2, 1, 2, 2, 1, 21), Gauge()).setMaxAccess("readonly")
ifSpecific = MibScalar((1, 3, 6, 1, 2, 1, 2, 2, 1, 22), ObjectIdentifier()).setMaxAccess("readonly")
at = MibIdentifier((1, 3, 6, 1, 2, 1, 3))
atTable = MibTable((1, 3, 6, 1, 2, 1, 3, 1))
atEntry = MibTableRow((1, 3, 6, 1, 2, 1, 3, 1, 1))
atIfIndex = MibScalar((1, 3, 6, 1, 2, 1, 3, 1, 1, 1), Integer32()).setMaxAccess("readwrite")
atPhysAddress = MibScalar((1, 3, 6, 1, 2, 1, 3, 1, 1, 2), OctetString()).setMaxAccess("readwrite")
atNetAddress = MibScalar((1, 3, 6, 1, 2, 1, 3, 1, 1, 3), IpAddress()).setMaxAccess("readwrite")
ip = MibIdentifier((1, 3, 6, 1, 2, 1, 4))
ipForwarding = MibScalar((1, 3, 6, 1, 2, 1, 4, 1), Integer().subtype(subtypeSpec=SingleValueConstraint(2,1,)).subtype(namedValues=NamedValues(("gateway", 1), ("host", 2), ))).setMaxAccess("readwrite")
ipDefaultTTL = MibScalar((1, 3, 6, 1, 2, 1, 4, 2), Integer32()).setMaxAccess("readwrite")
ipInReceives = MibScalar((1, 3, 6, 1, 2, 1, 4, 3), Counter()).setMaxAccess("readonly")
ipInHdrErrors = MibScalar((1, 3, 6, 1, 2, 1, 4, 4), Counter()).setMaxAccess("readonly")
ipInAddrErrors = MibScalar((1, 3, 6, 1, 2, 1, 4, 5), Counter()).setMaxAccess("readonly")
ipForwDatagrams = MibScalar((1, 3, 6, 1, 2, 1, 4, 6), Counter()).setMaxAccess("readonly")
ipInUnknownProtos = MibScalar((1, 3, 6, 1, 2, 1, 4, 7), Counter()).setMaxAccess("readonly")
ipInDiscards = MibScalar((1, 3, 6, 1, 2, 1, 4, 8), Counter()).setMaxAccess("readonly")
ipInDelivers = MibScalar((1, 3, 6, 1, 2, 1, 4, 9), Counter()).setMaxAccess("readonly")
ipOutRequests = MibScalar((1, 3, 6, 1, 2, 1, 4, 10), Counter()).setMaxAccess("readonly")
ipOutDiscards = MibScalar((1, 3, 6, 1, 2, 1, 4, 11), Counter()).setMaxAccess("readonly")
ipOutNoRoutes = MibScalar((1, 3, 6, 1, 2, 1, 4, 12), Counter()).setMaxAccess("readonly")
ipReasmTimeout = MibScalar((1, 3, 6, 1, 2, 1, 4, 13), Integer32()).setMaxAccess("readonly")
ipReasmReqds = MibScalar((1, 3, 6, 1, 2, 1, 4, 14), Counter()).setMaxAccess("readonly")
ipReasmOKs = MibScalar((1, 3, 6, 1, 2, 1, 4, 15), Counter()).setMaxAccess("readonly")
ipReasmFails = MibScalar((1, 3, 6, 1, 2, 1, 4, 16), Counter()).setMaxAccess("readonly")
ipFragOKs = MibScalar((1, 3, 6, 1, 2, 1, 4, 17), Counter()).setMaxAccess("readonly")
ipFragFails = MibScalar((1, 3, 6, 1, 2, 1, 4, 18), Counter()).setMaxAccess("readonly")
ipFragCreates = MibScalar((1, 3, 6, 1, 2, 1, 4, 19), Counter()).setMaxAccess("readonly")
ipAddrTable = MibTable((1, 3, 6, 1, 2, 1, 4, 20))
ipAddrEntry = MibTableRow((1, 3, 6, 1, 2, 1, 4, 20, 1))
ipAdEntAddr = MibScalar((1, 3, 6, 1, 2, 1, 4, 20, 1, 1), IpAddress()).setMaxAccess("readonly")
ipAdEntIfIndex = MibScalar((1, 3, 6, 1, 2, 1, 4, 20, 1, 2), Integer32()).setMaxAccess("readonly")
ipAdEntNetMask = MibScalar((1, 3, 6, 1, 2, 1, 4, 20, 1, 3), IpAddress()).setMaxAccess("readonly")
ipAdEntBcastAddr = MibScalar((1, 3, 6, 1, 2, 1, 4, 20, 1, 4), Integer32()).setMaxAccess("readonly")
ipAdEntReasmMaxSize = MibScalar((1, 3, 6, 1, 2, 1, 4, 20, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
ipRoutingTable = MibTable((1, 3, 6, 1, 2, 1, 4, 21))
ipRouteEntry = MibTableRow((1, 3, 6, 1, 2, 1, 4, 21, 1))
ipRouteDest = MibScalar((1, 3, 6, 1, 2, 1, 4, 21, 1, 1), IpAddress()).setMaxAccess("readwrite")
ipRouteIfIndex = MibScalar((1, 3, 6, 1, 2, 1, 4, 21, 1, 2), Integer32()).setMaxAccess("readwrite")
ipRouteMetric1 = MibScalar((1, 3, 6, 1, 2, 1, 4, 21, 1, 3), Integer32()).setMaxAccess("readwrite")
ipRouteMetric2 = MibScalar((1, 3, 6, 1, 2, 1, 4, 21, 1, 4), Integer32()).setMaxAccess("readwrite")
ipRouteMetric3 = MibScalar((1, 3, 6, 1, 2, 1, 4, 21, 1, 5), Integer32()).setMaxAccess("readwrite")
ipRouteMetric4 = MibScalar((1, 3, 6, 1, 2, 1, 4, 21, 1, 6), Integer32()).setMaxAccess("readwrite")
ipRouteNextHop = MibScalar((1, 3, 6, 1, 2, 1, 4, 21, 1, 7), IpAddress()).setMaxAccess("readwrite")
ipRouteType = MibScalar((1, 3, 6, 1, 2, 1, 4, 21, 1, 8), Integer().subtype(subtypeSpec=SingleValueConstraint(1,4,3,2,)).subtype(namedValues=NamedValues(("other", 1), ("invalid", 2), ("direct", 3), ("remote", 4), ))).setMaxAccess("readwrite")
ipRouteProto = MibScalar((1, 3, 6, 1, 2, 1, 4, 21, 1, 9), Integer().subtype(subtypeSpec=SingleValueConstraint(12,6,8,9,4,14,3,13,5,10,11,1,2,7,)).subtype(namedValues=NamedValues(("other", 1), ("es-is", 10), ("ciscoIgrp", 11), ("bbnSpfIgp", 12), ("ospf", 13), ("bgp", 14), ("local", 2), ("netmgmt", 3), ("icmp", 4), ("egp", 5), ("ggp", 6), ("hello", 7), ("rip", 8), ("is-is", 9), ))).setMaxAccess("readonly")
ipRouteAge = MibScalar((1, 3, 6, 1, 2, 1, 4, 21, 1, 10), Integer32()).setMaxAccess("readwrite")
ipRouteMask = MibScalar((1, 3, 6, 1, 2, 1, 4, 21, 1, 11), IpAddress()).setMaxAccess("readwrite")
ipNetToMediaTable = MibTable((1, 3, 6, 1, 2, 1, 4, 22))
ipNetToMediaEntry = MibTableRow((1, 3, 6, 1, 2, 1, 4, 22, 1))
ipNetToMediaIfIndex = MibScalar((1, 3, 6, 1, 2, 1, 4, 22, 1, 1), Integer32()).setMaxAccess("readwrite")
ipNetToMediaPhysAddress = MibScalar((1, 3, 6, 1, 2, 1, 4, 22, 1, 2), OctetString()).setMaxAccess("readwrite")
ipNetToMediaNetAddress = MibScalar((1, 3, 6, 1, 2, 1, 4, 22, 1, 3), IpAddress()).setMaxAccess("readwrite")
ipNetToMediaType = MibScalar((1, 3, 6, 1, 2, 1, 4, 22, 1, 4), Integer().subtype(subtypeSpec=SingleValueConstraint(4,1,3,2,)).subtype(namedValues=NamedValues(("other", 1), ("invalid", 2), ("dynamic", 3), ("static", 4), ))).setMaxAccess("readwrite")
icmp = MibIdentifier((1, 3, 6, 1, 2, 1, 5))
icmpInMsgs = MibScalar((1, 3, 6, 1, 2, 1, 5, 1), Counter()).setMaxAccess("readonly")
icmpInErrors = MibScalar((1, 3, 6, 1, 2, 1, 5, 2), Counter()).setMaxAccess("readonly")
icmpInDestUnreachs = MibScalar((1, 3, 6, 1, 2, 1, 5, 3), Counter()).setMaxAccess("readonly")
icmpInTimeExcds = MibScalar((1, 3, 6, 1, 2, 1, 5, 4), Counter()).setMaxAccess("readonly")
icmpInParmProbs = MibScalar((1, 3, 6, 1, 2, 1, 5, 5), Counter()).setMaxAccess("readonly")
icmpInSrcQuenchs = MibScalar((1, 3, 6, 1, 2, 1, 5, 6), Counter()).setMaxAccess("readonly")
icmpInRedirects = MibScalar((1, 3, 6, 1, 2, 1, 5, 7), Counter()).setMaxAccess("readonly")
icmpInEchos = MibScalar((1, 3, 6, 1, 2, 1, 5, 8), Counter()).setMaxAccess("readonly")
icmpInEchoReps = MibScalar((1, 3, 6, 1, 2, 1, 5, 9), Counter()).setMaxAccess("readonly")
icmpInTimestamps = MibScalar((1, 3, 6, 1, 2, 1, 5, 10), Counter()).setMaxAccess("readonly")
icmpInTimestampReps = MibScalar((1, 3, 6, 1, 2, 1, 5, 11), Counter()).setMaxAccess("readonly")
icmpInAddrMasks = MibScalar((1, 3, 6, 1, 2, 1, 5, 12), Counter()).setMaxAccess("readonly")
icmpInAddrMaskReps = MibScalar((1, 3, 6, 1, 2, 1, 5, 13), Counter()).setMaxAccess("readonly")
icmpOutMsgs = MibScalar((1, 3, 6, 1, 2, 1, 5, 14), Counter()).setMaxAccess("readonly")
icmpOutErrors = MibScalar((1, 3, 6, 1, 2, 1, 5, 15), Counter()).setMaxAccess("readonly")
icmpOutDestUnreachs = MibScalar((1, 3, 6, 1, 2, 1, 5, 16), Counter()).setMaxAccess("readonly")
icmpOutTimeExcds = MibScalar((1, 3, 6, 1, 2, 1, 5, 17), Counter()).setMaxAccess("readonly")
icmpOutParmProbs = MibScalar((1, 3, 6, 1, 2, 1, 5, 18), Counter()).setMaxAccess("readonly")
icmpOutSrcQuenchs = MibScalar((1, 3, 6, 1, 2, 1, 5, 19), Counter()).setMaxAccess("readonly")
icmpOutRedirects = MibScalar((1, 3, 6, 1, 2, 1, 5, 20), Counter()).setMaxAccess("readonly")
icmpOutEchos = MibScalar((1, 3, 6, 1, 2, 1, 5, 21), Counter()).setMaxAccess("readonly")
icmpOutEchoReps = MibScalar((1, 3, 6, 1, 2, 1, 5, 22), Counter()).setMaxAccess("readonly")
icmpOutTimestamps = MibScalar((1, 3, 6, 1, 2, 1, 5, 23), Counter()).setMaxAccess("readonly")
icmpOutTimestampReps = MibScalar((1, 3, 6, 1, 2, 1, 5, 24), Counter()).setMaxAccess("readonly")
icmpOutAddrMasks = MibScalar((1, 3, 6, 1, 2, 1, 5, 25), Counter()).setMaxAccess("readonly")
icmpOutAddrMaskReps = MibScalar((1, 3, 6, 1, 2, 1, 5, 26), Counter()).setMaxAccess("readonly")
tcp = MibIdentifier((1, 3, 6, 1, 2, 1, 6))
tcpRtoAlgorithm = MibScalar((1, 3, 6, 1, 2, 1, 6, 1), Integer().subtype(subtypeSpec=SingleValueConstraint(4,1,2,3,)).subtype(namedValues=NamedValues(("other", 1), ("constant", 2), ("rsre", 3), ("vanj", 4), ))).setMaxAccess("readonly")
tcpRtoMin = MibScalar((1, 3, 6, 1, 2, 1, 6, 2), Integer32()).setMaxAccess("readonly")
tcpRtoMax = MibScalar((1, 3, 6, 1, 2, 1, 6, 3), Integer32()).setMaxAccess("readonly")
tcpMaxConn = MibScalar((1, 3, 6, 1, 2, 1, 6, 4), Integer32()).setMaxAccess("readonly")
tcpActiveOpens = MibScalar((1, 3, 6, 1, 2, 1, 6, 5), Counter()).setMaxAccess("readonly")
tcpPassiveOpens = MibScalar((1, 3, 6, 1, 2, 1, 6, 6), Counter()).setMaxAccess("readonly")
tcpAttemptFails = MibScalar((1, 3, 6, 1, 2, 1, 6, 7), Counter()).setMaxAccess("readonly")
tcpEstabResets = MibScalar((1, 3, 6, 1, 2, 1, 6, 8), Counter()).setMaxAccess("readonly")
tcpCurrEstab = MibScalar((1, 3, 6, 1, 2, 1, 6, 9), Gauge()).setMaxAccess("readonly")
tcpInSegs = MibScalar((1, 3, 6, 1, 2, 1, 6, 10), Counter()).setMaxAccess("readonly")
tcpOutSegs = MibScalar((1, 3, 6, 1, 2, 1, 6, 11), Counter()).setMaxAccess("readonly")
tcpRetransSegs = MibScalar((1, 3, 6, 1, 2, 1, 6, 12), Counter()).setMaxAccess("readonly")
tcpConnTable = MibTable((1, 3, 6, 1, 2, 1, 6, 13))
tcpConnEntry = MibTableRow((1, 3, 6, 1, 2, 1, 6, 13, 1))
tcpConnState = MibScalar((1, 3, 6, 1, 2, 1, 6, 13, 1, 1), Integer().subtype(subtypeSpec=SingleValueConstraint(4,6,7,8,5,11,9,1,10,2,3,)).subtype(namedValues=NamedValues(("closed", 1), ("closing", 10), ("timeWait", 11), ("listen", 2), ("synSent", 3), ("synReceived", 4), ("established", 5), ("finWait1", 6), ("finWait2", 7), ("closeWait", 8), ("lastAck", 9), ))).setMaxAccess("readonly")
tcpConnLocalAddress = MibScalar((1, 3, 6, 1, 2, 1, 6, 13, 1, 2), IpAddress()).setMaxAccess("readonly")
tcpConnLocalPort = MibScalar((1, 3, 6, 1, 2, 1, 6, 13, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
tcpConnRemAddress = MibScalar((1, 3, 6, 1, 2, 1, 6, 13, 1, 4), IpAddress()).setMaxAccess("readonly")
tcpConnRemPort = MibScalar((1, 3, 6, 1, 2, 1, 6, 13, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
tcpInErrs = MibScalar((1, 3, 6, 1, 2, 1, 6, 14), Counter()).setMaxAccess("readonly")
tcpOutRsts = MibScalar((1, 3, 6, 1, 2, 1, 6, 15), Counter()).setMaxAccess("readonly")
udp = MibIdentifier((1, 3, 6, 1, 2, 1, 7))
udpInDatagrams = MibScalar((1, 3, 6, 1, 2, 1, 7, 1), Counter()).setMaxAccess("readonly")
udpNoPorts = MibScalar((1, 3, 6, 1, 2, 1, 7, 2), Counter()).setMaxAccess("readonly")
udpInErrors = MibScalar((1, 3, 6, 1, 2, 1, 7, 3), Counter()).setMaxAccess("readonly")
udpOutDatagrams = MibScalar((1, 3, 6, 1, 2, 1, 7, 4), Counter()).setMaxAccess("readonly")
udpTable = MibTable((1, 3, 6, 1, 2, 1, 7, 5))
udpEntry = MibTableRow((1, 3, 6, 1, 2, 1, 7, 5, 1))
udpLocalAddress = MibScalar((1, 3, 6, 1, 2, 1, 7, 5, 1, 1), IpAddress()).setMaxAccess("readonly")
udpLocalPort = MibScalar((1, 3, 6, 1, 2, 1, 7, 5, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
egp = MibIdentifier((1, 3, 6, 1, 2, 1, 8))
egpInMsgs = MibScalar((1, 3, 6, 1, 2, 1, 8, 1), Counter()).setMaxAccess("readonly")
egpInErrors = MibScalar((1, 3, 6, 1, 2, 1, 8, 2), Counter()).setMaxAccess("readonly")
egpOutMsgs = MibScalar((1, 3, 6, 1, 2, 1, 8, 3), Counter()).setMaxAccess("readonly")
egpOutErrors = MibScalar((1, 3, 6, 1, 2, 1, 8, 4), Counter()).setMaxAccess("readonly")
egpNeighTable = MibTable((1, 3, 6, 1, 2, 1, 8, 5))
egpNeighEntry = MibTableRow((1, 3, 6, 1, 2, 1, 8, 5, 1))
egpNeighState = MibScalar((1, 3, 6, 1, 2, 1, 8, 5, 1, 1), Integer().subtype(subtypeSpec=SingleValueConstraint(4,3,1,5,2,)).subtype(namedValues=NamedValues(("idle", 1), ("acquisition", 2), ("down", 3), ("up", 4), ("cease", 5), ))).setMaxAccess("readonly")
egpNeighAddr = MibScalar((1, 3, 6, 1, 2, 1, 8, 5, 1, 2), IpAddress()).setMaxAccess("readonly")
egpNeighAs = MibScalar((1, 3, 6, 1, 2, 1, 8, 5, 1, 3), Integer32()).setMaxAccess("readonly")
egpNeighInMsgs = MibScalar((1, 3, 6, 1, 2, 1, 8, 5, 1, 4), Counter()).setMaxAccess("readonly")
egpNeighInErrs = MibScalar((1, 3, 6, 1, 2, 1, 8, 5, 1, 5), Counter()).setMaxAccess("readonly")
egpNeighOutMsgs = MibScalar((1, 3, 6, 1, 2, 1, 8, 5, 1, 6), Counter()).setMaxAccess("readonly")
egpNeighOutErrs = MibScalar((1, 3, 6, 1, 2, 1, 8, 5, 1, 7), Counter()).setMaxAccess("readonly")
egpNeighInErrMsgs = MibScalar((1, 3, 6, 1, 2, 1, 8, 5, 1, 8), Counter()).setMaxAccess("readonly")
egpNeighOutErrMsgs = MibScalar((1, 3, 6, 1, 2, 1, 8, 5, 1, 9), Counter()).setMaxAccess("readonly")
egpNeighStateUps = MibScalar((1, 3, 6, 1, 2, 1, 8, 5, 1, 10), Counter()).setMaxAccess("readonly")
egpNeighStateDowns = MibScalar((1, 3, 6, 1, 2, 1, 8, 5, 1, 11), Counter()).setMaxAccess("readonly")
egpNeighIntervalHello = MibScalar((1, 3, 6, 1, 2, 1, 8, 5, 1, 12), Integer32()).setMaxAccess("readonly")
egpNeighIntervalPoll = MibScalar((1, 3, 6, 1, 2, 1, 8, 5, 1, 13), Integer32()).setMaxAccess("readonly")
egpNeighMode = MibScalar((1, 3, 6, 1, 2, 1, 8, 5, 1, 14), Integer().subtype(subtypeSpec=SingleValueConstraint(1,2,)).subtype(namedValues=NamedValues(("active", 1), ("passive", 2), ))).setMaxAccess("readonly")
egpNeighEventTrigger = MibScalar((1, 3, 6, 1, 2, 1, 8, 5, 1, 15), Integer().subtype(subtypeSpec=SingleValueConstraint(1,2,)).subtype(namedValues=NamedValues(("start", 1), ("stop", 2), ))).setMaxAccess("readwrite")
egpAs = MibScalar((1, 3, 6, 1, 2, 1, 8, 6), Integer32()).setMaxAccess("readonly")
transmission = MibIdentifier((1, 3, 6, 1, 2, 1, 10))
snmp = MibIdentifier((1, 3, 6, 1, 2, 1, 11))
snmpInPkts = MibScalar((1, 3, 6, 1, 2, 1, 11, 1), Counter()).setMaxAccess("readonly")
snmpOutPkts = MibScalar((1, 3, 6, 1, 2, 1, 11, 2), Counter()).setMaxAccess("readonly")
snmpInBadVersions = MibScalar((1, 3, 6, 1, 2, 1, 11, 3), Counter()).setMaxAccess("readonly")
snmpInBadCommunityNames = MibScalar((1, 3, 6, 1, 2, 1, 11, 4), Counter()).setMaxAccess("readonly")
snmpInBadCommunityUses = MibScalar((1, 3, 6, 1, 2, 1, 11, 5), Counter()).setMaxAccess("readonly")
snmpInASNParseErrs = MibScalar((1, 3, 6, 1, 2, 1, 11, 6), Counter()).setMaxAccess("readonly")
snmpInBadTypes = MibScalar((1, 3, 6, 1, 2, 1, 11, 7), Counter()).setMaxAccess("readonly")
snmpInTooBigs = MibScalar((1, 3, 6, 1, 2, 1, 11, 8), Counter()).setMaxAccess("readonly")
snmpInNoSuchNames = MibScalar((1, 3, 6, 1, 2, 1, 11, 9), Counter()).setMaxAccess("readonly")
snmpInBadValues = MibScalar((1, 3, 6, 1, 2, 1, 11, 10), Counter()).setMaxAccess("readonly")
snmpInReadOnlys = MibScalar((1, 3, 6, 1, 2, 1, 11, 11), Counter()).setMaxAccess("readonly")
snmpInGenErrs = MibScalar((1, 3, 6, 1, 2, 1, 11, 12), Counter()).setMaxAccess("readonly")
snmpInTotalReqVars = MibScalar((1, 3, 6, 1, 2, 1, 11, 13), Counter()).setMaxAccess("readonly")
snmpInTotalSetVars = MibScalar((1, 3, 6, 1, 2, 1, 11, 14), Counter()).setMaxAccess("readonly")
snmpInGetRequests = MibScalar((1, 3, 6, 1, 2, 1, 11, 15), Counter()).setMaxAccess("readonly")
snmpInGetNexts = MibScalar((1, 3, 6, 1, 2, 1, 11, 16), Counter()).setMaxAccess("readonly")
snmpInSetRequests = MibScalar((1, 3, 6, 1, 2, 1, 11, 17), Counter()).setMaxAccess("readonly")
snmpInGetResponses = MibScalar((1, 3, 6, 1, 2, 1, 11, 18), Counter()).setMaxAccess("readonly")
snmpInTraps = MibScalar((1, 3, 6, 1, 2, 1, 11, 19), Counter()).setMaxAccess("readonly")
snmpOutTooBigs = MibScalar((1, 3, 6, 1, 2, 1, 11, 20), Counter()).setMaxAccess("readonly")
snmpOutNoSuchNames = MibScalar((1, 3, 6, 1, 2, 1, 11, 21), Counter()).setMaxAccess("readonly")
snmpOutBadValues = MibScalar((1, 3, 6, 1, 2, 1, 11, 22), Counter()).setMaxAccess("readonly")
snmpOutReadOnlys = MibScalar((1, 3, 6, 1, 2, 1, 11, 23), Counter()).setMaxAccess("readonly")
snmpOutGenErrs = MibScalar((1, 3, 6, 1, 2, 1, 11, 24), Counter()).setMaxAccess("readonly")
snmpOutGetRequests = MibScalar((1, 3, 6, 1, 2, 1, 11, 25), Counter()).setMaxAccess("readonly")
snmpOutGetNexts = MibScalar((1, 3, 6, 1, 2, 1, 11, 26), Counter()).setMaxAccess("readonly")
snmpOutSetRequests = MibScalar((1, 3, 6, 1, 2, 1, 11, 27), Counter()).setMaxAccess("readonly")
snmpOutGetResponses = MibScalar((1, 3, 6, 1, 2, 1, 11, 28), Counter()).setMaxAccess("readonly")
snmpOutTraps = MibScalar((1, 3, 6, 1, 2, 1, 11, 29), Counter()).setMaxAccess("readonly")
snmpEnableAuthTraps = MibScalar((1, 3, 6, 1, 2, 1, 11, 30), Integer().subtype(subtypeSpec=SingleValueConstraint(2,1,)).subtype(namedValues=NamedValues(("enabled", 1), ("disabled", 2), ))).setMaxAccess("readwrite")

# Augmentions

# Exports

# Types
mibBuilder.exportSymbols("RFC1158-MIB", DisplayString=DisplayString)

# Objects
mibBuilder.exportSymbols("RFC1158-MIB", nullSpecific=nullSpecific, mib_2=mib_2, system=system, sysDescr=sysDescr, sysObjectID=sysObjectID, sysUpTime=sysUpTime, sysContact=sysContact, sysName=sysName, sysLocation=sysLocation, sysServices=sysServices, interfaces=interfaces, ifNumber=ifNumber, ifTable=ifTable, ifEntry=ifEntry, ifIndex=ifIndex, ifDescr=ifDescr, ifType=ifType, ifMtu=ifMtu, ifSpeed=ifSpeed, ifPhysAddress=ifPhysAddress, ifAdminStatus=ifAdminStatus, ifOperStatus=ifOperStatus, ifLastChange=ifLastChange, ifInOctets=ifInOctets, ifInUcastPkts=ifInUcastPkts, ifInNUcastPkts=ifInNUcastPkts, ifInDiscards=ifInDiscards, ifInErrors=ifInErrors, ifInUnknownProtos=ifInUnknownProtos, ifOutOctets=ifOutOctets, ifOutUcastPkts=ifOutUcastPkts, ifOutNUcastPkts=ifOutNUcastPkts, ifOutDiscards=ifOutDiscards, ifOutErrors=ifOutErrors, ifOutQLen=ifOutQLen, ifSpecific=ifSpecific, at=at, atTable=atTable, atEntry=atEntry, atIfIndex=atIfIndex, atPhysAddress=atPhysAddress, atNetAddress=atNetAddress, ip=ip, ipForwarding=ipForwarding, ipDefaultTTL=ipDefaultTTL, ipInReceives=ipInReceives, ipInHdrErrors=ipInHdrErrors, ipInAddrErrors=ipInAddrErrors, ipForwDatagrams=ipForwDatagrams, ipInUnknownProtos=ipInUnknownProtos, ipInDiscards=ipInDiscards, ipInDelivers=ipInDelivers, ipOutRequests=ipOutRequests, ipOutDiscards=ipOutDiscards, ipOutNoRoutes=ipOutNoRoutes, ipReasmTimeout=ipReasmTimeout, ipReasmReqds=ipReasmReqds, ipReasmOKs=ipReasmOKs, ipReasmFails=ipReasmFails, ipFragOKs=ipFragOKs, ipFragFails=ipFragFails, ipFragCreates=ipFragCreates, ipAddrTable=ipAddrTable, ipAddrEntry=ipAddrEntry, ipAdEntAddr=ipAdEntAddr, ipAdEntIfIndex=ipAdEntIfIndex, ipAdEntNetMask=ipAdEntNetMask, ipAdEntBcastAddr=ipAdEntBcastAddr, ipAdEntReasmMaxSize=ipAdEntReasmMaxSize, ipRoutingTable=ipRoutingTable, ipRouteEntry=ipRouteEntry, ipRouteDest=ipRouteDest, ipRouteIfIndex=ipRouteIfIndex, ipRouteMetric1=ipRouteMetric1, ipRouteMetric2=ipRouteMetric2, ipRouteMetric3=ipRouteMetric3, ipRouteMetric4=ipRouteMetric4, ipRouteNextHop=ipRouteNextHop, ipRouteType=ipRouteType, ipRouteProto=ipRouteProto, ipRouteAge=ipRouteAge, ipRouteMask=ipRouteMask, ipNetToMediaTable=ipNetToMediaTable, ipNetToMediaEntry=ipNetToMediaEntry, ipNetToMediaIfIndex=ipNetToMediaIfIndex, ipNetToMediaPhysAddress=ipNetToMediaPhysAddress, ipNetToMediaNetAddress=ipNetToMediaNetAddress, ipNetToMediaType=ipNetToMediaType, icmp=icmp, icmpInMsgs=icmpInMsgs, icmpInErrors=icmpInErrors, icmpInDestUnreachs=icmpInDestUnreachs, icmpInTimeExcds=icmpInTimeExcds, icmpInParmProbs=icmpInParmProbs, icmpInSrcQuenchs=icmpInSrcQuenchs, icmpInRedirects=icmpInRedirects, icmpInEchos=icmpInEchos, icmpInEchoReps=icmpInEchoReps, icmpInTimestamps=icmpInTimestamps, icmpInTimestampReps=icmpInTimestampReps, icmpInAddrMasks=icmpInAddrMasks, icmpInAddrMaskReps=icmpInAddrMaskReps, icmpOutMsgs=icmpOutMsgs, icmpOutErrors=icmpOutErrors, icmpOutDestUnreachs=icmpOutDestUnreachs, icmpOutTimeExcds=icmpOutTimeExcds, icmpOutParmProbs=icmpOutParmProbs, icmpOutSrcQuenchs=icmpOutSrcQuenchs, icmpOutRedirects=icmpOutRedirects, icmpOutEchos=icmpOutEchos, icmpOutEchoReps=icmpOutEchoReps, icmpOutTimestamps=icmpOutTimestamps, icmpOutTimestampReps=icmpOutTimestampReps, icmpOutAddrMasks=icmpOutAddrMasks, icmpOutAddrMaskReps=icmpOutAddrMaskReps, tcp=tcp, tcpRtoAlgorithm=tcpRtoAlgorithm, tcpRtoMin=tcpRtoMin, tcpRtoMax=tcpRtoMax, tcpMaxConn=tcpMaxConn, tcpActiveOpens=tcpActiveOpens, tcpPassiveOpens=tcpPassiveOpens, tcpAttemptFails=tcpAttemptFails, tcpEstabResets=tcpEstabResets, tcpCurrEstab=tcpCurrEstab, tcpInSegs=tcpInSegs)
mibBuilder.exportSymbols("RFC1158-MIB", tcpOutSegs=tcpOutSegs, tcpRetransSegs=tcpRetransSegs, tcpConnTable=tcpConnTable, tcpConnEntry=tcpConnEntry, tcpConnState=tcpConnState, tcpConnLocalAddress=tcpConnLocalAddress, tcpConnLocalPort=tcpConnLocalPort, tcpConnRemAddress=tcpConnRemAddress, tcpConnRemPort=tcpConnRemPort, tcpInErrs=tcpInErrs, tcpOutRsts=tcpOutRsts, udp=udp, udpInDatagrams=udpInDatagrams, udpNoPorts=udpNoPorts, udpInErrors=udpInErrors, udpOutDatagrams=udpOutDatagrams, udpTable=udpTable, udpEntry=udpEntry, udpLocalAddress=udpLocalAddress, udpLocalPort=udpLocalPort, egp=egp, egpInMsgs=egpInMsgs, egpInErrors=egpInErrors, egpOutMsgs=egpOutMsgs, egpOutErrors=egpOutErrors, egpNeighTable=egpNeighTable, egpNeighEntry=egpNeighEntry, egpNeighState=egpNeighState, egpNeighAddr=egpNeighAddr, egpNeighAs=egpNeighAs, egpNeighInMsgs=egpNeighInMsgs, egpNeighInErrs=egpNeighInErrs, egpNeighOutMsgs=egpNeighOutMsgs, egpNeighOutErrs=egpNeighOutErrs, egpNeighInErrMsgs=egpNeighInErrMsgs, egpNeighOutErrMsgs=egpNeighOutErrMsgs, egpNeighStateUps=egpNeighStateUps, egpNeighStateDowns=egpNeighStateDowns, egpNeighIntervalHello=egpNeighIntervalHello, egpNeighIntervalPoll=egpNeighIntervalPoll, egpNeighMode=egpNeighMode, egpNeighEventTrigger=egpNeighEventTrigger, egpAs=egpAs, transmission=transmission, snmp=snmp, snmpInPkts=snmpInPkts, snmpOutPkts=snmpOutPkts, snmpInBadVersions=snmpInBadVersions, snmpInBadCommunityNames=snmpInBadCommunityNames, snmpInBadCommunityUses=snmpInBadCommunityUses, snmpInASNParseErrs=snmpInASNParseErrs, snmpInBadTypes=snmpInBadTypes, snmpInTooBigs=snmpInTooBigs, snmpInNoSuchNames=snmpInNoSuchNames, snmpInBadValues=snmpInBadValues, snmpInReadOnlys=snmpInReadOnlys, snmpInGenErrs=snmpInGenErrs, snmpInTotalReqVars=snmpInTotalReqVars, snmpInTotalSetVars=snmpInTotalSetVars, snmpInGetRequests=snmpInGetRequests, snmpInGetNexts=snmpInGetNexts, snmpInSetRequests=snmpInSetRequests, snmpInGetResponses=snmpInGetResponses, snmpInTraps=snmpInTraps, snmpOutTooBigs=snmpOutTooBigs, snmpOutNoSuchNames=snmpOutNoSuchNames, snmpOutBadValues=snmpOutBadValues, snmpOutReadOnlys=snmpOutReadOnlys, snmpOutGenErrs=snmpOutGenErrs, snmpOutGetRequests=snmpOutGetRequests, snmpOutGetNexts=snmpOutGetNexts, snmpOutSetRequests=snmpOutSetRequests, snmpOutGetResponses=snmpOutGetResponses, snmpOutTraps=snmpOutTraps, snmpEnableAuthTraps=snmpEnableAuthTraps)

