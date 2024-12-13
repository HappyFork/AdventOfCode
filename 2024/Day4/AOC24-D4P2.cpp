/*  Advent of Code 2024
    Day 4 Part 2
    Casey Lee
*/

#include <fstream>
#include <iostream>
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

    int answer = 0;
    size_t cols = 0;
    size_t rows = 0;
    std::vector<std::string> grid;
    std::string temp;

    getline( file, temp );
    cols = temp.size();
    while( !file.eof() && temp != "" ){
        grid.push_back( temp );
        rows++;
        getline( file, temp );
    }

    for( size_t r = 1; r < rows-1; r++ ){
        for( size_t c = 1; c < cols-1; c++ ){
            if( grid[r][c] == 'A' ){
                // M M
                //  A
                // S S
                if( grid[r-1][c-1] == 'M' && grid[r-1][c+1] == 'M' && 
                grid[r+1][c-1] == 'S' && grid[r+1][c+1] == 'S' ) answer++;

                // M S
                //  A
                // M S
                if( grid[r-1][c-1] == 'M' && grid[r-1][c+1] == 'S' && 
                grid[r+1][c-1] == 'M' && grid[r+1][c+1] == 'S' ) answer++;

                // S M
                //  A
                // S M
                if( grid[r-1][c-1] == 'S' && grid[r-1][c+1] == 'M' && 
                grid[r+1][c-1] == 'S' && grid[r+1][c+1] == 'M' ) answer++;

                // S S
                //  A
                // M M
                if( grid[r-1][c-1] == 'S' && grid[r-1][c+1] == 'S' && 
                grid[r+1][c-1] == 'M' && grid[r+1][c+1] == 'M' ) answer++;
            }
        }
    }

    std::cout << answer << std::endl;
    return 0;
}