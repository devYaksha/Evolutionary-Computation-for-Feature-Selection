#include <iostream>
#include <string>
#include <fstream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <limits.h>
#include <float.h>
#include <unistd.h>
#include <sstream>
#include "utils.h"

using namespace std;


void create_files_for_grasp(vector <int> &s, string path);

vector <double> get_ranking(string path);

void write_final_result(vector <long double> hf, string path);
