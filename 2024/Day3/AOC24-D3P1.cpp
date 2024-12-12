/*  Advent of Code 2024
    Day 3 Part 1
    Casey Lee
*/

#include <fstream>
#include <iostream>
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

    int answer = 0, instr = 0;
    std::string p1 = "", p2 = "";
    char c;
    while( !file.get(c).eof() ){
        if( instr == 0 && c == 'm' ) instr++;
        else if( instr == 1 && c == 'u' ) instr++;
        else if( instr == 2 && c == 'l' ) instr++;
        else if( instr == 3 && c == '(' ) instr++;
        else if( instr == 4 ){
            if( c >= '0' && c <= '9' ) p1 += c;
            else if( c == ',' && p1 != "" ) instr++;
            else{
                // Reset everything
                instr = 0;
                p1 = "";
                p2 = "";
            } 
        } else if( instr == 5 ){
            if( c>= '0' && c <= '9' ) p2 += c;
            else if( c == ')' && p2 != "" ){
                // End of instruction. Add product to answer
                answer += ( stoi(p1)*stoi(p2) );
                // Then reset everything
                instr = 0;
                p1 = "";
                p2 = "";
            } else{
                // Reset everything
                instr = 0;
                p1 = "";
                p2 = "";
            }
        }
        else{
            // Reset everything
            instr = 0;
            p1 = "";
            p2 = "";
        } 
    }

    std::cout << answer << std::endl;
    return 0;
}