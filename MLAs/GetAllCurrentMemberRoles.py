import requests
import json
from datetime import datetime
from dateutil import parser
import unicodecsv as csv

CurrentMembersUrl = 'http://data.niassembly.gov.uk/members_json.ashx?m=GetAllCurrentMembers'
MemberRoleUrl = 'http://data.niassembly.gov.uk/members_json.ashx?m=GetMemberRolesByPersonId'

fullList = []

resp = requests.get(CurrentMembersUrl)
resp.encoding = 'utf-8'
print(resp.url)
json_result = resp.json()
for i in json_result['AllMembersList']['Member']:
    params = {'personId': i['PersonId']}
    r = requests.get(MemberRoleUrl, params = params)
    r.encoding = 'utf-8'
    json_result = r.json()
    for k in json_result['AllMembersRoles']['Role']:
        MLA = []
        MLA.append(i['AffiliationId'])
        MLA.append(i['PersonId'])
        MLA.append(i['MemberFirstName'])
        MLA.append(i['MemberLastName'])
        MLA.append(k['MemberFullDisplayName'])
        MLA.append(i['PartyOrganisationId'])
        MLA.append(i['PartyName'])
        MLA.append(k['RoleType'])
        if 'OrganisationId' not in k:
            MLA.append('')
        else:
            MLA.append(k['OrganisationId'])
        if 'Organisation' not in k:
            MLA.append('')
        else:
            MLA.append(k['Organisation'])
        if 'AffiliationTitle' not in k:
            MLA.append('')
        else:
            MLA.append(k['AffiliationTitle'])
        MLA.append(parser.parse(k['AffiliationStart']).strftime('%Y-%m-%d'))
        if 'AffiliationEnd' not in k:
            MLA.append('')
            MLA.append('YES')
        else:
            MLA.append(parser.parse(k['AffiliationEnd']).strftime('%Y-%m-%d'))
            MLA.append('NO')
        fullList.append(MLA)

with open('member_roles.csv', 'wb') as csvfile:
    w = csv.writer(csvfile, quoting=csv.QUOTE_MINIMAL)
    w.writerow(['AffiliationId','PersonId','Firstname','Lastname','MemberFullDisplayName','PartyOrganisationId','PartyName','RoleType','OrganisationId','Organisation','Title','Start','End','CurrentRole'])
    for i in fullList:
        w.writerow(i)
