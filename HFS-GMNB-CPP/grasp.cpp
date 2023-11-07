#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <cmath>
#include <limits.h>
#include <float.h>
#include <unistd.h>
#include <sstream>
#include "utils.h"
#include "chargeTrainingSet.h"
#include "chargeTestSet.h"
#include "classifier.h"
#include "nbayes.h"
#include "ranking.h"
#include "arquivos.h"

using namespace std;

struct solution{
    vector <int> att;
    vector <long double> hf;
};



char easytolower(char in){
  return tolower(in);
}

//deixa a string em lowercase em tempo de processamento, sem colocar a chamada do metodo na pilha de execucao
static inline std::string &str_lower(std::string &data) {
        transform(data.begin(), data.end(), data.begin(), easytolower);
        return data;
}

vector <long double> classifier_fo(string path){

    string trannig_file, testing_file, result_file;
    stringstream file_index;
    vector <long double> hf;

    //k eh a quantidade de folds
    for(int k = 0; k < 5; ++k){
        //treino
        file_index.str("");
        //file_index << "treino_bins" << k << "_final";
        file_index << "treino" << k;
        trannig_file.clear();
        trannig_file = (path + file_index.str() + ".arff");
        //teste
        file_index.str("");
        //file_index << "teste_bins" << k << "_final";
        file_index << "teste" << k;
        testing_file.clear();
        testing_file = (path + file_index.str() + ".arff");
        //resultado
        file_index.str("");
        file_index << "result_all_att" << k;
        result_file.clear();
        result_file = (path + file_index.str() + ".txt");

        hf.push_back(nbayes("y", "y", trannig_file, testing_file, result_file));
        //cout << result_file << "\n";

    }

    return hf;

}

/*

int main(int argc, char* argv[]){

    unsigned int opt;
    string path;
    vector <long double> fo;
    //pega o nome do caminho de entrada
	while((opt = getopt(argc, argv, "i:")) != EOF){
		switch(opt)
		{
			 case 'i': path = optarg; break;
			 default: fprintf(stderr, "Usage: -i [Name of input path]\n"); return (1);
		}
	}

	if(argc != 3){
		fprintf(stderr, "Usage: -i [Name of input path]\n");
		return (1);
	}

	fo = classifier_fo(path);

    write_final_result(fo, path);

    cout << "\nTerminei ";


    return 0;
}
*/