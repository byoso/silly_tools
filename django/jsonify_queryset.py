#! /usr/bin/env python3
# coding: utf-8


def jsonify(a_query_set):
    """Convert a Django queryset into a json format"""
    attrs = []
    list_json = []
    if len(a_query_set) > 0:
        for i in a_query_set[0]._meta.fields:
            attrs.append(i.name)
        for i in a_query_set:
            json_object = {}
            for attr in attrs:
                json_object[attr] = str(getattr(i, attr))
            list_json.append(json_object)
        return list_json
    else:
        return []
