# PySNMP SMI module. Autogenerated from smidump -f python SIP-SERVER-MIB
# by libsmi2pysnmp-0.1.3 at Thu May 22 11:58:11 2014,
# Python version sys.version_info(major=2, minor=7, micro=2, releaselevel='final', serial=0)

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
( InetAddress, InetAddressType, ) = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType")
( applIndex, ) = mibBuilder.importSymbols("NETWORK-SERVICES-MIB", "applIndex")
( SnmpAdminString, ) = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
( ModuleCompliance, ObjectGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup")
( Bits, Counter32, Gauge32, Integer32, ModuleIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, mib_2, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Gauge32", "Integer32", "ModuleIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "mib-2")
( DateAndTime, TimeStamp, TruthValue, ) = mibBuilder.importSymbols("SNMPv2-TC", "DateAndTime", "TimeStamp", "TruthValue")

# Objects

sipServerMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 151)).setRevisions(("2007-04-20 00:00",))
if mibBuilder.loadTexts: sipServerMIB.setOrganization("IETF Session Initiation Protocol\nWorking Group")
if mibBuilder.loadTexts: sipServerMIB.setContactInfo("SIP WG email: sip@ietf.org\n\nCo-editor: Kevin Lingle\n           Cisco Systems, Inc.\n   postal: 7025 Kit Creek Road\n           P.O. Box 14987\n           Research Triangle Park, NC 27709\n           USA\n  email:   klingle@cisco.com\n  phone:   +1 919 476 2029\n\nCo-editor: Joon Maeng\n    email: jmaeng@austin.rr.com\n\nCo-editor: Jean-Francois Mule\n           CableLabs\n   postal: 858 Coal Creek Circle\n           Louisville, CO 80027\n           USA\n    email: jf.mule@cablelabs.com\n    phone: +1 303 661 9100\n\nCo-editor: Dave Walker\n    email: drwalker@rogers.com")
if mibBuilder.loadTexts: sipServerMIB.setDescription("Session Initiation Protocol (SIP) Server MIB module.  SIP is an\napplication-layer signaling protocol for creating, modifying,\nand terminating multimedia sessions with one or more\nparticipants.  These sessions include Internet multimedia\nconferences and Internet telephone calls.  SIP is defined in\nRFC 3261 (June 2002).\n\nThis MIB is defined for the management of SIP Proxy, Redirect,\nand Registrar Servers.\n\n\n\nA Proxy Server acts as both a client and a server.  It accepts\nrequests from other clients, either responding to them or\npassing them on to other servers, possibly after modification.\n\nA Redirect Server accepts requests from clients and returns\nzero or more addresses to that client.  Unlike a User Agent\nServer, it does not accept calls.\n\nA Registrar is a server that accepts REGISTER requests.  A\nRegistrar is typically co-located with a Proxy or Redirect\nServer.\n\nCopyright (C) The IETF Trust (2007).  This version of\nthis MIB module is part of RFC 4780; see the RFC itself for\nfull legal notices.")
sipServerMIBObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 151, 1))
sipServerCfg = MibIdentifier((1, 3, 6, 1, 2, 1, 151, 1, 1))
sipServerCfgTable = MibTable((1, 3, 6, 1, 2, 1, 151, 1, 1, 1))
if mibBuilder.loadTexts: sipServerCfgTable.setDescription("This table contains configuration objects applicable to SIP\nRedirect and Proxy Servers.")
sipServerCfgEntry = MibTableRow((1, 3, 6, 1, 2, 1, 151, 1, 1, 1, 1)).setIndexNames((0, "NETWORK-SERVICES-MIB", "applIndex"))
if mibBuilder.loadTexts: sipServerCfgEntry.setDescription("A row of common configuration.\n\nEach row represents those objects for a particular SIP server\npresent in this system.  applIndex is used to uniquely identify\nthese instances of SIP servers and correlate them through\nthe common framework of the NETWORK-SERVICES-MIB (RFC 2788).\nThe same value of applIndex used in the corresponding\nSIP-COMMON-MIB is used here.")
sipServerCfgHostAddressType = MibTableColumn((1, 3, 6, 1, 2, 1, 151, 1, 1, 1, 1, 1), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sipServerCfgHostAddressType.setDescription("The type of Internet address by which the SIP server is\nreachable.")
sipServerCfgHostAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 151, 1, 1, 1, 1, 2), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sipServerCfgHostAddress.setDescription("This is the host portion of a SIP URI that is assigned to the\nSIP server.  It MAY contain a fully qualified domain name or\nan IP address.  The length of the value will depend on the type\nof address specified.  The type of address given by this object\nis controlled by sipServerCfgHostAddressType.")
sipServerProxyCfg = MibIdentifier((1, 3, 6, 1, 2, 1, 151, 1, 3))
sipServerProxyCfgTable = MibTable((1, 3, 6, 1, 2, 1, 151, 1, 3, 1))
if mibBuilder.loadTexts: sipServerProxyCfgTable.setDescription("This table contains configuration objects applicable to SIP\nProxy Servers.")
sipServerProxyCfgEntry = MibTableRow((1, 3, 6, 1, 2, 1, 151, 1, 3, 1, 1)).setIndexNames((0, "NETWORK-SERVICES-MIB", "applIndex"))
if mibBuilder.loadTexts: sipServerProxyCfgEntry.setDescription("A row of common proxy configuration.\n\nEach row represents those objects for a particular SIP server\npresent in this system.  applIndex is used to uniquely identify\nthese instances of SIP servers and correlate them through the\ncommon framework of the NETWORK-SERVICES-MIB (RFC 2788).  The\nsame value of applIndex used in the corresponding\nSIP-COMMON-MIB is used here.")
sipServerCfgProxyStatefulness = MibTableColumn((1, 3, 6, 1, 2, 1, 151, 1, 3, 1, 1, 1), Integer().subtype(subtypeSpec=SingleValueConstraint(1,2,3,)).subtype(namedValues=NamedValues(("stateless", 1), ("transactionStateful", 2), ("callStateful", 3), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sipServerCfgProxyStatefulness.setDescription("This object reflects the default mode of operation for the\nProxy Server entity.\n\nA stateless proxy is a logical entity that does not maintain\nthe client or server transaction state machines when it\nprocesses requests.  A stateless proxy forwards every request it\nreceives downstream and every response it receives upstream.  If\nthe value of this object is stateless(1), the proxy defaults to\nstateless operations.\n\nA transaction stateful proxy, or simply a 'stateful proxy', is\na logical entity that maintains the client and server\ntransaction state machines during the processing of a request.\nA (transaction) stateful proxy is not the same as a call\nstateful proxy.  If the value of this object is\ntransactionStateful(2), the proxy is stateful on a transaction\nbasis.\n\nA call stateful proxy is a logical entity if it retains state\nfor a dialog from the initiating INVITE to the terminating BYE\nrequest.  A call stateful proxy is always transaction stateful,\nbut the converse is not necessarily true.  If the value of this\nobject is callStateful(3), the proxy is call stateful.")
sipServerCfgProxyRecursion = MibTableColumn((1, 3, 6, 1, 2, 1, 151, 1, 3, 1, 1, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sipServerCfgProxyRecursion.setDescription("This object reflects whether or not the Proxy performs a\nrecursive search on the Contacts provided in 3xx redirects.\n\nIf the value of this object is 'true', a recursive search is\nperformed.  If the value is 'false', no search is performed,\nand the 3xx response is sent upstream towards the source of\nthe request.")
sipServerCfgProxyRecordRoute = MibTableColumn((1, 3, 6, 1, 2, 1, 151, 1, 3, 1, 1, 3), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sipServerCfgProxyRecordRoute.setDescription("This object reflects whether or not the proxy adds itself to\nthe Record-Route header as a default action.  This header is\nused to list the proxies that insist on being in the signaling\npath for subsequent requests related to the call leg.\n\nIf the value of this object is 'true', the proxy adds itself to\nthe end of the Record-Route header, creating the header if\nrequired.  If the value is 'false', the proxy does not add\nitself to the Record-Route header.")
sipServerCfgProxyAuthMethod = MibTableColumn((1, 3, 6, 1, 2, 1, 151, 1, 3, 1, 1, 4), Bits().subtype(namedValues=NamedValues(("none", 0), ("tls", 1), ("digest", 2), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sipServerCfgProxyAuthMethod.setDescription("This object reflects the authentication methods that MAY be\nused to authenticate request originators.\n\nbit 0  no authentication is performed\nbit 1  TLS is used\nbit 2  HTTP Digest is used.")
sipServerCfgProxyAuthDefaultRealm = MibTableColumn((1, 3, 6, 1, 2, 1, 151, 1, 3, 1, 1, 5), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sipServerCfgProxyAuthDefaultRealm.setDescription("This object reflects the default realm value used in\nProxy-Authenticate headers.  Note that this MAY need to be\nstored per user, in which case, this default value is ignored.")
sipServerProxyStats = MibIdentifier((1, 3, 6, 1, 2, 1, 151, 1, 4))
sipServerProxyStatsTable = MibTable((1, 3, 6, 1, 2, 1, 151, 1, 4, 1))
if mibBuilder.loadTexts: sipServerProxyStatsTable.setDescription("This table contains the statistics objects applicable to all\nSIP Proxy Servers in this system.")
sipServerProxyStatsEntry = MibTableRow((1, 3, 6, 1, 2, 1, 151, 1, 4, 1, 1)).setIndexNames((0, "NETWORK-SERVICES-MIB", "applIndex"))
if mibBuilder.loadTexts: sipServerProxyStatsEntry.setDescription("A row of summary statistics.\n\nEach row represents those objects for a particular SIP server\npresent in this system.  applIndex is used to uniquely identify\nthese instances of SIP servers and correlate them through the\ncommon framework of the NETWORK-SERVICES-MIB (RFC 2788).  The\nsame value of applIndex used in the corresponding\nSIP-COMMON-MIB is used here.")
sipServerProxyStatProxyReqFailures = MibTableColumn((1, 3, 6, 1, 2, 1, 151, 1, 4, 1, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sipServerProxyStatProxyReqFailures.setDescription("This object contains the number of occurrences of unsupported\noptions being specified in received Proxy-Require headers.\nSuch occurrences result in a 420 Bad Extension status code\nbeing returned.\n\nDiscontinuities in the value of this counter can occur at\nre-initialization of the SIP entity or service.  A Management\nStation can detect discontinuities in this counter by\n\n\nmonitoring the sipServerProxyStatsDisconTime object in the same\nrow.")
sipServerProxyStatsDisconTime = MibTableColumn((1, 3, 6, 1, 2, 1, 151, 1, 4, 1, 1, 2), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sipServerProxyStatsDisconTime.setDescription("The value of the sysUpTime object when the counters for the server\nstatistics objects in this row last experienced a discontinuity.")
sipServerRegCfg = MibIdentifier((1, 3, 6, 1, 2, 1, 151, 1, 5))
sipServerRegCfgTable = MibTable((1, 3, 6, 1, 2, 1, 151, 1, 5, 1))
if mibBuilder.loadTexts: sipServerRegCfgTable.setDescription("This table contains configuration objects applicable to SIP\nRegistrars.")
sipServerRegCfgEntry = MibTableRow((1, 3, 6, 1, 2, 1, 151, 1, 5, 1, 1)).setIndexNames((0, "NETWORK-SERVICES-MIB", "applIndex"))
if mibBuilder.loadTexts: sipServerRegCfgEntry.setDescription("A row of common Registrar configuration.\n\nEach row represents those objects for a particular SIP server\npresent in this system.  applIndex is used to uniquely identify\nthese instances of SIP servers and correlate them through the\ncommon framework of the NETWORK-SERVICES-MIB (RFC 2788).  The\nsame value of applIndex used in the corresponding\nSIP-COMMON-MIB is used here.")
sipServerRegMaxContactExpiryDuration = MibTableColumn((1, 3, 6, 1, 2, 1, 151, 1, 5, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sipServerRegMaxContactExpiryDuration.setDescription("This object reflects the maximum expiry that may be requested\nby a User Agent for a particular Contact.  User Agents can\nspecify expiry using either an Expiry header in a REGISTER\nrequest, or using an Expires parameter in a Contact header in\na REGISTER request.  If the value requested by the User Agent\nis greater than the value of this object, then the contact\ninformation is given the duration specified by this object, and\nthat duration is indicated to the User Agent in the response.")
sipServerRegMaxUsers = MibTableColumn((1, 3, 6, 1, 2, 1, 151, 1, 5, 1, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sipServerRegMaxUsers.setDescription("This object reflects the maximum number of users that the\nRegistrar supports.  The current number of users is reflected\nby sipServerRegCurrentUsers.")
sipServerRegCurrentUsers = MibTableColumn((1, 3, 6, 1, 2, 1, 151, 1, 5, 1, 1, 3), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sipServerRegCurrentUsers.setDescription("This object reflects the number of users currently registered\nwith the Registrar.")
sipServerRegDfltRegActiveInterval = MibTableColumn((1, 3, 6, 1, 2, 1, 151, 1, 5, 1, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sipServerRegDfltRegActiveInterval.setDescription("This object reflects the default time interval the Registrar\nconsiders registrations to be active.  The value is used to\ncompute the Expires header in the REGISTER response.  If a user\nagent requests a time interval shorter than specified by this\nobject, the Registrar SHOULD honor that request.  If a Contact\nentry does not have an 'expires' parameter, the value of the\nExpires header field is used instead.  If a Contact entry has no\n'expires' parameter and no Expires header field is present,\nthe value of this object is used as the default value.")
sipServerRegUserTable = MibTable((1, 3, 6, 1, 2, 1, 151, 1, 5, 2))
if mibBuilder.loadTexts: sipServerRegUserTable.setDescription("This table contains information on all users registered to each\nRegistrar in this system.")
sipServerRegUserEntry = MibTableRow((1, 3, 6, 1, 2, 1, 151, 1, 5, 2, 1)).setIndexNames((0, "NETWORK-SERVICES-MIB", "applIndex"), (0, "SIP-SERVER-MIB", "sipServerRegUserIndex"))
if mibBuilder.loadTexts: sipServerRegUserEntry.setDescription("This entry contains information for a single user registered to\nthis Registrar.\n\nEach row represents those objects for a particular SIP server\npresent in this system.  applIndex is used to uniquely identify\nthese instances of SIP servers and correlate them through the\ncommon framework of the NETWORK-SERVICES-MIB (RFC 2788).  The\nsame value of applIndex used in the corresponding\nSIP-COMMON-MIB is used here.")
sipServerRegUserIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 151, 1, 5, 2, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295))).setMaxAccess("noaccess")
if mibBuilder.loadTexts: sipServerRegUserIndex.setDescription("This object uniquely identifies a conceptual row in the table.")
sipServerRegUserUri = MibTableColumn((1, 3, 6, 1, 2, 1, 151, 1, 5, 2, 1, 2), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sipServerRegUserUri.setDescription("This object contains the user's address-of-record.  It is the\nmain form by which the Registrar knows the user.  The format is\ntypically 'user@domain'.  It is contained in the To header for\nall REGISTER requests.")
sipServerRegUserAuthenticationFailures = MibTableColumn((1, 3, 6, 1, 2, 1, 151, 1, 5, 2, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sipServerRegUserAuthenticationFailures.setDescription("This object contains a count of the number of times the user\nhas failed authentication.\n\nDiscontinuities in the value of this counter can occur due to\nsuccessful user authentications and at re-initialization of\nthe SIP entity or service.  A Management Station can detect\ndiscontinuities in this counter by monitoring the\nsipServerRegUserDisconTime object in the same row.")
sipServerRegUserDisconTime = MibTableColumn((1, 3, 6, 1, 2, 1, 151, 1, 5, 2, 1, 4), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sipServerRegUserDisconTime.setDescription("The value of the sysUpTime object when the counters for the\nuser registration statistics objects in this row last\nexperienced a discontinuity.")
sipServerRegContactTable = MibTable((1, 3, 6, 1, 2, 1, 151, 1, 5, 3))
if mibBuilder.loadTexts: sipServerRegContactTable.setDescription("This table contains information on every location where a\nregistered user (specified by sipServerRegUserIndex) wishes to\nbe found (i.e., the user has provided contact information to\neach SIP Registrar in this system).")
sipServerRegContactEntry = MibTableRow((1, 3, 6, 1, 2, 1, 151, 1, 5, 3, 1)).setIndexNames((0, "NETWORK-SERVICES-MIB", "applIndex"), (0, "SIP-SERVER-MIB", "sipServerRegUserIndex"), (0, "SIP-SERVER-MIB", "sipServerRegContactIndex"))
if mibBuilder.loadTexts: sipServerRegContactEntry.setDescription("This entry contains information for a single Contact.  Multiple\ncontacts may exist for a single user.\n\nEach row represents those objects for a particular SIP server\npresent in this system.  applIndex is used to uniquely identify\nthese instances of SIP servers and correlate them through the\ncommon framework of the NETWORK-SERVICES-MIB (RFC 2788).  The\nsame value of applIndex used in the corresponding\nSIP-COMMON-MIB is used here.")
sipServerRegContactIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 151, 1, 5, 3, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295))).setMaxAccess("noaccess")
if mibBuilder.loadTexts: sipServerRegContactIndex.setDescription("Along with the sipServerRegUserIndex, this object uniquely\nidentifies a conceptual row in the table.")
sipServerRegContactDisplayName = MibTableColumn((1, 3, 6, 1, 2, 1, 151, 1, 5, 3, 1, 2), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sipServerRegContactDisplayName.setDescription("This object contains the display name for the Contact.  For\nexample, 'Santa at Home', or 'Santa on his Sled', corresponding\nto contact URIs of sip:BigGuy@example.com or\nsip:sclaus817@example.com, respectively.")
sipServerRegContactURI = MibTableColumn((1, 3, 6, 1, 2, 1, 151, 1, 5, 3, 1, 3), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sipServerRegContactURI.setDescription("This object contains either a SIP URI where the user can be\ncontacted.  This URI is normally returned to a client from a\nRedirect Server, or is used as the RequestURI in a SIP request\nline for requests forwarded by a proxy.")
sipServerRegContactLastUpdated = MibTableColumn((1, 3, 6, 1, 2, 1, 151, 1, 5, 3, 1, 4), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sipServerRegContactLastUpdated.setDescription("This object indicates the time when this contact information\nwas accepted.  If the contact information is updated via a\nsubsequent REGISTER of the same information, this object is\nalso updated.")
sipServerRegContactExpiry = MibTableColumn((1, 3, 6, 1, 2, 1, 151, 1, 5, 3, 1, 5), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sipServerRegContactExpiry.setDescription("This object contains the date and time when the contact\ninformation will no longer be valid.  Such times may be\nspecified by the user at registration (i.e., Expires header or\nexpiry parameter in the Contact information), or a system\ndefault can be applied.")
sipServerRegContactPreference = MibTableColumn((1, 3, 6, 1, 2, 1, 151, 1, 5, 3, 1, 6), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sipServerRegContactPreference.setDescription("This object indicates a relative preference for the particular\nContact header field value compared to other bindings for this\naddress-of-record.  A registering user may provide this\npreference as a 'qvalue' parameter in the Contact header.\n\nThe format of this item is a decimal number between 0 and 1\n(for example 0.9).  Higher values indicate locations preferred\nby the user.")
sipServerRegStats = MibIdentifier((1, 3, 6, 1, 2, 1, 151, 1, 6))
sipServerRegStatsTable = MibTable((1, 3, 6, 1, 2, 1, 151, 1, 6, 1))
if mibBuilder.loadTexts: sipServerRegStatsTable.setDescription("This table contains the summary statistics objects applicable\nto all SIP Registrars in this system.")
sipServerRegStatsEntry = MibTableRow((1, 3, 6, 1, 2, 1, 151, 1, 6, 1, 1)).setIndexNames((0, "NETWORK-SERVICES-MIB", "applIndex"))
if mibBuilder.loadTexts: sipServerRegStatsEntry.setDescription("A row of summary statistics.\n\nEach row represents those objects for a particular SIP server\npresent in this system.  applIndex is used to uniquely identify\nthese instances of SIP servers and correlate them through the\ncommon framework of the NETWORK-SERVICES-MIB (RFC 2788).  The\nsame value of applIndex used in the corresponding\nSIP-COMMON-MIB is used here.")
sipServerRegStatsAcceptedRegs = MibTableColumn((1, 3, 6, 1, 2, 1, 151, 1, 6, 1, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sipServerRegStatsAcceptedRegs.setDescription("This object contains a count of the number of REGISTER requests\nthat have been accepted (status code 200) by the Registrar.\nThis includes additions of new contact information, refreshing\ncontact information, as well as requests for deletion of\ncontact information.\n\nDiscontinuities in the value of this counter can occur at\nre-initialization of the SIP entity or service.  A Management\nStation can detect discontinuities in this counter by\nmonitoring the sipServerRegStatsDisconTime object in the same\nrow.")
sipServerRegStatsRejectedRegs = MibTableColumn((1, 3, 6, 1, 2, 1, 151, 1, 6, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sipServerRegStatsRejectedRegs.setDescription("This object contains a count of the number REGISTER requests\nthat have been rejected by the Registrar.\n\nDiscontinuities in the value of this counter can occur at\nre-initialization of the SIP entity or service.  A Management\nStation can detect discontinuities in this counter by\nmonitoring the sipServerRegStatsDisconTime object in the same\nrow.")
sipServerRegStatsDisconTime = MibTableColumn((1, 3, 6, 1, 2, 1, 151, 1, 6, 1, 1, 3), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sipServerRegStatsDisconTime.setDescription("The value of the sysUpTime object when the counters for the\nregistrar statistics objects in this row last experienced a\ndiscontinuity.")
sipServerMIBConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 151, 2))
sipServerMIBCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 151, 2, 1))
sipServerMIBGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 151, 2, 2))

# Augmentions

# Groups

sipServerConfigGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 151, 2, 2, 1)).setObjects(*(("SIP-SERVER-MIB", "sipServerCfgHostAddress"), ("SIP-SERVER-MIB", "sipServerCfgHostAddressType"), ) )
if mibBuilder.loadTexts: sipServerConfigGroup.setDescription("A collection of objects providing configuration common to SIP\nProxy and Redirect servers.")
sipServerProxyConfigGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 151, 2, 2, 2)).setObjects(*(("SIP-SERVER-MIB", "sipServerCfgProxyRecursion"), ("SIP-SERVER-MIB", "sipServerCfgProxyRecordRoute"), ("SIP-SERVER-MIB", "sipServerCfgProxyStatefulness"), ("SIP-SERVER-MIB", "sipServerCfgProxyAuthDefaultRealm"), ("SIP-SERVER-MIB", "sipServerCfgProxyAuthMethod"), ) )
if mibBuilder.loadTexts: sipServerProxyConfigGroup.setDescription("A collection of objects providing configuration for SIP Proxy\nservers.")
sipServerProxyStatsGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 151, 2, 2, 3)).setObjects(*(("SIP-SERVER-MIB", "sipServerProxyStatsDisconTime"), ("SIP-SERVER-MIB", "sipServerProxyStatProxyReqFailures"), ) )
if mibBuilder.loadTexts: sipServerProxyStatsGroup.setDescription("A collection of objects providing statistics for SIP Proxy\nservers.")
sipServerRegistrarConfigGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 151, 2, 2, 4)).setObjects(*(("SIP-SERVER-MIB", "sipServerRegCurrentUsers"), ("SIP-SERVER-MIB", "sipServerRegMaxUsers"), ("SIP-SERVER-MIB", "sipServerRegMaxContactExpiryDuration"), ("SIP-SERVER-MIB", "sipServerRegDfltRegActiveInterval"), ) )
if mibBuilder.loadTexts: sipServerRegistrarConfigGroup.setDescription("A collection of objects providing configuration for SIP\nRegistrars.")
sipServerRegistrarStatsGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 151, 2, 2, 5)).setObjects(*(("SIP-SERVER-MIB", "sipServerRegStatsAcceptedRegs"), ("SIP-SERVER-MIB", "sipServerRegStatsDisconTime"), ("SIP-SERVER-MIB", "sipServerRegStatsRejectedRegs"), ) )
if mibBuilder.loadTexts: sipServerRegistrarStatsGroup.setDescription("A collection of objects providing statistics for SIP\nRegistrars.")
sipServerRegistrarUsersGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 151, 2, 2, 6)).setObjects(*(("SIP-SERVER-MIB", "sipServerRegUserDisconTime"), ("SIP-SERVER-MIB", "sipServerRegContactPreference"), ("SIP-SERVER-MIB", "sipServerRegContactDisplayName"), ("SIP-SERVER-MIB", "sipServerRegUserUri"), ("SIP-SERVER-MIB", "sipServerRegContactExpiry"), ("SIP-SERVER-MIB", "sipServerRegContactURI"), ("SIP-SERVER-MIB", "sipServerRegContactLastUpdated"), ("SIP-SERVER-MIB", "sipServerRegUserAuthenticationFailures"), ) )
if mibBuilder.loadTexts: sipServerRegistrarUsersGroup.setDescription("A collection of objects related to registered users.")

# Compliances

sipServerProxyServerCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 151, 2, 1, 1)).setObjects(*(("SIP-SERVER-MIB", "sipServerProxyConfigGroup"), ("SIP-SERVER-MIB", "sipServerConfigGroup"), ("SIP-SERVER-MIB", "sipServerProxyStatsGroup"), ) )
if mibBuilder.loadTexts: sipServerProxyServerCompliance.setDescription("The compliance statement for SIP entities acting as Proxy\nServers.")
sipRedirectServerCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 151, 2, 1, 2)).setObjects(*(("SIP-SERVER-MIB", "sipServerConfigGroup"), ) )
if mibBuilder.loadTexts: sipRedirectServerCompliance.setDescription("The compliance statement for SIP entities acting as Redirect\nServers.")
sipServerRegistrarServerCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 151, 2, 1, 3)).setObjects(*(("SIP-SERVER-MIB", "sipServerRegistrarConfigGroup"), ("SIP-SERVER-MIB", "sipServerRegistrarStatsGroup"), ("SIP-SERVER-MIB", "sipServerRegistrarUsersGroup"), ("SIP-SERVER-MIB", "sipServerConfigGroup"), ) )
if mibBuilder.loadTexts: sipServerRegistrarServerCompliance.setDescription("The compliance statement for SIP entities acting as\nRegistrars.")

# Exports

# Module identity
mibBuilder.exportSymbols("SIP-SERVER-MIB", PYSNMP_MODULE_ID=sipServerMIB)

# Objects
mibBuilder.exportSymbols("SIP-SERVER-MIB", sipServerMIB=sipServerMIB, sipServerMIBObjects=sipServerMIBObjects, sipServerCfg=sipServerCfg, sipServerCfgTable=sipServerCfgTable, sipServerCfgEntry=sipServerCfgEntry, sipServerCfgHostAddressType=sipServerCfgHostAddressType, sipServerCfgHostAddress=sipServerCfgHostAddress, sipServerProxyCfg=sipServerProxyCfg, sipServerProxyCfgTable=sipServerProxyCfgTable, sipServerProxyCfgEntry=sipServerProxyCfgEntry, sipServerCfgProxyStatefulness=sipServerCfgProxyStatefulness, sipServerCfgProxyRecursion=sipServerCfgProxyRecursion, sipServerCfgProxyRecordRoute=sipServerCfgProxyRecordRoute, sipServerCfgProxyAuthMethod=sipServerCfgProxyAuthMethod, sipServerCfgProxyAuthDefaultRealm=sipServerCfgProxyAuthDefaultRealm, sipServerProxyStats=sipServerProxyStats, sipServerProxyStatsTable=sipServerProxyStatsTable, sipServerProxyStatsEntry=sipServerProxyStatsEntry, sipServerProxyStatProxyReqFailures=sipServerProxyStatProxyReqFailures, sipServerProxyStatsDisconTime=sipServerProxyStatsDisconTime, sipServerRegCfg=sipServerRegCfg, sipServerRegCfgTable=sipServerRegCfgTable, sipServerRegCfgEntry=sipServerRegCfgEntry, sipServerRegMaxContactExpiryDuration=sipServerRegMaxContactExpiryDuration, sipServerRegMaxUsers=sipServerRegMaxUsers, sipServerRegCurrentUsers=sipServerRegCurrentUsers, sipServerRegDfltRegActiveInterval=sipServerRegDfltRegActiveInterval, sipServerRegUserTable=sipServerRegUserTable, sipServerRegUserEntry=sipServerRegUserEntry, sipServerRegUserIndex=sipServerRegUserIndex, sipServerRegUserUri=sipServerRegUserUri, sipServerRegUserAuthenticationFailures=sipServerRegUserAuthenticationFailures, sipServerRegUserDisconTime=sipServerRegUserDisconTime, sipServerRegContactTable=sipServerRegContactTable, sipServerRegContactEntry=sipServerRegContactEntry, sipServerRegContactIndex=sipServerRegContactIndex, sipServerRegContactDisplayName=sipServerRegContactDisplayName, sipServerRegContactURI=sipServerRegContactURI, sipServerRegContactLastUpdated=sipServerRegContactLastUpdated, sipServerRegContactExpiry=sipServerRegContactExpiry, sipServerRegContactPreference=sipServerRegContactPreference, sipServerRegStats=sipServerRegStats, sipServerRegStatsTable=sipServerRegStatsTable, sipServerRegStatsEntry=sipServerRegStatsEntry, sipServerRegStatsAcceptedRegs=sipServerRegStatsAcceptedRegs, sipServerRegStatsRejectedRegs=sipServerRegStatsRejectedRegs, sipServerRegStatsDisconTime=sipServerRegStatsDisconTime, sipServerMIBConformance=sipServerMIBConformance, sipServerMIBCompliances=sipServerMIBCompliances, sipServerMIBGroups=sipServerMIBGroups)

# Groups
mibBuilder.exportSymbols("SIP-SERVER-MIB", sipServerConfigGroup=sipServerConfigGroup, sipServerProxyConfigGroup=sipServerProxyConfigGroup, sipServerProxyStatsGroup=sipServerProxyStatsGroup, sipServerRegistrarConfigGroup=sipServerRegistrarConfigGroup, sipServerRegistrarStatsGroup=sipServerRegistrarStatsGroup, sipServerRegistrarUsersGroup=sipServerRegistrarUsersGroup)

# Compliances
mibBuilder.exportSymbols("SIP-SERVER-MIB", sipServerProxyServerCompliance=sipServerProxyServerCompliance, sipRedirectServerCompliance=sipRedirectServerCompliance, sipServerRegistrarServerCompliance=sipServerRegistrarServerCompliance)