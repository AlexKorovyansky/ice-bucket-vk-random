#!/usr/bin/env python
# -*- coding: utf-8 -*-

import webapp2
from google.appengine.api import urlfetch
import json

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

class MainHandler(webapp2.RequestHandler):

    def get(self):
        self.response.write(
            """
                <head>
                    <meta http-equiv="Content-Type" content="text/html;charset=UTF-8">
                    <link rel="stylesheet" type="text/css" href="css/site.css">
                    <style>
                        body {
                            margin: 0;
                            height: 100%;
                            background: url(static/back.jpg) no-repeat center center fixed; 
                            -webkit-background-size: cover;
                            -moz-background-size: cover;
                            -o-background-size: cover;
                            background-size: cover;
                        }
                    </style>
                    <script type="text/javascript" src="js/jquery-1.11.1.min.js"></script>
                    <script>
                        function randomAction() {
                            $('#input-container').css("visibility","hidden");
                            $('#result-container').css("visibility","hidden");
                            $('#progress').css("visibility","visible");
                            $.ajax({
                                url: "vk3rf",
                                data: {me: window.me, from: window.from},
                                success: function(message) {
                                    window.wasSuccess = true;
                                    $('#progress').css("visibility","hidden");
                                    $('#result-container').css("visibility","visible");
                                    $('#result-text').html(message);
                                    $("#result-final-button").click(function(){
                                        $("#result-copy-button").click();
                                    });
                                },
                                error: function(XMLHttpRequest, textStatus, errorThrown) { 
                                    $('#progress').css("visibility","hidden");
                                    if (window.wasSuccess) {
                                        $('#result-container').css("visibility","visible");
                                        alert('Ошибка при выполнении операции! Пожалуйста, повторите попытку позже.');
                                    } else {
                                        $('#input-container').css("visibility","visible");
                                        alert('Ошибка при выполнении операции! Пожалуйста удостоверьтесь, что вы ввели корректные ScreenName-ы пользователей, после чего повторите попытку.');
                                    }
                                }
                            });     
                        }
                        //DOM loaded 
                        $(document).ready(function() {
                            $('.nick101').each(function(){ $(this).click(function() {window.open("static/nick101.png");}); });
                            $('#input-action-button').click(function(){
                                window.me = $("#input-me").val();
                                window.from = $("#input-from").val();
                                randomAction();
                            });
                            $('#result-repeat-button').click(function(){
                                randomAction();
                            });
                            $("#result-final-button").click(function(){
                                window.open('http://vk.com');
                            });
                        });
                    </script>
                    <title>Ice Bucket Random Challenge</title>
                </head>
                <body>
                    <div id="input-container" class="centered" style="visibility:visible; padding:20px 30px 15px 30px; background:rgba(255, 255, 255, 0.9)">
                        <div style="margin-bottom:10px">
                            <fieldset>
                                <legend style="font-size:21px">ALS Ice Bucket Challenge:</legend>
                                <div style="margin-top:8px">Ваш nickname ВКонтакте: <span class="nick101">(?)</span></div>
                                <input id="input-me" type="text" style="font-size:17px; margin-top:4px; margin-right:30px; margin-bottom:15px; width: 100%" placeholder="Например, korovyansk"><br>
                                <div>Nickname того, кто передал вам эстафету: <span class="nick101">(?)</span></div>
                                <input id="input-from" type="text" name="from" style="font-size:17px; margin-top:4px; margin-right:30px; margin-bottom:30px; width: 100%" placeholder="Например, omskhawk"><br>
                                <input id="input-action-button" type="submit" class="button orange" style="width:100%; height:60px; font-size:18px" value="Передать 3 случайным VK-друзьям">
                            </fieldset>
                        </div>
                        <a class="left" target="_blank" href="http://youtu.be/jOknV4M03BU">Что это?</a>
                        <a class="right" target="_blank" href="http://github.com/korovyansk/ice-bucket-vk-random">Fork Me on GitHub</a>
                    </div>
                    <div id="progress" class="centered" style="visibility:hidden; padding:20px; text-align:center; background:rgba(255, 255, 255, 0.9)">
                        <div style="margin-bottom:4px">
                            Пожалуйста подождите...
                        </div>
                        <progress></progress>
                    </div>
                    <div id="result-container" class="centered" style="visibility:hidden; padding:20px; background:rgba(255, 255, 255, 0.9);">
                        <div id="result-text">
                            Text text text
                        </div>
                        <div style="margin-top:20px">
                            <button id="result-repeat-button" class="button left" style="text-align:center;height:40px;">Ещё раз</button>
                            <button id="result-final-button" class="button orange right" style="text-align:center;height:40px;">На сайт VK</a>
                        </div>
                    </div>
                <body>""")

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
