import ldap

def get_members(dn, conn):
    if dn == b'cn=dc=gov,dc=uk':
        try:
            results = conn.search_s(dn.decode('ascii'), ldap.SCOPE_SUBTREE, '(objectClass=*)', ["uniqueMember"])
            print(results)
            return results[0][1]["uniqueMember"]
        except ldap.NO_SUCH_OBJECT:
            return None

def remove_member(dn, conn):
    try:
        results = conn.search_s(dn.decode('ascii'), ldap.SCOPE_SUBTREE, '(objectClass=*)', ["uniqueMember"])
        return results[0][1]["uniqueMember"]
    except ldap.NO_SUCH_OBJECT:
        return None

ldap.set_option(ldap.OPT_X_TLS_REQUIRE_CERT, ldap.OPT_X_TLS_ALLOW)
conn_ro = ldap.initialize('ldaps://gov.uk:636', bytes_mode=False)
conn_ro.simple_bind_s('cn=nikhil.sharma,dc=gov,dc=uk', '<<<')

query1 = '(uid=nikhil.sharma)'
results = conn_ro.search_s('dc=gov,dc=uk', ldap.SCOPE_SUBTREE, query1, ["memberOf"])

dns = results[0][1]["memberOf"]

for dn in dns:
    members = get_members(dn, conn_ro)

    if members is not None:
        print(members)

