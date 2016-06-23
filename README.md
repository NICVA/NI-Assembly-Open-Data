# NI-Assembly-Open-Data
Extracting, creating and utilising useful information from the NI Assembly Open Data

## MLAs
### GetAllCurrentMemberRoles
Assembly Open Data API has [GetAllMemberRoles](http://data.niassembly.gov.uk/members_json.ashx?m=GetAllMemberRoles). Returns a list of all roles held by all [current] MLAs. However, this excludes former roles held by current MLAs. The script searches for every role held by every current member using the [GetMemberRolesByPersonId](http://data.niassembly.gov.uk/members.asmx?op=GetMemberRolesByPersonId_JSON) request.
