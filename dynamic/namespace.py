#!/usr/bin/env python

from dynamic.search import Search
class Namespace:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

nameSpace_Mappings = {
    "dynamic -v" : Namespace(DELETE=False, GET=False, POST=False, custom=False, 
                  file=False, new=None, notion=False, playbook=False, 
                  search=False, update=False, version=True, start=False ),

    "dynamic -s" : Namespace(DELETE=False, GET=False, POST=False, custom=False, 
                  file=False, new=None, notion=False, playbook=False, 
                  search=True, update=False, version=False, start=False ),

    "dynamic -no" : Namespace(DELETE=False, GET=False, POST=False, custom=False, 
                  file=False, new=None, notion=True, playbook=False, 
                  search=False, update=False, version=False, start=False ),
    
    "dynamic -c" : Namespace(DELETE=False, GET=False, POST=False, custom=True, 
                  file=False, new=None, notion=False, playbook=False, 
                  search=False, update=False, version=False, start=False ),

    "dynamic -p" : Namespace(DELETE=False, GET=False, POST=False, custom=False, 
                  file=False, new=None, notion=False, playbook=True, 
                  search=False, update=False, version=False, start=False ),

    "dynamic -GET" : Namespace(DELETE=False, GET=True, POST=False, custom=False, 
                  file=False, new=None, notion=False, playbook=False, 
                  search=False, update=False, version=False, start=False ),
    
    "dynamic -POST" : Namespace(DELETE=False, GET=False, POST=True, custom=False, 
                  file=False, new=None, notion=False, playbook=False, 
                  search=False, update=False, version=False, start=False ),

    "dynamic -DELETE" : Namespace(DELETE=True, GET=False, POST=False, custom=False, 
                  file=False, new=None, notion=False, playbook=False, 
                  search=False, update=False, version=False, start=False ),
    "dynamic -st" : Namespace(DELETE=True, GET=False, POST=False, custom=False, 
                  file=False, new=None, notion=False, playbook=False, 
                  search=False, update=False, version=False, start=True ),


}

def map_arguments(input):
    try:
        ARGV = nameSpace_Mappings[input]
    except KeyError:
        print("%s is an Invalid option" % input[8:len(input)])
        return
    search_flag = Search(ARGV)
    search_flag.search_args()
