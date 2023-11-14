#include <string>
#include "./HFS-GMNB/nbayes.h"

// g++ -shared -fPIC -o ./src/nbayes.so ./src/HFS-GMNB/*.cpp ./src/call_nbayes.cpp

extern "C" {

    #ifdef _WIN32
    #define EXPORT __declspec(dllexport)
    #else
    #define EXPORT __attribute__((visibility("default")))
    #endif

    EXPORT int call_nbayes(char mlnp, char usf, const char* training_dataset, const char* test_dataset, const char* result_file) {
        //printf("Mandatory Leaf Node Prediction: %c \nUsefulness: %c \nTraining Dataset Path: %s \nTest Dataset: %s \nResult file path: %s\n", mlnp, usf, training_dataset, test_dataset, result_file);
        
        std::string mlnpStr(1, mlnp);  
        std::string usfStr(1, usf);   

        long double result = nbayes(mlnpStr, usfStr, training_dataset, test_dataset, result_file);
        float floatValue_result = result; 

        //std::cout << "The result of the classification is: " << floatValue_result << std::endl;

        return floatValue_result;
    }
}
