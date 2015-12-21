import sys
sys.path.append(r"C:\apps\FME\fmeobjects\python27")
import fmeobjects

def RunMyWorkspace():
    try:
        #initiate FMEWorkspaceRunner Class 
        runner = fmeobjects.FMEWorkspaceRunner() 
        #Full path to Workspace, example comes from the FME 2014 Training Full Dataset
        workspace = r'C:\GCT\R&D\Perma_Creep\PermaCreepNoLanguageStats.fmw'
        #Set workspace parameters by creating a dictionary of name value pairs
        parameters = {}
        parameters['Output_CSV'] = r'C:\GCT\R&D\Perma_Creep'
        #parameters['not_geotagged'] = r'C:\GCT\R&D\Perma_Creep'
        runner.runWithParameters(workspace, parameters)
    except Exception:
        print "exception hit"
        RunMyWorkspace()
        
RunMyWorkspace()
