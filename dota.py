#!/usr/bin/env python
#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.

#You should have received a copy of the GNU General Public License
#along with this program.  If not, see <http://www.gnu.org/licenses/>.

import json
import urllib2
import config

class Dota(object):
    url = 'https://api.steampowered.com/IDOTA2Match_570/%s/V001/?'
    lang = 'en_us'

    def __get(self, method, *args, **kwargs):
        kwargs['key'] = config.apiKey
        url = self.url % (method) + '&'.join([str(keys) + '=' + str(items) for keys, items in kwargs.items()])
        return json.loads(urllib2.urlopen(url).read())

    def match_history(self, *args, **kwargs):
        return self.__get('GetMatchHistory', *args, **kwargs)

    def match_details(self, matchid):
        return self.__get('GetMatchDetails', match_id=matchid)

    def league_listing(self):
        return self.__get('GetLeagueListing', langage=self.lang)

    def live_league_games(self):
        return self.__get('GetLiveLeagueGames', language=self.lang)

if __name__ == '__main__':
    d = Dota()
    games = d.live_league_games()
    for g in games['result']['games']:
        print g
        print '"%s" vs "%s"' % (g['dire_team']['team_name'],
                                g['radiant_team']['team_name'])
