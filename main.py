#!/usr/bin/env python
"""
Monkey Studio free crossplatform IDE.
Main file processes command line arguments and starts the system.
"""
import sys

import mks.config

def showHelp():
    showVersion()
    print "Command line arguments:"
    print "\t-h, --help      Show command line help"
    print "\t-v, --version   Show program version"
    """TODO
    print "\t-projects      Open the projects given as parameters (-projects project1 ...)"
    print "\t-files         Open the files given as parameters (-files file1 ...)"
    """

def showVersion():
    print "%s version %s" % (mks.config.PACKAGE_NAME, mks.config.PACKAGE_VERSION)
    print "%s & The Monkey Studio Team" % mks.config.PACKAGE_COPYRIGHTS
    print "http://%s" % mks.config.PACKAGE_DOMAIN

def main():
    #TODO QT_REQUIRE_VERSION( argc, argv, "4.5.0" );
    
    if '-v' in sys.argv or '--version' in sys.argv:
        showVersion()
        return 0
    
    if '-h' in sys.argv or '--help' in sys.argv:
        showHelp()
        return 0
    
    try:
        import PyQt4.Qsci
    except ImportError:
        print >> sys.stderr, 'Failed to import QScintilla 2 python bindings.'
        print >> sys.stderr, 'Try to install python-qscintilla2 package, or download sources from ' + \
                             'http://www.riverbankcomputing.co.uk/software/qscintilla/download'
        return -1
    
    try:
        import PyQt4.fresh
    except ImportError:
        print >> sys.stderr, 'Failed to import Fresh framework. Probably it is not installed.'
        print >> sys.stderr, 'See http://github.com/hlamer/Fresh-framework/archives/master for installation instructions'
        return -1
    
    # Special hack for ability to get help and version info even on system without PyQt and Fresh.
    from PyQt4 import QtGui, QtCore
    import mks.config
    import mks.monkeycore
    
    app = QtGui.QApplication ( sys.argv );
    
    app.setApplicationName( mks.config.PACKAGE_NAME );
    app.setOrganizationName( mks.config.PACKAGE_NAME );
    app.setOrganizationDomain( mks.config.PACKAGE_DOMAIN );
    
    QtCore.QObject.connect(app, QtCore.SIGNAL('lastWindowClosed()'),
                            app, QtCore.SLOT('quit()'))
    
    """
    // init pSettings
    //pSettings::setIniInformations();
    """
    
    """TODO replace with python module
    // parse command line arguments
    //CommandLineManager clm;
    //clm.parse();
    """
    
    """TODO
    /*Properties p;
    p.writeToFile( "properties.xml" );*/
    """
        
    """TODO
    support projects and files opening
    """
    
    # init monkey studio core
    mks.monkeycore.init();
    """TODO
    // handle command line arguments
    clm.process();
    """
    
    # execute application
    result = app.exec_()
    """TODO
    // some cleanup
    MonkeyCore::pluginsManager()->clearPlugins();
    delete MonkeyCore::settings();
    // exit code
    """
    return result

if __name__ == '__main__':
    sys.exit(main())
