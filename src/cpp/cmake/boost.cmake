function(add_boost)
    #message("qualquer coisa aí")
    cmake_policy(SET CMP0135 NEW)
    include(FetchContent)
    FetchContent_Declare(
            Boost
            SOURCE_DIR "/home/jeronimo/GIT/PeR/src/cpp/thirdparty/boost_1_86_0/"
    )
    set(BOOST_INCLUDE_LIBRARIES pool)
    FetchContent_MakeAvailable(Boost)
endfunction()