#include <iostream>
#include <string>
#include <sstream>

using namespace std;

int main(){
	stringstream ss("This is just an example sentence.");

	string str;

	while(ss >> str){
		cout << str << endl;
	}

	return 0;
}