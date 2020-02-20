__G__ = "(G)bd249ce4"

from os import path
from analyzer.logger.logger import verbose, verbose_flag, verbose_timeout
from analyzer.services.online.hybridanalysis import HybridAnalysis
from analyzer.services.online.malshare import MalShare
from analyzer.services.online.metadefender import MetaDefender
from analyzer.services.online.virustotal import VirusTotal
from analyzer.services.online.alienvault import AlienVault
from analyzer.services.online.pulsedive import PulseDive
from copy import deepcopy

class OnlineMultiScanners:
    @verbose(True,verbose_flag,verbose_timeout,"Starting OnlineMultiScanners")
    def __init__(self):
        tokens_full_path = path.abspath(path.join(path.dirname( __file__ ),'tokens.json'))
        file = "analyzer" + tokens_full_path.split("analyzer")[1]
        self.ha = HybridAnalysis(tokens_full_path,file)
        self.ms = MalShare(tokens_full_path,file)
        self.md = MetaDefender(tokens_full_path,file)
        self.vt = VirusTotal(tokens_full_path,file)
        self.av = AlienVault(tokens_full_path,file)
        self.pd = PulseDive(tokens_full_path,file)
        self.datastruct = {  "HybridAnalysis":"",
                             "MalShare":"",
                             "MetaDefender":"",
                             "VirusTotal":"",
                             "AlienVault":"",
                             "PulseDive":"",
                             "_____HybridAnalysis":{},
                             "_____MalShare":{},
                             "_____MetaDefender":{},
                             "_____VirusTotal":{},
                             "_____AlienVault":{},
                             "_____PulseDive":{}}

    @verbose(True,verbose_flag,verbose_timeout,"Checking hash in online multiscanners services")
    def analyze(self,data,parsed):
        data["ONLINEMULTISCANNERS"] = deepcopy(self.datastruct)
        data["ONLINEMULTISCANNERS"]["HybridAnalysis"] = self.ha.get_hash_details(data["Details"]["Properties"]["md5"])
        data["ONLINEMULTISCANNERS"]["MalShare"] = self.ms.get_hash_details(data["Details"]["Properties"]["md5"])
        data["ONLINEMULTISCANNERS"]["MetaDefender"] = self.md.get_hash_details(data["Details"]["Properties"]["md5"])
        data["ONLINEMULTISCANNERS"]["VirusTotal"] = self.vt.get_hash_details(data["Details"]["Properties"]["md5"])
        data["ONLINEMULTISCANNERS"]["AlienVault"] = self.av.get_hash_details(data["Details"]["Properties"]["md5"])
        data["ONLINEMULTISCANNERS"]["PulseDive"] = self.pd.get_hash_details(data["Details"]["Properties"]["md5"])