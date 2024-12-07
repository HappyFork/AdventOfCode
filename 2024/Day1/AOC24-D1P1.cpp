/*  Advent of Code 2024
    Day 1 Part 1
    Casey Lee
*/

#include <fstream>
#include <iostream>
#include <optional>
#include <string>

int main( int argv, char* argc[] ){
    if( argv != 2 ){
        std::cout << "Give me a file, stupid." << std::endl;
        return 1;
    }

    std::ifstream file( argc[1] );
    if( !file ){
        std::cout << "Give me a real file, stupid." << std::endl;
        return 1;
    }

    std::optional<int> llist[];
    std::optional<int> rlist[];
    std::string line;
    getline( file, line );

    while( !file.eof() ){
        size_t f = line.find_first_of(" ");
        size_t l = line.find_last_of(" ");
        llist.append( stoi( line.substr(0,f) ) );
        rlist.append( stoi( line.substr(l+1) ) );
        getline( file, line );
    }
}