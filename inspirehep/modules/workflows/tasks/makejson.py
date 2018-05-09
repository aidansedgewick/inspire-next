from __future__ import absolute_import, division, print_function
import json

import numpy as np


def makejson(obj, eng):

    '''
    title         = obj.extra_data['source_data']['data']['titles'][0]['title']
    abstracts     = obj.extra_data['source_data']['data']['abstracts'][0]['value']
    authors_dict  = obj.extra_data['source_data']['data']['authors']
    arxiv_eprints = obj.extra_data['source_data']['data']['arxiv_eprints']
    preprint_date = obj.extra_data['source_data']['data']['preprint_date']
    


    refs = obj.data['references']
    authors_list = []
    for i in range(len(authors_dict)):
        a_d = authors_dict[i]
        authors_list.append(a_d["full_name"])

    for i in range(len(refs)):
        r = refs[i]["reference"]
        ref_authors_list = []
        ri_authors = r["authors"]
        for j in range(len(ri_authors)):
            r_auth_dict = ri_authors[j]
            ref_authors_list.append(r_auth_dict["full_name"])

        r["authors"] = ref_authors_list
        

    object_data = {"title": title, "abstracts": abstracts, "authors": authors_list,
                    "arxiv_eprints": arxiv_eprints, "preprint_date": preprint_date, "references": refs}
    '''

    object_data = {"extra_data": obj.extra_data, "data": obj.data }
    
    with open('./arXiv.json', 'a') as f:
        json.dump(object_data, f)
        f.write("\n")
        