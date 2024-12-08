/*  Advent of Code 2024
    Day 1 Part 1
    Casey Lee
*/

#include <cmath>
#include <fstream>
#include <iostream>
//#include <optional>
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
    int dist = 0;
    for( size_t z = 0; z < llist.size(); z++ ){
        size_t lloc = 0;
        size_t rloc = 0;
        int llow = INT_MAX;
        int rlow = INT_MAX;
        for( size_t i = 0; i < llist.size(); i++ ){
            if( llist[i] > 0 && llist[i] < llow ){
                llow = llist[i];
                lloc = i;
            }
            if( rlist[i] > 0 && rlist[i] < rlow ){
                rlow = rlist[i];
                rloc = i;
            }
        
        }
        dist += std::abs( llow - rlow );
        llist[lloc] = -1;
        rlist[rloc] = -1;
    }

    std::cout << dist << std::endl;
    return 0;
}