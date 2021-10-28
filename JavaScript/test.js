"use strict";

var water;
var req = new XMLHttpRequest;
req.overrideMimeType("application/json");
req.open('GET', 'https://gov.uk/issues/?filter=0000', true);
req.setRequestHeader('Authorization', 'Bearer ' + accessToken);
origThis = this;
var target = this;
req.onload = function() {
water = req;

req.send(null);