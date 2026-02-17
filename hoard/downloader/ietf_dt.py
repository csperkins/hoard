# Copyright (c) 2026 University of Glasgow
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import asyncio

from hoard.connector.ietf import DataTracker

class DownloaderIETFDataTracker:
    def __init__(self):
        self._dt = DataTracker()



    async def _download_person(self):
        first = True
        async for curr_person in self._dt.fetch_multi("/api/v1/person/person/"):
            print(curr_person["resource_uri"])
            #hist_uri = f"/api/v1/person/historicalperson/{curr_person['id']}/"
            #async for hist_person in await self._dt.fetch(hist_uri):
            #    print(hist_person["resource_uri"])
            #    if first:
            #        curr_person = {
            #            "ascii"               : person["ascii"],
            #            "ascii_short"         : person["ascii_short"],
            #            "biography"           : person["biography"],
            #            "id"                  : person["id"],
            #            "name"                : person["name"],
            #            "name_from_draft"     : person["name_from_draft"],
            #            "plain"               : person["plain"],
            #            "pronouns_freetext"   : person["pronouns_freetext"],
            #            "pronouns_selectable" : person["pronouns_selectable"],
            #            "resource_uri"        : person["resource_uri"],
            #            "time"                : person["time"]
            #        }
            #        print(hist_person)
            #    first = False



    async def update(self):
        endpoints = {
            "/api/v1/community/communitylist/":             None,
            "/api/v1/community/emailsubscription/":         None,
            "/api/v1/community/searchrule/":                None,
            "/api/v1/dbtemplate/dbtemplate/":               None,
            "/api/v1/doc/addedmessageevent/":               None,
            "/api/v1/doc/ballotdocevent/":                  None,
            "/api/v1/doc/ballotpositiondocevent/":          None,
            "/api/v1/doc/ballottype/":                      None,
            "/api/v1/doc/bofreqeditordocevent/":            None,
            "/api/v1/doc/bofreqresponsibledocevent/":       None,
            "/api/v1/doc/consensusdocevent/":               None,
            "/api/v1/doc/deletedevent/":                    None,
            "/api/v1/doc/docevent/":                        None,
            "/api/v1/doc/docextresource/":                  None,
            "/api/v1/doc/dochistory/":                      None,
            "/api/v1/doc/dochistoryauthor/":                None,
            "/api/v1/doc/docreminder/":                     None,
            "/api/v1/doc/document/":                        None,
            "/api/v1/doc/documentactionholder/":            None,
            "/api/v1/doc/documentauthor/":                  None,
            "/api/v1/doc/documenturl/":                     None,
            "/api/v1/doc/editedauthorsdocevent/":           None,
            "/api/v1/doc/editedrfcauthorsdocevent/":        None,
            "/api/v1/doc/ianaexpertdocevent/":              None,
            "/api/v1/doc/initialreviewdocevent/":           None,
            "/api/v1/doc/irsgballotdocevent/":              None,
            "/api/v1/doc/lastcalldocevent/":                None,
            "/api/v1/doc/newrevisiondocevent/":             None,
            "/api/v1/doc/relateddochistory/":               None,
            "/api/v1/doc/relateddocument/":                 None,
            "/api/v1/doc/reviewassignmentdocevent/":        None,
            "/api/v1/doc/reviewrequestdocevent/":           None,
            "/api/v1/doc/rfcauthor/":                       None,
            "/api/v1/doc/state/":                           None,
            "/api/v1/doc/statedocevent/":                   None,
            "/api/v1/doc/statetype/":                       None,
            "/api/v1/doc/storedobject/":                    None,
            "/api/v1/doc/submissiondocevent/":              None,
            "/api/v1/doc/telechatdocevent/":                None,
            "/api/v1/doc/writeupdocevent/":                 None,
            "/api/v1/group/appeal/":                        None,
            "/api/v1/group/appealartifact/":                None,
            "/api/v1/group/changestategroupevent/":         None,
            "/api/v1/group/group/":                         None,
            "/api/v1/group/groupevent/":                    None,
            "/api/v1/group/groupextresource/":              None,
            "/api/v1/group/groupfeatures/":                 None,
            "/api/v1/group/grouphistory/":                  None,
            "/api/v1/group/groupmilestone/":                None,
            "/api/v1/group/groupmilestonehistory/":         None,
            "/api/v1/group/groupstatetransitions/":         None,
            "/api/v1/group/groupurl/":                      None,
            "/api/v1/group/milestonegroupevent/":           None,
            "/api/v1/group/role/":                          None,
            "/api/v1/group/rolehistory/":                   None,
            "/api/v1/iesg/telechatagendacontent/":          None,
            "/api/v1/iesg/telechatagendaitem/":             None,
            "/api/v1/iesg/telechatdate/":                   None,
            "/api/v1/ipr/genericiprdisclosure/":            None,
            "/api/v1/ipr/holderiprdisclosure/":             None,
            "/api/v1/ipr/iprdisclosurebase/":               None,
            "/api/v1/ipr/iprdocrel/":                       None,
            "/api/v1/ipr/iprevent/":                        None,
            "/api/v1/ipr/legacymigrationiprevent/":         None,
            "/api/v1/ipr/nondocspecificiprdisclosure/":     None,
            "/api/v1/ipr/relatedipr/":                      None,
            "/api/v1/ipr/removediprdisclosure/":            None,
            "/api/v1/ipr/thirdpartyiprdisclosure/":         None,
            "/api/v1/liaisons/liaisonstatement/":           None,
            "/api/v1/liaisons/liaisonstatementattachment/": None,
            "/api/v1/liaisons/liaisonstatementevent/":      None,
            "/api/v1/liaisons/relatedliaisonstatement/":    None,
            "/api/v1/mailinglists/allowlisted/":            None,
            "/api/v1/mailinglists/nonwgmailinglist/":       None,
            "/api/v1/mailtrigger/historicalmailtrigger/":   None,
            "/api/v1/mailtrigger/historicalrecipient/":     None,
            "/api/v1/mailtrigger/mailtrigger/":             None,
            "/api/v1/mailtrigger/recipient/":               None,
            "/api/v1/meeting/attended/":                    None,
            "/api/v1/meeting/businessconstraint/":          None,
            "/api/v1/meeting/constraint/":                  None,
            "/api/v1/meeting/floorplan/":                   None,
            "/api/v1/meeting/importantdate/":               None,
            "/api/v1/meeting/meeting/":                     None,
            "/api/v1/meeting/meetinghost/":                 None,
            "/api/v1/meeting/proceedingsmaterial/":         None,
            "/api/v1/meeting/registration/":                None,
            "/api/v1/meeting/registrationticket/":          None,
            "/api/v1/meeting/resourceassociation/":         None,
            "/api/v1/meeting/room/":                        None,
            "/api/v1/meeting/schedtimesessassignment/":     None,
            "/api/v1/meeting/schedule/":                    None,
            "/api/v1/meeting/schedulingevent/":             None,
            "/api/v1/meeting/session/":                     None,
            "/api/v1/meeting/sessionpresentation/":         None,
            "/api/v1/meeting/slidesubmission/":             None,
            "/api/v1/meeting/timeslot/":                    None,
            "/api/v1/meeting/urlresource/":                 None,
            "/api/v1/message/announcementfrom/":            None,
            "/api/v1/message/message/":                     None,
            "/api/v1/message/messageattachment/":           None,
            "/api/v1/message/sendqueue/":                   None,
            "/api/v1/name/agendafiltertypename/":           None,
            "/api/v1/name/agendatypename/":                 None,
            "/api/v1/name/appealartifacttypename/":         None,
            "/api/v1/name/attendancetypename/":             None,
            "/api/v1/name/ballotpositionname/":             None,
            "/api/v1/name/constraintname/":                 None,
            "/api/v1/name/continentname/":                  None,
            "/api/v1/name/countryname/":                    None,
            "/api/v1/name/dbtemplatetypename/":             None,
            "/api/v1/name/docrelationshipname/":            None,
            "/api/v1/name/docremindertypename/":            None,
            "/api/v1/name/doctagname/":                     None,
            "/api/v1/name/doctypename/":                    None,
            "/api/v1/name/docurltagname/":                  None,
            "/api/v1/name/draftsubmissionstatename/":       None,
            "/api/v1/name/extresourcename/":                None,
            "/api/v1/name/extresourcetypename/":            None,
            "/api/v1/name/feedbacktypename/":               None,
            "/api/v1/name/formallanguagename/":             None,
            "/api/v1/name/groupmilestonestatename/":        None,
            "/api/v1/name/groupstatename/":                 None,
            "/api/v1/name/grouptypename/":                  None,
            "/api/v1/name/importantdatename/":              None,
            "/api/v1/name/intendedstdlevelname/":           None,
            "/api/v1/name/iprdisclosurestatename/":         None,
            "/api/v1/name/ipreventtypename/":               None,
            "/api/v1/name/iprlicensetypename/":             None,
            "/api/v1/name/liaisonstatementeventtypename/":  None,
            "/api/v1/name/liaisonstatementpurposename/":    None,
            "/api/v1/name/liaisonstatementstate/":          None,
            "/api/v1/name/liaisonstatementtagname/":        None,
            "/api/v1/name/meetingtypename/":                None,
            "/api/v1/name/nomineepositionstatename/":       None,
            "/api/v1/name/proceedingsmaterialtypename/":    None,
            "/api/v1/name/registrationtickettypename/":     None,
            "/api/v1/name/reviewassignmentstatename/":      None,
            "/api/v1/name/reviewerqueuepolicyname/":        None,
            "/api/v1/name/reviewrequeststatename/":         None,
            "/api/v1/name/reviewresultname/":               None,
            "/api/v1/name/reviewtypename/":                 None,
            "/api/v1/name/rolename/":                       None,
            "/api/v1/name/roomresourcename/":               None,
            "/api/v1/name/sessionpurposename/":             None,
            "/api/v1/name/sessionstatusname/":              None,
            "/api/v1/name/slidesubmissionstatusname/":      None,
            "/api/v1/name/stdlevelname/":                   None,
            "/api/v1/name/streamname/":                     None,
            "/api/v1/name/telechatagendasectionname/":      None,
            "/api/v1/name/timerangename/":                  None,
            "/api/v1/name/timeslottypename/":               None,
            "/api/v1/name/topicaudiencename/":              None,
            "/api/v1/nomcom/feedback/":                     None,
            "/api/v1/nomcom/feedbacklastseen/":             None,
            "/api/v1/nomcom/nomcom/":                       None,
            "/api/v1/nomcom/nomination/":                   None,
            "/api/v1/nomcom/nominee/":                      None,
            "/api/v1/nomcom/nomineeposition/":              None,
            "/api/v1/nomcom/position/":                     None,
            "/api/v1/nomcom/reminderdates/":                None,
            "/api/v1/nomcom/topic/":                        None,
            "/api/v1/nomcom/topicfeedbacklastseen/":        None,
            "/api/v1/nomcom/volunteer/":                    None,
            "/api/v1/person/alias/":                        None,
            "/api/v1/person/email/":                        None,
            "/api/v1/person/historicalemail/":              None,
            "/api/v1/person/historicalperson/":             self._download_person,
            "/api/v1/person/person/":                       self._download_person,
            "/api/v1/person/personalapikey/":               None,
            "/api/v1/person/personapikeyevent/":            None,
            "/api/v1/person/personevent/":                  None,
            "/api/v1/person/personextresource/":            None,
            "/api/v1/redirects/command/":                   None,
            "/api/v1/redirects/redirect/":                  None,
            "/api/v1/redirects/suffix/":                    None,
            "/api/v1/review/historicalreviewassignment/":   None,
            "/api/v1/review/historicalreviewersettings/":   None,
            "/api/v1/review/historicalreviewrequest/":      None,
            "/api/v1/review/historicalunavailableperiod/":  None,
            "/api/v1/review/nextreviewerinteam/":           None,
            "/api/v1/review/reviewassignment/":             None,
            "/api/v1/review/reviewersettings/":             None,
            "/api/v1/review/reviewrequest/":                None,
            "/api/v1/review/reviewsecretarysettings/":      None,
            "/api/v1/review/reviewteamsettings/":           None,
            "/api/v1/review/reviewwish/":                   None,
            "/api/v1/review/unavailableperiod/":            None,
            "/api/v1/stats/affiliationalias/":              None,
            "/api/v1/stats/affiliationignoredending/":      None,
            "/api/v1/stats/countryalias/":                  None,
            "/api/v1/stats/meetingregistration/":           None,
            "/api/v1/submit/preapproval/":                  None,
            "/api/v1/submit/submission/":                   None,
            "/api/v1/submit/submissioncheck/":              None,
            "/api/v1/submit/submissionemailevent/":         None,
            "/api/v1/submit/submissionevent/":              None,
            "/api/v1/submit/submissionextresource/":        None,
            "/api/v1/utils/dumpinfo/":                      None,
        }

        actions = []
        for e1 in await self._dt.fetch("/api/v1/"):
            for e2 in await self._dt.fetch(f"/api/v1/{e1}/"):
                endpoint = f"/api/v1/{e1}/{e2}/"
                if endpoint not in endpoints:
                    print(f"WARNING: no disposition for DataTracker endpoint: {endpoint}")
                else:
                    action = endpoints[endpoint]
                    if action is not None and action not in actions:
                        actions.append(endpoints[endpoint])

        for action in actions:
            await action()

        await self._dt.close()


# vim: set tw=0 ai:
