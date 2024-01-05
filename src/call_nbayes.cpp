#include <string>
#include "./GMNB/nbayes.h"

// g++ -shared -fPIC -o ./src/nbayes.so ./src/GMNB/*.cpp ./src/call_nbayes.cpp

extern "C" {

    #ifdef _WIN32
    #define EXPORT __declspec(dllexport)
    #else
    #define EXPORT __attribute__((visibility("default")))
    #endif

    EXPORT int call_nbayes(char mlnp, char usf, const char* training_dataset, const char* test_dataset, const char* result_file) {
        
        std::string mlnpStr(1, mlnp);  
        std::string usfStr(1, usf);   

        long double result = nbayes(mlnpStr, usfStr, training_dataset, test_dataset, result_file);
        float floatValue_result = result; 

        //std::cout << "C++ Result: " << floatValue_result << std::endl << "Training-path: " << training_dataset << std::endl << "Test-path: " << test_dataset << std::endl;

        return floatValue_result;
    }
}
