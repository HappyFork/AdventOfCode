/*  Advent of Code 2024
    Day 2 Part 1
    Casey Lee
*/

#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>

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

    std::string line = "";
    int answer = 0;
    getline( file, line );
    while( !file.eof() ){
        std::stringstream ss( line );
        std::vector<int> report;
        // I'm reusing line here bc I don't want to make a new string
        // and it doesn't matter what I do with line inside the loop
        while( ss >> line ) report.push_back( stoi(line) );

        // Check to see if the report is safe
        bool safe = true;
        if( report[0] < report[1] ){
            for( size_t i = 1; i < report.size(); i++ ){
                if( report[i] < report[i-1] || report[i] - report[i-1] > 3 || report[i] - report[i-1] < 1 ) safe = false;
            }
        } else if( report[0] > report[1]){
            for( size_t i = 1; i < report.size(); i++ ){
                if( report[i] > report[i-1] || report[i-1] - report[i] > 3 || report[i-1] - report[i] < 1 ) safe = false;
            }
        } else{
            safe = false;
        }

        if(safe) answer++;
        getline( file, line );
    }

    std::cout << answer << std::endl;
    return 0;
}