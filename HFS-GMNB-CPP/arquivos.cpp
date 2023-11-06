#include "arquivos.h"



//reescreve os aquivos usados pelo classificador apenas com os atributos em vector s
void create_files_for_grasp(vector <int> &s, string path){
    string input_file, output_file, str;
    stringstream file_index;

    for(int k = 0; k < 10; ++k){
        file_index.str("");
        if (k<5) file_index << "treino" << k;
        else {
            int aux_index = k-5;
            file_index << "teste" << aux_index;
        }
        input_file.clear();
        input_file = (path + file_index.str() + ".arff");
        //cout << input_file << "\n";
        ifstream file(input_file.c_str());
        vector< vector< string > >  data;
        vector< string > dist_class, header_attr;
        string header = "", header_attr_class = "";

        getline(file, str);

        header_attr.clear();
        while(str.find("@data") == string::npos){ //enquanto nao encontrar data

            //trata linhas em branco entre attribute classe e data
            if(str.find("@attribute class") != string::npos){ //se encontra atributo classe
                header_attr_class = str;
                while(str.find("@data") == string::npos){ //passa linhas em branco ate chegar em data
                    getline(file, str);
                }
                break;
            }

            //guarda o relation em header
            if(str.find("@relation") != string::npos)	header = str + "\n";

            //guarda no vector header_attr um atributo por linha quando acha attribute
            if(str.find("@attribute") != string::npos)	header_attr.push_back(str + "\n");

            getline(file, str);
        }
        //pega as instancias
        dist_class.clear();
        data.clear();
        while(getline(file, str)){

            if(!str.empty()){ //se str nao eh vazia
                vector< string > v_str = explode(str,',');
                int tam = v_str.size();

                //armazenando o atributo classe
                string classe = v_str[tam-1];
                if(in_array_string(classe, dist_class) == -1){
                    dist_class.push_back(classe); //se for classe nova, adicona no vector de classes distintas dist_class
                }
                data.push_back(v_str);
            }
        }
        file.close();


        //escreve o arff de saida
        output_file.clear();
        output_file = (path + file_index.str() + "grasp.arff");
        ofstream file2;
        file2.open(output_file.c_str());

        //junta header dos atributos da base que serao usados
        int num_att = data[0].size();
        for(int i = 0; i < num_att-1; ++i){
            int pos = in_array_int(i, s);
            if (pos != -1) header = (header + header_attr[i]);
        }

        header = (header + header_attr_class + "\n@data\n");
        file2 << header;
        for(unsigned int i = 0; i < data.size(); ++i){
            string v_line = "";
            for(int j = 0; j < num_att-1; ++j){
                int pos = in_array_int(j, s);
                if(pos != -1)   v_line = (v_line + data[i][j] +  ",");
            }
            v_line = v_line + data[i][num_att-1] + "\n";
            file2 << v_line;
        }
        file2.close();

    }
}

//le o arquivo de ranking da base e retorna o vector com seus valores para cada atributo
vector <double> get_ranking(string path){

    vector <double> ranking;
    string input_file, str;
    input_file = (path + "rankingSUH.txt");
    ifstream file(input_file.c_str());

    while(getline(file, str)){
        ranking.push_back(atof(str.c_str())); //converte a string para double
    }
    file.close();
    return ranking;
}

void write_final_result(vector <long double> hf, string path){

    string output_file;
    output_file = (path + "resultado_final_all_att.txt");
    ofstream file;
    file.open(output_file.c_str());
    ostringstream str_aux;

    for(unsigned int i = 0; i < hf.size(); ++i){

        str_aux  << hf[i] << "\n";
    }

    file << str_aux.str() << "\n";
    file.close();

}
