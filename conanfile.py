from conans import ConanFile, CMake, tools
import os


class Ubitracklog4cppConan(ConanFile):
    name = "ubitrack_log4cpp"
    version = "0.3.5"
    license = "http://log4cpp.sourceforge.net/#license"
    url = "https://github.com/Ubitrack/3rd_log4cpp"
    description = "Log4cpp is library of C++ classes for flexible logging to files, syslog, IDSA and other destinations. It is modeled after the Log4j Java library, staying as close to their API as is reasonable."
    options = {"shared": [True, False]}
    default_options = "shared=False"
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"
    exports_sources = "include/*", "src/*", "CMakeLists.txt"

    def build(self):
        cmake = CMake(self)
        cmake.definitions["BUILD_SHARED_LIBS"] = self.options.shared
        cmake.configure()
        cmake.build()
        cmake.install()

    def package_info(self):
        if self.options.shared and self.settings.os == "Windows":
            self.cpp_info.defines.append("LOG4CPP_HAS_DLL")
        suffix = ""
        if self.settings.build_type == "Debug":
            suffix = "_d"
        self.cpp_info.libs.append("log4cpp%s" % (suffix,))
