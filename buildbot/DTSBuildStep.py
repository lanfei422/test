# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 15:55:40 2017

@author: yanlf
"""
from buildbot.process import buildstep
from twisted.internet import defer

class RunTestScript(buildstep.ShellMixin,buildstep.BuildStep):
    def __init__(self,testScript="./run.sh",retrieveFile="regex",**kwargs):
        self.testScript=testScript
        kwargs=self.setupShellMixin(kwargs,prohibitArgs=['command'])
        buildstep.BuildStep.__init__(self,**kwargs)
        
    @defer.inlineCallbacks
    def run(self):
        cmd=yield self.makeRemoteShellCommand(command=[self.testScript])
        yield self.runCommand(cmd)
        
        if cmd.didiFail():
            cmd=yield self.makeRemoteShellCommand([self.testScript,'--force'],logEnviron=False)
            yield self.runCommand(cmd)
        defer.returnValue(cmd.results())
        
@defer.inlineCallbacks
def run(self):
    cmd = RemoteCommand(args)
    log = yield self.addLog('output')
    cmd.useLog(log, closeWhenFinished=True)
    yield self.runCommand(cmd)