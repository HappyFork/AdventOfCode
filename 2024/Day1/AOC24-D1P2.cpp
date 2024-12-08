/*  Advent of Code 2024
    Day 1 Part 2
    Casey Lee
*/

#include <cmath>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <limits.h>

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

    std::vector<int> llist;
    std::vector<int> rlist;
    std::string line = "";
    getline( file, line );

    while( !file.eof() ){
        size_t f = line.find_first_of(" ");
        size_t l = line.find_last_of(" ");
        llist.push_back( stoi( line.substr(0,f) ) );
        rlist.push_back( stoi( line.substr(l+1) ) );
        getline( file, line );
    }
    
    // Find lowest value
    int sim = 0;
    for( size_t li = 0; li < llist.size(); li++ ){
        int appearances = 0;
        for( size_t ri = 0; ri < llist.size(); ri++ ){
            if( llist[li] == rlist[ri] ) appearances++;
        }
        sim += llist[li] * appearances;
    }

    std::cout << sim << std::endl;
    return 0;
}