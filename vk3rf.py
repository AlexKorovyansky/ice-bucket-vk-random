#!/usr/bin/env python
# -*- coding: utf-8 -*-


import logging
import webapp2
from google.appengine.api import urlfetch
import json

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

class MainHandler(webapp2.RequestHandler):

    def get_person_from_json(self, resultJson, position=-1):
        if position == -1:
            person = resultJson.get('response')[0]
            return "@%s(%s %s)" % (person.get('domain'), person.get('first_name'), person.get('last_name'))
        else:
            person = resultJson.get('response').get('items')[position]
            return "@%s(%s %s)" % (person.get('domain'), person.get('first_name'), person.get('last_name'))

    def user_alias_to_user_id(self, user_alias):
        url = "https://api.vk.com/method/users.get?user_ids=%s&fields=domain&v=5.24" % user_alias
        result = urlfetch.fetch(url=url, method=urlfetch.GET, headers={'Accept-Language': 'ru'})
        resultJson = json.loads(result.content)
        return resultJson.get('response')[0].get('id')

    def get(self):
        user_id = self.user_alias_to_user_id(self.request.get('me'))
        urlFromPerson = "https://api.vk.com/method/users.get?user_ids=%s&fields=domain&name_case=gen&v=5.24" % self.request.get('from')
        urlPersons = "https://api.vk.com/method/friends.get?user_id=%s&order=random&count=3&fields=domain&name_case=acc&v=5.24" % user_id
        resultFromPerson = urlfetch.fetch(url=urlFromPerson, method=urlfetch.GET, headers={'Accept-Language': 'ru'})
        resultPersons = urlfetch.fetch(url=urlPersons, method=urlfetch.GET, headers={'Accept-Language': 'ru'})
        
        fromPersonJson = json.loads(resultFromPerson.content)
        resultPersonsJson = json.loads(resultPersons.content)
        person_from = self.get_person_from_json(fromPersonJson)
        person_to1 = self.get_person_from_json(resultPersonsJson, 0)
        person_to2 = self.get_person_from_json(resultPersonsJson, 1)
        person_to3 = self.get_person_from_json(resultPersonsJson, 2)
        message = """Я принимаю вызов Ice Bucket Challenge от %s и вызываю %s, %s и %s.</br><br/>\r\n\r\nПожертвовать деньги в фонд по изучению ALS в рамках акции #IceBucketChallenge можно на сайте www.alsa.org (красная кнопка Donate)</br></br>\r\n\r\nСлучайная передача эстафеты сделана с помощью сайта — http://ice-bucket-vk-random.appspot.com.""" % (person_from, person_to1, person_to2, person_to3)
        logging.debug(message)
        self.response.write(message)

    def handle_exception(self, exception, debug):
        logging.exception(exception)
        self.response.write('Internal server error')
        self.response.set_status(500)


app = webapp2.WSGIApplication([
    ('/vk3rf', MainHandler)
], debug=True)
