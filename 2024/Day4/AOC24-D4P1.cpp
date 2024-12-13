/*  Advent of Code 2024
    Day 4 Part 1
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

    const int CLUESIZE = 3;
    const std::string CLUE = "XMAS";
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

    for( size_t r = 0; r < rows; r++ ){
        for( size_t c = 0; c < cols; c++ ){
            if( grid[r][c] == CLUE[0] ){
                // Cardinals
                if( r >= CLUESIZE ){        // Check up
                    if( grid[r-1][c] == CLUE[1] && grid[r-2][c] == CLUE[2]
                    && grid[r-3][c] == CLUE[3] ) answer++;
                }
                if( c >= CLUESIZE ){        // Check left
                    if( grid[r][c-1] == CLUE[1] && grid[r][c-2] == CLUE[2]
                    && grid[r][c-3] == CLUE[3] ) answer++;
                }
                if( c+CLUESIZE < cols ){    // Check right
                    if( grid[r][c+1] == CLUE[1] && grid[r][c+2] == CLUE[2]
                    && grid[r][c+3] == CLUE[3] ) answer++;
                }
                if( r+CLUESIZE < rows ){    // Check down
                    if( grid[r+1][c] == CLUE[1] && grid[r+2][c] == CLUE[2]
                    && grid[r+3][c] == CLUE[3] ) answer++;
                }

                // Weh, this feels like hardcoding. Or at least repeating code

                // Diagonals
                if( r >= CLUESIZE && c >= CLUESIZE ){           // Check up and left
                    if( grid[r-1][c-1] == CLUE[1] && grid[r-2][c-2] == CLUE[2]
                    && grid[r-3][c-3] == CLUE[3] ) answer++;
                }        
                if( r >= CLUESIZE && c+CLUESIZE < cols ){       // Check up and right
                    if( grid[r-1][c+1] == CLUE[1] && grid[r-2][c+2] == CLUE[2]
                    && grid[r-3][c+3] == CLUE[3] ) answer++;
                }
                if( r+CLUESIZE < rows && c >= CLUESIZE ){       // Check down and left
                    if( grid[r+1][c-1] == CLUE[1] && grid[r+2][c-2] == CLUE[2]
                    && grid[r+3][c-3] == CLUE[3] ) answer++;
                }
                if( r+CLUESIZE < rows && c+CLUESIZE < cols ){   // Check down and left
                    if( grid[r+1][c+1] == CLUE[1] && grid[r+2][c+2] == CLUE[2]
                    && grid[r+3][c+3] == CLUE[3] ) answer++;
                }
            }
        }
    }

    std::cout << answer << std::endl;
    return 0;
}