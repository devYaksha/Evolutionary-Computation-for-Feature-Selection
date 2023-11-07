#include <string>
#include "./HFS-GMNB/nbayes.h"

extern "C" {
    // g++ -shared -fPIC -o nbayes.so ./src/HFS-GMNB/*.cpp ./src/call_nbayes.cpp
    #ifdef _WIN32
    #define EXPORT __declspec(dllexport)
    #else
    #define EXPORT __attribute__((visibility("default")))
    #endif

    EXPORT int call_nbayes(char mlnp, char usf, const char* training_dataset, const char* test_dataset, const char* result_file) {
        printf("mlnp: %c, usf %c, training_dataset: %s, test_dataset: %s, result_file: %s\n", mlnp, usf, training_dataset, test_dataset, result_file);
        std::string mlnpStr(1, mlnp);  // Convert char to a C++ string
        std::string usfStr(1, usf);    // Convert char to a C++ string

        long double result = nbayes(mlnpStr, usfStr, training_dataset, test_dataset, result_file);
        float floatValue_result = result; 

        std::cout << "The result of the classification is: " << floatValue_result << std::endl;

        return floatValue_result;
    }
}
