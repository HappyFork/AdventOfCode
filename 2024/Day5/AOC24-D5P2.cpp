/*  Advent of Code 2024
    Day 5 Part 2
    Casey Lee
*/

#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <utility>
#include <vector>

size_t find_pos( int m, std::vector<int>& v ){
    for( size_t z = 0; z < v.size(); z++ ){
        if( v[z] == m ) return z;
    }
    return -1;
}

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

    int answer = 0;
    std::string line;
    std::vector<std::pair<int,int>> rules;
    getline( file, line );
    while( line != "" ){
        size_t div = line.find( "|" );
        int first = stoi( line.substr( 0, div ) );
        int second = stoi( line.substr( div+1) );
        rules.push_back( std::pair( first, second ) );
        getline( file, line );
    }

    // Empty line means moving on to second type of input

    getline( file, line );
    while( !file.eof() && line != "" ){
        std::string ts = "";
        std::vector<int> tv;
        for( size_t s = 0; s < line.size(); s++ ){
            if( line[s] == ',' ){
                tv.push_back( stoi(ts) );
                ts = "";
            } else ts += line[s];
        }
        tv.push_back( stoi(ts) );
        // Check all the rules for each item in tv
        bool correct = true;
        for( size_t i = 0; i < tv.size(); i++ ){
            for( std::pair<int,int> j : rules ){
                if( j.first == tv[i] ){
                    size_t jpos = find_pos( j.second, tv );
                    if( jpos != -1 && i > jpos ){
                        correct = false;
                        std::swap( tv[i], tv[jpos] );
                        i = 0;
                        break;
                    } 
                } else if( j.second == tv[i] ){
                    size_t jpos = find_pos( j.first, tv );
                    if( jpos != -1 && i < jpos ){
                        correct = false;
                        std::swap( tv[i], tv[jpos] );
                        i = 0;
                        break;
                    } 
                }
            }
        }
        if( !correct) answer += tv[ tv.size()/2 ];
        getline( file, line );
    }

    std::cout << answer << std::endl;
    return 0;
}