import FWCore.ParameterSet.Config as cms

diphotonAnalyzer = cms.EDAnalyzer('ExoDiPhotonAnalyzer',
                                  photonCollection = cms.untracked.InputTag("photons"),
                                  ptMin = cms.untracked.double(10),
                                  hltResults = cms.untracked.InputTag("TriggerResults","","REDIGI311X"),
                                  L1Results = cms.untracked.InputTag("gtDigis"),
                                  rhoCorrection = cms.InputTag("kt6PFJets","rho"),
                                  pileupCorrection = cms.untracked.InputTag("addPileupInfo"),
                                  removeSpikes = cms.untracked.bool(False),
                                  requireTightPhotons = cms.untracked.bool(True)
)
