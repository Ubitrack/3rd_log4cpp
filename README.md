# conan-zlib

[Conan.io](https://conan.io) package for log4cpp library. 

## Add Remotes

    $ conan remote add camposs "https://conan.campar.in.tum.de/api/conan/conan-camposs"
    $ conan remote add ubitrack "https://conan.campar.in.tum.de/api/conan/conan-ubitrack"

## For Users: Use this package

### Basic setup

    $ conan install ubitrack_log4cpp/0.3.5@camposs/stable
    
### Project setup

If you handle multiple dependencies in your project is better to add a *conanfile.txt*
    
    [requires]
    ubitrack_log4cpp/0.3.5@camposs/stable

    [options]
    ubitrack_log4cpp:shared=true # false
    
    [generators]
    txt
    cmake

Complete the installation of requirements for your project running:</small></span>

    $ mkdir build && cd build && conan install .. 

Project setup installs the library (and all his dependencies) and generates the files *conanbuildinfo.txt* and *conanbuildinfo.cmake* with all the paths and variables that you need to link with your dependencies.

## For Packagers: Publish this Package

The example below shows the commands used to publish to campar conan repository. To publish to your own conan respository (for example, after forking this git repository), you will need to change the commands below accordingly. 

## Build packages

    $ conan create . ubitrack/stable

## Upload packages to server

    $ conan upload -r ubitrack ubitrack_log4cpp/0.3.5@camposs/stable --all




Notes on changes to original log4cpp library:
=============================================

This version of log4cpp is based on log4cpp 0.3.5rc3, but some improvements 
were made for the Ubitrack library:

* Less virtual functions in Category
* Category::getChainedPriority no longer walks through hierarchy, priority 
  changes instead are propagated when setPriority is called.
* Support for file name and line number: use %f (without path), %F (with path) and %l in PatternLayout
* Added LOG4CPP_DEBUG, ... macros to Category.hh for performance improvement
  and file/line numbers
* New log level: TRACE (like log4j)