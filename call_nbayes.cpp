#include <string>
#include "./HFS-GMNB-CPP/nbayes.h"

extern "C"{
//g++ -shared -o nbayes.dll ./HFS-GMNB-CPP/*.cpp ./call_nbayes.cpp
//g++ -shared -o nbayes.so ./HFS-GMNB-CPP/*.cpp ./call_nbayes.cpp

__declspec(dllexport) int call_nbayes(char *training_dataset, char *test_dataset, char *result_file) {
    string mlnp = "n";
    string usf = "n";

    long double result = nbayes(mlnp, usf, training_dataset, test_dataset, result_file);

    cout << "The result of the classification is: " << result << endl;

    return 0;
}

}