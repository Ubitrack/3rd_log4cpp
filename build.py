from conan.packager import ConanMultiPackager

if __name__ == "__main__":
    builder = ConanMultiPackager()
    builder.add_common_builds(shared_option_name="ubitrack_log4cpp:shared", pure_c=False)
    builder.run()
