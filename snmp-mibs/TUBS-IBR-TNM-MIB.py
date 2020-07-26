# PySNMP SMI module. Autogenerated from smidump -f python TUBS-IBR-TNM-MIB
# by libsmi2pysnmp-0.1.3 at Thu May 22 11:58:17 2014,
# Python version sys.version_info(major=2, minor=7, micro=2, releaselevel='final', serial=0)

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
( Bits, Counter32, Integer32, Integer32, ModuleIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Integer32", "Integer32", "ModuleIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32")
( DateAndTime, DisplayString, RowStatus, TAddress, TextualConvention, TimeStamp, TruthValue, ) = mibBuilder.importSymbols("SNMPv2-TC", "DateAndTime", "DisplayString", "RowStatus", "TAddress", "TextualConvention", "TimeStamp", "TruthValue")
( ibr, ) = mibBuilder.importSymbols("TUBS-SMI", "ibr")

# Types

class URL(TextualConvention, OctetString):
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec+ValueSizeConstraint(0,255)
    

# Objects

tnmMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 1575, 1, 1)).setRevisions(("2000-02-09 00:00","1997-02-14 10:23","1996-07-15 20:24",))
if mibBuilder.loadTexts: tnmMIB.setOrganization("TU Braunschweig")
if mibBuilder.loadTexts: tnmMIB.setContactInfo("Juergen Schoenwaelder\nTU Braunschweig\nBueltenweg 74/75\n38106 Braunschweig\nGermany\n\nTel: +49 531 391 3283\nFax: +49 531 391 5936\nE-mail: schoenw@ibr.cs.tu-bs.de")
if mibBuilder.loadTexts: tnmMIB.setDescription("Experimental MIB modules for tnm based agents.")
tnmStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 1575, 1, 1, 1))
tnmVersion = MibScalar((1, 3, 6, 1, 4, 1, 1575, 1, 1, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnmVersion.setDescription("The version number of the tnm agent.")
tnmTclVersion = MibScalar((1, 3, 6, 1, 4, 1, 1575, 1, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnmTclVersion.setDescription("The version number of the running Tcl interpreter.")
tnmTclCmdCount = MibScalar((1, 3, 6, 1, 4, 1, 1575, 1, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnmTclCmdCount.setDescription("The nummber of Tcl statements evaluated so far.")
tnmDate = MibScalar((1, 3, 6, 1, 4, 1, 1575, 1, 1, 1, 4), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnmDate.setDescription("The current date.")
tnmTrapDst = MibScalar((1, 3, 6, 1, 4, 1, 1575, 1, 1, 1, 5), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnmTrapDst.setDescription("The host name of the trap sink host.")
tnmTrapMsg = MibScalar((1, 3, 6, 1, 4, 1, 1575, 1, 1, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnmTrapMsg.setDescription("The description of the last trap create by this entity.")
tnmDownload = MibIdentifier((1, 3, 6, 1, 4, 1, 1575, 1, 1, 2))
tnmHttpProxy = MibScalar((1, 3, 6, 1, 4, 1, 1575, 1, 1, 2, 1), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnmHttpProxy.setDescription("This variable specifies the proxy server. It must be of the\nform <name>[:<port>] where <name> is either a domain name\nor an IP address and <port> is the port number used to access\nthe proxy server. The default port number is 80.")
tnmHttpSource = MibScalar((1, 3, 6, 1, 4, 1, 1575, 1, 1, 2, 2), URL()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnmHttpSource.setDescription("Setting this variable will make tnm to download\nand source the document with the given URL. The agent\nwill try to retrieve the document and sets the variable\nto the URL if this operations was successfull. \nOtherwise, the value will become an empty string.")
tnmHttpError = MibScalar((1, 3, 6, 1, 4, 1, 1575, 1, 1, 2, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnmHttpError.setDescription("This variable contains an error string is an http\noperation fails. An empty string signals that the\nlast operation completed successfully.")
tnmPeers = MibIdentifier((1, 3, 6, 1, 4, 1, 1575, 1, 1, 3))
tnmPeerTable = MibTable((1, 3, 6, 1, 4, 1, 1575, 1, 1, 3, 1))
if mibBuilder.loadTexts: tnmPeerTable.setDescription("A (conceptual) table storing known tnm peers.")
tnmPeerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1575, 1, 1, 3, 1, 1)).setIndexNames((0, "TUBS-IBR-TNM-MIB", "tnmPeerTAddress"))
if mibBuilder.loadTexts: tnmPeerEntry.setDescription("An entry (conceptual row) in the peer table.")
tnmPeerTAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 1575, 1, 1, 3, 1, 1, 1), TAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tnmPeerTAddress.setDescription("The address and port number of the peer agent.")
tnmPeerAuth = MibTableColumn((1, 3, 6, 1, 4, 1, 1575, 1, 1, 3, 1, 1, 2), OctetString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tnmPeerAuth.setDescription("The authentication information for this peer. This will\nusually be a community string until we get the final SNMPv2\ndecisions about the security model.")
tnmPeerState = MibTableColumn((1, 3, 6, 1, 4, 1, 1575, 1, 1, 3, 1, 1, 3), Integer().subtype(subtypeSpec=SingleValueConstraint(2,1,)).subtype(namedValues=NamedValues(("up", 1), ("down", 2), ))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tnmPeerState.setDescription("The current status of the peer as returned by the last\nstatus probe message.")
tnmPeerLastChecked = MibTableColumn((1, 3, 6, 1, 4, 1, 1575, 1, 1, 3, 1, 1, 4), TimeStamp()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tnmPeerLastChecked.setDescription("The value of sysUpTime when the status of the peer was\nretrieved and written to tnmPeerState.")
tnmPeerStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1575, 1, 1, 3, 1, 1, 5), RowStatus().clone('active')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tnmPeerStatus.setDescription("The status column used for creating, modifying,\nand deleting instances of the columnar objects in\nthe tnm peer table.")
tnmElection = MibIdentifier((1, 3, 6, 1, 4, 1, 1575, 1, 1, 4))
tnmElectionIndex = MibScalar((1, 3, 6, 1, 4, 1, 1575, 1, 1, 4, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnmElectionIndex.setDescription("The (hopefully) unique index of this peer used by the\nbully election algorithm.")
tnmElectionPanic = MibScalar((1, 3, 6, 1, 4, 1, 1575, 1, 1, 4, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnmElectionPanic.setDescription("Reading this variable will start the panic algorithm\non this peer. (We should use an inform request here.)")
tnmElectionMain = MibScalar((1, 3, 6, 1, 4, 1, 1575, 1, 1, 4, 3), TAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnmElectionMain.setDescription("This variable will be set by a new main appearing\non the scene. (We should use an inform request here.)")
tnmEval = MibIdentifier((1, 3, 6, 1, 4, 1, 1575, 1, 1, 5))
tnmEvalSlot = MibScalar((1, 3, 6, 1, 4, 1, 1575, 1, 1, 5, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnmEvalSlot.setDescription("The index number of the first unassigned entry in\nthe evaluation table.	\n\nA management station should create new entries in\nthe evaluation table using this algorithm: first,\nissue a management protocol retrieval operation to\ndetermine the value of evalSlot; and, second,\nissue a management protocol set operation to\ncreate an instance of the evalStatus object\nsetting its value to underCreation(1).  If this\nlatter operation succeeds, then the management\nstation may continue modifying the instances\ncorresponding to the newly created conceptual row,\nwithout fear of collision with other management\nstations.")
tnmEvalTable = MibTable((1, 3, 6, 1, 4, 1, 1575, 1, 1, 5, 2))
if mibBuilder.loadTexts: tnmEvalTable.setDescription("The (conceptual) evaluation table.")
tnmEvalEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1575, 1, 1, 5, 2, 1)).setIndexNames((0, "TUBS-IBR-TNM-MIB", "tnmEvalIndex"))
if mibBuilder.loadTexts: tnmEvalEntry.setDescription("An entry (conceptual row) in the evaluation table.")
tnmEvalIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1575, 1, 1, 5, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnmEvalIndex.setDescription("The auxiliary variable used for identifying\ninstances of the columnar objects in the\nevaluation table.")
tnmEvalString = MibTableColumn((1, 3, 6, 1, 4, 1, 1575, 1, 1, 5, 2, 1, 2), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tnmEvalString.setDescription("The string to evaluate.")
tnmEvalValue = MibTableColumn((1, 3, 6, 1, 4, 1, 1575, 1, 1, 5, 2, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnmEvalValue.setDescription("The value resturned by executing evalString.")
tnmEvalStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1575, 1, 1, 5, 2, 1, 4), RowStatus().clone('active')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tnmEvalStatus.setDescription("The status column used for creating, modifying,\nand deleting instances of the columnar objects in\nthe evaluation table.")

# Augmentions

# Exports

# Module identity
mibBuilder.exportSymbols("TUBS-IBR-TNM-MIB", PYSNMP_MODULE_ID=tnmMIB)

# Types
mibBuilder.exportSymbols("TUBS-IBR-TNM-MIB", URL=URL)

# Objects
mibBuilder.exportSymbols("TUBS-IBR-TNM-MIB", tnmMIB=tnmMIB, tnmStatus=tnmStatus, tnmVersion=tnmVersion, tnmTclVersion=tnmTclVersion, tnmTclCmdCount=tnmTclCmdCount, tnmDate=tnmDate, tnmTrapDst=tnmTrapDst, tnmTrapMsg=tnmTrapMsg, tnmDownload=tnmDownload, tnmHttpProxy=tnmHttpProxy, tnmHttpSource=tnmHttpSource, tnmHttpError=tnmHttpError, tnmPeers=tnmPeers, tnmPeerTable=tnmPeerTable, tnmPeerEntry=tnmPeerEntry, tnmPeerTAddress=tnmPeerTAddress, tnmPeerAuth=tnmPeerAuth, tnmPeerState=tnmPeerState, tnmPeerLastChecked=tnmPeerLastChecked, tnmPeerStatus=tnmPeerStatus, tnmElection=tnmElection, tnmElectionIndex=tnmElectionIndex, tnmElectionPanic=tnmElectionPanic, tnmElectionMain=tnmElectionMain, tnmEval=tnmEval, tnmEvalSlot=tnmEvalSlot, tnmEvalTable=tnmEvalTable, tnmEvalEntry=tnmEvalEntry, tnmEvalIndex=tnmEvalIndex, tnmEvalString=tnmEvalString, tnmEvalValue=tnmEvalValue, tnmEvalStatus=tnmEvalStatus)

