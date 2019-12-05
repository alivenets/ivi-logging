from conans import ConanFile, CMake, tools


class IviLoggingConan(ConanFile):
    name = "ivi-logging"
    version = "1.3.0"
    license = "<Put the package license here>"
    author = "<Put your name here> <And your email here>"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "<Description of Ivilogging here>"
    topics = ("<Put some tag here>", "<here>", "<and here>")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], 'with_dlt': [True, False], 'with_console': [True, False]}
    default_options = {"shared": True, 'with_dlt': False, 'with_console': True}
    generators = ("cmake", "pkg_config",)

# TODO: add conditional dependencies on dlt-daemon

    def source(self):
        self.run("git clone https://github.com/Pelagicore/ivi-logging.git")
        # This small hack might be useful to guarantee proper /MT /MD linkage
        # in MSVC if the packaged project doesn't have variables to set it
        # properly
#        tools.replace_in_file("hello/CMakeLists.txt", "PROJECT(HelloWorld)",
#                              '''PROJECT(HelloWorld)
#include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
#conan_basic_setup()''')

    def _configure_cmake(self):
        cmake = CMake(self)

        for option_name in self.options.values.fields:
            activated = getattr(self.options, option_name)
            if option_name == "with_dlt":
                cmake.definitions['ENABLE_DLT_BACKEND'] = "ON" if activated else "OFF"
            elif option_name == "with_console":
                cmake.definitions['ENABLE_CONSOLE_BACKEND'] = "ON" if activated else "OFF"

        cmake.configure(source_dir="ivi-logging")
        return cmake

    def build(self):
        cmake = self._configure_cmake()
        cmake.build()

        # Explicit way:
        # self.run('cmake %s/hello %s'
        #          % (self.source_folder, cmake.command_line))
        # self.run("cmake --build . %s" % cmake.build_config)

    def package(self):
        cmake = self._configure_cmake()
        cmake.install()
#        self.copy("*.h", dst="include", src="include")
#        self.copy("*hello.lib", dst="lib", keep_path=False)
#        self.copy("*.dll", dst="bin", keep_path=False)
#        self.copy("*.so", dst="lib", keep_path=False)
#        self.copy("*.dylib", dst="lib", keep_path=False)
#        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["ivi-logging"]

