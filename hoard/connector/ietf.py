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

import logging
import os
import requests
import sys
import time

from typing            import List, Optional, Tuple, Dict, Iterator, Type, TypeVar, Any, Generic
from typing_extensions import Self

class DataTracker:
    def __init__(self):
        logging.basicConfig(level=os.getenv("IETFDATA_LOGLEVEL", default="INFO"))
        self._ua          = "glasgow-ietfdata/0.9.0 (hoard)"  # Update when making a new relaase
        self._base_url    = os.environ.get("IETFDATA_DT_URL", "https://datatracker.ietf.org")
        self._multi_delay = 0.1
        self._session     = requests.Session()
        self._log         = logging.getLogger("hoard.connector.ietf")
        self._log.info(f"Connecting to IETF DataTracker at {self._base_url}")


    def close(self):
        self._session.close()


    def fetch(self, endpoint: str) -> Optional[Dict[str, Any]]:
        """
        Fetch the data for a single API endpoint from the datatracker:
        """
        assert endpoint.startswith("/api/v1/")
        retry_delay = 1.875
        while True:
            try:
                r = self._session.get(self._base_url + endpoint, headers={'User-Agent': self._ua})
                self._log.debug(f"fetch: {r.status_code} {endpoint}")
                if r.status_code == 200:
                    res = r.json() # type: Dict[str,Any]
                    return res
                elif r.status_code == 400:
                    self._log.error(f"fetch: bad request {self._base_url}{endpoint}")
                    sys.exit(1)
                elif r.status_code == 404:
                    return None
                elif r.status_code == 429:
                    retry_after = int(r.headers['Retry-After']) 
                    if retry_after != 0:
                        self._log.warning(f"fetch: rate limited, will retry in {retry_after}s")
                        time.sleep(retry_after)
                        # Increase the delay between repeated fetches, to try to avoid
                        # rate limiting in future:
                        self._multi_delay *= 1.1
                        self._log.debug(f"fetch: multi_delay now {self._multi_delay}s")
                    else:
                        # Some versions of the datatracker incorrectly send 429 with "Retry-After: 0".
                        # Handle this with an exponential backoff as-if we got a 500 error.
                        self._log.warning(f"fetch: rate limited, will retry in {retry_delay}s (implicit)")
                        if retry_delay > 60:
                            self._log.error(f"fetch: retry limit exceeded")
                            sys.exit(1)
                        time.sleep(retry_delay)
                        retry_delay *= 2
                else:
                    self._log.warning(f"fetch: received {r.status_code} response, will retry in {retry_delay}s")
                    if retry_delay > 60:
                        self._log.error(f"fetch: retry limit exceeded")
                        sys.exit(1)
                    time.sleep(retry_delay)
                    retry_delay *= 2
            except requests.exceptions.ConnectionError:
                self._log.warning(F"fetch: connection error, will retry in {retry_delay}s")
                if retry_delay > 60:
                    self._log.error(f"fetch: retry limit exceeded")
                    sys.exit(1)
                time.sleep(retry_delay)
                retry_delay *= 2


    def fetch_multi(self, endpoint: str) -> Iterator[Dict[str, Any]]:
        uri = endpoint
        while uri is not None:
            r = self.fetch(uri)
            if r is None:
                # Sometimes the datatracker will return a 404 error for a URL
                # returned in the r["meta"]["next"] field of the previous value. 
                # This appears to be due to corrupt values in the database.
                # In the following, we attempt to correct for this, by fetching
                # the items in the query one-by-one, returning any that succeed.
                # If any succeed, we then construct an appropriate next URL and 
                # continue the multi fetch.
                if "?limit=" in uri and "&offset=" in uri:
                    self._log.warning(f"fetch_multi: cannot fetch {uri} - trying individual")
                    found_some = False
                    limit_pos  = uri.find("?limit=")
                    offset_pos = uri.find("&offset=")
                    base   = uri[:limit_pos-1]
                    limit  = int(uri[limit_pos+7:offset_pos])
                    offset = int(uri[offset_pos+8:])
                    for index in range(offset, offset+limit):
                        item_uri = f"{base}/?limit=1&offset={index}"
                        r = self.fetch(item_uri)
                        if r is not None:
                            found_some = True
                            for obj in r["objects"]:
                                yield obj
                    if not found_some:
                        break
                    uri = f"{base}/?limit={limit}&offset={offset+limit}"
                else:
                    break
            else:
                for obj in r["objects"]:
                    yield obj
                uri = r["meta"]["next"]
            # Rate limit the fetch of large amounts of data
            time.sleep(self._multi_delay)

# vim: set tw=0 ai:
