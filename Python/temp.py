#!/usr/bin/python
import json

def get():
    Service = "myservice"
    UniqueID = "888888"
    Device = "DEV1"
    Pagepath = "/page1/666"
    NumVisit = "300"
    resp = []
    #resp.append({'name': Service,
    #             'data': {'UniqueID': UniqueID,
    #                      'details': { 'Device':Device,'Pagepath':Pagepath,'NumVisit':NumVisit}}})
    resp.append({'name': Service, 'data': {'UniqueID': UniqueID, 'details': { 'Device':Device,'Pagepath':Pagepath,'NumVisit':NumVisit}}})

    print(json.dumps(resp))
    return json.dumps(resp)

get()
