#ifndef TIME_H
#define TIME_H
#include <string>
//#include <sys/resource.h>

using namespace std;


/*
double getCurrentCPUTime() {
	static struct rusage usage;
	getrusage(RUSAGE_SELF, &usage);
	//cout << "usage: seconds: " << usage.ru_utime.tv_sec << " microseconds " << usage.ru_utime.tv_usec << endl;
	return ((double)usage.ru_utime.tv_sec)+(((double)usage.ru_utime.tv_usec)/((double)1000000));
}*/

#endif

